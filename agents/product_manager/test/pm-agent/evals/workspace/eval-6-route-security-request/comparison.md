# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-006-route-security-request`
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

Classified `security`, covered assets/resources, permissions, dependencies, secrets, data flow and remediation output, then prepared a bounded Security handoff.

## Fresh Without-Skill Baseline

Also produced a reasonable security scope, but without the PM packet semantics and canonical request type.

## Failures

- None.

## Next Steps

- None.

## Runtime Artifacts Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-006-route-security-request/` and are not committed.
