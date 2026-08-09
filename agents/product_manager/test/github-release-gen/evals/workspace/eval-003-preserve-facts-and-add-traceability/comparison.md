# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Fixture SHA-256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `13218ab4a7abff52fb220f782ffa27173bde4d7c9a5b1ae26ef3115112e26b3d`
- Eval definition SHA-256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- Metadata SHA-256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | FAIL | with_skill 保留了文件卡片、失败消息重试、统一附件模型、nullable JSONB 迁移风险、部署顺序与开关、双架构资产、升级说明和旧浏览器限制，但正文新增了证据未确认的发布日期“2026-08-09”。 |
| `adds_verified_traceability_links` | FAIL | with_skill 使用了代表性 PR、commit 和最终 compare 链接，但未提供 github-evidence.md 中的贡献者链接。 |
| `curates_instead_of_dumping` | PASS | with_skill 围绕版本事实组织说明，仅列出代表性 PR/commit，并明确未粘贴 18 个维护 commit feed。 |
| `blocks_on_fact_conflict` | NOT_EXERCISED | 锁定证据未包含 GitHub 与站内事实的冲突，因此该阻塞分支未被实际触发，无法证明其是否会返回 docs-agent:release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=4b2899973f574f8ae6d359a2ee4b152511a14d01a917a147aa63b4901f9c5659; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了不执行 GitHub 写入的 Release 预览，并正确等待 tag 与发布确认；但预览含未经证实的日期且缺少贡献者链接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=29d0179f8a9c62a86efe8306a371440a38587056aa581a19151ed62c7117eac8; snapshot_sha256=1ea865ec9c72220b04727c251c9040170fb92274b4f400bf8fef43b4ef335f15
- Behavior: 生成了文件型 Release 预览，覆盖主要事实并包含贡献者链接，但 compare 链接出现旧目标提交与最终 tag 的不一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 新增了未由锁定证据确认的发布日期。
- with_skill 缺少贡献者链接。
- Next: 移除未经证据确认的发布日期。
- Next: 为代表性 PR/commit 补充对应贡献者链接。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
