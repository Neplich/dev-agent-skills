# Eval Result: pm-agent-change-tier-hotfix-fast-lane

## Evaluation Target

- Skill: `pm-agent`
- Test case: change-tier-hotfix-fast-lane
- Test set: change-tier contract evals for issue #55 / FR-008
- Entry: workspace `eval-10-change-tier-hotfix-fast-lane`
- Latest result: PARTIAL - deterministic Batch 4 definition and pytest coverage
  exist, but fresh centralized subagent validation is deferred to the
  post-merge skill-eval pass.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: already-scoped README link fix with verification evidence

## With Skill

- Classifies the request as `hotfix` because it does not change approved
  behavior and can be covered by direct evidence.
- Allows the fast lane only after classification.
- Keeps scope, source evidence, and verification evidence requirements.

## Without Skill / Baseline

- May skip `change_tier` classification.
- May treat the fast lane as permission to omit verification evidence.

## Failures / Coverage Gaps

- Fresh Codex subagent validation has not run for this scenario in this PR.
- A new without-skill baseline will be generated in the post-merge centralized
  skill-eval pass.

## Next Steps

- Run fresh with-skill and without-skill validation in the centralized eval
  phase after Batch 4 merges.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
