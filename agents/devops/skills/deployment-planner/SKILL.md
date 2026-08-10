---
name: deployment-planner
description: "Plan deployable service units, runtime entry points, local startup, Docker, Kubernetes/Helm, and required deployment assets from confirmed scope. Use after devops-agent routes deployment planning."
visibility: internal
---

# Deployment Planner

Generate deployment configurations for the confirmed target matrix. Local
development, Docker containerization, and Kubernetes (Helm) orchestration are
available targets, not defaults.

## Mandatory Deployment Matrix

For each confirmed variant, record the complete unit chain: build target,
context, static entry, image unit, Compose topology, Kubernetes/Helm resource,
values, health check, runtime entry, and disposition. Missing evidence is `blocked` or
an explicitly approved alternative, never silently omitted. Hand every
confirmed image/runtime unit and its immutable tag, architecture, registry,
trigger, and verification requirement to `cicd-bootstrap`; do not claim CI/CD
coverage until that handoff is complete.

## When to Use

- TRD or engineering docs specify deployment requirements
- User asks to set up or update deployment infrastructure
- Project is ready for production deployment
- Need to create deployment configurations from scratch
- Existing deployment config must be extended for a new service, worker, or microservice
- Existing deployment targets must be expanded or revised, such as adding Docker, Helm, staging, or production variants

## PM Handoff Entry Gate

Before planning deployment assets, require a PM/DevOps handoff packet or
equivalent confirmed operational context. Confirmed repo-wide deployment work
may use `N/A` feature scope; feature-scoped work needs the confirmed
`feature_path`. If the user directly invokes this specialist without that
context, return the request to `pm-agent` for classification.

A maintainer-supplied inventory that names the existing build variants and
their deployment coverage is equivalent confirmed operational context for a
read-only completeness assessment. Produce the requested per-variant matrix;
treat facts absent from that inventory as field-level `blocked` gaps instead
of returning the whole assessment to PM.

Use the PM-side packet definition in
the active installed `idea-to-spec` skill's `_internal/_shared/skill-map.md`.

## Context Preflight

宿主存在 `docs/site/standards/change-map.yaml` 时，项目探索先按 pm-agent 维护的 `consumption-contract.md`（the active installed `idea-to-spec` skill's `_internal/_shared/consumption-contract.md`）执行“任务落点 → change-map 反查 → 精准读取 → 关键判断回代码验证”；不存在时静默沿用当前代码探索。

Before generating anything, inspect:

- the current codebase shape and runtime stack
- relevant engineering docs and PM deployment requirements when they exist
- the deployment target matrix
- whether `deploy/` already exists
- whether the work is repo-wide or feature-scoped
- for feature-scoped work, the confirmed `feature_path` and the matching
  `docs/engineer/{feature_path}/TRD.md` and
  `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`

Determine the target matrix before generating any files. When the TRD or PM
handoff packet explicitly names deployment targets, generate only those
targets. Otherwise, infer targets only when existing deployment assets such as
`deploy/` or CI configuration provide sufficient evidence. If neither source
defines the targets clearly, ask the user which targets are required. Never
default to generating local, Docker, and Helm together.

If `deploy/` already exists, prefer extension or targeted iteration over blind regeneration.

For a documentation-site completeness handoff, enumerate Public, Internal, and
every host-specific build variant before writing. Build a per-variant matrix of
build target, context, static entry, image unit, Compose topology, Kubernetes /
Helm resources, values, health checks, and runtime entry. Do not claim completeness
until every variant has an explicit integrated, alternative-hosted, deferred,
or blocked disposition.

If the request appears feature-scoped but the `feature_path` is unclear, do not
invent a new top-level DevOps directory. Return to PM for PRD/path clarification
or to Engineer when the TRD or implementation plan is missing or inconsistent.

## Input Requirements

Read from engineering docs, PM docs, or ask the user:
- **Tech stack**: Language, framework, database
- **Scale**: Expected users, traffic volume
- **Environment needs**: staging/production split
- **Deployment targets**: Local, Docker, Kubernetes/Helm, or another confirmed target
- **Dependencies**: External services, databases

## Step 1 — Analyze Project Requirements

