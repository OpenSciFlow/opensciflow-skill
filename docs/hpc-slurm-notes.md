# HPC and Slurm Notes

OpenSciFlow Skill should not invent cluster configuration.

## Required HPC Questions

- Which scheduler is used?
- Which partition, account, module, container, and GPU resources are required?
- Can the dry run happen on a login node, or must it be a Slurm job?
- Are model weights staged before job submission?
- Where are logs written?
- Where are temporary files written?
- Which paths are allowed by local policy?

## Agent Behavior

The agent should show rendered Slurm options and ask for approval before submission.

It must refuse when a required account, partition, module, or model-weight location is unknown and cannot be safely omitted.

Slurm job submission success is not scientific validation.

