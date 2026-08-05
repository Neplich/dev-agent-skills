# Eval Result: eval-016-draft-status-continues-current-plan

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-016-draft-status-continues-current-plan`
- Test case: draft-status-continues-current-plan
- Workspace: `workspace/eval-016-draft-status-continues-current-plan`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-27
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`,
  `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and
  `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- Fixture summary: the prompt omits plan status; the active plan frontmatter has
  `status: Draft`, `version: 0.1.0`, and
  `implementation_scope: refund-reason-codes`.

## Assertions

- PASS `reads_active_plan_frontmatter`: the response derives the current state
  from the active plan frontmatter instead of the prompt.
- PASS `detects_non_implemented_status`: it recognizes `status: Draft` as an
  unfinished current round.
- PASS `continues_current_plan`: it keeps the fixed active entry and does not
  create a second plan.
- PASS `bumps_plan_version`: it requires a substantive version bump and
  `last_updated` refresh.
- PASS `does_not_force_archive_link`: it does not require archive handling or
  `previous_plan_archive`.
- PASS `waits_before_coding`: it waits for confirmation after updating the plan.

## With Skill Behavior

The fresh with-skill validator read the Engineer entry and feature-implementor
planner instructions, inspected the fixture active plan, and identified
`status: Draft`, `version: 0.1.0`, and the current scope. It chose the continued
update path, required a version and date update, omitted archive linkage, and
stopped before code until user confirmation.

## Without Skill Baseline

A separate fresh zero-exposure subagent received only the eval prompt, fixture,
and assertions. It did not read the feature-implementor skill, internal
instructions, or Engineer README and did not reuse a historical baseline. It
also passed all six assertions by deriving the Draft state from the fixture and
continuing the fixed active plan.

## Failures

- None.
- The paired run showed no assertion-level difference. The assertions expose
  the full desired behavior, so this eval confirms correctness but has limited
  with-skill differentiation.

## Next Steps

- Keep the case focused on discovering the non-`Implemented` state from
  frontmatter and allowing a continued update.
- If stronger differentiation is needed later, reduce rule-level hints without
  weakening the real active-plan evidence.

## Runtime Artifacts Policy

- The paired validation returned results in the subagent response and did not
  create repository runtime files.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status
  files, and `comparison.auto.md` must not be committed.