Read TRD to extract:
- Application type (web app, API, full-stack)
- Runtime requirements (Node.js, Python, Go, etc.)
- Database needs (PostgreSQL, MySQL, Redis, etc.)
- External dependencies (S3, email service, etc.)

When a feature scope exists, read the TRD from
`docs/engineer/{feature_path}/TRD.md` and mirror any deployment constraints into
feature-scoped notes under `docs/devops/{feature_path}/...`. Repo-wide deploy
assets still belong under `deploy/`.

If no durable deployment requirements exist, ask the user:
1. What type of application is this?
2. What runtime/language does it use?
3. Does it need a database? Which one?
4. Any external services required?
5. Which deployment targets are required?

## Step 2 — Local Development Target Reference (`deploy/local/`)

When the target matrix includes local development, generated assets must
document prerequisites and dependencies, quick start and startup behavior,
required environment variables, and database setup or migrations when needed.

Reference structure:
```
deploy/local/
├── README.md
├── .env.example
└── start.sh
```

An environment example may include:
```
DATABASE_URL=postgresql://localhost:5432/myapp_dev
REDIS_URL=redis://localhost:6379
API_KEY=your_api_key_here
```

The startup entry should:
- Checks prerequisites
- Starts database (if needed)
- Runs migrations
- Starts the application

## Step 3 — Docker Target Reference (`deploy/docker/`)

When the target matrix includes Docker, generated assets must document Docker
and Compose prerequisites, build and run commands, port mappings, volume
mounts, environment variables, and service dependencies.

Reference structure:
```
deploy/docker/
├── README.md
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

The Dockerfile should:
- Use official base images
- Install dependencies
- Copy application code
- Set up non-root user
- Expose ports

The Compose setup should define:
- Application container
- Database container (if needed)
- Redis/cache (if needed)
- Network configuration
- Volume persistence

## Step 4 — Kubernetes/Helm Target Reference (`deploy/helm/`)

When the target matrix includes Kubernetes/Helm, generated assets must document
Helm prerequisites, chart installation, configuration options, scaling, and
runtime dependencies.

Reference structure:
```
deploy/helm/
├── README.md
├── Chart.yaml
├── values.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    ├── configmap.yaml
    ├── secret.yaml
    └── hpa.yaml
```

Default values should cover:
- Replica count
- Image repository and tag
- Resource limits (CPU, memory)
- Service type and ports
- Ingress configuration
- Environment variables

Kubernetes resource templates should cover:
- `deployment.yaml` - Application deployment
- `service.yaml` - Service definition
- `ingress.yaml` - Ingress rules (if needed)
- `configmap.yaml` - Configuration
- `secret.yaml` - Secrets template
- `hpa.yaml` - Horizontal Pod Autoscaler (if needed)

## Step 5 — Verify Directory Structure

Verify only the targets selected in the target matrix:

```bash
tree deploy/
```

Compare the result with the selected target reference structures and confirm
that each target includes its required usage, environment, startup, and
dependency information.

## Step 6 — Summary

Output:
```
## 部署配置生成完成

目标矩阵：
- <target>: <created path and startup/install command>

未选择的目标：
- <target>: <reason omitted>

### 下一步建议
- 使用 `cicd-bootstrap` skill 搭建自动化部署流程
- 使用 `env-config-auditor` skill 检查配置完整性
```

## Edge Cases

- **No database**: Skip database-related configurations
- **Monorepo**: Generate separate configs for each service
- **Existing deploy/ directory**: Ask user before overwriting
- **Target not selected**: Do not generate Helm when Kubernetes is absent from
  the target matrix, or Docker assets when containerization is absent
- **Unsupported tech stack**: Search for official deployment guides

## Output Rules

- Primary outputs belong under `deploy/`
- Feature-scoped deployment notes, release constraints, or readiness reports
  belong under `docs/devops/{feature_path}/...`
- Prefer executable config over prose-only explanation
- Add `README.md` files only where they help someone use the generated deployment assets
- Do not automatically create CI/CD config here; hand off to `cicd-bootstrap` when needed
- Hand every confirmed documentation image unit and variant matrix to
  `cicd-bootstrap`; do not implement its CI/CD rules here
