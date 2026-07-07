from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def validate(instance_path: str, schema_path: str) -> None:
    jsonschema.validate(load_json(instance_path), load_json(schema_path))


def test_valid_skill_input_passes() -> None:
    validate("tests/fixtures/valid_skill_input.json", "schemas/skill-input.schema.json")


def test_valid_skill_output_passes() -> None:
    validate("examples/gromacs-rmsd/skill-output.example.json", "schemas/skill-output.schema.json")


def test_execution_requests_pass() -> None:
    for path in [
        "examples/gromacs-rmsd/execution-request.json",
        "examples/diffdock-docking/execution-request.json",
        "examples/boltz-structure-prediction/execution-request.json",
        "examples/slurm-gromacs-rmsd/execution-request.json",
        "examples/slurm-mace-evaluation/execution-request.json"
    ]:
        validate(path, "schemas/execution-request.schema.json")


def test_valid_run_records_pass() -> None:
    for path in [
        "tests/fixtures/valid_run_record.json",
        "examples/gromacs-rmsd/run-record.example.json",
        "examples/diffdock-docking/run-record.example.json",
        "examples/boltz-structure-prediction/run-record.example.json",
        "examples/slurm-gromacs-rmsd/run-record.example.json",
        "examples/slurm-mace-evaluation/run-record.example.json",
        "examples/biopilot-md-stability/skill-run-record.projection.json"
    ]:
        validate(path, "schemas/run-record.schema.json")


def test_run_record_crosswalk_passes() -> None:
    validate("data/run-record-crosswalk.biopilot-v0.1.json", "schemas/run-record-crosswalk.schema.json")


def test_missing_citation_fails_run_record_schema() -> None:
    schema = load_json("schemas/run-record.schema.json")
    data = load_json("tests/fixtures/valid_run_record.json")
    data["citation"] = []
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, schema)


def test_missing_required_inputs_fails_closed() -> None:
    schema = load_json("schemas/skill-input.schema.json")
    data = load_json("tests/fixtures/valid_skill_input.json")
    data["input_files"] = []
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, schema)
