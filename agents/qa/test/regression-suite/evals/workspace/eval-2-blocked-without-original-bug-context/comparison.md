# Eval Result: regression-suite-blocked-without-original-bug-context

## Evaluation Target

- Skill: `regression-suite`
- Test case: blocked-without-original-bug-context
- Test set: QA availability evals
- Entry: workspace `eval-2-blocked-without-original-bug-context`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-04

## With Skill

- Detects that original bug, fix, and environment evidence are missing.
- Returns a blocked regression verdict instead of inventing a verification result.
- Lists the minimum evidence needed to proceed.
- Marks original failure recheck, fixed behavior, adjacent regression checks, platform version confirmation, and PRD/TRD alignment as `blocked` or not executed when evidence is missing.
- Includes original failure recheck, fixed behavior, adjacent regression checks, release recommendation, and evidence confidence in the blocked report.
- Keeps the release recommendation at needs more verification or blocked; it does not infer release readiness from absent failures.
- Requires the platform version and release environment before archiving results, avoids `unknown`, and does not treat a local feature-update check as a release-wide E2E conclusion.

## Baseline

- More likely to provide speculative verification steps as if validation were possible.
- Does not consistently preserve blocked status.
- More likely to omit the missing platform version, original bug evidence, fix context, and environment as explicit blockers.

## Failures

- None. Current `regression-suite` instructions satisfy all eval assertions for missing original evidence, blocked status, structured blocked output, release boundary, and avoiding `unknown` or unscoped release conclusions.

## Next Steps

- Keep this eval for blocked regression handling.
- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
