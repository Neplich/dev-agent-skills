# Eval Result: pm-agent-change-tier-standard-full-gate

## Evaluation Target

- Skill: `pm-agent`
- Test case: change-tier-standard-full-gate
- Test set: change-tier contract evals for issue #55 / FR-008
- Entry: workspace `eval-11-change-tier-standard-full-gate`
- Latest result: PARTIAL - deterministic Batch 4 definition and pytest coverage
  exist, but fresh centralized subagent validation is deferred to the
  post-merge skill-eval pass.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: refund approval behavior change mislabeled as small

## With Skill

- Classifies the request as `existing_update`.
- Rejects `hotfix` because the approved business behavior changes.
- Keeps PRD/TRD or equivalent expectation alignment before downstream handoff.

## Without Skill / Baseline

- May accept the user's "small" framing and skip expectation alignment.
- May hand off implementation before product behavior is confirmed.

## Failures / Coverage Gaps

- Fresh Codex subagent validation has not run for this scenario in this PR.
- A new without-skill baseline will be generated in the post-merge centralized
  skill-eval pass.

## Next Steps

- Run fresh with-skill and without-skill validation in the centralized eval
  phase after Batch 4 merges.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
