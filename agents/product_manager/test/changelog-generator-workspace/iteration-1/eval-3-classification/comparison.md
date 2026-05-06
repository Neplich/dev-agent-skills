# Eval Result: changelog-classification

## Evaluation Target

- Skill: `changelog-generator`
- Test case: conventional-commit title classification
- Test set: `agents/product_manager/test/changelog-generator-workspace/evals/evals.json`
- Entry: workspace `iteration-1/eval-3-classification`
- Latest result: PASS

## With Skill

- Strips conventional prefixes from final user-facing entries.
- Skips dependency, docs, and CI-only changes.
- Marks the breaking `feat!` entry clearly and places it before normal additions.
- Produces Added, Changed, Removed, Fixed, and Security sections.

## Without Skill

- Leaves raw prefixes in several final entries.
- Misplaces the breaking feature as a normal `Changed` item.
- Produces a usable but less polished changelog.

## Failures

- None recorded.

## Next Steps

- Keep this eval to protect changelog classification and title cleanup rules.
- Runtime changelog files and execution logs should not be committed.
