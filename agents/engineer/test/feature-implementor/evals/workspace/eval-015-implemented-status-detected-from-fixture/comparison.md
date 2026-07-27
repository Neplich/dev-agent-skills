# Eval Result: eval-015-implemented-status-detected-from-fixture

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-015-implemented-status-detected-from-fixture`
- Test case: implemented-status-detected-from-fixture
- Workspace: `workspace/eval-015-implemented-status-detected-from-fixture`
- Latest result: PARTIAL - the 2026-07-27 fresh validation still covers reading
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
