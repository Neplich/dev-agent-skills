# Eval Result: eval-001-docker-rollback

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-001-docker-rollback`
- Test case: `docker-rollback`
- Workspace: `agents/devops/test/incident-playbook-writer/evals/workspace/eval-001-docker-rollback`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: FAIL
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: FAIL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/incident-playbook-writer/evals/evals.json`
- Metadata: `agents/devops/test/incident-playbook-writer/evals/workspace/eval-001-docker-rollback/eval_metadata.json`
- Expected output: 仅生成用户明确请求且有仓库证据支撑的回滚与故障响应手册，不默认生成排查和值班文档
- Fixture: `PM_HANDOFF.md`, `deploy/docker/docker-compose.yml`, `deploy/docker/.env.example`, `deploy/docker/README.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `deploy_rollback_md` | PASS | PASS | 两条 lane 均实际生成 deploy/ROLLBACK.md。 |
| `rollback_md_docker` | PASS | PASS | 两条 lane 的 ROLLBACK.md 均包含 Docker Compose 拉取镜像、重建 app、状态/日志/health 验证等命令。 |
| `deploy_incident_response_md` | PASS | PASS | 两条 lane 均实际生成 deploy/INCIDENT_RESPONSE.md。 |
| `incident_response_md` | PASS | PASS | 两条 lane 的 INCIDENT_RESPONSE.md 均覆盖应用不可用、healthcheck 失败、容器重启/启动失败、发布后降级等常见故障场景。 |
| `does_not_generate_unrequested_playbooks` | FAIL | FAIL | 两条 lane 均额外生成 deploy/TROUBLESHOOTING.md 和 deploy/ON_CALL.md；实际输出明确称生成四份手册，违反仅生成回滚与故障响应手册的断言。 |

## With-Skill Behavior

- with_skill 的五条断言均可核对，Coverage 为 FULL；但额外生成未请求的 TROUBLESHOOTING.md 与 ON_CALL.md，因此 durable Overall 按 binding_result_model 判定为 FAIL。without_skill 同样失败，仅作为对照。
- Workspace changes: added: `deploy/INCIDENT_RESPONSE.md`, `deploy/ON_CALL.md`, `deploy/ROLLBACK.md`, `deploy/TROUBLESHOOTING.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `deploy/INCIDENT_RESPONSE.md`, `deploy/ON_CALL.md`, `deploy/ROLLBACK.md`, `deploy/TROUBLESHOOTING.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `does_not_generate_unrequested_playbooks`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（5/5）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
