# Eval Result: eval-004-greenfield-bootstrap-routing

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`
- Workspace: `workspace/iteration-2/eval-4-greenfield-bootstrap-routing`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; empty-workspace AI assistant request with stale root `PRD.md` excluded by `execution_cleanup`.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-004-greenfield-bootstrap-routing/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `assertion_1`: PASS — reports an empty workspace, undetermined stack, and no current docs after cleanup.
- `pm_first_lane`: PASS — selects PM-first `greenfield-bootstrap`.
- `pm_first`: PASS — explicitly avoids engineering scaffold commands.
- `assertion_4`: PASS — routes to `project-init`, PRD skeleton, and DECISIONS after one product decision.

## With-Skill Behavior

The response did not reuse stale root output or start implementation. It kept the feature path provisional, used a single product-positioning decision, and described the durable bootstrap as PRD/DECISIONS only. Removing BRD therefore produces the intended simplified document chain.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and cleaned fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It respected the no-code request but drafted a broad PRD skeleton immediately and expanded multiple unresolved topics at once.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused the expected artifact-chain difference, not a regression: bootstrap no longer includes any BRD step.

## Next Steps

- Keep this eval as coverage for empty-workspace PM-first routing and the PRD/DECISIONS bootstrap contract.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-004-greenfield-bootstrap-routing/` and are not committed.
