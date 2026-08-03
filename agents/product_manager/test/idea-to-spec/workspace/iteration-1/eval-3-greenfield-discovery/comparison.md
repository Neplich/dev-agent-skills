# Eval Result: eval-003-greenfield-discovery

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
- Overall result: PASS

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
