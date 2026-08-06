# Eval Result: eval-006-nested-feature-path

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: FAIL — 3/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: FAIL

### Assertion Results

- `scan_existing_prds`: PASS — the trace shows the existing PM PRDs were scanned and read before choosing a path.
- `nested_feature_path`: PASS — resolved `chat-interface/messages/history/search`.
- `no_parallel_top_level`: PASS — did not choose a truncated or top-level sibling path.
- `handoff_fields`: FAIL — no complete handoff packet was produced, and `feature_path_evidence` was missing.

### With-Skill / Baseline Comparison

The with-skill candidate correctly resolved the four-level path and stayed read-only. The baseline also found the nested path; it is comparison evidence only.

### Failures / Next Steps

- Include `feature_path`, `feature`, `parent_feature`, `feature_level`, and evidence-backed `feature_path_evidence` in an explicit handoff packet.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-006-nested-feature-path/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`
- Workspace: `workspace/iteration-3/eval-6-nested-feature-path`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; approved three-level PRD chain with all candidate stale child paths excluded by `execution_cleanup`.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-006-nested-feature-path/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `scan_existing_prds`: PASS — reads the complete `chat-interface/messages/history` PRD ancestry.
- `nested_feature_path`: PASS — resolves `chat-interface/messages/history/search` with parent and level metadata.
- `no_parallel_top_level`: PASS — rejects all parallel and truncated candidate directories.
- `handoff_fields`: PASS — includes `feature_path`, `feature`, `parent_feature`, `feature_level`, and structured `feature_path_evidence`.

## With-Skill Behavior

The response uses the existing PRD chain as the authoritative ownership evidence, proposes a child PRD and DECISIONS directory only under the confirmed parent, and keeps the handoff not ready until search scope is confirmed. No BRD context is required or emitted.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and cleaned fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It found the correct four-level path but used weaker path-only evidence and did not consistently preserve the not-ready PM gate.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no feature-path or handoff regression; ownership is fully established by PRDs.

## Next Steps

- Keep this eval as coverage for PRD-based nested feature ownership after BRD removal.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-006-nested-feature-path/` and are not committed.
