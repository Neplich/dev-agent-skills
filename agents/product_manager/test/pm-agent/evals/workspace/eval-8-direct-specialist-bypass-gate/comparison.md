# Eval Result: pm-agent-direct-specialist-bypass-gate

## Evaluation Target

- Skill: `pm-agent`
- Test case: direct-specialist-bypass-gate
- Test set: PM entry evals for issue #52 / FR-006 scenario 8
- Entry: workspace `eval-8-direct-specialist-bypass-gate`
- Latest result: PARTIAL - deterministic Batch 4 specialist-gate coverage exists,
  but fresh Codex subagent validation and a newly generated without-skill
  baseline are deferred to the post-merge centralized skill-eval pass.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: direct internal specialist request without PRD/TRD, implementation
  scope, or handoff

## With Skill

- Enforces the specialist PM handoff entry gate even when the user names the
  internal specialist directly.
- Requires a PM handoff packet or equivalent confirmed PRD/TRD plus current
  implementation scope. Existing `IMPLEMENTATION_PLAN.md` is not required for
  first-time `feature-implementor` planning, because this specialist creates
  that plan.
- Blocks planning, code changes, and test implementation, then returns the
  request to `pm-agent` classification.

## Without Skill / Baseline

- May assume direct specialist invocation is permission to plan or implement.
- May skip PM classification and source document checks.

## Failures / Coverage Gaps

- Fresh Codex subagent validation has not run for this scenario in this PR.
- A new without-skill baseline will be generated in the post-merge centralized
  skill-eval pass.

## Next Steps

- Run fresh with-skill and without-skill validation in the centralized eval
  phase after Batch 4 merges.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
