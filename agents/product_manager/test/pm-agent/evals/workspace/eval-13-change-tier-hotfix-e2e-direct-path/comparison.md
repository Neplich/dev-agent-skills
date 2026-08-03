# pm-agent Eval Comparison: eval-013

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-013-change-tier-hotfix-e2e-direct-path`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
- Overall result: PASS

## With-skill behavior

Limited hotfix QA/E2E to directly affected paths, retained verification results and blocked checks, and made full-suite expansion conditional on risk or tier escalation.

## Without-skill baseline

The fresh baseline suggested a manual spot check but omitted durable evidence and blocked-check recording.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-013-change-tier-hotfix-e2e-direct-path/` and is not committed.
