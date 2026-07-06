from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def test_missing_manifest_fails_skill_input_schema() -> None:
    schema = load_json("schemas/skill-input.schema.json")
    data = load_json("tests/fixtures/invalid_missing_manifest.json")
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, schema)


def test_arbitrary_shell_is_rejected() -> None:
    schema = load_json("schemas/execution-request.schema.json")
    data = load_json("tests/fixtures/invalid_arbitrary_shell.json")
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, schema)


def test_refusal_output_can_explain_missing_metadata() -> None:
    schema = load_json("schemas/skill-output.schema.json")
    output = {
        "parsed_task": {"task_type": "protein-ligand-docking"},
        "selected_workflow": None,
        "selected_manifests": [],
        "readiness_checks": [],
        "missing_requirements": ["model weight checksum", "model weight license"],
        "proposed_execution_plan": None,
        "approval_required": False,
        "refusal": {
            "refused": True,
            "reason": "Required model-weight metadata is missing.",
            "safe_next_action": "Record model-weight source, license, and checksum before execution."
        },
        "warnings": ["No execution was attempted."],
        "expected_outputs": [],
        "run_record_template": None
    }
    jsonschema.validate(output, schema)
