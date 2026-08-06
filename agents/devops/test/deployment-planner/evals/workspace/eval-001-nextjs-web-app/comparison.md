# Eval Result: eval-001-nextjs-web-app

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-001-nextjs-web-app`
- Test case: `nextjs-web-app`
- Workspace: `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/deployment-planner/evals/evals.json`
- Metadata: `agents/devops/test/deployment-planner/evals/workspace/eval-001-nextjs-web-app/eval_metadata.json`
- Expected output: 在 deploy/ 目录下生成三个子目录，每个包含 README.md 和相应的配置文件
- Fixture: `PM_HANDOFF.md`, `package.json`, `app/api/health/route.ts`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `deploy_local_readme_md` | PASS | PASS | 两条 lane 均存在 deploy/local/README.md。 |
| `deploy_local_env_example_database_url_redis_url` | PASS | PASS | 两条 lane 的 deploy/local/.env.example 均包含 DATABASE_URL 和 REDIS_URL。 |
| `deploy_local_start_sh` | PASS | PASS | 两条 lane 的 deploy/local/start.sh 均具有可执行权限（-rwxr-xr-x）。 |
| `deploy_docker_dockerfile` | PASS | PASS | 两条 lane 均存在 deploy/docker/Dockerfile。 |
| `deploy_docker_docker_compose_yml_app_postgres_redis` | PASS | FAIL | with_skill 存在 deploy/docker/docker-compose.yml，且包含 app、postgres、redis；without_skill 仅有 compose.yaml，目标 docker-compose.yml 缺失。 |
| `deploy_helm_chart_yaml` | PASS | FAIL | with_skill 存在 deploy/helm/Chart.yaml；without_skill 的 Chart.yaml 位于 deploy/helm/analytics-web/Chart.yaml，目标路径缺失。 |
| `deploy_helm_values_yaml_replicacount` | PASS | FAIL | with_skill 的 deploy/helm/values.yaml 包含 replicaCount；without_skill 目标路径 deploy/helm/values.yaml 缺失，文件位于嵌套目录。 |
| `deploy_helm_templates_deployment_yaml` | PASS | FAIL | with_skill 存在 deploy/helm/templates/deployment.yaml；without_skill 目标路径缺失，文件位于 deploy/helm/analytics-web/templates/deployment.yaml。 |

## With-Skill Behavior

- with_skill 实际产物满足全部 8 项断言，覆盖完整，因此 durable Overall 为 PASS。without_skill 作为对照在 4 项路径/文件断言上失败，但不影响 durable Overall。
- Workspace changes: added: `deploy/docker/.dockerignore`, `deploy/docker/.env.example`, `deploy/docker/Dockerfile`, `deploy/docker/README.md`, `deploy/docker/docker-compose.yml`, `deploy/helm/Chart.yaml`, `deploy/helm/README.md`, `deploy/helm/templates/_helpers.tpl`, `deploy/helm/templates/configmap.yaml`, `deploy/helm/templates/deployment.yaml`, `deploy/helm/templates/hpa.yaml`, `deploy/helm/templates/ingress.yaml`, `deploy/helm/templates/secret.yaml`, `deploy/helm/templates/service.yaml`, `deploy/helm/values.yaml`, `deploy/local/.env.example`, `deploy/local/README.md`, `deploy/local/start.sh`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `deploy/README.md`, `deploy/docker/Dockerfile`, `deploy/docker/README.md`, `deploy/docker/compose.yaml`, `deploy/helm/analytics-web/Chart.yaml`, `deploy/helm/analytics-web/README.md`, `deploy/helm/analytics-web/templates/_helpers.tpl`, `deploy/helm/analytics-web/templates/deployment.yaml`, `deploy/helm/analytics-web/templates/ingress.yaml`, `deploy/helm/analytics-web/templates/service.yaml`, `deploy/helm/analytics-web/values.yaml`, `deploy/local/.env.example`, `deploy/local/.gitignore`, `deploy/local/README.md`, `deploy/local/start.sh`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（8/8）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
