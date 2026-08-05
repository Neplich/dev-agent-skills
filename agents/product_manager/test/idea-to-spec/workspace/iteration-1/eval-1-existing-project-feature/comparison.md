# Eval Result: eval-001-existing-project-feature-design

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-001-existing-project-feature-design`
- Workspace: `workspace/iteration-1/eval-1-existing-project-feature`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; cleaned existing Web app workspace with Next.js markers and app-catalog TRD; stale `docs/pm/app-tags/` excluded by `execution_cleanup`.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-001-existing-project-feature-design/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `assertion_1`: PASS — starts with current project context and selects `existing-project-feature`.
- `assertion_2`: PASS — advances only the v1 product-goal decision.
- `assertion_3`: PASS — compares three scope options with trade-offs and a recommendation.
- `section`: PASS — asks for confirmation of the current section before continuing.
- `assertion_5`: PASS — names `DECISIONS.md` and the PM feature docs as durable memory.

## With-Skill Behavior

The response inspected the cleaned fixture, summarized the current app-catalog constraints, and kept the first turn inside incremental product shaping. Confirmed outcomes would be stored in `docs/pm/app-tags/DECISIONS.md` and later formalized in `PRD.md`; it did not introduce any BRD generation, validation, or iteration stage.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and cleaned fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It proposed sensible tag features but expanded several design topics at once and did not establish the section-confirmation or `DECISIONS.md` memory contract.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no behavioral regression; this case now uses only PRD and DECISIONS as PM artifacts.

## Next Steps

- Keep this eval as coverage for first-turn context detection, single-decision progression, and durable PM memory after BRD removal.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-001-existing-project-feature-design/` and are not committed.
