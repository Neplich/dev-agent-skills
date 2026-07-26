# Eval Result: eval-002-detect-monorepo

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-002-detect-monorepo`
- Test case: detect-monorepo
- Workspace: `workspace/eval-002-detect-monorepo`
- Latest result: PASS (2/2 assertions) - fresh Codex paired validation completed on 2026-07-26

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: repo-level Engineering context, root workspaces metadata, `pnpm-workspace.yaml`, and three package manifests
- Fresh run: isolated paired copies under `tmp/eval-runs/issue-158-round1/engineer-a/`; baseline was regenerated from the same prompt and fixture
- Source branch: `test/issue-158-round1-thin-fixtures`

## Assertions

- PASS `assertion_1`: explicitly identifies a pnpm monorepo from both workspace markers.
- PASS `assertion_2`: lists `apps/web`, `apps/api`, and `packages/shared`.

## With Skill Behavior

The candidate tied the monorepo conclusion to both root manifests and reported every discovered workspace path with package evidence.

## Without Skill Baseline

The fresh baseline also satisfied 2/2 assertions. The fixture makes the classification explicit; the skill adds evidence structure but no assertion-level gain.

## Failures

- With-skill and baseline: none.

## Next Steps

Keep the eval as a stable positive monorepo detection case.

## Runtime Artifacts Policy

Paired outputs and scratch copies are ignored runtime artifacts and are not committed.
