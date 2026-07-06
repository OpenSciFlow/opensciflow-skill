# Agent Skill Specification

An OpenSciFlow-compatible agent should implement these stages.

## Stages

1. Parse scientific intent.
2. Match a workflow template.
3. Load and validate manifests.
4. Check readiness level.
5. Check inputs, weights, environment, hardware, license, citation, and limitations.
6. Render reviewed command templates.
7. Ask for approval.
8. Execute through a controlled local runner.
9. Write a run record.
10. Report outputs, warnings, citations, and limitations.

## Required Agent State

- `user_request`
- `selected_workflow`
- `selected_manifests`
- `readiness_checks`
- `missing_requirements`
- `approval_status`
- `execution_requests`
- `run_record`

## Compatibility Target

The skill should be easy to adapt into:

- coding agents;
- AI Scientist-style systems;
- local notebook assistants;
- lab server agents;
- HPC workflow assistants.

It should not assume one vendor, model provider, or hosted execution platform.

