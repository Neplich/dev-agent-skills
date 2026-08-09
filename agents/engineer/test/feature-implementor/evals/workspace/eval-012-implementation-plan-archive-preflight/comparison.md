# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e` from `agents/engineer/test/feature-implementor/evals/workspace/eval-012-implementation-plan-archive-preflight`.
- Fixture SHA-256: `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e`
- Prompt SHA-256: `9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e820a1098a32d64fe76bdf4ec719cd859ebecfdb70fa28be1309b656ec71bd22`
- Skill overlay SHA-256: `226a387f9ef93d9f4c106e1f240f22e5014d390eeb37da0fd61da0c129ca36ba`
- Judge schema SHA-256: `097d311377d0abb4f2fcb1bfa46de1df83e6feccaa7b6f38bb1fb185a5118ab5`
- Eval definition SHA-256: `3628876acf1d52ad92b5faf79f556bf7cb6aca5a88b0bd15975a544759685f18`
- Metadata SHA-256: `158f5bafaa3ad4ac6ba561642292db5794c29432044a423049518391aa4f0dbd`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `runs_pre_plan_archive_scan` | NOT_EXERCISED | 锁定证据无法证明写新计划前的实际扫描顺序；输出仅列出活跃计划和归档目录状态。 |
| `blocks_direct_overwrite` | PASS | with_skill 的 git 状态、diff 和 delivery_snapshot 均显示未修改文件，并明确下游行动在计划确认前被禁止。 |
| `offers_implemented_handling_options` | PASS | 输出要求用户在归档后新建与归档为 Superseded 并记录原因后新建之间选择，未提供继续更新 Implemented 计划的选项。 |
| `keeps_active_entry_fixed` | PASS | 输出明确列出活跃入口 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，并将归档目录限定为 implementation-plans/archive/。 |
| `does_not_implement_directly` | PASS | with_skill 无工作区变更、无交付快照，且输出将实现、测试及交付行动列为确认前禁止事项。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=6630d8c775bdb8f50b89aa06ac2a3a2f23346ec05846bf21fb9f37ef34aae4ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到现有完成态计划并暂停后续工作，要求用户先选择归档处理方式；没有直接修改或实施。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=d16d3a34f847be82f4a018671ce7d534a75f6da2d308545c705971a7613e2bb8; snapshot_sha256=2b2056c82b850dd7175361ba3e866adea7fe7eef232def31f6fab06e03ad4b7f
- Behavior: 直接修改活跃计划并创建归档文件，未先请求处理方式选择。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 确认归档前置扫描的实际执行顺序后再评估 runs_pre_plan_archive_scan。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
