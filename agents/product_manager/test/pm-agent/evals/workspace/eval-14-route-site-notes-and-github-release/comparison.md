# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`
- Review context: issue #196 L2-4 fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt and fixture
- Validation date: 2026-07-31
- Sources: fresh with-skill session `019fb589-672e-7bc0-95ff-2ada072730dd`; fresh isolated baseline session `019fb58b-f4fa-7232-abda-91612bafb9a3`

## Latest Result

- Latest result: PASS
- Behavior result: PASS (4/4 assertions)
- Coverage result: FULL (4/4 assertions exercised)
- Overall result: PASS

## With-Skill Behavior

Routed site notes to `docs-agent:release-notes-generator`, GitHub Release work to PM `github-release-generator`, and preserved the ready-handoff/release-audit sequence without reviving the old PM name.

## Fresh Without-Skill Baseline

Preserved the sequence and avoided collapsing the tasks, but omitted both canonical specialist owner names.

## Failures

- None.

## Next Steps

- None.

## Runtime Artifacts Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-014-route-site-notes-and-github-release/` and are not committed.
