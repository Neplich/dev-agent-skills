# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-005-route-deployment-request`
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

Classified `deployment`, used `N/A` feature fields and empty feature-path evidence, and required operational goal, environment, release scope, rollback needs, and risks before DevOps handoff.

## Fresh Without-Skill Baseline

Correctly chose deployment and `N/A`, but omitted the canonical empty `feature_path_evidence` and an explicit rollback requirement.

## Failures

- None.

## Next Steps

- None.

## Runtime Artifact Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-005-route-deployment-request/` and are not committed.
