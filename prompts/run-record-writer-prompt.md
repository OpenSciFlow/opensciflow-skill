# Run Record Writer Prompt

Write an OpenSciFlow run record after dry-run, smoke-test, full execution, or post-start failure.

The run record must include:

- run id;
- workflow id;
- tool manifest id;
- timestamps;
- status;
- commands;
- parameters;
- input files;
- output files;
- tool versions;
- environment;
- model weights;
- hardware;
- logs;
- artifacts;
- file hashes;
- return code;
- license;
- citation;
- limitations;
- warnings.

Do not omit failed steps. If execution fails, record status `failed`, return code, log path, and known artifacts.

Do not claim scientific validation beyond what the run record supports.

