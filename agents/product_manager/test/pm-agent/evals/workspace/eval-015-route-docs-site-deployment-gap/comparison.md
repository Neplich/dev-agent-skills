# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`
- Review context: issue #196 L2-4 fresh paired validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current evidence fixture
- Validation date: 2026-07-31
- Sources: fresh with-skill session `019fb589-672e-7bc0-95ff-2ada072730dd`; fresh isolated baseline session `019fb58b-f4fa-7232-abda-91612bafb9a3`

## Latest Result

- Behavior result: FAIL (2/3 assertions)
- Coverage result: FULL (3/3 assertions exercised)
- Overall result: FAIL

## With-Skill Behavior

Kept insufficient evidence `unknown`, then produced a repo-wide `deployment` packet with N/A feature scope, empty feature-path evidence, real source evidence, and authorization blockers. It handed off only generically to DevOps.

## Fresh Without-Skill Baseline

Correctly preserved `unknown` and the authorization boundary, but produced neither the structured deployment packet nor the ordered DevOps/Docs chain.

## Failures

- FAIL `routes_ordered_devops_chain`: the candidate did not name `deployment-planner → cicd-bootstrap → env-config-auditor → formal-docs-sync` or the verified-facts-only Docs closeout.

## Next Steps

- Restore the explicit ordered chain in the candidate behavior without inventing deployment authorization.

## Runtime Artifact Policy

- Runtime outputs remain in `tmp/eval-runs/issue-196-l2-3-4/pm-agent/eval-015-route-docs-site-deployment-gap/` and are not committed.
