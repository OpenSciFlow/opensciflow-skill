# Slurm workflow alignment

The Slurm examples must keep four artifacts aligned:

- `selected-workflow.yaml`
- `execution-request.json`
- `run-record.example.json`
- `job.sbatch.template`

The validator checks that:

- `execution-request.workflow_id` matches the selected workflow name;
- `execution-request.step_id` exists in the selected workflow;
- `execution-request.manifest_id` is listed in selected workflow plugins;
- required workflow inputs are present in execution inputs or mapped scheduler environment fields;
- workflow outputs are present in execution outputs;
- execution outputs are carried into the run record;
- wrapper placeholders are either reviewed wrapper arguments, declared input placeholders, or `run_directory`.

Run:

```bash
python scripts/validate_slurm_workflow_alignment.py
```

This check does not submit Slurm jobs. It only prevents protocol examples from drifting apart.
