# Eval Result: eval-001-missing-variables

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-001-missing-variables`
- Test case: `missing-variables`
- Workspace: `agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables`

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
- Metadata: `agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables/eval_metadata.json`
- Expected output: 生成 durable 审计报告，指出 deploy 和 CI/CD 配置中缺失的变量
- Fixture: metadata 未声明 `fixture_context`；本轮复制 workspace 中除 comparison、metadata、README 和声明输出外的纯净 fixture 文件。

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `deploy_env_audit_md_docs_devops_feature_path_env_audit_md` | PASS | FAIL | with_skill 创建了 deploy/ENV_AUDIT.md；without_skill 未创建耐久审计报告文件。 |
| `missing_variables` | PASS | FAIL | with_skill 报告包含 ## Missing Variables 章节并列出 API_KEY、REDIS_URL 等缺失项；without_skill 仅输出摘要，没有该章节。 |
| `api_key_stripe_secret_key_deploy_ci_cd` | PASS | PASS | with_skill 明确指出 API_KEY 在 CI/CD 缺失；without_skill 也明确指出 CI 缺少 API_KEY。 |
| `recommendations` | PASS | FAIL | with_skill 报告包含 ## Recommendations 章节；without_skill 未生成报告或 Recommendations 章节。 |

## With-Skill Behavior

- with_skill 的四项断言均满足且全部可评估，因此 durable Overall 按 binding_result_model 为 PASS；without_skill 仅作对照，基线缺少耐久报告并不改变 durable Overall。
- Workspace changes: added: `deploy/ENV_AUDIT.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PARTIAL，原因是没有 fresh without_skill baseline；issue #234 后进一步标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
