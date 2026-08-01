# pm-agent Eval Comparison: eval-008

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-008-direct-specialist-bypass-gate`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: same prompt/fixture, newly generated with-skill and without-skill responses; no reused baseline.

## Latest result:

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised.
- Overall result: PASS

## With-skill behavior

Applied the specialist entry gate, required a PM handoff or equivalent confirmed PRD/TRD and current implementation scope, correctly stated that an existing plan is not the entry prerequisite, blocked plan/code/test work, and returned to PM classification.

## Without-skill baseline

The fresh baseline blocked immediate coding but incorrectly treated a pre-existing implementation plan as a prerequisite and did not identify the PM specialist-entry contract.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Runtime evidence is isolated under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-008-direct-specialist-bypass-gate/` and is not committed.
