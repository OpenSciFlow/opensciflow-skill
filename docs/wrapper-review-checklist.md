# Wrapper Review Checklist

Some scientific workflows need wrapper scripts. Slurm jobs, module setup, container launchers, and multi-step preprocessing are common examples.

OpenSciFlow Skill allows wrappers only when they are reviewed as protocol artifacts, not invented by an LLM at execution time.

## Required Metadata

A reviewed wrapper should declare:

- wrapper path;
- review status;
- reviewer or reviewing project;
- allowed arguments;
- expected inputs and outputs;
- allowed working directory;
- environment setup;
- scheduler or container fields, if relevant;
- citation and license propagation behavior;
- log and run-record paths.

## Rejection Conditions

Reject a wrapper when:

- it is generated ad hoc by the agent;
- it downloads model weights without explicit metadata and approval;
- it writes outside the approved run directory;
- it contains broad shell composition without review;
- it hides scheduler account, partition, or module requirements;
- it suppresses errors without preserving logs;
- it does not preserve citation, license, and limitations in the run record.

## Slurm Wrapper Minimum

A Slurm wrapper should expose these fields before submission:

- `account`;
- `partition`;
- `time_limit`;
- `cpu_cores`;
- `memory_gb`;
- `modules` or container image;
- stdout and stderr paths;
- run directory;
- exact scientific command.

Submitting a Slurm job is an execution action. The agent must ask for approval before submission unless the user has already granted explicit approval for that exact request.

