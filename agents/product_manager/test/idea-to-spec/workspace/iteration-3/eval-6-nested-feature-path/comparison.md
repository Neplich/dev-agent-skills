# Eval Result: eval-006-nested-feature-path

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
- Overall result: PASS

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
