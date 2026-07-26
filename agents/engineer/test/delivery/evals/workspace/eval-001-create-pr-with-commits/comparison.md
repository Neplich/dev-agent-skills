# Eval Result: eval-001-create-pr-with-commits

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`
- Test case: create-pr-with-commits
- Workspace: `workspace/eval-001-create-pr-with-commits`
- Latest result: PASS (4/4 assertions) - fresh Codex paired validation completed on 2026-07-26

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: completed-work handoff, PM reference, changed source/test, passing test command and CI workflow
- Fresh run: both isolated copies created a feature branch and Conventional Commit, ran `npm test`, pushed a remote branch, opened a real temporary GitHub PR, and waited for hosted CI.
- Hosted evidence: with_skill [PR #170](https://github.com/Neplich/dev-agent-skills/pull/170) at `129da903c5a2be7d25d53ed58ab28d7ab77459d5`; fresh without_skill [PR #169](https://github.com/Neplich/dev-agent-skills/pull/169) at `602726696738d32095ee63225837946e247b7152`.
- Cleanup: both temporary PRs were closed without merge after validation and both remote branches were deleted.

## Assertions

- PASS `assertion_1`: creates a project-conformant feature branch.
- PASS `assertion_2`: creates a Conventional Commit.
- PASS `pr`: each side created a real GitHub PR whose body includes a summary, canonical PM document, Issue #123 and passing tests.
- PASS `ci`: each side waited for hosted `repository-contract`, `eval-contract`, `doc-contract` and `python-tests`; all eight checks completed with `SUCCESS`.

## With Skill Behavior

The candidate verified scope and tests, staged only scoped files, completed branch/commit/push/PR delivery, and waited for all hosted CI checks before reporting success.

## Without Skill Baseline

The fresh baseline independently created PR #169 and waited for all four hosted CI checks, so it also satisfied 4/4 assertions. The skill adds a more explicit staged-scope review and CI evidence structure, but the assertions do not distinguish it.

## Failures

- With-skill and baseline: none.

## Next Steps

Keep the temporary-PR cleanup rule and hosted CI evidence requirement explicit in future paired runs.

## Runtime Artifacts Policy

Scratch `.git` directories, responses and diagnostics are ignored and not committed. Temporary PRs are retained only as closed GitHub evidence; their remote branches were deleted.
