# Context And Evidence Rationale

Scientific tools often require agents to inspect many long or scattered sources before they can make a safe execution decision:

- README files;
- installation pages;
- issue discussions;
- example notebooks;
- model cards;
- Slurm scripts;
- paper supplements.

OpenSciFlow Skill does not treat a capsule as a replacement for upstream documentation. The capsule is an execution-facing evidence package that records what an agent must check before acting.

The useful compression is conditional:

- R1/R2 artifacts may reduce documentation inspection cost.
- R3 artifacts may reduce command-template ambiguity.
- R4/R5 artifacts may reduce setup trial-and-error inside the verified environment.
- R6/R7 artifacts provide limited evidence for cross-environment transfer.

OpenSciFlow Skill organizes this context into:

- manifests for tool requirements;
- environment specs for runtime assumptions;
- reviewed command templates for safe rendering;
- smoke tests for minimal checks;
- verified environment matrices for bounded portability claims;
- known failure records for diagnosis;
- run records for attempted execution.

The goal is not to hide complexity. The goal is to expose the parts an agent must check before acting and record after acting.
