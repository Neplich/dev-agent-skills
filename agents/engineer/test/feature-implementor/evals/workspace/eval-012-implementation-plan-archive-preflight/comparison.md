# Eval Result: eval-012-implementation-plan-archive-preflight

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`
- Test case: implementation-plan-archive-preflight
- Workspace: `workspace/eval-012-implementation-plan-archive-preflight`
- Latest result: PASS - fresh Codex subagent validation confirmed the archive preflight gate blocks direct overwrite of an unarchived active plan.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Confirmed PRD/TRD plus an existing completed `IMPLEMENTATION_PLAN.md` on `feature_path: payment-refund` that has not been archived.
- Run set: with-skill fresh subagent validation and a separate fresh without_skill baseline run against the same prompt and fixture.
- Expected output: block direct overwrite of the active plan; report the existing plan path, status, and scope; ask the user to archive-then-create, continue updating, or supersede with a reason.

## Assertions

- PASS `runs_pre_plan_archive_scan`: with-skill behavior scans the existing active plan and `implementation-plans/archive/` before writing a new plan.
- PASS `blocks_direct_overwrite`: with-skill behavior blocks overwriting or replacing the active `IMPLEMENTATION_PLAN.md` while the handling decision is unresolved.
- PASS `offers_three_handling_options`: with-skill behavior asks the user to choose archive-then-create, continue-updating, or supersede-with-reason.
- PASS `keeps_active_entry_fixed`: with-skill behavior keeps the active plan entry at `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- PASS `does_not_implement_directly`: with-skill behavior does not modify code or claim implementation completed.

## With Skill

Fresh Codex subagent validation applied `feature-implementor` and read the Agent
README, public skill doc, planner, reviewer, output conventions, eval definition,
and fixture.

The subagent concluded that `feature-implementor` should first confirm PRD/TRD
alignment, then run the pre-plan archive scan. The fixture contains
`docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` with
`status: Implemented`, `implementation_scope: full-refund-flow`, and no archive
record. Therefore the skill must not create or overwrite a new active plan for
the partial-refund scope. It must report the old plan path, status, and scope,
then ask the user to choose one of the three allowed handling paths.

With-skill assertion verdicts were all PASS. There were no blocking findings.

## Without Skill / Baseline

A separate fresh Codex subagent generated a without_skill baseline without
reading or applying `feature-implementor` or the Engineer Agent README.

The baseline would likely read the PRD/TRD and notice the existing
`IMPLEMENTATION_PLAN.md`, but without the archive gate it would probably draft
or prepare a replacement plan instead of formally blocking. Baseline behavior
was assessed as:

- PARTIAL `runs_pre_plan_archive_scan`: likely notices active plan, but does not reliably scan archive.
- PARTIAL `blocks_direct_overwrite`: likely avoids coding, but may still draft a replacement active plan.
- FAIL `offers_three_handling_options`: does not reliably require the exact three archive/update/supersede choices.
- PARTIAL `keeps_active_entry_fixed`: may use the active path, but does not reliably state archive-only history handling.
- PASS `does_not_implement_directly`: prompt already asks not to code.

The baseline gap confirms the new skill rule adds behavior that generic
implementation planning does not reliably provide.

## Failures

- None.

## Next Steps

- Keep this eval in the `feature-implementor` regression set.
- If archive metadata rules change, update the fixture and re-run fresh with-skill and without_skill validation.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, diagnostics, run status files, and `comparison.auto.md` should not be committed.
