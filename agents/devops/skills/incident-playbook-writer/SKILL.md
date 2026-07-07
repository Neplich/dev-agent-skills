---
name: incident-playbook-writer
description: "Internal DevOps specialist—not a direct entry point. Invoked by devops-agent after pm-agent handoff to write rollback guidance, incident response steps, troubleshooting runbooks, and on-call preparation tied to deployment setup."
visibility: internal
---

# Incident Playbook Writer

Create operational runbooks for common incidents and failure scenarios.

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
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

## Context Preflight

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

## Step 2 — Create Rollback Playbook

### 2.1 Create `deploy/ROLLBACK.md`

For Docker deployment:
- How to rollback to previous image version
- Database migration rollback steps
- Cache clearing procedures

For Helm deployment:
- `helm rollback` command
- Check rollback status
- Verify application health

## Step 3 — Create Incident Response Guide

### 3.1 Create `deploy/INCIDENT_RESPONSE.md`

Common scenarios:
- **Application Down**: Health check, logs, restart procedure
- **Database Connection Failed**: Check credentials, network, restart
- **High CPU/Memory**: Identify cause, scale up, restart
- **Deployment Failed**: Rollback steps, log collection

## Step 4 — Create Troubleshooting Guide

### 4.1 Create `deploy/TROUBLESHOOTING.md`

Debug commands:
- View logs: `docker logs` / `kubectl logs`
- Check status: `docker ps` / `kubectl get pods`
- Access shell: `docker exec` / `kubectl exec`
- Check resources: CPU, memory, disk usage

## Step 5 — Create On-Call Guide

### 5.1 Create `deploy/ON_CALL.md`

Document:
- Escalation contacts
- Critical alerts and thresholds
- Response time expectations
- Communication channels

## Step 6 — Summary

Output:
```
## 运维手册生成完成

已创建以下文档：

- `deploy/ROLLBACK.md` - 回滚操作指南
- `deploy/INCIDENT_RESPONSE.md` - 故障响应流程
- `deploy/TROUBLESHOOTING.md` - 问题排查手册
- `deploy/ON_CALL.md` - 值班指南

### 建议
- 团队成员熟悉这些流程
- 定期演练回滚操作
```

## Edge Cases

- **No deploy/ directory**: Create it first
- **Custom deployment**: Ask for specific procedures
- **Multiple services**: Generate separate playbooks

## Output Rules

- Primary outputs belong in durable operational paths under `deploy/`
- Feature-scoped rollback, release, or incident supplements belong under
  `docs/devops/{feature_path}/...`
- Tie instructions to the repository's actual deployment methods and commands
- Do not generate generic on-call prose detached from the configured runtime
