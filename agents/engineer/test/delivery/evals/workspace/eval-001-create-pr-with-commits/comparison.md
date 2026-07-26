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
- Fresh run: both isolated copies initialized local git repositories, created a feature branch and Conventional Commit, ran `npm test`, and pushed to local bare remotes under `tmp/eval-runs/issue-158-round1/engineer-a/`
- External policy: no real GitHub PR or CI run was created; PR body and CI-check steps were assessed semantically

## Assertions

- PASS `assertion_1`: creates a project-conformant feature branch.
- PASS `assertion_2`: creates a Conventional Commit.
- PASS `pr`: proposed PR body includes summary, PM document, Issue #123 and passing tests.
- PASS `ci`: explicitly checks PR CI after creation.

## With Skill Behavior

The candidate verified scope and tests, staged only scoped files, created the branch/commit/push simulation, and produced a complete PR checklist and CI follow-up.

## Without Skill Baseline

The fresh baseline also satisfied 4/4 assertions. The skill adds a more explicit staged-scope review and CI evidence structure, but the assertions do not distinguish it.

## Failures

- With-skill and baseline: none.
- Limitation: real `gh pr create` and hosted CI were intentionally not executed in the fixture sandbox.

## Next Steps

Keep the external-side-effect limitation explicit in future paired runs.

## Runtime Artifacts Policy

Scratch `.git` directories, local bare remotes, responses and diagnostics are ignored and not committed.
