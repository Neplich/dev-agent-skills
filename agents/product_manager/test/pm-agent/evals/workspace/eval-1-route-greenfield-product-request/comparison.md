# Eval Result: eval-001-route-greenfield-product-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`
- Workspace: `workspace/eval-1-route-greenfield-product-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; current near-empty greenfield README and eval metadata with the BRD-free artifact assertion.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-001-route-greenfield-product-request/`

## Latest result:

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `route_to_idea_to_spec`: PASS — selects `idea-to-spec` as the narrowest PM route.
- `pm_first_guardrail`: PASS — enforces normal `pm-agent` classification and no skip-PM override.
- `context_to_collect`: PASS — names goals, core flow, boundaries, acceptance criteria, and open decisions.
- `expected_pm_artifacts`: PASS — explicitly limits PM artifacts to PRD/DECISIONS and assigns TRD to `engineer-agent:trd-gen`.
- `handoff_boundary`: PASS — delays Designer/Engineer handoff until requirements stabilize.

## With-Skill Behavior

The dispatcher correctly keeps the empty-workspace request on the PM path, defines the required discovery context, and states the updated artifact ownership contract. The former BRD output is absent exactly as required by issue #198.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It advised requirements work before implementation but omitted the explicit no-override classification contract and complete PRD/DECISIONS versus Engineer TRD ownership split.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused the expected behavior difference: the PM artifact list no longer contains BRD.

## Next Steps

- Keep this eval as the direct dispatcher regression gate for the BRD-free greenfield artifact chain.

## Runtime Artifacts Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-001-route-greenfield-product-request/` and are not committed.
