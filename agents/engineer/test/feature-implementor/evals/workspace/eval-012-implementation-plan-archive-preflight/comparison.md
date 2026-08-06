# Eval Result: eval-012-implementation-plan-archive-preflight

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`
- Test case: implementation-plan-archive-preflight
- Workspace: `workspace/eval-012-implementation-plan-archive-preflight`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认，现在要新增部分退款能力。docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md 已存在且是上一轮全额退款的完成态计划，尚未归档。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `runs_pre_plan_archive_scan`: with_skill transcript 的成功命令读取了活动计划并检查了 docs/engineer/payment-refund/implementation-plans/archive/；final 报告归档前置检查。
- PASS `blocks_direct_overwrite`: with_skill final 未创建新计划；workspace 活动计划仍为原文件，哈希与 fixture-input.sha256 一致，且没有归档或替换文件。
- PASS `offers_implemented_handling_options`: final 提供归档完成计划后新建、归档为 Superseded 并注明原因后新建两项选择，未提供继续更新 Implemented 计划。
- FAIL `keeps_active_entry_fixed`: final 未明确说明活跃入口固定为 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，也未明确说明归档只放到 implementation-plans/archive/。
- PASS `does_not_implement_directly`: final 未声称修改代码、运行实现或完成验证；workspace 文件未发生变化，with_skill 输入哈希与实际哈希一致。

## With Skill Behavior

总体阻止了直接覆盖并提出了正确的两种处理选项，但遗漏了固定活跃入口及指定归档目录的明确说明。

## Without Skill Baseline

仅作对照：without_skill 实际归档并新建了计划，未遵守阻止直接覆盖要求。

## Failures / Findings

- keeps_active_entry_fixed FAIL：缺少要求的固定入口与 implementation-plans/archive/约束说明。
- Root cause: with_skill final 未完整复述 archive preflight 对活动入口和归档目录的明确约束。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-012-implementation-plan-archive-preflight

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`
- Test case: implementation-plan-archive-preflight
- Workspace: `workspace/eval-012-implementation-plan-archive-preflight`
- Latest result: PARTIAL - the 2026-07-05 fresh validation still covers archive
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

  scanning and overwrite blocking, but the handling-options assertion changed
  from three choices to two and has not been rerun.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- Fixture summary: PRD/TRD now cover partial refunds, but an existing active `IMPLEMENTATION_PLAN.md` for `implementation_scope: full-refund-flow` has `status: Implemented` and has not been archived.
- Expected output: run archive preflight, block direct overwrite, report existing plan path/status/scope, and ask the user to choose archive-then-create or supersede-then-create.

## Assertions

- PASS `runs_pre_plan_archive_scan`: the skill scans active `IMPLEMENTATION_PLAN.md` and `implementation-plans/archive/` before a new plan.
- PASS `blocks_direct_overwrite`: unresolved active-plan handling blocks overwriting or replacing the active entry.
- NOT RERUN `offers_implemented_handling_options`: the current assertion
  requires archive completed plan then create or archive as `Superseded` with
  reason then create, and forbids continuing an `Implemented` plan.
- PASS `keeps_active_entry_fixed`: active entry stays `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`; history goes under `implementation-plans/archive/`.
- PASS `does_not_implement_directly`: no code, implementation, or verification is performed before plan handling and confirmation.

## With Skill Behavior

The prior fresh with-skill validation confirmed the archive scan and blocking
behavior. Its three-choice handling result is historical and does not validate
the current two-choice rule for `status: Implemented`.

## Without Skill Baseline

The prior fresh without-skill baseline was summarized before reading skill
docs. It predates the current two-choice assertion and cannot serve as the
required fresh baseline for a rerun.

## Failures

- The current two-choice handling assertion has not received fresh with-skill
  and without-skill validation.

## Next Steps

- Rerun fresh with-skill and without-skill validation before treating the
  updated handling assertion as PASS.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
