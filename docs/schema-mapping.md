# Schema Mapping

OpenSciFlow Skill is an adapter layer between a user-facing agent and the lower-level OpenSciFlow protocol artifacts.

## Artifact Map

| Skill artifact | Source artifact | Purpose |
| --- | --- | --- |
| `skill-input.schema.json` | user request, available manifests, available workflow templates | Defines what the agent may consider before planning. |
| `workflow-plan.schema.json` | workflow template | Describes the proposed task boundary, steps, inputs, outputs, and unresolved requirements. |
| `tool-resolution.schema.json` | `opensciflow.yaml` manifest | Records why a tool/model was selected or rejected. |
| `execution-request.schema.json` | manifest command template or reviewed wrapper | Captures the exact command that may be executed after approval. |
| `skill-output.schema.json` | agent decision | Returns selected workflow, readiness checks, missing requirements, refusal, and run-record template. |
| `run-record.schema.json` | execution result | Records commands, versions, inputs, outputs, logs, hashes, citations, licenses, limitations, and warnings. |

## Minimum Execution Path

The minimum safe execution path is:

```text
skill input
-> workflow plan
-> tool resolution
-> execution request
-> user approval
-> local runner or scheduler
-> run record
```

An agent may stop before execution. Stopping with a clear refusal or missing-requirements report is considered correct behavior.

## Command Source Mapping

`execution-request.command_source` must describe where the executable command came from:

- `manifest-template`: a command template declared directly in `opensciflow.yaml`.
- `workflow-template`: a command declared by a reviewed workflow template.
- `reviewed-wrapper`: a wrapper script such as a Slurm job script that has separate review metadata.

For `reviewed-wrapper`, the request must include `reviewed_wrapper.path`, `reviewed_wrapper.review_status`, and `reviewed_wrapper.reviewed_by`.

## Field Ownership

Agents should not invent fields that belong to site policy or upstream projects.

| Field type | Owner |
| --- | --- |
| Model weight source, checksum, license | upstream model/tool maintainer or local curator |
| Citation | upstream project or publication |
| Scheduler account, partition, walltime | local HPC user or cluster administrator |
| Container image and module names | local platform owner |
| Input file paths and data license | user |
| Run record hashes and logs | local runner |

When ownership is unclear, the skill should return a missing requirement instead of proceeding.

