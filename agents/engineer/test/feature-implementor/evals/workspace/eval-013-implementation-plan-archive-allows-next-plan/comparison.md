# Eval Result: eval-013-implementation-plan-archive-allows-next-plan

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-013-implementation-plan-archive-allows-next-plan`
- Test case: implementation-plan-archive-allows-next-plan
- Workspace: `workspace/eval-013-implementation-plan-archive-allows-next-plan`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认，现在要新增部分退款能力。上一轮全额退款计划已归档到 docs/engineer/payment-refund/implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md，当前没有活跃计划。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_prior_plan_archived`: 归档文件存在且 frontmatter 为 status: "Archived"；计划正文和 transcript 明确记录该归档及当前无 active plan。
- PASS `allows_new_active_plan`: 已创建 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，范围为部分退款。
- PASS `records_previous_plan_archive`: 新计划 frontmatter 的 previous_plan_archive 精确指向归档文件。
- PASS `keeps_active_entry_fixed`: 新计划位于 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，未写入 archive 目录。
- PASS `waits_for_user_confirmation`: 计划 status 为 Draft，final 明确要求确认后再实现；workspace 未出现源代码修改。

## With Skill Behavior

with_skill 创建了正确的 Draft 活跃计划，保留归档入口并设置 previous_plan_archive；所有 input/output manifest hash 校验通过。

## Without Skill Baseline

without_skill 也创建了活跃计划，但未记录 previous_plan_archive，且未明确等待确认；仅作对照。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-013-implementation-plan-archive-allows-next-plan

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-013-implementation-plan-archive-allows-next-plan`
- Test case: implementation-plan-archive-allows-next-plan
- Workspace: `workspace/eval-013-implementation-plan-archive-allows-next-plan`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and `docs/engineer/payment-refund/implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md`.
- Fixture summary: the prior full-refund plan is archived with `status: "Archived"`, `implementation_scope: full-refund-flow`, `archived_at`, `archive_approved_by`, and `source_plan`; no active `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` exists.
- Expected output: allow a new active plan for partial refunds, require `previous_plan_archive`, keep the active entry fixed, and wait for confirmation before coding.

## Assertions

- PASS `detects_prior_plan_archived`: the skill recognizes the archived prior plan and no active-plan blocker.
- PASS `allows_new_active_plan`: planning may create a new `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` for the partial-refund scope.
- PASS `records_previous_plan_archive`: the new plan frontmatter must point `previous_plan_archive` to the archived full-refund plan.
- PASS `keeps_active_entry_fixed`: the new active plan path remains `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`, not an archive path.
- PASS `waits_for_user_confirmation`: coding waits until the new active plan is confirmed.

## With Skill Behavior

Fresh with-skill validation confirmed the archived-plan positive path. The current skill should scan the active plan path and archive directory, find no active plan, identify the archived full-refund plan as valid historical context, and proceed to write a new active plan for partial refunds. The plan must record `previous_plan_archive: docs/engineer/payment-refund/implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md`, keep the live entry at `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`, and wait for user confirmation before implementation.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic planner would likely allow a new plan because the prompt says no active plan exists, but it would not reliably require exact `previous_plan_archive` linkage metadata, validate that the archive is on the same feature path, or explicitly forbid writing the new plan inside the archive directory.

## Failures

- None.

## Next Steps

- Keep this eval focused on allowing a new active plan only after proper archival and linkage metadata.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
