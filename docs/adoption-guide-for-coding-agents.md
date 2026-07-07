# Adoption Guide for Coding Agents

Coding agents can use this skill when asked to install, wrap, or run scientific tools.

## Practical Rules

- Search for `opensciflow.yaml` before reading long upstream docs.
- Validate manifests before generating code.
- Prefer existing workflow templates over ad hoc plans.
- Do not create shell commands from scratch when a reviewed template exists.
- Write run records for every executed dry run, smoke test, or full run.
- Treat missing metadata as a blocker, not a minor warning.
- Treat placeholder values such as `to-be-filled`, `to-be-reviewed`, and `to-be-confirmed` as review warnings before execution.
- Ask for explicit user approval before running anything beyond validation or review-only planning.

## Suggested Workflow

1. Read `skill.md`.
2. Validate `skill-input.schema.json`.
3. Load manifest and workflow template.
4. Produce `skill-output.schema.json` output.
5. If execution is allowed, produce `execution-request.schema.json`.
6. After execution, validate `run-record.schema.json`.

## Behavior Review

The current behavior review is in:

```text
docs/coding-agent-behavior-review.md
```
