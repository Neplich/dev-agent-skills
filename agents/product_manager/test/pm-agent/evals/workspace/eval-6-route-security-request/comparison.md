# Eval Result: pm-agent-route-security-request

## Evaluation Target

- Skill: `pm-agent`
- Test case: route-security-request
- Test set: PM entry evals for issue #52 / FR-006 scenario 6
- Entry: workspace `eval-6-route-security-request`
- Latest result: PASS (deterministic Batch 2 route coverage)

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: authorization, dependency, and secret-risk review request

## With Skill

- Classifies the request as `security`.
- Records risk surface, assets, permissions, data flow, and remediation
  expectations.
- Hands off to Security with scope and required output.

## Without Skill / Baseline

- May start a security checklist without PM-side classification.
- Less consistently names assets, permissions, and data-flow scope before
  handoff.

## Failures

- None recorded in deterministic coverage.

## Next Steps

- Re-run with fresh Codex subagent validation when the Batch 4 full eval pass is
  authorized.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
