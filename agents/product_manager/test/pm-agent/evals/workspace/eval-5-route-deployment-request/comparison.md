# Eval Result: pm-agent-route-deployment-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-deployment-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 5
- Entry: workspace `eval-5-route-deployment-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: repo-wide CI and release-readiness request
- Expected output: classify as `deployment`, allow repo-wide `N/A` feature fields, and prepare DevOps handoff with operational scope.

## Assertions

- PASS `request_type_deployment`: CI and release-readiness work is classified as `deployment`.
- PASS `repo_wide_scope_allowed`: Confirmed repository-level non-feature work can use `N/A` feature fields and empty `feature_path_evidence`.
- PASS `devops_handoff_packet`: DevOps handoff requires operational goal, environment, release scope, rollback needs, and risks.

## With Skill Behavior

- The `pm-agent` protocol maps CI and release-readiness work to `deployment`.
- It allows confirmed non-feature repo-wide work to use `feature_path: N/A`, related feature fields as `N/A`, and `feature_path_evidence: []`.
- It requires operational goal, environment, release scope, rollback needs, and risks before DevOps handoff.
- Issue #81 safety-net behavior remains within boundary: closeout may recommend DevOps as next owner, but PM does not create CI, deployment config, or release-readiness artifacts itself.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-06 without applying `pm-agent` or the Product Manager Agent README. A generic response could jump directly into CI configuration.
- It may not preserve the repo-wide non-feature scope rule or the complete DevOps handoff context.

## Failures

- None. The current `pm-agent` protocol satisfies deployment classification and repo-wide scope assertions.
- No issue #81 regression found; auto-continue does not bypass the DevOps handoff packet or execute DevOps work from PM.

## Next Steps

- Keep this eval as PM entry coverage for deployment and CI routing.
- Re-run fresh validation if repo-wide feature-scope handling changes.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
