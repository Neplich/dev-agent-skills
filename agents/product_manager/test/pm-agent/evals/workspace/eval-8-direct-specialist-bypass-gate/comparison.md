# Eval Result: pm-agent-direct-specialist-bypass-gate

## Evaluation Target

- Skill: `pm-agent`
- Test case: direct-specialist-bypass-gate
- Test set: PM entry evals for issue #52 / FR-006 scenario 8
- Entry: workspace `eval-8-direct-specialist-bypass-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08 for PR #98 trigger description revisions

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: direct internal specialist invocation without PRD, TRD, implementation plan, or PM handoff packet
- Expected output: specialist entry gate blocks plan, code, and test implementation, then returns to `pm-agent` classification.

## Assertions

- PASS `specialist_gate_runs`: Direct invocation of an internal specialist still triggers the PM handoff entry gate.
- PASS `requires_handoff_or_docs`: The gate requires a PM handoff packet or equivalent confirmed PRD / TRD and current implementation scope; an existing implementation plan is not treated as the upstream entry prerequisite.
- PASS `blocks_implementation`: The route blocks plan creation, code, and tests, then returns to `pm-agent` classification.

## With Skill Behavior

- Applied `pm-agent` entry routing, Product Manager Agent README guidance, and `feature-implementor` specialist gate evidence.
- The direct request to trigger `feature-implementor` cannot continue because the fixture states that PRD, TRD, implementation plan, and PM handoff packet are missing.
- `feature-implementor` may only start planning after an explicit Engineer / delivery-adjacent PM handoff packet or an equivalent confirmed PRD / TRD plus current implementation-scope decision.
- The correct with-skill response blocks implementation-plan creation, code changes, and test implementation, then returns the request to `pm-agent` for classification, scope, source documents, and `change_tier`.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-08 from the same prompt and fixture without applying or citing the `pm-agent` skill or Product Manager Agent README.
- A generic assistant would likely notice that PRD / TRD / implementation plan are missing and ask for requirements, but it may treat the explicit specialist invocation as permission to start an implementation plan or requirements draft.
- The baseline is weaker because it does not reliably name the internal specialist PM handoff entry gate, does not require a PM handoff packet or equivalent confirmed PRD / TRD plus current implementation scope, and may not return the request to `pm-agent`.

## Failures

- None. The PR #98 trigger description revision and current gate language satisfy all direct-specialist bypass assertions.
- No bypass path found: direct specialist invocation remains blocked without upstream PM handoff or equivalent confirmed documents.

## Next Steps

- Keep this eval as coverage for internal specialist bypass attempts.
- Re-run fresh validation if specialist entry prerequisites change.

## Runtime Artifacts Policy

- No tmp runtime artifacts were created in this validation.
- Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
