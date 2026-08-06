# Eval Result: eval-003-monorepo-scope-clarification

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 4/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `blocked_on_scope`: PASS — detected independent web, admin, and API workspaces and stopped for scope clarification.
- `minimal_clarification`: PASS — asked one scope question only.
- `no_fabricated_catalog`: PASS — wrote no formal catalog or PRD.
- `no_parallel_top_level`: PASS — did not guess workspace names as confirmed feature paths.

### With-Skill / Baseline Comparison

The with-skill response stopped at the smallest scope gate. The baseline wrote a root `FEATURES.md` despite the unresolved scope.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-003-monorepo-scope-clarification/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-003-monorepo-scope-clarification`
- Test case: monorepo-scope-clarification
- Workspace: `workspace/eval-003-monorepo-scope-clarification`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


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
