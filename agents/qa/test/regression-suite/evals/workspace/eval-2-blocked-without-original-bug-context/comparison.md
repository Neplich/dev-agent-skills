# Eval Result: regression-suite-blocked-without-original-bug-context

## Evaluation Target

- Skill: `regression-suite`
- Test case: blocked-without-original-bug-context
- Test set: QA availability evals
- Entry: workspace `eval-2-blocked-without-original-bug-context`
- Latest result: PASS

## With Skill

- Detects that original bug, fix, and environment evidence are missing.
- Returns a blocked regression verdict instead of inventing a verification result.
- Lists the minimum evidence needed to proceed.

## Baseline

- More likely to provide speculative verification steps as if validation were possible.
- Does not consistently preserve blocked status.

## Failures

- None recorded.

## Next Steps

- Keep this eval for blocked regression handling.
- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
