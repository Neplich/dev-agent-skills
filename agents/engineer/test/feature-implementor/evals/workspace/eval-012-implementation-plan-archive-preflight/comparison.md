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
- Identity schema: `2`
- target_skill_sha256: `7f71c78ab97a67d477751886a8f46d8cfd865bac113be49568de86ccf5343ee9`
- eval_definition_sha256: `7f61bff44513e544647aa068492b4fc39b7ba0f0b8a502c36472dbc74575e45e`
- metadata_sha256: `d61de6289d375a4f846be423a72cc4b82b03d964cc2e5dac6f44d3f3c1fe9492`
- fixture_sha256: `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `097d311377d0abb4f2fcb1bfa46de1df83e6feccaa7b6f38bb1fb185a5118ab5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6ba93c2da62bbbed9ea41d72d153901f8e8bbbbad20322168e3cf7c265e800fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `runs_pre_plan_archive_scan` | PASS | with_skill 的锁定 trace 显示先读取活跃计划并检查归档目录状态，之后才执行后续操作；输出也列出两者路径及归档状态。 |
| `blocks_direct_overwrite` | PASS | with_skill 输出明确将决策标记为 blocked_pending_archive_choice，并要求确认；trace 中未发生新计划写入或代码变更。 |
| `offers_implemented_handling_options` | PASS | 输出要求用户在归档后新建与以 Superseded 归档并记录原因后新建两项中选择，未提供继续更新 Implemented 计划的选项。 |
| `keeps_active_entry_fixed` | PASS | 输出明确固定 active_plan_path 为 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，并规定归档目录为 archive/。 |
| `does_not_implement_directly` | PASS | with_skill 输出停留在计划确认前，明确后续实现待确认，未声称修改代码、运行实现或完成验证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=25427d686f42e683c2d75f477da0c181b33c6a56f8e1f228079cfc3cf471376d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成前置扫描与状态判断，阻止未经确认的计划写入，并提供两种合规归档处理选项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=52834bba7edf10e9e8522190b7ab41c83d7187d13c0293647b905654fe1f5c00; snapshot_sha256=3997b14c0bdd8c8bb2d05b509f3a31fc5f15519f901f2feea029530a8bd720eb
- Behavior: 基线直接归档并覆盖活跃计划，未等待用户选择。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
