---
name: codebase-analyzer
description: "Inspect a repository to explain its architecture, runtime paths, dependencies, conventions, and change impact from source evidence."
---

# Codebase Analysis

Inspect the portion of the repository needed for the question. Start with the
working tree, manifests, entry points, and nearby tests. Use an existing code-to-
document map when it helps locate relevant evidence, then verify claims in code.

## Evidence to collect

- Languages, frameworks, package managers, runtime versions, and build commands.
- Entry points, routes, services, data stores, and external integrations.
- Data and control flow through the affected feature, including errors.
- Naming, module boundaries, dependency patterns, and test conventions.
- Configuration, migrations, CI checks, deployment files, and operational hooks
  relevant to the requested change.

Follow a representative request or operation end to end. Link findings to
actual files and symbols. Distinguish declared dependencies from runtime use
and generated code from maintained source. Scale exploration to uncertainty.

For a project profile, summarize stack, directory responsibilities, key flows,
tests, risks, and the commands needed to reproduce findings. Build a feature
inventory from reachable code or documented behavior, identifying evidence gaps.
For implementation work, use the findings directly to choose and verify the
change. A standalone analysis request ends with the requested explanation.
