# Eval Result: eval-007-api-adr-engineer-handoff

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: FAIL — 2/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: FAIL

### Assertion Results

- `does_not_use_pm_api_adr_generators`: FAIL — it said the artifacts are Engineer-owned but did not explicitly reject PM internal `api-gen` / `adr-gen`.
- `routes_to_trd_gen`: PASS — routed both artifacts to `engineer-agent:trd-gen`.
- `engineer_paths_mirror_feature_path`: PASS — used `docs/engineer/chat-interface/history-search/`.
- `handoff_contains_feature_path_evidence`: FAIL — the handoff omitted explicit `parent_feature` and `feature_level` fields.

### With-Skill / Baseline Comparison

The with-skill response preserved Engineer ownership and correct paths without writing API/ADR files. The baseline proposed unrelated `docs/api/` and `docs/adr/` paths.

### Failures / Next Steps

- Explicitly state that PM internal API/ADR generators are not used.
- Emit a complete handoff packet with the full feature-path metadata and decision background.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-007-api-adr-engineer-handoff/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-007-api-adr-engineer-handoff`
- Workspace: `workspace/iteration-3/eval-7-api-adr-engineer-handoff`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; confirmed PM PRD at `docs/pm/chat-interface/history-search/PRD.md`, with stale Engineer paths excluded by `execution_cleanup`.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-007-api-adr-engineer-handoff/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `does_not_use_pm_api_adr_generators`: PASS — states that API and ADR are Engineer-owned and PM must not generate them.
- `routes_to_trd_gen`: PASS — explicitly hands off to `engineer-agent:trd-gen`.
- `engineer_paths_mirror_feature_path`: PASS — requires `API.md` and `ADR-*.md` under the full Engineer feature path.
- `handoff_contains_feature_path_evidence`: PASS — includes the feature metadata, approved PRD path, API needs, and ADR decision context.

## With-Skill Behavior

The response preserves the PM/Engineer boundary, uses the confirmed PRD as the source of product truth, and leaves unknown technical constraints as blockers rather than fabricating them. It does not use BRD as a handoff source or lifecycle stage.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and cleaned fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It retained general Engineer ownership but omitted the precise `engineer-agent:trd-gen` route and preferred a non-canonical ADR subdirectory.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no ownership, path, or handoff regression.

## Next Steps

- Keep this eval as coverage for Engineer-owned API/ADR handoff from a confirmed PRD.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-007-api-adr-engineer-handoff/` and are not committed.
