# Eval Result: eval-012-implementation-plan-archive-preflight

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`
- Test case: implementation-plan-archive-preflight
- Workspace: `workspace/eval-012-implementation-plan-archive-preflight`
- Latest result: PARTIAL - the 2026-07-05 fresh validation still covers archive
- Overall result: BLOCKED
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
