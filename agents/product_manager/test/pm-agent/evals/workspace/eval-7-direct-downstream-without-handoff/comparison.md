# Eval Result: pm-agent-direct-downstream-without-handoff

## Evaluation Target

- Skill: `pm-agent`
- Test case: direct-downstream-without-handoff
- Test set: PM entry evals for issue #52 / FR-006 scenario 7
- Entry: workspace `eval-7-direct-downstream-without-handoff`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: direct downstream role-router request without PM handoff context
- Expected output: reject direct downstream execution, return to `pm-agent`, and require PM handoff packet or equivalent confirmed docs.

## Assertions

- PASS `reject_direct_downstream`: The request cannot directly enter `engineer-agent`, code modification, or downstream execution.
- PASS `return_to_pm_agent`: The route returns to `pm-agent` for request type, scope, feature path, and handoff readiness classification.
- PASS `require_handoff_or_docs`: Downstream role routers require a PM handoff packet or equivalent confirmed source documents.

## With Skill Behavior

- The `pm-agent` and downstream execution contract reject starting Engineer implementation without PM classification and source context.
- It returns the request to `pm-agent` for request type, scope, feature path, and handoff readiness classification.
- It requires PM handoff packet or equivalent confirmed PRD / TRD / design / test / deployment / security docs before downstream execution.
- Issue #81 safety-net behavior remains within boundary: direct downstream invocation without prerequisite context is guided back to PM; auto-continue does not turn this into permission to execute Engineer work.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-06 without applying `pm-agent` or the Product Manager Agent README. A generic response could honor the user's "directly use engineer-agent" instruction and start implementation planning.
- It is less reliable about enforcing the PM handoff entry gate when the user explicitly asks to skip PM docs.

## Failures

- None. The current PM entry gate satisfies all direct-downstream defense assertions.
- No issue #81 regression found; the safety-net guidance path returns missing-basis requests to PM and does not authorize downstream work.

## Next Steps

- Keep this eval as PM entry coverage for direct role-router bypass attempts.
- Re-run fresh validation if downstream role-router entry gates change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
