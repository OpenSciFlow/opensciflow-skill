from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "run-record-crosswalk.schema.json"
DEFAULT_CROSSWALK = ROOT / "data" / "run-record-crosswalk.biopilot-v0.1.json"
SKILL_SCHEMA = ROOT / "schemas" / "run-record.schema.json"


def top_level(path: str) -> str:
    return path.split("[", 1)[0].split(".", 1)[0]


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CROSSWALK
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    crosswalk = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(crosswalk, schema)

    skill_schema = json.loads(SKILL_SCHEMA.read_text(encoding="utf-8"))
    skill_required = set(skill_schema["required"])
    crosswalk_targets = {top_level(item["target"]) for item in crosswalk["field_mappings"]}
    declared_targets = set(crosswalk["target_required_fields"])

    missing_from_declared = sorted(skill_required - declared_targets)
    missing_from_mappings = sorted(skill_required - crosswalk_targets)

    errors = []
    if missing_from_declared:
        errors.append(f"target_required_fields missing Skill fields: {', '.join(missing_from_declared)}")
    if missing_from_mappings:
        errors.append(f"field_mappings missing Skill targets: {', '.join(missing_from_mappings)}")

    source_required = set(crosswalk["source_required_fields"])
    crosswalk_sources = {top_level(item["source"]) for item in crosswalk["field_mappings"]}
    missing_source_coverage = sorted(source_required - crosswalk_sources)
    if missing_source_coverage:
        errors.append(f"field_mappings missing BioPilot source coverage: {', '.join(missing_source_coverage)}")

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"PASS run-record crosswalk: {path}")


if __name__ == "__main__":
    main()

