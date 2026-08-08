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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e4cd9b0e262233f5d6a944962f6bf7c4c1323776752d0c1e41ea8bac4c33f829`
- Skill overlay SHA-256: `3f39f62240fb387c41fff7ebe0f42bb66e13cd2eda97d0b2c78636c06bb45d87`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `381b074083537f3d71cb0a28bd3dbbcbf80ece8371ca5fba3a891d822f995603`
- Metadata SHA-256: `9511751d671a5ae5883161ea664a79cdce7fc89cb2e17e607a976174a239c8f6`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `parent_prd_context_read` | NOT_EXERCISED | with_skill 引用了父 PRD 并复用了 order-management，但锁定证据无法证明实际读取顺序。 |
| `child_nested_under_parent` | PASS | 建议路径 order-management/refunds，明确作为 order-management 的二级子功能，而非顶层目录。 |
| `feature_level_metadata` | PASS | 表格同时给出 parent_feature=order-management、层级=2，且路径包含两段。 |
| `handoff_packet_fields` | NOT_EXERCISED | 候选正确停在等待用户确认目录的交互步骤；确认后的 handoff packet 尚未发生，故字段完整性无法 exercised。 |
| `no_bulk_prd` | NOT_EXERCISED | 候选未直接生成 PRD/TRD，并等待确认后再交接；后续生成流程尚未发生，无法判定所需 handoff 字段和具体生成器指向。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=aacabee51e8d8dca9d73fbf4becaaecd48da0836c34ef18593c0062464b70362; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 读取并复用父功能上下文，提出嵌套退款路径及元数据，先请求用户确认，再说明后续交接步骤；未执行文档写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=8018b64c15f2a060bb95bec3edca11a45b8a1335714ee6b9edf40335a639eac7; snapshot_sha256=46feb464d83fdab46766fde7db2b2f251ba07acaece81362cee41ce0f8f56f45
- Behavior: 直接修改了父 PRD并生成退款 PRD，未提供确认式流程或完整 handoff packet。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 用户确认退款目录后，再验证 catalog 更新及完整 handoff packet 字段。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c7dc67ac03b6fbf2bf69bb7af239cc79636a61220df238e51a6c8f891a2b2bbf`
- Skill overlay SHA-256: `5fabe64a432e7077b010b055323ac846ade69c047e7f21a1ce71459e61d31a42`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `381b074083537f3d71cb0a28bd3dbbcbf80ece8371ca5fba3a891d822f995603`
- Metadata SHA-256: `9511751d671a5ae5883161ea664a79cdce7fc89cb2e17e607a976174a239c8f6`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `parent_prd_context_read` | PASS | with_skill 引用了并依据 docs/pm/order-management/PRD.md，使用 order-management 作为 parent_feature，并将退款路径置于其下。 |
| `child_nested_under_parent` | PASS | with_skill 明确建议 feature_path 为 order-management/refund，并展示为 order-management 下的二级 refund，而非顶层目录。 |
| `feature_level_metadata` | PASS | with_skill 给出 parent_feature=order-management、feature_path=order-management/refund、feature_level=2，元数据与路径段数一致。 |
| `handoff_packet_fields` | FAIL | with_skill 未提供包含 feature_path、feature、parent_feature、feature_level、feature_path_evidence 的完整 handoff packet，也未提供 {source, reason} 条目列表或确认后的 catalog 证据归并。 |
| `no_bulk_prd` | FAIL | with_skill 未直接生成 PRD/TRD 正文，但后续仅泛称“补充退款 PRD”及交给 Engineer 生成 TRD，没有明确指向 prd-gen 或 engineer-agent:trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=29f67b40db330b17d99881411f477210ceadb5dd84c688892042ce2e52e9716f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确读取并复用父 PRD 上下文，提出 order-management/refund 的二级归属并给出一致元数据；但缺少完整 handoff packet 和明确的 prd-gen、engineer-agent:trd-gen 路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d30a63f3453aaf3bd01618d870dc101f5d610329fec8c95cdf338a27c46a679e; fixture_sha256=e64d0dc500eb5720a57f43e64b9a52c75b87f674117c2e966a459db4cd412910; output_sha256=14da5b75a5fc939b7bb016f402948d0615ce4943d8a982ae03b09b023d589d53; snapshot_sha256=4d9bef83d1238e2322950a13d92248f4b5e2d4da9197585ff04360334c32d9ea
- Behavior: 创建并更新了功能目录和父 PRD，建议退款归入 order-management/refund-management；但未提供要求的 handoff packet 字段，也未按指定代理路由 PRD/TRD。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- handoff packet 字段及共享证据契约缺失
- PRD/TRD 后续流程未明确指向 prd-gen 和 engineer-agent:trd-gen
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
