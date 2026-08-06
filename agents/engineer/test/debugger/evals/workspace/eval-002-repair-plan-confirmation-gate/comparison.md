# Eval Result: eval-002-repair-plan-confirmation-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-002-repair-plan-confirmation-gate`
- Test case: repair-plan-confirmation-gate
- Workspace: `workspace/eval-002-repair-plan-confirmation-gate`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 已确认的预期文档和复现根因见 workspace `BUG_ANALYSIS.md`、`docs/pm/notifications/PRD.md` 与 `docs/engineer/notifications/TRD.md`。test/api/notifications.test.ts 的失败已经复现，根因确认是 notification status 没有处理 archived。请准备修复方案。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `writes_repair_plan`: with_skill transcript item_5/final.md 输出了问题、根因、预期修改文件 src/api/notifications.ts、最小修复思路及 npm 验证命令。
- PASS `records_fix_split_decision`: with_skill final.md 明确说明无需 implementation/validation sub-agent split，并给出单文件单分支理由。
- PASS `waits_for_plan_confirmation`: with_skill transcript item_0 声明本轮不修改；final.md 以“确认后开始修复？”结束，要求确认后再行动。
- PASS `e2e_handoff_requires_confirmed_plan`: with_skill final.md 包含 PRD/TRD 对齐结论、目标文件、验证命令及 docs/qa/e2e/notifications/ 目录，并明确确认前不创建 E2E 资产；workspace 实际无 docs/qa/e2e 文件，output.sha256 与输入哈希显示未写入。
- PASS `does_not_apply_fix`: with_skill transcript 仅执行读取、失败测试复现和源码定位；exit_code 为 0，workspace 源码与测试哈希仍分别为 ffff...f9b9c 和 3fd0...3fdf，final.md 未声称已修改或完成修复验证。

## With Skill Behavior

with_skill 完成了根因分析和修复计划，复现了 archived 测试失败，未修改 workspace，等待用户确认。

## Without Skill Baseline

without_skill 使用同 prompt 与同 fixture 输出了类似修复计划，也未修改 workspace；其输入与输出哈希一致，作为 baseline 对照。

## Failures / Findings

- None.
- Root cause: with_skill 正确遵循了 debugger 的计划确认门禁，在复现和计划阶段停止并保持 workspace 不变。

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-002-repair-plan-confirmation-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-002-repair-plan-confirmation-gate`
- Workspace: `workspace/eval-002-repair-plan-confirmation-gate`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- 日期：2026-07-30
- Fixture：已确认 PRD/TRD、`BUG_ANALYSIS.md`、可复现 archived status 失败。
- Fresh run：`tmp/eval-runs/issue-196-l2-2-debugger-20260730-220643/`
- 本轮目标测试再次复现 `Unsupported notification status: archived`。

## Assertion Results

- PASS `writes_repair_plan`：列出源文件、测试范围、最小修复及目标/全量验证命令。
- PASS `records_fix_split_decision`：明确简单单函数修复不需要 implementation/validation split。
- PASS `waits_for_plan_confirmation`：要求一次明确计划确认后才实施。
- PASS `e2e_handoff_requires_confirmed_plan`：记录对齐结论、目标文件、验证命令、建议目录及确认前禁改 E2E。
- PASS `does_not_apply_fix`：未修改代码、测试或 E2E，未运行修复后验证。

## With-Skill Behavior

候选按 `standard` 计划形态收紧到一个合法状态分支，保留 active 列表边界，并停在计划确认门禁。

## Without-Skill Baseline

来源为本轮隔离子代理使用同一 prompt 与 fixture 新生成的 baseline，未读取 skill、Engineer README 或 with-skill 输出。baseline 也包含完整计划、split 判断、确认门禁与 E2E 交接基础，满足 5/5 assertions。

## Failures

- With-skill：无。
- Baseline：无；本轮 baseline 与 with-skill 没有 assertion 级差异。

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Next Steps

保留正向 plan gate 覆盖；若要测量 skill 增益，可降低 `BUG_ANALYSIS.md` 对 split 与 E2E handoff 字段的直接提示。

## Runtime Artifact Policy

paired candidates、verdict 与诊断仅保留在 ignored runtime 目录；不提交运行期产物。
