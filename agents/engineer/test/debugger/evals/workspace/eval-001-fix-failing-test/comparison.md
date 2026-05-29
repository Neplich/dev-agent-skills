# Eval Result: debugger-fix-failing-test

## Evaluation Target

- Skill: `debugger`
- Test case: fix-failing-test
- Test set: bug reproduction and repair planning gate evals
- Entry: workspace `eval-001-fix-failing-test`
- Latest result: pending fresh Codex subagent validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Notification API returns archived notifications in the active list,
  causing `test/api/notifications.test.ts` to fail.

## With Skill

Expected behavior:

- Reads the failing test and related source.
- Reproduces the failing command and records the assertion failure.
- Uses PRD/TRD expectation to identify that archived notifications must be
  excluded from the active list.
- Outputs a bug analysis report.
- Asks whether to produce a repair implementation plan before modifying code.
- Does not apply the fix, update tests, or claim verification success before
  repair plan confirmation.

## Without Skill / Baseline

- May jump directly to code changes after seeing the failing assertion.
- May skip PRD/TRD expectation checks.
- May report a fix without first asking for repair plan confirmation.

## Failures

- Pending model validation.

## Next Steps

- Run fresh Codex subagent validation after this fixture is reviewed.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be
  committed.
