# Eval Result: cli-feature-release-notes

## Evaluation Target

- Skill: `release-notes-generator`
- Test case: GitHub CLI `v2.88.0` release notes
- Test set: `agents/product_manager/test/release-notes-generator/evals/evals.json`
- Entry: workspace `eval-1-cli-feature`
- Latest result: PASS

## With Skill

- Produces user-facing release notes with highlights, bug fixes, improvements, upgrade commands, and PR links.
- Avoids raw conventional-commit prefixes and bot-noise content.
- Iteration 2 expands feature coverage and examples while preserving release-note structure.

## Without Skill

- Produces a plausible release note, but is more exhaustive and less curated.

## Failures

- None recorded.

## Next Steps

- Keep this eval for CLI-style feature-heavy release notes.
- Runtime release-note files and timing data should not be committed.
