---
name: incident-playbook-writer
description: "Write evidence-backed rollback guidance, incident response steps, troubleshooting runbooks, and on-call preparation for a confirmed deployment surface. Use after devops-agent routes the incident-playbook scope."
visibility: internal
---

# Incident Playbook Writer

Create operational runbooks for common incidents and failure scenarios.

## Mandatory Runbook Evidence

Read any mapped operational document first, record its freshness, then verify
alerts, thresholds, rollback actions, and recovery checks against code,
configuration, or executable tests. An `unverified` document is low-trust. If
documented and implemented thresholds differ, state both values and explain
how the difference changes detection, escalation, rollback timing, and release
risk instead of choosing one silently.

## When to Use

- Before first production deployment
- After experiencing an incident
- Setting up on-call procedures
- Need rollback documentation
- After adding a new service, worker, or deployment target
- When existing rollback or troubleshooting docs are outdated
- When operational procedures must be revised after topology or release-process changes

## PM Handoff Entry Gate

Before writing runbooks, require a PM/DevOps handoff packet or equivalent
confirmed operational context. Confirmed repo-wide incident or rollback work may
use `N/A` feature scope; feature-scoped runbooks need the confirmed
`feature_path`. If the user directly invokes this specialist without that
context, return the request to `pm-agent` for classification.

Use the PM-side packet definition in
the plugin-local generated `../devops-agent/_internal/_generated/shared-contracts/handoff-contract.md`.

## Context Preflight

宿主存在 `docs/site/standards/change-map.yaml` 时，项目探索先按 pm-agent 维护的 `consumption-contract.md`（the plugin-local generated `../devops-agent/_internal/_generated/shared-contracts/consumption-contract.md`）执行“任务落点 → change-map 反查 → 精准读取 → 关键判断回代码验证”；不存在时静默沿用当前代码探索。

Before generating playbooks, inspect:

- which deployment methods are actually configured under `deploy/`
- current CI/CD and operational entrypoints if they affect rollback or incident response
- whether this is a repo-wide runbook or tied to a specific feature/release
- existing runbooks so you can extend rather than overwrite by habit
- for feature-scoped runbooks, the confirmed `feature_path`,
  `docs/engineer/{feature_path}/TRD.md`, and
  `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`

If feature scope is requested but `feature_path` is unclear, do not invent a
new top-level `docs/devops/{name}/` directory. Return to PM for PRD/path
clarification or Engineer for missing or stale TRD/implementation plan.

## Step 1 — Identify Deployment Method

Check which deployment methods are configured:
```bash
ls deploy/docker/ deploy/helm/ 2>/dev/null
```

Also inspect whether local-only deployment exists and whether rollback is even meaningful for the current setup.

## Step 2 — Confirm Requested Playbooks

Before generating files, confirm which playbooks the user needs:

- `deploy/ROLLBACK.md` — rollback guidance
- `deploy/INCIDENT_RESPONSE.md` — incident response
- `deploy/TROUBLESHOOTING.md` — troubleshooting
- `deploy/ON_CALL.md` — on-call guidance

If the user has not named the required playbooks, present these four candidates
and ask them to select. Do not generate all four by default. Generate only the
files the user explicitly selects.

For each selected playbook, verify that the repository and operational context
provide enough evidence to write actionable guidance. If evidence is missing,
do not generate it. Report the gap and name the evidence needed, such as
monitoring and alerts for incident response or an established rotation and
escalation mechanism for on-call guidance.

## Step 3 — Write Selected Playbooks

- `deploy/ROLLBACK.md` must include the supported rollback actions and recovery
  checks. Database migration rollback, cache clearing, previous-image restore,
  and `helm rollback` are example topics to include only when applicable.
- `deploy/INCIDENT_RESPONSE.md` must include evidence-backed incident scenarios,
  detection and investigation steps, recovery actions, and restoration checks.
  Application, database, resource, and deployment failures are example
  scenarios, not a required fixed structure.
- `deploy/TROUBLESHOOTING.md` must include repository-specific diagnostic
  entrypoints, status, log and resource checks, plus escalation or recovery
  conditions. Container log, status, shell, CPU, memory, and disk commands are
  example content to adapt to the configured runtime.
- `deploy/ON_CALL.md` must include established escalation contacts, actionable
  alerts and thresholds, response-time expectations, and communication
  channels. Monitoring, rotation, and escalation evidence are required before
  generating it.

## Step 4 — Summary

Summarize only the files actually created and any requested files that were
blocked by missing evidence. A list of created paths and a separate list of
blocked paths with their missing evidence is one acceptable example; the exact
summary structure is not fixed.

## Edge Cases

- **No deploy/ directory**: Create it first
- **Custom deployment**: Ask for specific procedures
- **Multiple services**: Generate separate playbooks only when explicitly requested

## Output Rules

- Primary outputs belong in durable operational paths under `deploy/`
- Feature-scoped rollback, release, or incident supplements belong under
  `docs/devops/{feature_path}/...`
- Tie instructions to the repository's actual deployment methods and commands
- Do not generate generic on-call prose detached from the configured runtime
- Generate only the playbooks explicitly selected by the user
