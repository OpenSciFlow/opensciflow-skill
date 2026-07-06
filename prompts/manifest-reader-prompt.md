# Manifest Reader Prompt

Read the provided `opensciflow.yaml` manifest.

Extract only fields that are present. Do not fill missing fields from memory.

Required extraction:

- manifest name and version;
- domain and task types;
- inputs and outputs;
- environment;
- hardware;
- model weights;
- execution command templates;
- validation commands;
- readiness evidence;
- license;
- citation;
- safety notes;
- limitations.

If a required field is missing, report it under `missing_requirements`.

Do not execute commands. Do not render commands. This step is read-only.

