# Contributing

OpenSciFlow Skill is an early draft. Contributions should improve clarity, safety, reproducibility, or missing-case coverage.

## Useful Contributions

- Correct schema fields.
- Add refusal cases.
- Add HPC / Slurm examples.
- Add manifest-reading examples for real tools.
- Add workflow-matching examples.
- Correct license and citation propagation.
- Report unsafe execution assumptions.

## Rules

- Do not claim any external project has adopted OpenSciFlow unless maintainers explicitly say so.
- Do not present computational outputs as clinical, drug-efficacy, or experimental validation.
- Do not add prompt text that allows arbitrary LLM-generated shell execution.
- Keep examples mock or public-data based unless license, citation, size, and hashes are recorded.
- Prefer small, reviewable pull requests.

## Review Checklist

- Are inputs and outputs explicit?
- Are command templates reviewed rather than invented?
- Are license and citation fields preserved?
- Are limitations visible?
- Does failure stop safely?
- Is a run record produced or explicitly refused?

