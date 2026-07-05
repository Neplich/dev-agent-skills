# Eval Result: eval-008-feature-path-mismatch-blocked

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-008-feature-path-mismatch-blocked`
- Test case: feature-path-mismatch-blocked
- Workspace: `workspace/eval-008-feature-path-mismatch-blocked`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/chat-interface/history-search/PRD.md`, and `docs/engineer/chat-interface/TRD.md`.
- Fixture summary: the PRD declares `feature_path: chat-interface/history-search`; the TRD declares parent `feature_path: chat-interface` and `related_prd: docs/pm/chat-interface/PRD.md`.
- Expected output: detect PRD/TRD metadata and related PRD mismatch, block implementation planning, and hand back to `engineer-agent:trd-gen`.

## Assertions

- PASS `detects_prd_trd_path_mismatch`: the skill requires matching PRD/TRD `feature_path`, `parent_feature`, and `feature_level`.
- PASS `checks_related_prd`: output conventions and planner require TRD `related_prd` to point to `docs/pm/{feature_path}/PRD.md`.
- PASS `blocks_implementation_plan`: mismatched TRD blocks `docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md`, code, and tests.
- PASS `hands_off_to_trd_gen`: stale, incomplete, path-mismatched, or conflicting TRDs return to `engineer-agent:trd-gen`.

## With Skill Behavior

Fresh with-skill validation confirmed that Batch 3's direct specialist gate is not diluted by a parent TRD. The current skill should compare the nested PRD with the supplied parent TRD, explicitly report `chat-interface/history-search` versus `chat-interface`, detect that `related_prd` points to `docs/pm/chat-interface/PRD.md` instead of the nested PRD, and stop before writing any plan. The correct handoff is to `engineer-agent:trd-gen` to create or correct the mirrored nested TRD.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic response could accept the parent Chat Interface TRD as close enough and proceed with a plan, or mention mismatch without validating `related_prd`. It would not reliably enforce the mirrored feature path and related-PRD gates before planning.

## Failures

- None.

## Next Steps

- Keep this eval focused on blocking parent/child feature path mismatches before implementation planning.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
