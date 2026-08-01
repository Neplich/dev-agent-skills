# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-009-missing-handoff-target-unavailable`
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

Detected unavailable `designer-agent`, marked the handoff blocked, named installation/restoration as the unblock, and refused to substitute PM or Engineer for design work.

## Fresh Without-Skill Baseline

Matched the main behavior but allowed a vaguely defined “equivalent role” alternative, making the capability boundary less precise.

## Failures

- None.

## Next Steps

- None.

## Runtime Artifacts Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-009-missing-handoff-target-unavailable/` and are not committed.
