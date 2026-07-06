# Eval Result: pm-agent-route-greenfield-product-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-greenfield-product-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 1
- Entry: workspace `eval-1-route-greenfield-product-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: empty-workspace product idea request
- Expected output: route to `idea-to-spec`, keep the PM-first boundary, name the PM artifacts and downstream handoff points.

## Assertions

- PASS `route_to_idea_to_spec`: `pm-agent` selects `idea-to-spec` as the narrowest PM route for product discovery, scope shaping, and spec creation.
- PASS `pm_first_guardrail`: The empty-workspace product idea is kept out of `engineer-agent` and project scaffolding unless the user explicitly bypasses PM.
- PASS `context_to_collect`: The route names goals, core flows, scope, acceptance criteria, and open questions as the next PM context.
- PASS `expected_pm_artifacts`: The PM outputs are PRD, BRD, and DECISIONS; TRD remains an Engineer-owned follow-up after requirements stabilize.
- PASS `handoff_boundary`: Designer or Engineer handoff only happens after PM scope is stable.

## With Skill Behavior

- The `pm-agent` protocol treats empty or near-empty product requests as PM-first and routes the AI chat assistant idea to `idea-to-spec`.
- It blocks direct engineering bootstrap unless the user explicitly asks to skip PM.
- It names the context to collect: user goal, core flows, scope, acceptance criteria, open questions, PRD / BRD / DECISIONS output, and later `engineer-agent:trd-gen` after scope is stable.
- Issue #81 safety-net behavior remains within boundary: closeout can propose Designer or Engineer as the next owner after PM discovery, but `pm-agent` does not execute design or engineering work itself.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-06 without applying `pm-agent` or the Product Manager Agent README. A generic response could recommend scaffolding or implementation planning for the left-right chat UI because the user describes a concrete screen.
- It may mention product clarification, but it is less reliable about the formal PM-first guardrail, the `idea-to-spec` route, and the delayed Designer / Engineer handoff boundary.

## Failures

- None. All assertions are satisfied by the current `pm-agent` routing and PM-first guardrail.
- No issue #81 regression found; auto-continue does not bypass the empty-workspace PM-first gate or cross-role handoff boundary.

## Next Steps

- Keep this eval as PM entry coverage for empty-workspace product ideas.
- Re-run fresh validation only when `pm-agent`, `idea-to-spec`, or PM handoff rules change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
