# Eval Result: eval-003-greenfield-discovery

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 3/3 assertions passed.
- Coverage result: FULL — all 3 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `assertion_1`: PASS — no PRD or TRD was generated in the first turn.
- `assertion_2`: PASS — one core product-scenario decision was presented with options and a recommendation.
- `assertion_3`: PASS — the response correctly stayed in discovery until the direction stabilizes.

### With-Skill / Baseline Comparison

The with-skill response stayed in `greenfield-discovery` and advanced one decision. The baseline also avoided a PRD but asked five questions and presented five routes at once.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-003-greenfield-discovery/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-003-greenfield-discovery`
- Workspace: `workspace/iteration-1/eval-3-greenfield-discovery`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; near-empty knowledge Q&A workspace with minimal notes, no formal PM docs, and no selected stack.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-003-greenfield-discovery/`

## Latest Result

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `assertion_1`: PASS — does not generate a full PRD or TRD in the first turn.
- `assertion_2`: PASS — selects `greenfield-discovery` and asks one use-case decision.
- `assertion_3`: PASS — defers PRD/DECISIONS formalization until direction stabilizes.

## With-Skill Behavior

The response explicitly avoided assumptions about users, sources, permissions, and metrics, compared three primary-use-case options, and stopped at one confirmation point. The post-discovery artifact chain is PRD plus DECISIONS; no BRD stage appears.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It avoided an immediate PRD but asked several discovery questions in parallel and did not make lane or durable-memory timing explicit.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no behavioral regression.

## Next Steps

- Keep this eval as coverage for greenfield discovery discipline and direct PRD/DECISIONS formalization after scope stability.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-003-greenfield-discovery/` and are not committed.
