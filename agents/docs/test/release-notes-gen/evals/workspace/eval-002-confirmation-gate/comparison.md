# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-002-confirmation-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc` from `agents/docs/test/release-notes-gen/evals/workspace/eval-002-confirmation-gate`.
- Identity schema: `2`
- target_skill_sha256: `9d15471128b5c653c03406ba512b69c7510ab64bfd6b1cba8b6458bff7449a16`
- eval_definition_sha256: `734d8912f6102b866e236fb845ac847f11fde3651b05c29ee143e730ba9a8ce3`
- metadata_sha256: `244623c4cb29666e66fbef86938647497dad20990909aac70827020a236484a7`
- fixture_sha256: `d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f52a12716f836504537cf75e93c1e10d802a32eb7ad0a9945e2057c1a94c3f7c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `875d94bbeede7fb3f25ae54a8099f5bb996a939530b57c2c2295a2fa54bd46e9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_derived_surfaces_unchanged` | PASS | with_skill 的 git_evidence 显示仅新增候选页面；其输出明确列出未修改 releases.json、release-notes/index.md 和导航，并注明待正文确认后执行后续检查。 |
| `reports_unconfirmed_not_ready` | PASS | with_skill 输出包含 confirmation_status: unconfirmed、handoff_status: blocked、release_execution_authorized: false，且未将 pm-agent:github-release-gen 描述为 ready。 |
| `waits_for_explicit_confirmation` | PASS | with_skill 输出展示完整候选正文、六份来源证据映射、确认后涉及的派生路径，并明确请求维护者回复“确认正文”或提出修改。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc; output_sha256=cafe26b0b12ec99203e1b419b9e2104b019a9064f29afa76fd11e0bb09cf9fa6; snapshot_sha256=cd93a5f7bbec3d5c6b30d75d1b50082a0e7f19e4eed780a39a137af0091400e2
- Behavior: 生成完整候选版本说明，保留派生面不变，明确未确认和 blocked 状态，并等待维护者确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc; output_sha256=7bce74b516474866960691b1c7cb645be7833b6ef76db20e0bb61e280a5baea1; snapshot_sha256=cac5bf35bce9034b31a55a4cff04a267c4960df3393ab472b67647bcc97e2f61
- Behavior: 生成候选页面并声称未修改索引、metadata 和导航，但未提供结构化 unconfirmed/blocked handoff，也未展示完整正文、来源映射或确认后计划。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
