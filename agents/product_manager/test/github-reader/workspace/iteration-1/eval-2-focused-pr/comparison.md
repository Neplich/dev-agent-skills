# Eval Result: github-reader-focused-pr

## Evaluation Target

- Skill: `github-reader`
- Test case: focused PR review queue for `cli/cli`
- Test set: `agents/product_manager/test/github-reader/evals/evals.json`
- Entry: workspace `iteration-1/eval-2-focused-pr`
- Latest result: PASS

## With Skill

- Selects a focused PR-query path instead of fetching unrelated project data.
- Sorts review-waiting PRs by wait time.
- Separates human review queue, bot PRs, drafts, and changes-requested items.

## Without Skill

- Can produce a useful PR report, but has weaker routing discipline and less explicit scope control.

## Failures

- None recorded.

## Next Steps

- Keep this eval to protect focused-query behavior.
- Runtime PR reports and execution logs should not be committed.
