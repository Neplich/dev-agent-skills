# Eval Result: github-reader-focused-pr-iteration-2

## Evaluation Target

- Skill: `github-reader`
- Test case: refined focused PR queue for `cli/cli`
- Test set: `agents/product_manager/test/github-reader/evals/evals.json`
- Entry: workspace `iteration-2/eval-2-focused-pr`
- Latest result: PASS

## With Skill

- Produces a concise PR queue grouped by human review, bot PRs, drafts, and changes requested.
- Orders human review items by waiting time and flags long-wait backlog risk.
- Avoids unrelated milestone or issue exploration for a focused PR request.

## Without Skill

- Not retained for this iteration.

## Failures

- None recorded.

## Next Steps

- Treat this as the latest focused-PR result.
- Runtime PR reports should not be committed.
