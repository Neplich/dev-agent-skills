# Eval Result: eval-002-python-api-only

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-002-python-api-only`
- Test case: `python-api-only`
- Workspace: `agents/devops/test/deployment-planner/evals/workspace/eval-002-python-api-only`

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
- Metadata: `agents/devops/test/deployment-planner/evals/workspace/eval-002-python-api-only/eval_metadata.json`
- Expected output: 生成简化的部署配置，不包含数据库相关内容
- Fixture: `PM_HANDOFF.md`, `pyproject.toml`, `app/main.py`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `deploy_local_env_example_database_url` | PASS | FAIL | with_skill/deploy/local/.env.example exists and contains only APP_HOST and APP_PORT, with no DATABASE_URL. The without_skill lane lacks the expected deploy/local/.env.example artifact. |
| `deploy_docker_docker_compose_yml_app` | PASS | FAIL | with_skill/deploy/docker/docker-compose.yml defines exactly one service, api. The without_skill lane lacks the expected deploy/docker/docker-compose.yml artifact. |
| `deploy_local_start_sh` | PASS | FAIL | with_skill/deploy/local/start.sh only checks Python dependencies and starts uvicorn; it has no database initialization. The without_skill lane lacks the expected deploy/local/start.sh artifact. |

## With-Skill Behavior

- with_skill 三条断言均可核查且全部满足，因此 Coverage 为 FULL、durable Overall 为 PASS。without_skill 缺少断言所要求的文件，按 baseline_policy 判为 FAIL，但不影响 durable Overall。
- Workspace changes: added: `deploy/docker/.env.example`, `deploy/docker/Dockerfile`, `deploy/docker/README.md`, `deploy/docker/docker-compose.yml`, `deploy/helm/Chart.yaml`, `deploy/helm/README.md`, `deploy/helm/templates/_helpers.tpl`, `deploy/helm/templates/deployment.yaml`, `deploy/helm/templates/hpa.yaml`, `deploy/helm/templates/ingress.yaml`, `deploy/helm/templates/service.yaml`, `deploy/helm/values.yaml`, `deploy/local/.env.example`, `deploy/local/README.md`, `deploy/local/start.sh`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `.dockerignore`, `DEPLOYMENT.md`, `Dockerfile`, `compose.yaml`, `helm/status-api/Chart.yaml`, `helm/status-api/templates/NOTES.txt`, `helm/status-api/templates/_helpers.tpl`, `helm/status-api/templates/deployment.yaml`, `helm/status-api/templates/service.yaml`, `helm/status-api/values.yaml`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
