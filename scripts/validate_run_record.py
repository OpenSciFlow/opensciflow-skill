from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "run-record.schema.json"


def check_required_metadata(data: dict) -> list[str]:
    errors: list[str] = []
    for field in ("commands", "versions", "inputs", "outputs", "citation", "license"):
        value = data.get(field)
        if value in (None, [], {}):
            errors.append(f"missing required run-record metadata: {field}")
    return errors


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "tests" / "fixtures" / "valid_run_record.json"
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    data = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(data, schema)
    errors = check_required_metadata(data)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS run record: {path}")


if __name__ == "__main__":
    main()

