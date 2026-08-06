# Eval Result: eval-004-docs-entry-access-audit

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`
- Test case: `docs-entry-access-audit`
- Workspace: `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`

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
- Eval definition: `agents/devops/test/env-config-auditor/evals/evals.json`
- Metadata: `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit/eval_metadata.json`
- Expected output: 逐环境报告 DNS/TLS、认证或网络限制、端口、探针、Ingress/Gateway、配置引用与未知项。
- Fixture: `evidence.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `audits_public_and_internal_access` | PASS | PASS | with_skill 逐行列出 Staging/Production 的 Public/Internal；Public 覆盖 DNS/TLS，Internal 覆盖认证与网络限制，并对缺失项标记 unknown。 |
| `audits_runtime_environment_differences` | PASS | FAIL | with_skill 覆盖探针、Service/Ingress、端口和值、staging/production 差异，并明确四个入口缺少 secret/config 引用证据；without_skill 未实际核对或明确记录 secret/config 引用。 |
| `does_not_overclaim_missing_evidence` | PASS | PASS | 两条 lane 均将不可检查的生产 TLS、探针、认证等标为 unknown，且明确域名或 Service 不足以证明安全/集成；with_skill 未声称已完成 formal-docs-sync。 |

## With-Skill Behavior

- with_skill 的三项断言均有实际、可评估证据，故行为 PASS、Coverage FULL，按 binding_result_model durable Overall 为 PASS。without_skill 作为对照在 secret/config 引用核对上缺失，判 baseline FAIL，但不影响 durable Overall。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
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
