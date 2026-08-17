# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-005-outline-sections-quality-exclusion`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-005-outline-sections-quality-exclusion`.
- Identity schema: `2`
- target_skill_sha256: `ed7c0a44968df88c4831e9abe2b9be4922e4fa2cd6bcbd8dc6dd7e927ff9c87a`
- eval_definition_sha256: `5768440d836f6d58f2492f6254c4eaae18fe913a310437aaee98134c39857a50`
- metadata_sha256: `a9879c47e38cec76a35a3ff0087c5b764086d8e7ca04745f8977bbd30db8f459`
- fixture_sha256: `f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f3cdc20a6c2d6d35b8761172794fe96e07166b0922a8d802a01f520259d39177`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41bf9818330e1ae365d336932a5653b591537342874ba68ae701f1478bc7b159`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `follows_outline_sections` | PASS | with_skill 正文仅包含“重点更新、其他改进、升级说明、变更明细”四个约定外层小节。 |
| `excludes_internal_quality_evidence` | PASS | GitHub Release 正文未包含 skill eval、assertion 计数、review 轮次或 QA 汇总等内部审计证据；门禁信息位于正文之外。 |
| `preserves_confirmed_facts` | PASS | 正文保留了文件卡片、原位重试、统一附件模型、nullable JSONB 迁移与删列风险、部署顺序和开关、双架构资产、升级动作及旧浏览器限制。 |
| `title_matches_gate` | PASS | 标题为“v1.0.0 - 文件卡片、统一附件模型与失败消息重试”，不是裸版本号。 |
| `upgrade_note_fixed_structure` | PASS | “升级说明”包含备份、迁移与部署顺序、验证和开关、回滚风险及兼容性说明；未臆造 coding-agent 小节、安装命令或 plugin 更新事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79; output_sha256=c1735cb3ede0d2dbc2112be828fa26c2e72ac55e4d72e591edc77fa181e27346; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了符合四节结构、事实完整且不含内部审计内容的 GitHub Release 预览，并明确保持 preview-only。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79; output_sha256=2b6337999f7ea8a16ad8997d48681386c933c1b8f6cc0ccc6a2f764eb731306c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了可用但结构偏离要求的基线预览，使用了发布亮点、部署与兼容等非约定小节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
