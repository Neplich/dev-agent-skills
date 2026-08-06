# Eval Result: eval-002-resolve-trd-gap-packet

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-002-resolve-trd-gap-packet`
- Test case: resolve-trd-gap-packet
- Workspace: `workspace/eval-002-resolve-trd-gap-packet`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: workspace `TRD_GAP_PACKET.md` 记录了当前缺少的技术决策，PM 的 docs/pm/capture-loop/PRD.md 已确认。请补齐技术方案。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `accepts_gap_packet_as_trd_work`: Transcript states entering Engineer TRD stage and updating docs/engineer/capture-loop/TRD.md; final says handoff occurs only after confirmation.
- PASS `resolves_named_gap_categories`: TRD documents components, data flow and envelope, validation command, rollout/rollback, error handling, observability, and security.
- PASS `keeps_finder_trd_gen_boundary`: Gap packet and AGENTS.md state finder reports gaps while trd-gen owns the Engineer document; transcript follows this boundary.
- PASS `unresolved_gap_blocks_e2e`: TRD records open questions and explicitly keeps implementation, debugger, and QA E2E updates blocked until confirmation.
- PASS `no_implementation_plan_or_code`: Only TRD.md was added; source-file hashes are unchanged, no IMPLEMENTATION_PLAN.md exists, and tests were not run.

## With Skill Behavior

With-skill final and transcript show TRD gap resolution. Workspace TRD exists, covers all named gaps, records open questions, and preserves implementation boundaries. Runtime exited 0 and output hashes match workspace files.

## Without Skill Baseline

Without-skill produced a comparable TRD artifact and exited 0; it is used only as contrast and does not determine the with-skill judgment.

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-002-resolve-trd-gap-packet

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-002-resolve-trd-gap-packet`
- Test case: resolve-trd-gap-packet
- Workspace: `workspace/eval-002-resolve-trd-gap-packet`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 5/5 assertions.
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed PRD, explicit TRD gap packet, and minimal capture/queue code evidence
- Expected output: 确认发现者负责说明缺口，trd-gen 负责补完整 docs/engineer/capture-loop/TRD.md；逐项处理 gap packet 中的组件、数据流、验证命令、发布风险和错误处理策略，不进入实现计划或代码。

## Assertions

- PASS `accepts_gap_packet_as_trd_work`: 将 gap packet 识别为 TRD 补全，不是实现任务。
- PASS `resolves_named_gap_categories`: 覆盖组件、数据流、验证、发布/回滚、错误、可观测性和安全。
- PASS `keeps_finder_trd_gen_boundary`: 保持 finder 与 trd-gen 的职责边界。
- PASS `unresolved_gap_blocks_e2e`: 未决 gap 阻断 plan、debugger 和 QA E2E。
- PASS `no_implementation_plan_or_code`: 没有进入计划或代码实现。

## With Skill

- 逐项处理 gap packet，并识别 `maxAttempts=3` 与 `[5,30,120]` 的语义歧义，记录 Queue owner 与 unblock condition。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 trd-gen skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 5/5 assertions，但静默选择 retry 语义，没有显式记录该冲突的 owner 与 unblock condition。

## Failures

- 无 assertion failure。
- 当前 assertions 没有捕获“保留未决技术语义”这一产物质量增益。

## Next Steps

- 保留 gap 分类、角色边界和阻断门禁；后续可单独评估是否增强 open-question 断言。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, generated TRD, outputs, and diagnostics were kept only in an ignored scratch workspace and are not committed.
