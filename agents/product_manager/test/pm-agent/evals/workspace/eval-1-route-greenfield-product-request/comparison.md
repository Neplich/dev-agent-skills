# Eval Result: pm-agent-route-greenfield-product-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-greenfield-product-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 1; PR #98 trigger-description routing check
- Entry: workspace `eval-1-route-greenfield-product-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: empty-workspace product idea request
- Expected output: route to `idea-to-spec`, keep the PM-first boundary, name the PM artifacts and downstream handoff points.

## Assertions

- PASS `route_to_idea_to_spec`: `pm-agent` selects `idea-to-spec` as the narrowest PM route for product discovery, scope shaping, and spec creation.
- PASS `pm_first_guardrail`: The empty-workspace product idea is kept out of `engineer-agent` and project scaffolding unless the user explicitly bypasses PM.
- PASS `context_to_collect`: The route names user goals, core flows, scope boundaries, acceptance criteria, and open questions as the next PM context.
- PASS `expected_pm_artifacts`: The PM outputs are PRD, BRD, and DECISIONS; TRD remains an Engineer-owned follow-up after requirements stabilize.
- PASS `handoff_boundary`: Designer or Engineer handoff only happens after PM scope is stable.

## With Skill Behavior

- Fresh subagent applied the current-branch `pm-agent` SKILL.md and Product Manager Agent README.
- The router treats the empty or near-empty AI chat assistant request as PM-first and routes it to `pm-agent:idea-to-spec`.
- It blocks direct `engineer-agent` handoff or project scaffolding because the user is still describing product behavior and explicitly asked not to write code.
- It names the context to collect: user goal, core chat flow, conversation-history scope, acceptance criteria, open questions, PRD / BRD / DECISIONS output, and later `engineer-agent:trd-gen` after scope is stable.

## Without Skill Baseline

- Fresh without_skill baseline was regenerated on 2026-07-08 from the eval prompt and fixture README only; it did not reuse historical baseline text and did not apply `pm-agent` SKILL.md or the Product Manager Agent README.
- The generic baseline tends to recommend first clarifying requirements or a product spec before design and development, but it does not reliably name `idea-to-spec`, the PM-first guardrail, PRD / BRD / DECISIONS, TRD ownership, or delayed Designer / Engineer handoff.

## Failures

- None. All assertions are satisfied by the current `pm-agent` routing and PM-first guardrail.
- No routing regression found from the PR #98 trigger-description changes.

## Next Steps

- Keep this eval as PM entry coverage for empty-workspace product ideas.
- Re-run fresh validation only when `pm-agent`, `idea-to-spec`, PM handoff rules, or entry trigger descriptions change.

## Runtime Artifacts Policy

- No runtime artifacts were committed. The validating subagent did not create runtime files.
- If future transcripts, verdicts, timing data, outputs, or diagnostics are generated, keep them under `tmp/eval-runs/pm-agent-20260708/eval-001/` or another isolated scratch path and do not commit them.
