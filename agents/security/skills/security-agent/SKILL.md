---
name: security-agent
description: "Review application security, authentication and authorization, dependencies, and personal-data flows with code-backed findings."
---

# Security Review

Identify the requested scope, assets, entry points, trust boundaries, and
available evidence. Use the relevant capability directly and combine review,
remediation, tests, and documentation within the user's authorized task.

| Surface | Reference |
| --- | --- |
| Application inputs, sinks, and configuration | [AppSec review](../appsec-checklist/SKILL.md) |
| Identity, permissions, and sessions | [Authorization review](../authz-reviewer/SKILL.md) |
| Packages, provenance, and advisories | [Dependency audit](../dependency-risk-auditor/SKILL.md) |
| Collection, storage, sharing, and deletion | [Privacy mapping](../privacy-surface-mapper/SKILL.md) |

Trace findings to reachable code and concrete impact. Calibrate severity and
confidence separately, distinguish observations from hypotheses, and keep
sensitive evidence protected. Use a safe reproduction where it improves
confidence and fits the authorized environment.

Present actionable findings with locations, preconditions, impact, and repair
options. Report coverage and limitations even when the review finds no defect.
