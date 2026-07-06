# Refusal Policy

Refusal is a normal and useful outcome.

## Refuse Execution When

- Manifest validation fails.
- Workflow validation fails.
- Required inputs are missing.
- Required model weights are missing.
- License or citation metadata is unclear.
- Command template uses undeclared variables.
- Command includes unreviewed shell composition.
- The task asks for clinical, drug-efficacy, or high-risk scientific conclusions.
- The task writes outside approved paths.
- The requested workflow exceeds declared capabilities.

## Refusal Output

A refusal should include:

- concise reason;
- missing fields or evidence;
- whether the task can be converted to review-only mode;
- next safe action.

