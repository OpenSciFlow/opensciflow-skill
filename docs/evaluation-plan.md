# Evaluation Plan

Research question:

> Can verified execution capsules help agents check requirements earlier, refuse unsafe execution more consistently, and record scientific tool runs more completely?

This evaluation should not claim that OpenSciFlow makes tools run across all environments. It measures inspection quality, refusal quality, smoke-test behavior, and run-record completeness.

## Baseline A

The agent reads upstream READMEs, installation docs, GitHub issues, paper instructions, examples, and HPC notes directly.

## OpenSciFlow Mode B

The agent reads:

- verified execution capsule;
- `opensciflow.yaml`;
- environment spec;
- reviewed command templates;
- smoke-test definition;
- verified environment matrix;
- known failure records;
- prior run records.

## Metrics

| Metric | Baseline A | OpenSciFlow Mode B | Notes |
|---|---:|---:|---|
| Missing requirement detection | TBD | TBD | Inputs, weights, hardware, scheduler, license, citation. |
| Unsafe command refusal | TBD | TBD | Whether arbitrary LLM-generated shell is blocked. |
| Known failure reporting | TBD | TBD | Whether matching failure cases are surfaced before execution. |
| Smoke-test success or blocked reason | TBD | TBD | Only measured when smoke tests exist. |
| Failed command attempts | TBD | TBD | Count command failures before a valid run or refusal. |
| Human intervention count | TBD | TBD | User corrections, approvals, or missing information. |
| License completeness | TBD | TBD | Required license fields present. |
| Citation completeness | TBD | TBD | Required citation fields present. |
| Run-record completeness | TBD | TBD | Required run-record fields present after an attempted execution. |
| Verified environment match | TBD | TBD | Whether target environment is inside or outside verified matrix. |

## Initial Benchmark Tasks

| Task | Tool | Baseline source | OpenSciFlow source | Success criterion |
|---|---|---|---|---|
| MD RMSD analysis | GROMACS or MDAnalysis | Upstream docs | Capsule + reviewed command template | Check requirements, run smoke test if available, write run-record template. |
| Docking | DiffDock | Upstream docs | Capsule + known failure records | Refuse if weights/license/checksum are missing; otherwise render reviewed command. |
| Structure prediction | Boltz | Upstream docs | Capsule + environment matrix | Report environment mismatch instead of claiming portability. |

## Interpretation

R1/R2 artifacts can only be evaluated for metadata clarity and inspection cost.

R4/R5 artifacts can be evaluated for smoke-test behavior, failed-command reduction in the verified environment, and run-record completeness.

R6/R7 artifacts can be evaluated for limited cross-environment migration evidence.

The evaluation should measure agent reliability and metadata completeness, not scientific accuracy or experimental validity.
