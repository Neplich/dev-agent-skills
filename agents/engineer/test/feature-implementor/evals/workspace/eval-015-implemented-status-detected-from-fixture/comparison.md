# Eval Result: eval-015-implemented-status-detected-from-fixture

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-015-implemented-status-detected-from-fixture`
- Test case: implemented-status-detected-from-fixture
- Workspace: `workspace/eval-015-implemented-status-detected-from-fixture`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认。现在要在这个功能上做下一轮更新。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_active_plan_frontmatter`: transcript item_5 明确执行并输出 IMPLEMENTATION_PLAN.md 内容，包含 frontmatter。
- PASS `detects_implemented_status`: final 明确指出活动计划路径、status `Implemented` 与 implementation scope `full-refund-flow`。
- PASS `blocks_direct_overwrite`: final 在处理决定确认前停下并提供选择；with_skill 输入/输出 workspace hash 完全一致，未新增归档或计划文件。
- PASS `offers_implemented_handling_options`: final 明确提供“归档后新建”和“归档为 Superseded 并填写原因后新建”两项，未提供继续更新当前计划选项。
- PASS `does_not_implement_code`: final 未声称开始实现；workspace 仅保留原有文档，hash 与 fixture/input manifest 一致。

## With Skill Behavior

with_skill transcript、final、JSONL、hash manifest 与 workspace 均核验通过；正确识别 Implemented 活动计划并触发归档门禁。

## Without Skill Baseline

without_skill 仅作对照：识别了 Implemented，但未按要求停在两选项归档门禁，转而要求代码仓库或更新计划。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-015-implemented-status-detected-from-fixture

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-015-implemented-status-detected-from-fixture`
- Test case: implemented-status-detected-from-fixture
- Workspace: `workspace/eval-015-implemented-status-detected-from-fixture`
- Latest result: PARTIAL - the 2026-07-27 fresh validation still covers reading
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

  frontmatter, detecting `Implemented`, and blocking overwrite, but the
  handling-options assertion changed from three choices to two and has not been
  rerun.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`,
  `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and
  `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- Fixture summary: the prompt omits plan status; the active plan frontmatter has
  `status: Implemented` and `implementation_scope: full-refund-flow`.

## Assertions

- PASS `reads_active_plan_frontmatter`: the response derives the completed state
  from the active plan frontmatter instead of the prompt.
- PASS `detects_implemented_status`: it reports the active path,
  `status: Implemented`, and `implementation_scope: full-refund-flow`.
- PASS `blocks_direct_overwrite`: it stops before creating or overwriting an
  active plan.
- NOT RERUN `offers_implemented_handling_options`: the current assertion
  requires archive-then-create or Superseded-then-create and forbids continuing
  an `Implemented` plan.
- PASS `does_not_implement_code`: it makes no code or implementation claim.

## With Skill Behavior

The prior fresh with-skill validator read the Engineer entry and
feature-implementor planner instructions, inspected the fixture active plan,
and stopped at the archive gate. Its three-choice result is historical and
does not validate the current two-choice rule.

## Without Skill Baseline

The prior fresh zero-exposure baseline predates the current two-choice
assertion and cannot serve as the required fresh baseline for a rerun.

## Failures

- The current two-choice handling assertion has not received fresh with-skill
  and without-skill validation.

## Next Steps

- Keep the case focused on discovering `Implemented` from frontmatter rather
  than from a prompt hint.
- Rerun fresh with-skill and without-skill validation before treating the
  updated handling assertion as PASS.
- If stronger differentiation is needed later, reduce rule-level hints in the
  fixture README and metadata without weakening the real active-plan evidence.

## Runtime Artifacts Policy

- The paired validation returned results in the subagent response and did not
  create repository runtime files.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status
  files, and `comparison.auto.md` must not be committed.
