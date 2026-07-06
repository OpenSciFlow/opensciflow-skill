from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "skill-output.schema.json"


def main() -> None:
    path = Path(sys.argv[1])
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    data = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(data, schema)
    print(f"PASS skill output: {path}")


if __name__ == "__main__":
    main()

