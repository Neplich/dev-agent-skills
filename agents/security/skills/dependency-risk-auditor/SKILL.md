---
name: dependency-risk-auditor
description: "Audit resolved dependencies for relevant vulnerabilities, maintenance, licensing, provenance, and supply-chain risk."
---

# Dependency Risk Audit

Inspect ecosystem manifests and lockfiles to determine resolved versions and
direct/transitive dependency relationships. Trace how important packages are
used at build time and runtime.

Examples of evidence sources include package.json and package-lock.json,
pyproject.toml and Python lockfiles, go.mod/go.sum, Gemfile.lock, Maven/Gradle
metadata, and Cargo.lock. Use the ecosystem's available audit tooling and
current authoritative advisories for vulnerability claims.

## Assess applicability

- Record advisory identifiers, affected version ranges, and the resolved package.
- Trace reachable vulnerable behavior and the runtime conditions required.
- Inspect transitive paths and whether an upgrade can be made at a direct parent.
- Check maintenance, repository status, deprecation, ownership, provenance, and
  license information with dated evidence.
- Separate package advisory severity from the application's demonstrated impact.

Recommend a verified target version or mitigation, describing compatibility
changes and the tests needed to validate it. For requested upgrades, update
through the project's package manager, review the lockfile diff, and run
relevant build and behavior checks.

Report audited scope, tool/advisory dates, findings, reachability, remediation,
and unavailable evidence. Protect registry credentials and keep captured audit
output free of secret values.
