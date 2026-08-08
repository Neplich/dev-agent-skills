# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-002-child-feature-under-parent-prd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-002-child-feature-under-parent-prd`.
- Fixture SHA-256: `e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910`
- Prompt SHA-256: `d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `807b576a5130a49581d58f258e32f9a7f916850f2f335e3a48ede3a7886a942b`
- Skill overlay SHA-256: `96eaf3768827f13d232245de107b17f5e814bef969da3eb231f62d9287d9d070`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `381b074083537f3d71cb0a28bd3dbbcbf80ece8371ca5fba3a891d822f995603`
- Metadata SHA-256: `9511751d671a5ae5883161ea664a79cdce7fc89cb2e17e607a976174a239c8f6`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `parent_prd_context_read` | PASS | with_skill 输出明确引用 docs/pm/order-management/PRD.md，并复用 order-management 作为父功能路径。 |
| `child_nested_under_parent` | PASS | 建议路径为 order-management/refund，并明确不是新建顶层目录。 |
| `feature_level_metadata` | PASS | 候选目录信息包含 parent_feature: order-management、feature_level: 2，且建议路径为两段 lower-kebab-case 路径。 |
| `handoff_packet_fields` | FAIL | 输出未提供包含 feature_path、feature、parent_feature、feature_level、feature_path_evidence 的完整 handoff packet，也未提供要求的 {source, reason} 条目列表。 |
| `no_bulk_prd` | FAIL | with_skill 未直接生成 PRD/TRD 正文，但确认后的交接说明未明确指向 prd-gen，也未显式指向 engineer-agent:trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=4c4f210721edc8909432ea1f8a3c812989d6ea097510529d8e53bdda82dfd32b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并复用父 PRD 路径，将退款嵌套为 L2 子功能，且等待路径确认后再更新目录；handoff packet 字段和明确的 prd-gen、engineer-agent:trd-gen 指向不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=9229c01cd6f635a1dc05961af7284242121144f02846ea55120617bd674712f1; snapshot_sha256=ae87eac831773902b7fdd7ae79884f2dd1e9f88885b71f65e763dc0138a9e069
- Behavior: 完成了目录建议并直接修改/生成目录和退款 PRD，但缺少规范化 handoff packet，并越界生成了退款 PRD。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未提供完整共享契约 handoff packet。
- with_skill 未明确给出 prd-gen 和 engineer-agent:trd-gen 的后续指向。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

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
