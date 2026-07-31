# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-010-change-tier-hotfix-fast-lane`
- Review context: issue #196 L2-4 fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt and fixture
- Validation date: 2026-07-31
- Sources: fresh with-skill session `019fb589-672e-7bc0-95ff-2ada072730dd`; fresh isolated baseline session `019fb58b-f4fa-7232-abda-91612bafb9a3`

## Latest Result

- Behavior result: PASS (3/3 assertions)
- Coverage result: FULL (3/3 assertions exercised)
- Overall result: PASS

## With-Skill Behavior

Used `delivery` plus `hotfix`, allowed fast lane only after classification, and retained scope, source and verification evidence.

## Fresh Without-Skill Baseline

Also passed the three behavioral points; it mislabeled `request_type` as hotfix, which is outside this eval's assertions. Differentiation is limited for this fixture.

## Failures

- None.

## Next Steps

- Consider a future assertion for stable `request_type` if that distinction is required.

## Runtime Artifact Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-010-change-tier-hotfix-fast-lane/` and are not committed.
