# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-007-direct-downstream-without-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-7-direct-downstream-without-handoff`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0b60a8fdef1023247fb430f4647e03f742c09fbfdb17e32a3a03dc6059ae9e02`
- Skill overlay SHA-256: `7093347dda9d009dc74c5bd9b37b3d0d8b980466e82f7a4efbacd767a0e9fa19`
- Judge schema SHA-256: `7c8f04de1d3d5d7be3420b0f2beb357c1f51529b632197ee0b99337d048e9452`
- Eval definition SHA-256: `b986e7826ca166d1da0b8e0017bd8206728589a4fd4770b206226ac2a418b2fb`
- Metadata SHA-256: `70b36659756bbd4d7fc0e09d0fabc7ee5ba1a168323c148fa735110fb59ec768`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reject_direct_downstream` | FAIL | with_skill 明确表示“暂时无法直接改代码”，但未明确提及不能进入 `engineer-agent` 或其他 downstream execution。 |
| `return_to_pm_agent` | FAIL | with_skill 输出为 `idea-to-spec` checkpoint，仅要求确认布局，未返回 `pm-agent` 进行 request_type、scope、feature_path 和 handoff readiness 分类。 |
| `require_handoff_or_docs` | NOT_EXERCISED | 当前停在等待用户确认布局的交互步骤，尚未进入 role router；因此后续 handoff/docs 要求尚未可执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=87d13323a745352fe81d2772b00b03e84cfb9c42a2d315b9356888d2957c6576; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未修改代码并请求用户先确认目标布局，但未完成 PM 入口分类及明确的 downstream 拒绝说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=55c8db98e3fd7a1bbdf437412a3e4a499ce6a6b1ffb11d69a1cc81cc1ec95fdf; snapshot_sha256=c57b3fcbece46054cba8da1a95853e856e8498d4ff14594b315f4d06d4fc7a42
- Behavior: 直接实现设置页并创建 index.html、styles.css、script.js，作为 fresh baseline 对比。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确拒绝进入 `engineer-agent` 或其他 downstream execution。
- with_skill 未将请求返回 `pm-agent` 分类。
- Next: 确认目标布局后，再验证 handoff packet 或等价 PRD/TRD/design/test/deployment/security 文档要求。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
