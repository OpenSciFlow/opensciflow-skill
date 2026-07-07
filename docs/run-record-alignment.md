# Run Record Alignment

OpenSciFlow currently has two related run-record shapes:

- **OpenSciFlow Skill run record**: agent-execution audit record.
- **BioPilot run manifest**: reference-app workflow record.

They should be mappable, but they should not be forced into one identical schema too early.

## Why They Differ

The Skill run record is stricter about execution safety:

- exact command source;
- rendered commands;
- return codes;
- model weights;
- hardware;
- logs;
- file hashes;
- licenses;
- warnings.

BioPilot records app-level workflow state:

- user task text;
- selected workflow object;
- plugin list;
- workflow steps;
- sample-data policy;
- report artifacts.

## Current Crosswalk

Machine-readable crosswalk:

```text
data/run-record-crosswalk.biopilot-v0.1.json
```

Schema:

```text
schemas/run-record-crosswalk.schema.json
```

Projection fixture:

```text
examples/biopilot-md-stability/skill-run-record.projection.json
```

## Key Mappings

| BioPilot field | Skill field | Rule |
|---|---|---|
| `run_id` | `run_id` | copy |
| `workflow.name` | `workflow_id` | copy |
| `plugins[0].name` | `tool_manifest_id` | copy primary plugin |
| `created_at` | `started_at` | copy for planned records |
| `task_text` | `task_text` | copy as optional context |
| `steps[*].command` | `commands[*].command` | render or copy reviewed command |
| `inputs` | `inputs` | copy file records |
| `steps[*].artifacts` | `outputs` | collect produced artifacts |
| `environment` | `environment` | copy and normalize |
| `citations` | `citation` | rename |
| `limitations` | `limitations` | copy |
| `sample_data.policy` | `warnings` | copy unresolved policy warnings |

## Alignment Rule

A planned BioPilot record may project into a planned Skill run record.

A completed BioPilot record should not project into a completed Skill run record unless it also contains:

- rendered commands;
- command sources;
- return codes;
- logs;
- tool versions;
- input/output hashes;
- license metadata;
- warnings and limitations.
