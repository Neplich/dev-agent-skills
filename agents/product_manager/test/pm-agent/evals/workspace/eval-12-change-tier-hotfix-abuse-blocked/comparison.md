# pm-agent Eval Comparison: eval-012

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-012-change-tier-hotfix-abuse-blocked`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
- Overall result: PASS

## With-skill behavior

Explicitly rejected hotfix abuse, classified the business-rule change as `standard` or higher, blocked downstream execution, and returned it to PM scope and expectation confirmation.

## Without-skill baseline

The fresh baseline advised product confirmation but did not explicitly enforce classification or the no-direct-handoff gate.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-012-change-tier-hotfix-abuse-blocked/` and is not committed.
