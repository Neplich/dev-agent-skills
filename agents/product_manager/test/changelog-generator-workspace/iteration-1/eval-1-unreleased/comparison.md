# Eval Result: unreleased-changelog

## Evaluation Target

- Skill: `changelog-generator`
- Test case: latest release has no unreleased user-facing changes
- Test set: `agents/product_manager/test/changelog-generator-workspace/evals/evals.json`
- Entry: workspace `iteration-1/eval-1-unreleased`
- Latest result: PASS

## With Skill

- Correctly detects that `main` is identical to the latest release tag.
- Writes an empty `Unreleased` section with a clear no-change note.
- Skips release-bot noise and avoids listing open PRs as shipped changes.

## Without Skill

- Also identifies no merged unreleased changes, but includes extra pending PR context and a prior release section.
- The extra material is useful for diagnosis but less focused for the requested changelog output.

## Failures

- None recorded.

## Next Steps

- Keep the no-change case because it prevents hallucinated changelog entries.
- Runtime changelog files and execution logs should not be committed.
