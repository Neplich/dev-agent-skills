# Eval Result: eval-002-python-api-only

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-002-python-api-only`
- Test case: python-api-only
- Workspace: `workspace/eval-002-python-api-only`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 3/3 assertions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed API-only deployment handoff, FastAPI manifest, and health endpoint with an explicit no-database boundary
- Expected output: 生成简化的部署配置，不包含数据库相关内容

## Assertions

- PASS `deploy_local_env_example_database_url`: local env 不包含 `DATABASE_URL`。
- PASS `deploy_docker_docker_compose_yml_app`: Compose 仅包含 app 服务。
- PASS `deploy_local_start_sh`: start script 不包含数据库初始化。

## With Skill

- 满足 3 项负向边界断言，并额外提供 non-root 镜像、healthcheck 和 Helm probes/resources。
- Compose 解析通过。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 deployment-planner skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 3/3 assertions，没有引入数据库变量、服务或初始化步骤。

## Failures

- 无 assertion failure。
- 环境中没有 Helm，未运行 `helm lint`；当前 assertions 对 skill 增益的区分度有限。

## Next Steps

- 保留 API-only 的 no-database 负向覆盖。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics were generated only in an ignored scratch workspace and are not committed.
