# Eval Result: eval-002-child-feature-under-parent-prd

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-002-child-feature-under-parent-prd`
- Test case: child-feature-under-parent-prd
- Workspace: `workspace/eval-002-child-feature-under-parent-prd`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

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
