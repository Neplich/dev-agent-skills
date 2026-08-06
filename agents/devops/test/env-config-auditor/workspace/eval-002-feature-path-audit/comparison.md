# Eval Result: eval-002-feature-path-audit

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-002-feature-path-audit`
- Test case: `feature-path-audit`
- Workspace: `agents/devops/test/env-config-auditor/workspace/eval-002-feature-path-audit`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: PARTIAL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS (partial coverage)

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/env-config-auditor/evals/evals.json`
- Metadata: `agents/devops/test/env-config-auditor/workspace/eval-002-feature-path-audit/eval_metadata.json`
- Expected output: 读取同一 feature_path 下的 PM/Engineer 文档，输出 docs/devops/chat-interface/messages/history/search/ENV_AUDIT.md，不生成 docs/devops/history-search/ENV_AUDIT.md 或 docs/devops/chat-interface/history-search/ENV_AUDIT.md。
- Fixture: `docs/pm/chat-interface/messages/history/search/PRD.md`, `docs/engineer/chat-interface/messages/history/search/TRD.md`, `docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md`, `src/server.ts`, `deploy/local/.env.example`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | PASS | 两条 lane 均读取了同路径的 docs/engineer/chat-interface/messages/history/search/TRD.md 与 IMPLEMENTATION_PLAN.md；with-skill trace 明确记录了这些读取。 |
| `writes_nested_devops_report` | PASS | FAIL | with-skill status 显示新增 docs/devops/chat-interface/messages/history/search/ENV_AUDIT.md；without-skill status 显示新增错误路径 docs/engineer/chat-interface/messages/history/search/ENV_CONFIG_AUDIT.md。 |
| `does_not_invent_feature_directory` | NOT_EXERCISED | NOT_EXERCISED | fixture 中 feature_path 明确，且同路径 TRD 与 IMPLEMENTATION_PLAN 均存在，因此该条件分支未触发。 |

## With-Skill Behavior

- with-skill 正确使用确认的嵌套 feature_path，并输出要求的 DevOps 审计报告路径；条件分支断言因 fixture 不具备触发前提而未执行，因此 Coverage 为 PARTIAL。without-skill 输出路径错误，作为 baseline FAIL，不影响 durable Overall。
- Workspace changes: added: `docs/devops/chat-interface/messages/history/search/ENV_AUDIT.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `docs/engineer/chat-interface/messages/history/search/ENV_CONFIG_AUDIT.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- NOT EXERCISED: `does_not_invent_feature_directory`；fixture 未触发对应条件分支。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS，但仅做静态审查且没有 fresh baseline；issue #234 后标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前行为结果；若要获得 FULL coverage，需要新增能够触发 NOT EXERCISED 条件分支的独立 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
