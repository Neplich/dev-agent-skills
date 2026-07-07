# Eval Result: pm-agent-route-test-writing-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-test-writing-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 3; PR #98 trigger-description routing check
- Entry: workspace `eval-3-route-test-writing-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: test-writing request without confirmed test basis
- Expected output: classify as `validation`, name PRD / TRD / IMPLEMENTATION_PLAN or existing acceptance evidence, then hand off QA or Engineer/test-writer only after expectations are stable.

## Assertions

- PASS `request_type_validation`: The request is classified as `validation` / test verification work.
- PASS `test_basis_first`: The route requires PRD, TRD, confirmed implementation plan, or existing acceptance evidence as the test basis.
- PASS `qa_or_test_writer_handoff`: QA or Engineer/test-writer handoff waits until expectations and source documents are stable.

## With Skill Behavior

- Fresh subagent applied the current-branch `pm-agent` SKILL.md and Product Manager Agent README.
- The router classifies the order-refund exception-branch test request as `validation`.
- It does not treat the request as ready for direct test writing because the source basis is not confirmed.
- It requires PRD, TRD, confirmed IMPLEMENTATION_PLAN, or existing acceptance evidence before handoff to `qa-agent` or `engineer-agent` test-writer path.

## Without Skill Baseline

- Fresh without_skill baseline was regenerated on 2026-07-08 from the eval prompt and fixture README only; it did not reuse historical baseline text and did not apply `pm-agent` SKILL.md or the Product Manager Agent README.
- The generic baseline tends to ask about refund rules, exception lists, APIs, and desired test types, and may suggest QA or a test engineer, but it does not reliably produce `request_type: validation`, `change_tier`, a PM handoff packet, or the formal test-basis gate.

## Failures

- None. The current `pm-agent` protocol satisfies the validation and test-basis assertions.
- No routing regression found from the PR #98 trigger-description changes.

## Next Steps

- Keep this eval as PM entry coverage for test-writing requests.
- Re-run fresh validation if QA or Engineer/test-writer handoff criteria, test-basis rules, or entry trigger descriptions change.

## Runtime Artifacts Policy

- No runtime artifacts were committed. The validating subagent did not create runtime files.
- If future transcripts, verdicts, timing data, outputs, or diagnostics are generated, keep them under `tmp/eval-runs/pm-agent-20260708/eval-003/` or another isolated scratch path and do not commit them.
