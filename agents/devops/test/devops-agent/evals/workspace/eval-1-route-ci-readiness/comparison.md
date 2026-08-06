# Eval Result: eval-001-route-ci-readiness

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-001-route-ci-readiness`
- Test case: `route-ci-readiness`
- Workspace: `agents/devops/test/devops-agent/evals/workspace/eval-1-route-ci-readiness`

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
- Eval definition: `agents/devops/test/devops-agent/evals/evals.json`
- Metadata: `agents/devops/test/devops-agent/evals/workspace/eval-1-route-ci-readiness/eval_metadata.json`
- Expected output: DevOps 路由决策，明确 CI/CD 是当前主 route，配置审计和 runbook 是后续检查，而不是一次性直接执行所有 DevOps skill。
- Fixture: `deploy/docker/README.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `routes_primary_to_cicd` | PASS | FAIL | with_skill-final 明确识别 CI/CD 为缺口，并在建议链中将 cicd-bootstrap 排在后续 DevOps 路由首位；without_skill 未进行路由决策。 |
| `keeps_deployment_context` | PASS | PASS | 两条 lane 均保留并读取 deploy/docker/README.md 上下文；with_skill-final 还明确指出该目录已存在。 |
| `names_followups` | PASS | FAIL | with_skill-final 明确列出 env-config-auditor 与 incident-playbook-writer，并按 CI/CD 后续链路排列；without_skill 仅直接编写文档，未命名这些后续 route。 |
| `does_not_run_all_skills` | FAIL | FAIL | with_skill-final 给出 pm-agent → cicd-bootstrap → env-config-auditor → incident-playbook-writer 的全链路执行建议，未清晰区分当前主 route 与后续检查；without_skill 实际直接新增 workflow、环境变量文档和回滚文档。 |
| `does_not_write_workflow` | PASS | FAIL | with_skill-status 的 changes.added/modified 均为空，且 with_skill lane 没有 .github/workflows 文件；without_skill-status 显示新增 .github/workflows/pr-checks.yml。 |

## With-Skill Behavior

- with_skill 成功识别 CI/CD 主方向、保留部署上下文并命名后续 route，也未写入 workflow；但其最终建议仍扩展为未区分主 route 与后续检查的全链路，因此 durable Behavior 为 FAIL。Coverage 为 FULL。without_skill 作为对照，直接实施了全部变更。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `.github/workflows/pr-checks.yml`, `deploy/docker/ENVIRONMENT.md`, `deploy/docker/ROLLBACK.md`；modified: `deploy/docker/README.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `does_not_run_all_skills`。
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
