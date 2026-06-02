# Eval Result: eval-001-nextjs-web-app

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-001-nextjs-web-app`
- Test case: nextjs-web-app
- Workspace: `workspace/eval-001-nextjs-web-app`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that deployment-planner handles nextjs-web-app and produces the expected role-specific artifact.
- Expected output: 在 deploy/ 目录下生成三个子目录，每个包含 README.md 和相应的配置文件

## Assertions

- `deploy_local_readme_md`: deploy/local/README.md 存在
- `deploy_local_env_example_database_url_redis_url`: deploy/local/.env.example 包含 DATABASE_URL 和 REDIS_URL
- `deploy_local_start_sh`: deploy/local/start.sh 可执行
- `deploy_docker_dockerfile`: deploy/docker/Dockerfile 存在
- `deploy_docker_docker_compose_yml_app_postgres_redis`: deploy/docker/docker-compose.yml 包含 app、postgres、redis 三个服务
- `deploy_helm_chart_yaml`: deploy/helm/Chart.yaml 存在
- `deploy_helm_values_yaml_replicacount`: deploy/helm/values.yaml 包含 replicaCount 配置
- `deploy_helm_templates_deployment_yaml`: deploy/helm/templates/deployment.yaml 存在

## With Skill

Observed behavior:

- 当前 skill 明确生成 deploy/local、deploy/docker、deploy/helm 三类部署资产；Next.js + PostgreSQL + Redis 场景下会包含 DATABASE_URL、REDIS_URL、start.sh、Dockerfile、app/postgres/redis compose 服务、Helm Chart、values replicaCount 和 deployment template。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
