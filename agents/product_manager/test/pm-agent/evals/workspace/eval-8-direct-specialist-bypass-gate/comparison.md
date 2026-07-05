# Eval Result: pm-agent-direct-specialist-bypass-gate

## Evaluation Target

- Skill: `pm-agent`
- Test case: direct-specialist-bypass-gate
- Test set: PM entry evals for issue #52 / FR-006 scenario 8
- Entry: workspace `eval-8-direct-specialist-bypass-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: direct internal specialist invocation without PRD, TRD, implementation plan, or PM handoff packet
- Expected output: specialist entry gate blocks plan/code/test implementation and returns to `pm-agent` classification.

## With Skill

- The PM handoff entry gate applies even when an internal specialist is directly invoked.
- It requires a PM handoff packet or equivalent confirmed PRD / TRD and current implementation scope before `feature-implementor` planning can proceed.
- It blocks creating an implementation plan, writing code, or writing tests until the request returns to `pm-agent` classification.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic response could treat the explicit specialist invocation as permission to start planning.
- It may incorrectly treat the missing implementation plan as something to create immediately instead of a downstream step after confirmed PM / TRD context.

## Failures

- None. The current gate language satisfies all direct-specialist bypass assertions.

## Next Steps

- Keep this eval as coverage for internal specialist bypass attempts.
- Re-run fresh validation if specialist entry prerequisites change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
