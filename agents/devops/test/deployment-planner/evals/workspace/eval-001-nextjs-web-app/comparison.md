# Eval Result: eval-001-nextjs-web-app

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-001-nextjs-web-app`
- Test case: nextjs-web-app
- Workspace: `workspace/eval-001-nextjs-web-app`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 8/8 assertions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed repo-wide deployment handoff, Next.js manifest, and health endpoint
- Expected output: 在 deploy/ 目录下生成三个子目录，每个包含 README.md 和相应的配置文件

## Assertions

- PASS `deploy_local_readme_md`: 生成 local README。
- PASS `deploy_local_env_example_database_url_redis_url`: local env 包含 `DATABASE_URL` 与 `REDIS_URL`。
- PASS `deploy_local_start_sh`: local start script 可执行。
- PASS `deploy_docker_dockerfile`: 生成 Dockerfile。
- PASS `deploy_docker_docker_compose_yml_app_postgres_redis`: Compose 包含 app、postgres、redis。
- PASS `deploy_helm_chart_yaml`: 生成 Helm Chart。
- PASS `deploy_helm_values_yaml_replicacount`: values 包含 `replicaCount`。
- PASS `deploy_helm_templates_deployment_yaml`: 生成 deployment template。

## With Skill

- 除满足 8 项断言外，还提供 multi-stage/non-root 镜像、依赖健康门禁、持久卷、外部服务 values、probes 与 resources。
- with_skill 与 baseline 的 Compose 均通过 `config --quiet`。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 deployment-planner skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 8/8 assertions，但镜像加固、健康门禁和 Helm 运行约束较简略。

## Failures

- 无 assertion failure。
- 环境中没有 Helm，未运行 `helm lint`；当前 assertions 对 skill 增益的区分度有限。

## Next Steps

- 保留 local、Docker、Helm 三目标覆盖。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics were generated only in an ignored scratch workspace and are not committed.
