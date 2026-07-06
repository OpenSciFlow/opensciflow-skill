# Adoption Guide for AI Scientist Systems

AI Scientist-style systems can use OpenSciFlow Skill as an execution protocol layer.

## Suggested Integration

1. Keep ideation and hypothesis generation separate from execution.
2. Convert planned tasks into OpenSciFlow workflow-template queries.
3. Require manifests for every executable tool.
4. Use readiness levels to decide what the system may attempt.
5. Route execution through a local agent with run-record writing.
6. Carry citations and limitations into reports.

## What This Adds

- Safer tool invocation.
- Less repeated README parsing.
- More explicit license and citation handling.
- Better reproducibility evidence.
- Clearer refusal behavior.

## What It Does Not Add

- Scientific correctness certification.
- Automatic discovery validation.
- Permission to bypass upstream installation or data rules.

