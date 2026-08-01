# pm-agent Eval Comparison: eval-005

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-005-route-deployment-request`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
- Overall result: PASS

## With-skill behavior

Classified `deployment`, used repo-wide `N/A` feature fields with empty feature-path evidence, collected operational goal/environment/release/rollback/risk context, and then handed off DevOps.

## Without-skill baseline

The fresh baseline selected DevOps and general deployment context but omitted the explicit repo-wide packet shape and evidence rules.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-005-route-deployment-request/` and is not committed.
