# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-002-route-bugfix-request`
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

Classified `bug_report`, required approved PRD/TRD expectation checks, and gated Engineer/debugger handoff on a confirmed implementation deviation.

## Fresh Without-Skill Baseline

Preserved expectation-first debugging semantics, but used generic “bug fix” wording rather than the canonical request type and provided a less structured handoff.

## Failures

- None.

## Next Steps

- Keep the expectation-first gate explicit.

## Runtime Artifact Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-002-route-bugfix-request/`; only this comparison is durable.
