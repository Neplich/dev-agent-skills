# Eval Result: eval-003-monorepo-scope-clarification

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-003-monorepo-scope-clarification`
- Test case: monorepo-scope-clarification
- Workspace: `workspace/eval-003-monorepo-scope-clarification`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: pnpm monorepo with independently deployed `apps/web`, `apps/admin`, and `services/api`, with no PM docs
- Expected output: blocked on scope, ask exactly one minimal scope clarification question, and avoid confirmed catalog or guessed parallel top-level feature paths.

## Assertions

- `blocked_on_scope`: identify multiple workspaces and unresolved scope
- `minimal_clarification`: ask one smallest clarification question
- `no_fabricated_catalog`: do not fabricate a confirmed catalog or PRD
- `no_parallel_top_level`: do not guess each workspace as a settled top-level feature path

## With Skill

- The `feature-catalog` edge-case rule treats undetermined monorepo scope as `blocked`.
- The fixture clearly exposes three independently deployed surfaces: `apps/web`, `apps/admin`, and `services/api`.
- The correct with-skill behavior is to ask one minimal question, such as whether to catalog `apps/web`, `apps/admin`, `services/api`, or all of them, and stop.
- It does not create `docs/pm/FEATURE_CATALOG.md`, generate PRDs, or present guessed top-level feature paths as confirmed conclusions.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic response could eagerly inventory all packages and produce a catalog despite unresolved scope.
- It may ask several discovery questions or treat each workspace name as a confirmed top-level feature path.

## Failures

- None. The current `feature-catalog` protocol satisfies the blocked, single-question, no-fabrication, and no-parallel-top-level assertions.

## Next Steps

- Keep this eval as coverage for monorepo scope clarification.
- Re-run fresh validation if monorepo scope or blocked-state rules change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, outputs, timing, and diagnostics must remain outside git; the durable result is this `comparison.md`.
