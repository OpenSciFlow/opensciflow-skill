# Adoption Guide for AI Scientist Systems

AI Scientist-style systems can use OpenSciFlow Skill as an execution protocol layer.

## Suggested Integration

1. Keep ideation and hypothesis generation separate from execution.
2. Convert planned tasks into OpenSciFlow workflow-template queries.
3. Require verified execution capsules, or clearly mark missing capsule evidence.
4. Use readiness levels to decide what the system may attempt.
5. Route execution through a local agent with smoke-test checks and run-record writing.
6. Carry citations and limitations into reports.

## What This Adds

- Safer tool invocation.
- Less repeated inspection of already-captured execution evidence.
- More explicit license and citation handling.
- More complete run records and bounded reproducibility evidence.
- Clearer refusal behavior.

## What It Does Not Add

- Scientific correctness certification.
- Automatic discovery validation.
- A guarantee that tools run across all environments.
- Permission to bypass upstream installation or data rules.
