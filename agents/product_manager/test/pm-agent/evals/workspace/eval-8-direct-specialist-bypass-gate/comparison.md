# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`
- Review context: issue #196 L2-4 fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt and fixture
- Validation date: 2026-07-31
- Sources: fresh with-skill session `019fb589-672e-7bc0-95ff-2ada072730dd`; fresh isolated baseline session `019fb58b-f4fa-7232-abda-91612bafb9a3`

## Latest Result

- Latest result: PASS
- Behavior result: PASS (3/3 assertions)
- Coverage result: FULL (3/3 assertions exercised)
- Overall result: PASS

## With-Skill Behavior

Applied the direct-specialist gate, blocked plan/code work, returned to PM, and correctly placed IMPLEMENTATION_PLAN creation after confirmed PRD/TRD rather than requiring a pre-existing plan.

## Fresh Without-Skill Baseline

Blocked implementation and returned to PM, but its wording treated the missing implementation plan as part of the pre-entry deficiency and did not distinguish plan-as-output.

## Failures

- None.

## Next Steps

- Preserve the explicit plan-as-output wording in future runs.

## Runtime Artifacts Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-008-direct-specialist-bypass-gate/` and are not committed.
