# Workflow Matcher Prompt

Match the user task to an existing OpenSciFlow workflow template.

Check:

- task boundary;
- required inputs;
- expected outputs;
- steps and DAG;
- required and optional plugins;
- artifact handoff;
- fallbacks;
- report template;
- reproducibility requirements;
- limitations.

If no workflow template matches, return a refusal for execution and optionally propose a review-only draft workflow.

Do not assemble a new executable workflow ad hoc.

