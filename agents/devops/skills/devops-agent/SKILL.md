---
name: devops-agent
description: Route DevOps work to the right downstream skill. Use when the user needs deployment planning, runtime packaging, Docker or Helm setup, CI/CD automation, environment variable auditing, release readiness checks, rollback/runbook documentation, or operational hardening for a repo or service. Trigger on phrases like "怎么部署", "补 docker/helm", "配 CI", "加 GitHub Actions", "环境变量对齐一下", "检查 secrets", "发布前运维准备", "写回滚手册", "做 runbook", or any DevOps-oriented request that should be routed before execution."
---

# DevOps Agent Dispatcher

`devops-agent` is the DevOps capability entry point. It recognizes whether the
request is about deployment setup, delivery automation, configuration
governance, or operational readiness, then routes to the narrowest downstream
DevOps skill.

## Role Boundary

`devops-agent` is responsible for:

- identifying the primary DevOps outcome the user wants
- selecting the narrowest downstream DevOps skill
- sequencing multiple DevOps skills only when the user clearly wants a broader
  operational workflow
- preserving an already-confirmed `feature_path` for feature-scoped DevOps
  work
- asking at most one route-level clarification question when the target outcome
  is truly ambiguous

`devops-agent` is not responsible for:

- replacing the downstream implementation protocol of
  `deployment-planner`, `cicd-bootstrap`, `env-config-auditor`, or
  `incident-playbook-writer`
- forcing every feature through a DevOps phase
- deciding or inventing a feature path when PM/Engineer docs are unclear
- acting as a general incident response or feature implementation agent

## Available Skills

- `devops-agent:deployment-planner` - Deployment assets, packaging, runtime targets, `deploy/` expansion
- `devops-agent:cicd-bootstrap` - CI/CD workflows, pipeline automation, release paths
- `devops-agent:env-config-auditor` - Environment variable, config, and secret coverage audits
- `devops-agent:incident-playbook-writer` - Rollback, runbook, and operational procedure docs

## Routing Signals

Route by the operational outcome the user wants.

- Deployment setup, Docker, Helm, runtime packaging, local/dev/prod deployment
  assets, "怎么部署", "补 deploy", "容器化", "加 helm"
  -> `deployment-planner`
- CI/CD, workflows, pipelines, release automation, build-and-deploy paths,
  "配 GitHub Actions", "上 CI", "自动部署"
  -> `cicd-bootstrap`
- Env vars, secrets coverage, config drift, missing runtime settings,
  "缺环境变量", "检查配置", "对齐 secrets"
  -> `env-config-auditor`
- Rollback guides, incident runbooks, on-call procedures, operational docs,
  "回滚手册", "故障手册", "runbook", "发布出问题怎么办"
  -> `incident-playbook-writer`

## Default Routes

| DevOps Outcome | Primary Skill |
| --- | --- |
| 新建或扩展部署配置、容器化、运行时打包、`deploy/` 资产 | `deployment-planner` |
| CI/CD、workflow、pipeline、发布自动化 | `cicd-bootstrap` |
| 环境变量、secrets、配置覆盖率、运行时配置审计 | `env-config-auditor` |
| 回滚文档、故障排查手册、运维 runbook | `incident-playbook-writer` |

If the request is DevOps-shaped but underspecified, use these defaults:

- if it is about getting software deployable -> `deployment-planner`
- if it is about automating an existing release path -> `cicd-bootstrap`
- if it is about readiness or missing configuration -> `env-config-auditor`
- if it is about operational response or rollback guidance -> `incident-playbook-writer`

## Common Multi-Skill Chains

Use these only when the user clearly wants the broader operational workflow:

- 首次部署准备 -> `deployment-planner` -> `cicd-bootstrap` -> `env-config-auditor`
- 发布前运维准备 -> `env-config-auditor` -> `incident-playbook-writer`
- 现有部署补自动化 -> `cicd-bootstrap` -> `env-config-auditor`
- 新增运行目标后补运维手册 -> `deployment-planner` -> `incident-playbook-writer`

Do not expand into a full operational chain by default.

## Escalation Rules

- Ask one route-level clarification question only when two routes are equally
  plausible and repo context cannot resolve the difference.
- If deployment and CI/CD are both needed but one is clearly foundational,
  route to the foundational step first.
- If the user is actually asking for application code changes, tests, or
  product/design work, keep the DevOps route narrow and make the next handoff
  explicit to the owning agent.

## Feature Path Gate

For feature-scoped DevOps work, consume the `feature_path` already confirmed by
PM and Engineer:

- read `docs/pm/{feature_path}/PRD.md` when product deployment constraints are
  relevant
- read `docs/engineer/{feature_path}/TRD.md` and
  `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` when engineering
  deployment, release, config, or rollback details are relevant
- write durable feature-scoped DevOps reports under
  `docs/devops/{feature_path}/...`

If the request names only a feature display name and the matching
`feature_path` is unclear, do not create a synonymous top-level
`docs/devops/{name}/` directory. Return the work to PM for PRD/path
clarification or to Engineer when the TRD/implementation plan is missing or
inconsistent. Repo-wide deployment assets and reports may still use `deploy/`.

## Output Behavior

When routing is complete:

- state which DevOps skill should handle the request
- if relevant, state the follow-up DevOps chain
- make it clear whether outputs are expected under `deploy/`,
  repo-native CI/CD paths such as `.github/workflows/`, or durable operational
  docs under `docs/devops/{feature_path}/` or `deploy/`
