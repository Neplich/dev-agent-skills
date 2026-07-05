# Eval Result: pm-agent-route-security-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-security-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 6
- Entry: workspace `eval-6-route-security-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: authorization, dependency, and secrets-risk review request
- Expected output: classify as `security`, capture risk scope, and hand off Security with scope and required output.

## With Skill

- The `pm-agent` protocol maps authorization, dependency risk, secrets, privacy, upload, webhook, login, and data-flow risk requests to `security`.
- It requires recording risk surface, assets, permissions, data flow, and remediation expectations.
- It hands off to Security with a bounded review packet instead of doing the security specialist work itself.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic response could start a broad security checklist immediately.
- It may miss the PM-side scope packet and required output definition for Security.

## Failures

- None. The current `pm-agent` protocol satisfies security classification and handoff assertions.

## Next Steps

- Keep this eval as PM entry coverage for security routing.
- Re-run fresh validation if Security handoff fields change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git.
