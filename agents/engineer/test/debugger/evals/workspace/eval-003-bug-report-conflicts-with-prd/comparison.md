# Eval Result: eval-003-bug-report-conflicts-with-prd

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-003-bug-report-conflicts-with-prd`
- Test case: bug-report-conflicts-with-prd
- Workspace: `workspace/eval-003-bug-report-conflicts-with-prd`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 用户说：通知中心 active 列表没有显示 archived 通知，这是个 bug，请直接修一下。现有 docs/pm/notifications/PRD.md 和 docs/engineer/notifications/TRD.md 都写着 active 列表排除 archived。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_prd_conflict`: with_skill final.md 将请求归类为 requirement_change，并说明 PRD 排除 archived、TRD 条件为 status IN ('active', 'read')；transcript.jsonl 的 item_1 实际读取了 PRD/TRD。
- PASS `hands_off_to_pm_update`: final.md 明确要求交由 pm-agent:idea-to-spec 的 existing-project-update，先更新 PRD/产品决策，随后同步 TRD，并生成确认的 IMPLEMENTATION_PLAN.md。
- FAIL `blocks_e2e_when_expectation_changes`: final.md 仅说明文档完成前不修改代码或测试，未明确禁止将 archived 进入 active 写入 docs/qa/e2e 功能树，也未完整列出 PRD/产品决策、TRD 同步及确认 IMPLEMENTATION_PLAN.md 的 E2E 阻断条件。
- PASS `does_not_produce_repair_plan`: with_skill final.md 未产出修复实施计划、代码或测试修改，也未声称已修复；实际 workspace 文件哈希与输入记录一致，未发生工作区改动。
- NOT EXERCISED `blocks_explicit_skip_override`: 本轮 prompt 未提出跳过 PRD 对齐，因此显式 skip override 路径未触发。

## With Skill Behavior

正确识别需求变更并完成 PM handoff，未修改代码或测试；遗漏了明确的 E2E 功能树阻断说明。

## Without Skill Baseline

baseline 同样读取 PRD/TRD 且未修改 workspace，但未明确给出 existing-project-update handoff、IMPLEMENTATION_PLAN.md 和 E2E 阻断要求。

## Failures / Findings

- blocks_e2e_when_expectation_changes：最终输出未明确禁止在前置文档和 IMPLEMENTATION_PLAN.md 确认前把新预期写入 docs/qa/e2e 功能树。
- Root cause: with_skill 已执行需求冲突分流，但最终答复遗漏了 assertion 要求的 E2E 验收预期阻断条件。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-003-bug-report-conflicts-with-prd

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-003-bug-report-conflicts-with-prd`
- Workspace: `workspace/eval-003-bug-report-conflicts-with-prd`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- 日期：2026-07-30
- Fixture：同路径 Approved PRD/TRD 均规定 active 排除 archived。
- Fresh run：`tmp/eval-runs/issue-196-l2-2-debugger-20260730-220643/`
- paired candidates 均为本轮新生成，未复用旧 baseline。

## Assertion Results

- PASS `detects_prd_conflict`：明确分类为 `requirement_change`。
- PASS `hands_off_to_pm_update`：精确交回 `pm-agent:idea-to-spec` 的 `existing-project-update`，并要求随后同步 TRD。
- PASS `blocks_e2e_when_expectation_changes`：在 PRD/decision、TRD、confirmed IMPLEMENTATION_PLAN 完成前阻断新 E2E 预期。
- PASS `does_not_produce_repair_plan`：不进入修复计划、代码或测试修改。
- PASS `blocks_explicit_skip_override`：明确 skip 请求只能作为 blocker/risk。

## With-Skill Behavior

候选使用已批准预期链识别产品行为变更，停止 debugger 路径并给出完整 PM handoff 与后续门禁。

## Without-Skill Baseline

来源为本轮隔离子代理基于相同 prompt/fixture 的全新响应，未接触 skill、Engineer README 或 with-skill。baseline 也精确给出 PM lane、TRD 同步、E2E blocker chain 与 skip override，满足 5/5 assertions。

## Failures

- With-skill：无。
- Baseline：无；本轮未观察到 assertion 级差异。

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Next Steps

保留 requirement-change 负路径；如需测量 skill 增益，可避免 fixture TRD 直接写出完整 PM lane 与 IMPLEMENTATION_PLAN 链。

## Runtime Artifact Policy

paired candidates 与 verdict 只存放于 ignored runtime 目录，不提交；durable 结果仅为本文件。
