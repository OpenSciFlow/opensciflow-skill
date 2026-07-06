# Overview

OpenSciFlow Skill is an early adapter layer for AI agents that need to use scientific tools safely and reproducibly.

It is built around a conservative sequence:

```text
manifest first
workflow template first
dry-run first
approval before execution
run record always
fail closed on missing metadata
```

The skill is not a tool runner by itself. It defines the behavior, schemas, prompts, and examples that an agent or coding assistant can follow when integrating OpenSciFlow protocol artifacts.

