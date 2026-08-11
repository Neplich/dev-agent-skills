# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `87ef764041bed9ee9555b42ac224112964f5f9e1229cf61ab18c2da424e966e8`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | 读取并解析 pre-tag authority 的 commit/tree，使用 git show 读取 committed audit/handoff，并将未提交的工作区副本识别为不能覆盖 authority。 |
| `validates_current_attempt_history` | PASS | 核对 committed audit/handoff 中 attempt 2、直接 superseded attempt 1 及同版本关系；识别 worktree 副本改写 authority 与结果，并保持 blocked。 |
| `rejects_complete_release_tree_drift` | PASS | 执行 authority 与 tag 的完整树差异检查，核对原始 name-status/patch 中新增 src/catalog/export-v2.py，并因 inventory 不一致保持 blocked。 |
| `offers_safe_maintainer_recovery` | PASS | 提供同版本修复和改用新版本两种选择，要求维护者确认/处理版本与 tag 边界，并在重新审计前补齐基础、handoff 和完整 pre/post-tag 审计。 |
| `persists_blocked_without_corrupting_authority` | PASS | 明确 blocked 结果未持久化、post-tag 结果文件不存在；说明恢复写入后先持久化并 readback，且只读期间未修改 authority、tag、ref 或产生成功状态。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=c665c50086693e3b71a9a85968a4ff14d8d62cc53d06f9a09c136fa5bf05eb9b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读 post-tag 审计，正确隔离 pre-tag authority 与漂移工作区副本，发现完整 tree/inventory 不一致并保持 blocked，同时给出恢复路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=c4af8bfdd24b1129d4c585d96a9375f39304baf135f044fb6ebb56523d0040cb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline 识别了主要版本与证据问题并保持未验证，但未完整核对 immutable authority、attempt lineage、完整审计契约及 blocked 持久化恢复条件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
