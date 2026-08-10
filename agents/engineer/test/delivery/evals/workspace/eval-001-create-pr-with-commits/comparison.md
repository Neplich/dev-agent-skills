# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `80143710c96793bf7a6f9a4804a3d60ffaac7dece4a2f7557d0f1f0713ea31bd`
- Skill overlay SHA-256: `c8b7fb40dd202ef7d4a2346a2ebf1af166a6cf34ac5e5f640ac543c8febcfa5e`
- Judge schema SHA-256: `eaac8d5ec4179daca7a6c1c98e4847ae0114d9d33168a84593f70ca6474abe10`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | with_skill 的 git_evidence 显示分支从 main 创建为 fix/archived-notification-status，且分支 ref 已建立。 |
| `meaningful_commit_created` | NOT_EXERCISED | 提交命令因缺少 user.name 和 user.email 失败；git_evidence 显示没有新提交。 |
| `pr` | PASS | 未配置 remote，候选明确未创建 PR，并提供了包含标题、Issue 关联、PM 文档引用和测试状态的 PR 预览。 |
| `ci` | NOT_EXERCISED | 没有实际 PR，因此未读取 CI；候选明确标示 PR/CI 未创建且 CI unavailable。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=5a72d189c9ff66c679dd3f23dd75cd3d1a26eac6f84fcfb75f244b0c66198594; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 创建了规范功能分支，测试通过；提交因缺少 Git 身份阻塞，并提供了真实的 PR 预览及未运行 CI 状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=ccd1b439378719865b4b136a0fa2d54e72170f16af015714a368f55f3bc518df; snapshot_sha256=faa598f9304cb339bcac6b3a1076ee43f6a2d2da3ee341546dca68483c9ab6d1
- Behavior: 创建分支并完成提交，但无法创建 PR；作为新鲜基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 配置 Git user.name 和 user.email 后完成提交；获得 remote/gh 后创建 PR，再读取 CI。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
