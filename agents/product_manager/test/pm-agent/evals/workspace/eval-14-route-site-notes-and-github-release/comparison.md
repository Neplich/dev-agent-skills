# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0b60a8fdef1023247fb430f4647e03f742c09fbfdb17e32a3a03dc6059ae9e02`
- Skill overlay SHA-256: `7093347dda9d009dc74c5bd9b37b3d0d8b980466e82f7a4efbacd767a0e9fa19`
- Judge schema SHA-256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | with_skill 明确将站内版本说明 owner 指向 docs-agent:release-notes-gen，并说明先完成 Docs 阶段。 |
| `routes_github_release_to_pm_specialist` | PASS | with_skill 将下游 GitHub Release owner 指向 pm-agent:github-release-gen，并拒绝由 Docs 阶段执行下游预览。 |
| `preserves_release_sequence` | NOT_EXERCISED | 输出声明 site-first 顺序，但因缺少版本来源、交接证据且 specialist 不可用，尚未实际完成确认、Docs gates 或 PM 消费步骤。 |
| `does_not_use_old_pm_skill_name` | PASS | PM owner 使用 github-release-gen；release-notes-gen 仅用于 docs-agent，未将其作为 PM owner。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4b41c94cdb1530584bf8a4a4516ac766782734e1316f290fb3be6fd04cf5f48b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 Docs → PM 的路由和 site-first 边界；因输入与运行证据不足而安全阻塞，未创建文件或发布内容。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b6a2d85d61a704cefe02b05941740410ad9481a21b341e96ceac8415a69bf4e6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告仓库缺少发布事实依据，未体现专 specialist 路由或顺序控制。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供 v1.0.0 变更来源并启用所需 specialist 后，完成 Docs 确认与 gates，再生成 PM GitHub Release 预览。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
