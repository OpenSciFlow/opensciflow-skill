# Evaluation Plan

Research question:

> Can standardized tool manifests reduce the context and trial-and-error cost of AI agents in scientific computing?

## Baseline A

The agent reads README files, installation docs, GitHub issues, paper instructions, and examples directly to install and run a scientific tool.

## OpenSciFlow Mode B

The agent reads:

- `opensciflow.yaml`;
- workflow template;
- local agent contract;
- readiness evidence.

## Metrics

| Metric | Baseline A | OpenSciFlow Mode B | Notes |
|---|---:|---:|---|
| Token usage before first plan | TBD | TBD | Count prompt + retrieved context. |
| Number of attempts | TBD | TBD | Count command attempts and plan revisions. |
| Failed commands | TBD | TBD | Shell or runner failures before success. |
| Time to first dry run | TBD | TBD | From task start to dry-run completion. |
| Time to first execution | TBD | TBD | From task start to first full execution. |
| Human intervention count | TBD | TBD | User corrections or approvals. |
| License completeness | TBD | TBD | Required license fields present. |
| Citation completeness | TBD | TBD | Required citation fields present. |
| Run-record completeness | TBD | TBD | Required run-record fields present. |
| Reproducibility score | TBD | TBD | Composite of hashes, versions, commands, artifacts. |

## Initial Benchmark Tasks

| Task | Tool | Baseline source | OpenSciFlow source | Success criterion |
|---|---|---|---|---|
| MD RMSD analysis | GROMACS or MDAnalysis | README/docs | manifest + workflow template | Dry run and mock run record. |
| Docking | DiffDock | upstream docs | manifest + workflow template | Refuse if weights/license missing; otherwise dry run. |
| Structure prediction | Boltz | upstream docs | manifest + workflow template | Render reviewed command and record requirements. |

## Interpretation

The evaluation should measure agent reliability and metadata completeness, not scientific accuracy.

OpenSciFlow Mode B should be considered useful if it reduces failed commands, missing metadata, and unrecorded execution details while preserving explicit limitations.

