# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-012-change-tier-hotfix-abuse-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-12-change-tier-hotfix-abuse-blocked`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0b60a8fdef1023247fb430f4647e03f742c09fbfdb17e32a3a03dc6059ae9e02`
- Skill overlay SHA-256: `7093347dda9d009dc74c5bd9b37b3d0d8b980466e82f7a4efbacd767a0e9fa19`
- Judge schema SHA-256: `05754bc7141a9de585a1127391112d0da97f3c7138eba96f4377a8a50be63d7c`
- Eval definition SHA-256: `757872d7dabcbeb5f63781cd39c51a0fbd55c644aaecd2a814401a4e784d4603`
- Metadata SHA-256: `5be95630fc657c3ddfcd1eee211fb45bdc7cc20a37cf20c50f58a72635d4712c`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reject_hotfix_abuse` | FAIL | with_skill 输出未提及或明确拒绝按 `hotfix` 处理。 |
| `expectation_change_standard` | FAIL | with_skill 输出描述了 7 天 → 30 天的 delta 和 change-impact analysis，但未说明这是 expectation change / 业务规则变化，也未要求按 `standard` 或更高处理。 |
| `block_or_return_pm` | PASS | with_skill 输出明确表示无法直接修改或合并，标记 `confirmation_required: 是`，并要求确认工作区/提供资料后再继续收敛范围。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4f4db92527a116feef9cc734daaa4b4ade8efbc7e64d46eacf15ce46aafc660b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 阻止了立即修改和合并，并要求确认范围所需的项目资料，但遗漏 hotfix 拒绝和 standard 流程要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fd21822d29f9f59daea200bd14c26fadf30442cbe2bd48489976827d9b597907; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=29bda40f171f51bf7c04a8fc4ea76d5fa877b2543f51fa590d586a6098edefb3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅因工作区为空而拒绝修改或合并，未处理 hotfix、standard 或 PM 范围确认要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确拒绝将请求按 hotfix 处理。
- with_skill 未说明该请求应按 standard 或更高流程处理。
- Next: 明确拒绝按 hotfix 处理。
- Next: 明确将该 expectation change / 业务规则变化按 standard 或更高流程处理。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
