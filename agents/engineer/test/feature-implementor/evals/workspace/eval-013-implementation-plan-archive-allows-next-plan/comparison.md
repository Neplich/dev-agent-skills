# Eval Result: eval-013-implementation-plan-archive-allows-next-plan

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-013-implementation-plan-archive-allows-next-plan`
- Test case: implementation-plan-archive-allows-next-plan
- Workspace: `workspace/eval-013-implementation-plan-archive-allows-next-plan`
- Latest result: PASS - fresh Codex subagent validation confirmed an archived prior plan allows a new active plan when linkage metadata is required.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Confirmed PRD/TRD plus an archived prior plan at `implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md` and no current active `IMPLEMENTATION_PLAN.md` on `feature_path: payment-refund`.
- Run set: with-skill fresh subagent validation and a separate fresh without_skill baseline run against the same prompt and fixture.
- Expected output: allow creating a new active plan; require the new plan to record `previous_plan_archive`; keep the active entry fixed; wait for confirmation before coding.

## Assertions

- PASS `detects_prior_plan_archived`: with-skill behavior recognizes the prior plan is already archived and no active plan blocks creation.
- PASS `allows_new_active_plan`: with-skill behavior proceeds to write a new `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` for the partial refund scope.
- PASS `records_previous_plan_archive`: with-skill behavior requires the new plan frontmatter to record `previous_plan_archive` pointing to the archived plan.
- PASS `keeps_active_entry_fixed`: with-skill behavior keeps the active plan entry at `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- PASS `waits_for_user_confirmation`: with-skill behavior waits for confirmation before coding and does not modify code directly.

## With Skill

Fresh Codex subagent validation applied `feature-implementor` and read the Agent
README, public skill doc, planner, reviewer, output conventions, eval definition,
and fixture.

The subagent concluded that `feature-implementor` should confirm PRD/TRD
alignment, then run the archive scan. The fixture has no active
`docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`; the prior plan is already
archived at
`docs/engineer/payment-refund/implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md`
with `status: "Archived"`, `implementation_scope`, `archived_at`,
`archive_approved_by`, and `source_plan`. Therefore the skill may create a new
active plan for the partial-refund scope, but the new plan frontmatter must
record `previous_plan_archive` pointing to the archived plan, and the skill must
wait for user confirmation before coding.

With-skill assertion verdicts were all PASS. There were no blocking findings.

## Without Skill / Baseline

A separate fresh Codex subagent generated a without_skill baseline without
reading or applying `feature-implementor` or the Engineer Agent README.

The baseline would likely recognize the archived prior plan and allow a new
active implementation plan, but it would not reliably require exact linkage
metadata. Baseline behavior was assessed as:

- PASS `detects_prior_plan_archived`: prompt and fixture clearly show the archived prior plan.
- PASS `allows_new_active_plan`: baseline likely allows a new active plan because no active plan exists.
- FAIL `records_previous_plan_archive`: baseline does not reliably require the exact `previous_plan_archive` frontmatter field.
- PARTIAL `keeps_active_entry_fixed`: baseline may use the active path, but does not reliably forbid writing the new plan into archive.
- PARTIAL `waits_for_user_confirmation`: baseline avoids coding because prompt asks not to code, but may not clearly require plan confirmation before implementation.

The baseline gap confirms the new skill rule is needed for stable archived-plan
linkage and active-entry discipline.

## Failures

- None.

## Next Steps

- Keep this eval in the `feature-implementor` regression set.
- If active/archive linkage metadata changes, update the fixture and re-run fresh with-skill and without_skill validation.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, diagnostics, run status files, and `comparison.auto.md` should not be committed.
