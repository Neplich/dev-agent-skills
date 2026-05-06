# Eval Result: bug-analyzer-analyze-test-failure

## Evaluation Target

- Skill: `bug-analyzer`
- Test case: analyze-test-failure
- Test set: QA availability evals
- Entry: workspace `eval-1-analyze-test-failure`
- Latest result: PASS

## With Skill

- Collects failure log and build environment evidence before writing the bug report.
- Separates observed failure facts from suspected root cause.
- Produces a defect-ready summary with reproduction context and evidence references.

## Baseline

- Tends to jump from the 500 error directly to a generic bug report.
- Provides weaker evidence handling and less explicit uncertainty.

## Failures

- None recorded.

## Next Steps

- Keep this eval for evidence-first bug analysis.
- Runtime transcripts, verdicts, timing, and diagnostics should not be committed.
