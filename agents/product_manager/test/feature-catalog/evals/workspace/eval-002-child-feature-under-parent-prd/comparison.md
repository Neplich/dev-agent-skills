# Eval Result: eval-002-child-feature-under-parent-prd

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: FAIL — 4/5 assertions passed after contract review corrected one raw-judge semantic misclassification; Overall remains FAIL.
- Coverage result: FULL — all 5 assertion scenarios were exercised.
Overall result: FAIL

### Assertion Results

- `parent_prd_context_read`: PASS — the trace read `docs/pm/order-management/PRD.md` before refund code and reused the parent path.
- `child_nested_under_parent`: PASS — `order-management/refunds` is a valid lower-kebab child path under `order-management`; the assertion presents singular `refund` only as an example.
- `feature_level_metadata`: PASS — `parent_feature: order-management` and `feature_level: 2` matched the two-segment path.
- `handoff_packet_fields`: FAIL — the response described next steps but omitted a complete handoff packet and `{source, reason}` evidence entries.
- `no_bulk_prd`: PASS — no PRD/TRD was generated, and the future route named `prd-gen` then `engineer-agent:trd-gen`.

### With-Skill / Baseline Comparison

The with-skill response stayed at the confirmation gate and reused the parent PRD. The baseline wrote a catalog and refund PRD immediately; it is comparison evidence only.

### Failures / Next Steps

- Show the complete post-confirmation handoff packet, including merged `{source, reason}` evidence plus the confirmed catalog source.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-002-child-feature-under-parent-prd/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-002-child-feature-under-parent-prd`
- Test case: child-feature-under-parent-prd
- Workspace: `workspace/eval-002-child-feature-under-parent-prd`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: existing `docs/pm/order-management/PRD.md` parent PRD plus new refund API/service/test code
- Expected output: reuse parent `order-management`, propose refund as a child feature, include consistent metadata and handoff packet fields, and avoid generating PRD/TRD content directly.

## Assertions

- `parent_prd_context_read`: read parent PRD and reuse its `feature_path`
- `child_nested_under_parent`: suggest refund under `order-management`
- `feature_level_metadata`: `parent_feature` and `feature_level` match the nested path
- `handoff_packet_fields`: handoff packet includes feature path fields and `{source, reason}` evidence
- `no_bulk_prd`: no direct PRD/TRD generation

## With Skill

- The `feature-catalog` protocol makes existing PRD feature paths authoritative. The fixture PRD confirms `feature_path: order-management`, `parent_feature: N/A`, and `feature_level: 1`.
- The refund evidence belongs under the parent order-management capability, so the expected suggestion is `order-management/refund` or equivalent lower-kebab child path with `parent_feature: order-management` and `feature_level: 2`.
- The handoff packet must include `feature_path`, `feature`, `parent_feature`, `feature_level`, and `feature_path_evidence` as `{source, reason}` entries derived from the confirmed catalog, plus `source_catalog`.
- The protocol sends confirmed requirements work to `prd-gen` via `pm-agent:idea-to-spec`, and only after PM docs are confirmed does it hand off to `engineer-agent:trd-gen`.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic scan could notice `src/orders/refund/`, but might propose a new top-level `refund` feature or inline route/service/test objects directly into `feature_path_evidence`.
- It may also start writing a refund PRD or TRD instead of stopping at feature path confirmation and handoff.

## Failures

- None. The current `feature-catalog` protocol satisfies parent reuse, child nesting, metadata, handoff packet, and no-PRD/TRD assertions.

## Next Steps

- Keep this eval as coverage for child features under an existing parent PRD.
- Re-run fresh validation if feature-path evidence or catalog-to-spec handoff rules change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, outputs, timing, and diagnostics must remain outside git; the durable result is this `comparison.md`.
