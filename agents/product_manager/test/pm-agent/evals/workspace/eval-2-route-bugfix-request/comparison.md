# pm-agent Eval Comparison: eval-002

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-002-route-bugfix-request`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: new with-skill response and new without-skill baseline generated from the same prompt and fixture; no historical baseline was reused.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
- Overall result: PASS

## With-skill behavior

Classified `bug_report`, required approved PRD/TRD or equivalent expectation and reproduction evidence first, and allowed Engineer/debugger handoff only after confirming an implementation deviation.

## Without-skill baseline

Fresh baseline used only the prompt and fixture. It moved from reproduction directly to technical diagnosis without the approved-expectation gate.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Fresh responses and verdict live only under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-002-route-bugfix-request/` and are not committed.
