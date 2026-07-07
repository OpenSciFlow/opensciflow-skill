# Slurm MACE Evaluation Example

This example shows how OpenSciFlow Skill can prepare a reviewed Slurm wrapper request for atomistic-model inference with MACE.

It is a planning and approval example only. No real Slurm job was submitted and no scientific result is claimed.

## What This Example Demonstrates

- A non-GROMACS reviewed-wrapper example.
- GPU/resource fields using OpenSciFlow-normalized names.
- Model-weight metadata is treated as required before execution.
- The run record stays `planned` until the user approves submission.

## Files

- `user-request.md`: user-facing request.
- `selected-workflow.yaml`: workflow template selected by the agent.
- `selected-manifest.yaml`: manifest excerpt with MACE Slurm metadata.
- `execution-request.json`: schema-validated request for a reviewed Slurm submission.
- `run-record.example.json`: planned run record before job submission.
- `job.sbatch.template`: reviewed wrapper sketch.

