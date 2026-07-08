# Eval Result: pm-agent-direct-downstream-without-handoff

## Evaluation Target

- Skill: `pm-agent`
- Test case: direct-downstream-without-handoff
- Test set: PM entry evals for issue #52 / FR-006 scenario 7; PR #98 trigger-description routing check
- Entry: workspace `eval-7-direct-downstream-without-handoff`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: direct downstream role-router request without PM handoff context
- Expected output: reject direct downstream execution, return to `pm-agent`, and require PM handoff packet or equivalent confirmed docs.

## Assertions

- PASS `reject_direct_downstream`: The request cannot directly enter `engineer-agent`, code modification, or downstream execution.
- PASS `return_to_pm_agent`: The route returns to `pm-agent` for request type, scope, feature path, and handoff readiness classification.
- PASS `require_handoff_or_docs`: Downstream role routers require a PM handoff packet or equivalent confirmed source documents.

## With Skill Behavior

- Fresh subagent applied the current-branch `pm-agent` SKILL.md, Product Manager Agent README, and relevant AGENTS.md downstream gate guidance.
- The router / downstream entry gate rejects the user's attempt to directly use `engineer-agent` and start code changes for a settings-page layout adjustment.
- Because PM handoff packet, equivalent confirmed document chain, and specialist entry basis are missing, the request returns to `pm-agent` for `request_type`, scope, `feature_path`, `change_tier`, and handoff readiness classification.
- Only after PM classification and confirmed source documents can the work be handed to the matching role router.

## Without Skill Baseline

- Fresh without_skill baseline was regenerated on 2026-07-08 from the eval prompt and fixture README only; it did not reuse historical baseline text and did not apply `pm-agent` SKILL.md or the Product Manager Agent README.
- The baseline also tends to reject immediate implementation because the fixture README says missing-handoff downstream requests should return to `pm-agent`, but it does not reliably provide the full PM handoff packet fields, `change_tier`, or downstream gate rationale.

## Failures

- None. The current PM entry gate satisfies all direct-downstream defense assertions.
- No routing regression found from the PR #98 trigger-description changes.

## Next Steps

- Keep this eval as PM entry coverage for direct role-router bypass attempts.
- Re-run fresh validation if downstream role-router entry gates, PM handoff readiness rules, or entry trigger descriptions change.

## Runtime Artifacts Policy

- No runtime artifacts were committed. The validating subagent did not create runtime files.
- If future transcripts, verdicts, timing data, outputs, or diagnostics are generated, keep them under `tmp/eval-runs/pm-agent-20260708/eval-007/` or another isolated scratch path and do not commit them.
