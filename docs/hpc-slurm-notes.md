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
- Is the Slurm wrapper reviewed, and which arguments may the agent fill?

## Agent Behavior

The agent should show rendered Slurm options and ask for approval before submission.

It must refuse when a required account, partition, module, or model-weight location is unknown and cannot be safely omitted.

Slurm job submission success is not scientific validation.

## Minimum Slurm Execution Request

A Slurm execution request should include:

- `command_source: reviewed-wrapper`;
- reviewed wrapper metadata;
- account and partition;
- walltime, CPU, memory, and GPU request;
- module or container environment;
- stdout and stderr paths;
- run directory;
- explicit approval status.

If these fields are missing, the agent should return a missing-requirements response instead of inventing local cluster policy.

## Normalized Scheduler Fields

Use OpenSciFlow-normalized field names in skill inputs and execution requests:

- `account`;
- `partition`;
- `time_limit`;
- `cpu_cores`;
- `memory_gb`;
- `gpu_resources`;
- `module` or `modules`.

The reviewed wrapper maps these names to Slurm-specific options such as `--time`, `--cpus-per-task`, `--mem`, and `--gres`.
