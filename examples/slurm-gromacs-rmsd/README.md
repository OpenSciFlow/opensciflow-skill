# Slurm GROMACS RMSD Example

This example shows how OpenSciFlow Skill should prepare a Slurm execution request for an existing GROMACS trajectory analysis.

It is a planning and approval example only. No real Slurm job was submitted.

## What This Example Demonstrates

- The agent selects a workflow template and manifest.
- The agent renders a reviewed Slurm wrapper submission command.
- The agent records scheduler fields before asking for approval.
- The agent refuses to silently invent account, partition, walltime, or module details.
- The run record stays in `planned` status until a user-approved submission occurs.

## Files

- `user-request.md`: user-facing request.
- `selected-workflow.yaml`: workflow template selected by the agent.
- `selected-manifest.yaml`: manifest excerpt with Slurm execution metadata.
- `execution-request.json`: schema-validated request for a Slurm submission.
- `run-record.example.json`: planned run record before job submission.

