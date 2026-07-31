# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-004-route-ui-update-request`
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

Classified `existing_update`, separated PM expectation alignment, Designer artifacts, and Engineer frontend implementation, and required PM/TRD/design alignment before code.

## Fresh Without-Skill Baseline

Reached the same broad PM → Designer → Engineer sequence but did not name the canonical request type.

## Failures

- None.

## Next Steps

- Keep the frontend/UI routing signal in this regression case.

## Runtime Artifact Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-004-route-ui-update-request/` and are not committed.
