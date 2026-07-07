from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = (
    ROOT / "examples" / "slurm-gromacs-rmsd",
    ROOT / "examples" / "slurm-mace-evaluation",
)
PLACEHOLDER_RE = re.compile(r"{([^{}]+)}")
SCHEDULER_INPUT_ALIASES = {
    "scheduler_account": "account",
    "scheduler_partition": "partition",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not parse to an object")
    return data


def names(items: object) -> set[str]:
    if not isinstance(items, list):
        return set()
    return {
        item["name"]
        for item in items
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    }


def step_ids(workflow: dict[str, Any]) -> set[str]:
    steps = workflow.get("steps", [])
    if not isinstance(steps, list):
        return set()
    return {
        step["id"]
        for step in steps
        if isinstance(step, dict) and isinstance(step.get("id"), str)
    }


def required_input_names(workflow: dict[str, Any]) -> set[str]:
    inputs = workflow.get("inputs", [])
    if not isinstance(inputs, list):
        return set()
    return {
        item["name"]
        for item in inputs
        if isinstance(item, dict) and item.get("required") is True and isinstance(item.get("name"), str)
    }


def plugin_names(workflow: dict[str, Any]) -> set[str]:
    plugins = workflow.get("plugins", {})
    if not isinstance(plugins, dict):
        return set()
    return set(plugins.get("required", [])) | set(plugins.get("optional", []))


def available_request_inputs(request: dict[str, Any]) -> set[str]:
    available = names(request.get("inputs", []))
    environment = request.get("environment", {})
    if isinstance(environment, dict):
        for workflow_name, environment_name in SCHEDULER_INPUT_ALIASES.items():
            if environment.get(environment_name):
                available.add(workflow_name)
    return available


def wrapper_placeholders(template_text: str) -> set[str]:
    return set(PLACEHOLDER_RE.findall(template_text))


def validate_example(example_dir: Path) -> list[str]:
    errors: list[str] = []
    workflow = load_yaml(example_dir / "selected-workflow.yaml")
    request = load_json(example_dir / "execution-request.json")
    run_record = load_json(example_dir / "run-record.example.json")
    wrapper_text = (example_dir / "job.sbatch.template").read_text(encoding="utf-8")

    workflow_name = workflow.get("workflow_name")
    if request.get("workflow_id") != workflow_name:
        errors.append(f"{example_dir.name}: execution workflow_id does not match selected workflow_name")
    if run_record.get("workflow_id") != request.get("workflow_id"):
        errors.append(f"{example_dir.name}: run record workflow_id does not match execution request")

    if request.get("step_id") not in step_ids(workflow):
        errors.append(f"{example_dir.name}: execution step_id is not a workflow step")

    if request.get("manifest_id") not in plugin_names(workflow):
        errors.append(f"{example_dir.name}: execution manifest_id is not listed in workflow plugins")
    if run_record.get("tool_manifest_id") != request.get("manifest_id"):
        errors.append(f"{example_dir.name}: run record tool_manifest_id does not match execution request")

    missing_inputs = required_input_names(workflow) - available_request_inputs(request)
    if missing_inputs:
        errors.append(f"{example_dir.name}: execution request is missing workflow inputs: {', '.join(sorted(missing_inputs))}")

    missing_outputs = names(workflow.get("outputs", [])) - names(request.get("outputs", []))
    if missing_outputs:
        errors.append(f"{example_dir.name}: execution request is missing workflow outputs: {', '.join(sorted(missing_outputs))}")

    missing_record_outputs = names(request.get("outputs", [])) - names(run_record.get("outputs", []))
    if missing_record_outputs:
        errors.append(f"{example_dir.name}: run record is missing execution outputs: {', '.join(sorted(missing_record_outputs))}")

    reviewed_wrapper = request.get("reviewed_wrapper", {})
    allowed_arguments = set(reviewed_wrapper.get("allowed_arguments", [])) if isinstance(reviewed_wrapper, dict) else set()
    request_input_placeholders = {f"inputs.{name}" for name in names(request.get("inputs", []))}
    allowed_placeholders = allowed_arguments | request_input_placeholders | {"run_directory"}
    unknown_placeholders = wrapper_placeholders(wrapper_text) - allowed_placeholders
    if unknown_placeholders:
        errors.append(f"{example_dir.name}: wrapper template has undeclared placeholders: {', '.join(sorted(unknown_placeholders))}")

    environment = request.get("environment", {})
    if isinstance(environment, dict):
        for argument in allowed_arguments - {"run_directory"}:
            if argument == "module" and (environment.get("module") or environment.get("modules")):
                continue
            if argument not in environment:
                errors.append(f"{example_dir.name}: allowed wrapper argument {argument!r} is not present in environment")

    return errors


def main() -> None:
    errors: list[str] = []
    for example_dir in EXAMPLES:
        errors.extend(validate_example(example_dir))

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"Validated {len(EXAMPLES)} Slurm workflow/execution alignments")


if __name__ == "__main__":
    main()
