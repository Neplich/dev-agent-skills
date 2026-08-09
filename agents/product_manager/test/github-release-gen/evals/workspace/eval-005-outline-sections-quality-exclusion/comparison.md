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
- Fixture SHA-256: `f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `f3cdc20a6c2d6d35b8761172794fe96e07166b0922a8d802a01f520259d39177`
- Eval definition SHA-256: `5768440d836f6d58f2492f6254c4eaae18fe913a310437aaee98134c39857a50`
- Metadata SHA-256: `a9879c47e38cec76a35a3ff0087c5b764086d8e7ca04745f8977bbd30db8f459`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `follows_outline_sections` | PASS | 正文仅包含「重点更新」「其他改进」「升级说明」「变更明细」四个二级小节。 |
| `excludes_internal_quality_evidence` | PASS | 正文未包含 skill eval、assertion 计数、QA、review 或其他内部审计证据。 |
| `preserves_confirmed_facts` | PASS | 正文保留了文件卡片、原位重试、统一附件模型、迁移与删列风险、部署顺序与开关、双架构资产、升级动作及旧浏览器限制。 |
| `title_matches_gate` | PASS | 预览标题为「v1.0.0 - 文件卡片、附件模型与失败消息重试」，不是裸版本号。 |
| `upgrade_note_fixed_structure` | PASS | 「升级说明」包含完整升级步骤、兼容性说明和回滚风险；未臆造 coding-agent 小节、命令或 plugin 更新事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79; output_sha256=1b43a4e11b3cad8cce77a29d378a90daeed0d99602453587215a7d3462ff69ab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了符合四节结构、事实完整且不含内部审计内容的 GitHub Release 预览，并正确声明尚未创建或发布。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79; output_sha256=70e1a9738308c84da2ca21c5e554fefc70d2aeca6db7b6b979f199352ed4d9b8; snapshot_sha256=405a3724dd600e396cb40027eca6f62dd84f4f3d2f18d37f59caf48cbbaa8187
- Behavior: 生成了包含发布亮点、部署与兼容、质量验证、维护者说明等约定外小节及内部质量证据的预览。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
