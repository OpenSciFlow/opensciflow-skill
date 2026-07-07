# Coding-agent behavior review

This note reviews `skill.md` against the behavior expected from coding agents that can read files, edit repositories, run terminal commands, and possibly call local runners.

The goal is not to certify any particular agent implementation. The goal is to keep the skill instructions compatible with realistic agent behavior.

## Review result

`skill.md` is acceptable as a draft coding-agent instruction set if the agent implements three boundaries:

1. It treats OpenSciFlow artifacts as structured inputs, not as permission to improvise shell commands.
2. It fails closed when required manifest, workflow, license, citation, input, weight, wrapper, or environment metadata is missing.
3. It produces execution requests and run records before claiming that a scientific workflow was run reproducibly.

## Behavior assumptions

A coding agent using this skill may be able to:

- inspect repository files;
- validate JSON/YAML schemas;
- render command templates;
- create wrapper or runner code;
- run local validation commands;
- update documentation and tests.

A coding agent using this skill must not assume it can:

- execute arbitrary shell produced by an LLM;
- download model weights silently;
- infer missing licenses or citations from memory;
- claim scientific correctness from computational output;
- submit Slurm jobs without reviewed wrapper metadata and user/site approval;
- write outside the approved run directory without explicit approval.

## Required coding-agent behavior

When asked to run or prepare a scientific tool, the agent should:

1. Locate a relevant workflow template or refuse into review-only planning.
2. Locate each referenced `opensciflow.yaml` manifest.
3. Validate manifest, workflow, execution-request, and run-record schemas where applicable.
4. Report missing required fields before proposing execution.
5. Render only reviewed command templates or reviewed wrapper submissions.
6. Show the rendered command, input paths, output directory, license, citation, limitations, and model-weight status before execution.
7. Ask for explicit approval before execution beyond validation/dry-run steps.
8. Write or project a run record for every dry run, smoke test, or full run.

## Fail-closed cases

The agent should refuse execution and produce a safe next action when:

- no matching manifest exists;
- no matching workflow template exists for an execution request;
- the command would require arbitrary shell composition;
- a reviewed wrapper is missing review metadata;
- model weights are required but source, license, or checksum is absent;
- citation or license metadata is missing;
- required inputs are absent;
- environment readiness cannot be checked for the requested readiness level;
- the requested output asks for clinical, drug-efficacy, toxicity, or experimental-validation claims.

## Current evidence in this repository

- `tests/test_refusal_cases.py` checks missing manifest, arbitrary shell, missing wrapper review metadata, and missing required inputs.
- `tests/test_schema_validation.py` checks skill input, skill output, execution request, run record, and BioPilot run-record projection fixtures.
- `examples/slurm-gromacs-rmsd` and `examples/slurm-mace-evaluation` exercise reviewed-wrapper execution requests.
- `data/run-record-crosswalk.biopilot-v0.1.json` documents how a BioPilot run manifest projects into the skill run-record schema.

## Remaining gaps

- Add real dry-run evidence for at least one MDAnalysis or GROMACS example.
- Add external review for DiffDock and Boltz examples against current upstream guidance.
- Cross-check Slurm wrapper examples against at least one real cluster policy before claiming production HPC readiness.
- Add a runner-level fixture once BioPilot moves beyond review-only planning.
