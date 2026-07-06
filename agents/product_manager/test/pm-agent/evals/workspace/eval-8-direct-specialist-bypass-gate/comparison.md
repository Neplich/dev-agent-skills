# Eval Result: pm-agent-direct-specialist-bypass-gate

## Evaluation Target

- Skill: `pm-agent`
- Test case: direct-specialist-bypass-gate
- Test set: PM entry evals for issue #52 / FR-006 scenario 8
- Entry: workspace `eval-8-direct-specialist-bypass-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: direct internal specialist invocation without PRD, TRD, implementation plan, or PM handoff packet
- Expected output: specialist entry gate blocks plan/code/test implementation and returns to `pm-agent` classification.

## Assertions

- PASS `specialist_gate_runs`: Direct invocation of an internal specialist still triggers the PM handoff entry gate.
- PASS `requires_handoff_or_docs`: The gate requires PM handoff packet or equivalent confirmed PRD / TRD and current implementation scope; an implementation plan is not treated as the upstream entry prerequisite.
- PASS `blocks_implementation`: The route blocks plan creation, code, and tests, then returns to `pm-agent` classification.

## With Skill Behavior

- The PM handoff entry gate applies even when an internal specialist is directly invoked.
- It requires a PM handoff packet or equivalent confirmed PRD / TRD and current implementation scope before `feature-implementor` planning can proceed.
- It blocks creating an implementation plan, writing code, or writing tests until the request returns to `pm-agent` classification.
- Issue #81 safety-net behavior remains within boundary: auto-continue cannot bypass the specialist entry gate or let PM execute `feature-implementor` planning.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-06 without applying `pm-agent` or the Product Manager Agent README. A generic response could treat the explicit specialist invocation as permission to start planning.
- It may incorrectly treat the missing implementation plan as something to create immediately instead of a downstream step after confirmed PM / TRD context.

## Failures

- None. The current gate language satisfies all direct-specialist bypass assertions.
- No issue #81 regression found; the role-boundary priority blocks direct specialist execution without upstream basis.

## Next Steps

- Keep this eval as coverage for internal specialist bypass attempts.
- Re-run fresh validation if specialist entry prerequisites change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
