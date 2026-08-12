# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Identity schema: `2`
- target_skill_sha256: `c8459f189e8d92d91e1c7ede8875090bfc1c2e1e04b8f18983b4339e6b65ba34`
- eval_definition_sha256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- metadata_sha256: `79c5171e280a55a386cc65ee64ce2254d37bdb1b11edec578be748642efe98aa`
- fixture_sha256: `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b3d43ca97793c6a0f8faf70ea92518e7709890635e7a921da0c1ddde071762ab`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | with_skill 输出识别缺少 docs/site/release-notes 基础及 Release Notes 规则/索引，并说明不能自行初始化；trace 也确认目录与 .meta/releases.json 不存在。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | with_skill 输出声明未创建页面、未修改 metadata/index/navigation；git_evidence 显示 HEAD、分支、索引、工作树及未跟踪文件均无变化。 |
| `hands_missing_foundation_to_bootstrap` | PASS | with_skill 输出明确 blocked -> docs-site-bootstrap，携带当前仓库主机和缺失 foundation，并保留后续 docs-audit 与下游职责。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | with_skill 输出明确未创建 GitHub Release 或 v1.0.0 tag，trace 显示无 tag、无 remote 且 git 状态未变；同时要求 foundation 授权后重新进入 Release Notes 流程，并等待 docs-audit 的 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=33b807b33c1715903514aa1b08ad1ae8d60441c8742c1a482b004406f8f50895; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别站点基础缺失，停止写入并将工作交接给 docs-site-bootstrap；保持 Git 与外部发布链零写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=2c0b0cc7da37bb2825f403b1b1e0d454652b5611269b0fc1d0e410566ee9fc5f; snapshot_sha256=d474ff97e963863cf7bf17e2d72219d019f2f587d0bf49bcd09f273d7534f792
- Behavior: 基线错误地生成站内页面和元数据、创建本地 tag，并准备 GitHub Release 草稿。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
