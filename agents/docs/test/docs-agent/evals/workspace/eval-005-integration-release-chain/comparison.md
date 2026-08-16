# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Identity schema: `2`
- target_skill_sha256: `cf826e2e86ef193d8a7294a87c743dead6af892aefcc220dd56ae949fa5c3b40`
- eval_definition_sha256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- metadata_sha256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- fixture_sha256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b9267b74f801c2a671c1ca7ba9bdf9a650058f23cd2d09d1d407f78b09a9bd1c`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | 识别并保留 v1.4.0、ai-search 范围、JOTO-AI/aiportal、签认证据和只读授权边界。 |
| `evaluates_site_release_notes_gate` | PASS | 发现 handoff 自称 ready 但缺少可信 post-tag 权威且版本验证状态冲突，因此阻塞并路由至正式文档审计负责人。 |
| `validates_release_window_basis` | PASS | 确认签认快照中的 release-base、release-candidate 及 v1.3.0/v1.4.0 版本引用可解析，并以快照为依据未猜测替代锚点。 |
| `rejects_missing_pre_tag_authority` | PASS | 明确实际 tag 已存在但没有可复用的可信 pre-tag audit record、anchor、handoff commit 或 inventory identity，未宣称 pre-tag 通过。 |
| `detects_post_tag_evidence_drift` | PASS | 正确识别 release-candidate/tag-entry/evidence-expected 与实际 tag/release-evidence 的 tree 不一致，并判定 blocked。 |
| `blocks_github_release_handoff` | PASS | 明确当前不可进入 GitHub Release 准备或发布，仅在 release_verified 后再移交。 |
| `preserves_no_mutation_boundaries` | PASS | 锁定证据显示 HEAD、分支、ref、diff 和工作区均无变化；候选明确未执行 tag 或 GitHub Release 写入。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=ca84672dc4cfc91d1ac7c8997db0e086a793873be0e1edf5fc8803e7cb9e4f8b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整识别入口、版本窗口、tag/tree 漂移、缺失 pre-tag 权威和 Release Notes 状态冲突，并正确阻塞 GitHub Release handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=aa7316ba43ff1d7f65f526a13b7eedd63ac2d93e05c038c36d94690be511e428; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别主要 tag/tree 漂移和缺失 release_verified，但未呈现 with_skill 的路由与 inventory-authority 细节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
