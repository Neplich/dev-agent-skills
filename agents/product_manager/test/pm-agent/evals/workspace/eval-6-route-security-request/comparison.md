# Eval Result: pm-agent-route-security-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-security-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 6; PR #98 trigger-description routing check
- Entry: workspace `eval-6-route-security-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: authorization, dependency, and secrets-risk review request
- Expected output: classify as `security`, capture risk scope, and hand off Security with scope and required output.

## Assertions

- PASS `request_type_security`: Authz, dependency, and secrets-risk review is classified as `security`.
- PASS `security_scope_first`: The route requires risk surface, assets, permissions, data flow, and remediation expectations.
- PASS `security_handoff`: Security receives a bounded handoff with scope and required output.

## With Skill Behavior

- Fresh subagent applied the current-branch `pm-agent` SKILL.md and Product Manager Agent README.
- The router classifies authorization control, dependency vulnerabilities, and secrets risk as `request_type: security`.
- It records risk surface, assets, permissions, data flow, and remediation expectations before handoff.
- It prepares a bounded Security handoff with scope decision, downstream owner, required output, and blockers / risks; PM does not run the security specialist review itself.

## Without Skill Baseline

- Fresh without_skill baseline was regenerated on 2026-07-08 from the eval prompt and fixture README only; it did not reuse historical baseline text and did not apply `pm-agent` SKILL.md or the Product Manager Agent README.
- The generic baseline tends to start a security checklist for authz, dependencies, and secrets, but it does not reliably require PM-side scope capture or produce a Security handoff packet with required output.

## Failures

- None. The current `pm-agent` protocol satisfies security classification and handoff assertions.
- No routing regression found from the PR #98 trigger-description changes.

## Next Steps

- Keep this eval as PM entry coverage for security routing.
- Re-run fresh validation if Security handoff fields, security routing, or entry trigger descriptions change.

## Runtime Artifacts Policy

- No runtime artifacts were committed. The validating subagent did not create runtime files.
- If future transcripts, verdicts, timing data, outputs, or diagnostics are generated, keep them under `tmp/eval-runs/pm-agent-20260708/eval-006/` or another isolated scratch path and do not commit them.
