# Dry-run Output

Dry-run command:

```text
gmx --version
```

Expected readiness signal:

```text
GROMACS version information is printed.
Exit code: 0
```

If `gmx` is missing, the agent must stop before rendering or executing the RMSD command.

