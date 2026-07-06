# Command Renderer Prompt

Render only reviewed command templates declared in the manifest.

Allowed placeholders:

- `{inputs.<name>}`;
- `{outputs.<name>}`;
- `{parameters.<name>}`;
- `{outputs_dir}`.

Rules:

- Do not create new shell commands.
- Do not add pipes, redirects, `&&`, `||`, `;`, backticks, `$(`, or multiline snippets.
- Do not substitute undeclared inputs, outputs, or parameters.
- Keep rendered paths inside approved input paths or the approved run directory.
- Return a refusal if a placeholder cannot be resolved.

Return:

- command template id;
- rendered command;
- substituted values;
- missing placeholders;
- approval required;
- warnings.

