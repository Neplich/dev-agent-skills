# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | with_skill 将目标识别为独立的 release-notes-gen 站内发布说明工作流，并明确不属于当前 Product 或 Ops 页面同步。 |
| `routes_complete_entry_to_site_owner` | PASS | with_skill 的交接记录包含 release-request、v1.5.0、dashboard 10→25、目标站点页面、已接受/缺失证据及站内范围，并指向负责发布说明生成与确认的 release-notes-gen。 |
| `keeps_entire_site_zero_diff` | PASS | with_skill 输出明确报告工作区零改动；git_status、git_diff 和 delivery_snapshot 均为空，docs/site 未发生写入。 |
| `preserves_external_release_boundary` | PASS | with_skill 未执行或声称执行 tag、GitHub Release 或外部发布授权；git_evidence 也显示无 ref、commit 或 reflog 变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=ee4c0704be1c0ebf38c4a861ced257d5b4ef55a2047a1e46334fbf34236d4037; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为站内发布说明交接，在证据门禁未通过时保持 docs/site 零写入，并保留站内范围与外部发布边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=9639a315ce49ce35064dd18af0d0405ef3f7dceeba83de48af8b517cc880266d; snapshot_sha256=bc547f43aa4a886d2f90ca2b86c496a089952da937a27c23de80df0e7551f995
- Behavior: 直接修改发布页面、版本列表和发布元数据，完成了用户可见产物但绕过了交接门禁与零写入要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
