# Context Compression Rationale

Scientific tools often require agents to read many long documents before doing anything useful:

- README files;
- installation pages;
- issue discussions;
- example notebooks;
- model cards;
- Slurm scripts;
- paper supplements.

This creates high token cost and high trial-and-error cost.

OpenSciFlow Skill compresses this context into:

- manifests for tool requirements;
- workflow templates for task structure;
- readiness levels for execution confidence;
- command templates for safe rendering;
- run records for reproducibility.

The goal is not to hide complexity. The goal is to expose the parts an agent must check before acting.

