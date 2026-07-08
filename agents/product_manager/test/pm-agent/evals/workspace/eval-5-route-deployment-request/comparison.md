# Eval Result: pm-agent-route-deployment-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-deployment-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 5; PR #98 trigger-description routing check
- Entry: workspace `eval-5-route-deployment-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: repo-wide CI and release-readiness request
- Expected output: classify as `deployment`, allow repo-wide `N/A` feature fields, and prepare DevOps handoff with operational scope.

## Assertions

- PASS `request_type_deployment`: CI and release-readiness work is classified as `deployment`.
- PASS `repo_wide_scope_allowed`: Confirmed repository-level non-feature work can use `N/A` feature fields and empty `feature_path_evidence`.
- PASS `devops_handoff_packet`: DevOps handoff requires operational goal, environment, release scope, rollback needs, and risks.

## With Skill Behavior

- Fresh subagent applied the current-branch `pm-agent` SKILL.md and Product Manager Agent README.
- The router maps repo-level CI and pre-launch checks to `request_type: deployment`.
- Because the work is confirmed as repository-level and not feature-scoped, feature fields may use `N/A` and `feature_path_evidence: []`.
- It prepares DevOps handoff only after recording operational goal, environment, release scope, rollback needs, and risks; PM does not directly create CI or deployment configuration.

## Without Skill Baseline

- Fresh without_skill baseline was regenerated on 2026-07-08 from the eval prompt and fixture README only; it did not reuse historical baseline text and did not apply `pm-agent` SKILL.md or the Product Manager Agent README.
- The generic baseline can identify CI and launch readiness as DevOps/deployment work, but may jump into CI configuration advice and omit the PM handoff packet, `change_tier`, repo-wide `N/A` feature-scope rule, and full DevOps handoff context.

## Failures

- None. The current `pm-agent` protocol satisfies deployment classification and repo-wide scope assertions.
- No routing regression found from the PR #98 trigger-description changes.

## Next Steps

- Keep this eval as PM entry coverage for deployment and CI routing.
- Re-run fresh validation if repo-wide feature-scope handling, DevOps handoff packet fields, or entry trigger descriptions change.

## Runtime Artifacts Policy

- No runtime artifacts were committed. The validating subagent did not create runtime files.
- If future transcripts, verdicts, timing data, outputs, or diagnostics are generated, keep them under `tmp/eval-runs/pm-agent-20260708/eval-005/` or another isolated scratch path and do not commit them.
