# BioPilot MD Stability Projection

This example shows how a planned BioPilot run record can be projected into the stricter OpenSciFlow Skill run-record shape.

The projection is not evidence of execution. It is a schema-alignment fixture.

## Files

- `skill-run-record.projection.json`: Skill-compatible planned run record derived from the BioPilot sample run-manifest shape.

## Why This Exists

BioPilot uses a reference-app run manifest. OpenSciFlow Skill uses an agent-execution audit record.

The two records should not be identical, but their fields should be mappable.

