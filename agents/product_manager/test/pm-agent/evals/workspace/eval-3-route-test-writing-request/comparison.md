# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-003-route-test-writing-request`
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

Classified `validation`, named PRD/TRD/confirmed plan or acceptance evidence as the basis, and split QA from Engineer/test-writer only after expectations stabilized.

## Fresh Without-Skill Baseline

Also required business and acceptance evidence, but omitted the canonical `validation` type and the confirmed implementation-plan basis.

## Failures

- None.

## Next Steps

- None.

## Runtime Artifacts Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-003-route-test-writing-request/` and are not committed.
