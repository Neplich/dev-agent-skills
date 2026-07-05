# Eval Result: pm-agent-direct-downstream-without-handoff

## Evaluation Target

- Skill: `pm-agent`
- Test case: direct-downstream-without-handoff
- Test set: PM entry evals for issue #52 / FR-006 scenario 7
- Entry: workspace `eval-7-direct-downstream-without-handoff`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: direct downstream role-router request without PM handoff context
- Expected output: reject direct downstream execution, return to `pm-agent`, and require PM handoff packet or equivalent confirmed docs.

## With Skill

- The `pm-agent` and downstream execution contract reject starting Engineer implementation without PM classification and source context.
- It returns the request to `pm-agent` for request type, scope, feature path, and handoff readiness classification.
- It requires PM handoff packet or equivalent confirmed PRD / TRD / design / test / deployment / security docs before downstream execution.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic response could honor the user's "directly use engineer-agent" instruction and start implementation planning.
- It is less reliable about enforcing the PM handoff entry gate when the user explicitly asks to skip PM docs.

## Failures

- None. The current PM entry gate satisfies all direct-downstream defense assertions.

## Next Steps

- Keep this eval as PM entry coverage for direct role-router bypass attempts.
- Re-run fresh validation if downstream role-router entry gates change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
