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
- Fixture SHA-256: `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `b3d43ca97793c6a0f8faf70ea92518e7709890635e7a921da0c1ddde071762ab`
- Eval definition SHA-256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- Metadata SHA-256: `79c5171e280a55a386cc65ee64ce2254d37bdb1b11edec578be748642efe98aa`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | with_skill 明确识别缺少 docs/site/release-notes/ Release Notes 基础，并将页面状态置为 blocked，未进入页面生成流程。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | with_skill 的 git_evidence 显示 HEAD、分支、refs、工作树和索引均无变化；git_status 与 git_diff 均为空。 |
| `hands_missing_foundation_to_bootstrap` | PASS | 输出将缺失基础交给 docs-site-bootstrap 初始化，未交给 docs audit、GitHub Release owner，也未自行继续。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | 输出明确 tag 与 GitHub Release 均未创建，并等待 docs-audit 返回 ready_for_tag；git_evidence 的 ref_delta、result_diffs 和状态均为空。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=c795bdddf39289886240bbe1cce87106225985318f6d9fbe574aae93d646e2a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 Release Notes 基础缺失，阻塞生成并完成正确的 bootstrap handoff；保持站内、Git 和外部发布链零写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=bbf8e599adb4e0da8586193d4ccc1f44d8a0693ccc569f6962ee0981f1b09ec1; snapshot_sha256=39b391f82c97b7045b03f4e7cd72f06c05a987b788fdb40e776adb0c7dcbb3a5
- Behavior: 错误地创建站内 Release Notes、元数据和提交，并创建 v1.0.0 tag；仅未创建 GitHub Release。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
