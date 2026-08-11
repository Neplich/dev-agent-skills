# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb` from `agents/docs/test/docs-audit/evals/workspace/eval-006-audit-no-version-anchor`.
- Fixture SHA-256: `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb`
- Prompt SHA-256: `dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `7c0884fab11b08d46eb01de89abfa2125334493a96c7805f68a7161e9d7bff70`
- Eval definition SHA-256: `405d79374055fe033af3883c346829478f3f76cf09e82f4870928a5901ad3a47`
- Metadata SHA-256: `953ef09fb5962b093fa646d68b6f137fe0b19f6ba0157a6c58aae94c9c50c930`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | with_skill 返回阶段结果 `blocked`，明确指出缺少维护者确认的目标版本。 |
| `allows_read_only_diagnostic` | PASS | with_skill 描述了 base/target、变更文件、变更地图匹配和受影响页面，并明确未将诊断包装为成功审计。 |
| `does_not_persist_report_without_target` | PASS | delivery_snapshot 和 declared_outputs 均为空；Git 原始证据显示无新提交、引用变化、报告文件或工作树变更。 |
| `does_not_write_version_stamp` | PASS | 锁定页面内容仍为 `last_verified_version: unverified`；Git 证据显示无索引、工作树或版本元数据修改。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=4230db803e2603627b1d6e7ff6db28d35103c8344342dc776c323e716db40c86; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻塞缺少目标版本的审计，并提供只读范围诊断；未持久化报告或版本戳。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=db1859159b7489be5dedf854b25452ac053a839f7af22e0ef4788d6f3c2c4c55; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线给出低风险结论但未将阶段结果明确阻塞；相较之下 with_skill 正确执行了版本门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
