# pm-agent Eval Comparison: eval-001

## Evaluation target

- Skill: `pm-agent`
- Test: `eval-001-route-greenfield-product-request`
- Fixture version: current `README.md` and `eval_metadata.json` at 2026-08-01 13:12 +0800
- Fresh run: new with-skill response and new without-skill baseline generated from the same prompt and fixture; no historical baseline was reused.

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised.
- Overall result: PASS

## With-skill behavior

Selected `idea-to-spec`, explicitly enforced the no-skip-PM contract after `project-bootstrap` removal, named the required discovery context and PM artifacts, kept TRD with `engineer-agent:trd-gen`, and delayed Designer/Engineer handoff until requirements stabilize.

## Without-skill baseline

Fresh baseline used only the prompt and fixture. It recommended generic requirement analysis and later design/development, but did not identify the no-override PM entry contract, the full artifact ownership split, or the explicit normal-classification return path.

## Failures and next steps

- Failures: none.
- Next steps: none for this fixture.

## Runtime Artifacts Policy

Fresh responses and the verdict were written only under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/pm-agent/eval-001-route-greenfield-product-request/`; runtime artifacts are not durable repository outputs.
