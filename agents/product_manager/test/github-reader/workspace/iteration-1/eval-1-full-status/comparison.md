# Eval Result: github-reader-full-status

## Evaluation Target

- Skill: `github-reader`
- Test case: full project status for `anthropics/anthropic-sdk-python`
- Test set: `agents/product_manager/test/github-reader/evals/evals.json`
- Entry: workspace `iteration-1/eval-1-full-status`
- Latest result: PASS

## With Skill

- Separates milestones, open issues, PR queue, and health summary.
- Calls out missing milestones, unassigned issues, stale issues, draft PRs, approved PRs, and review backlog.
- Produces a report oriented toward project status decisions.

## Without Skill

- Fetches similar GitHub data, but mixes more raw repository overview and manual-analysis notes into the output.
- Less clearly separates queue status from general repository metadata.

## Failures

- None recorded.

## Next Steps

- Keep this eval as the broad status-report case.
- Runtime status reports and execution logs should not be committed.
