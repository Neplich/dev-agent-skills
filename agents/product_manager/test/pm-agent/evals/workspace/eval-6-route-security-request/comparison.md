# pm-agent Eval Comparison: eval-006

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-006-route-security-request`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
- Overall result: PASS

## With-skill behavior

Classified `security`, collected risk surface/assets/permissions/data flow/remediation expectations, and prepared a bounded Security handoff with scope and required output.

## Without-skill baseline

The fresh baseline chose security review but omitted the complete pre-handoff scope contract.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-006-route-security-request/` and is not committed.
