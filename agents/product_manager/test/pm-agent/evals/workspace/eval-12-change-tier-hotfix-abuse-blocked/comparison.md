# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-012-change-tier-hotfix-abuse-blocked`
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

Rejected hotfix abuse, classified the expectation change as `existing_update`/`standard`, and kept the request blocked on the PM path.

## Fresh Without-Skill Baseline

Also satisfied all three assertions using general product-governance reasoning; assertion-level differentiation is limited.

## Failures

- None.

## Next Steps

- None.

## Runtime Artifact Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-012-change-tier-hotfix-abuse-blocked/` and are not committed.
