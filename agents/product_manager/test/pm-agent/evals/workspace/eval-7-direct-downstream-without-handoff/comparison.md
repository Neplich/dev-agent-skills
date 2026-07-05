# Eval Result: pm-agent-direct-downstream-without-handoff

## Evaluation Target

- Skill: `pm-agent`
- Test case: direct-downstream-without-handoff
- Test set: PM entry evals for issue #52 / FR-006 scenario 7
- Entry: workspace `eval-7-direct-downstream-without-handoff`
- Latest result: PARTIAL - deterministic Batch 4 gate coverage exists, but fresh
  Codex subagent validation and a newly generated without-skill baseline are
  deferred to the post-merge centralized skill-eval pass.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: direct downstream role-router request without PM handoff context

## With Skill

- Rejects direct downstream execution without a PM handoff packet or equivalent
  confirmed source documents.
- Returns the request to `pm-agent` for request type, scope, feature path, and
  handoff readiness classification.
- Avoids starting implementation, tests, delivery, or other role execution.

## Without Skill / Baseline

- May treat the named downstream role as direct execution permission.
- May begin implementation before source documents or scope are confirmed.

## Failures / Coverage Gaps

- Fresh Codex subagent validation has not run for this scenario in this PR.
- A new without-skill baseline will be generated in the post-merge centralized
  skill-eval pass.

## Next Steps

- Run fresh with-skill and without-skill validation in the centralized eval
  phase after Batch 4 merges.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
