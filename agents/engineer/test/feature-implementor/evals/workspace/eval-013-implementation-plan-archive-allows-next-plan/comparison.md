# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-013-implementation-plan-archive-allows-next-plan`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b1196f3cc740d50faa388fb3640408e1ae15382be34fb5cbb8ccf574f355b7b3` from `agents/engineer/test/feature-implementor/evals/workspace/eval-013-implementation-plan-archive-allows-next-plan`.
- Fixture SHA-256: `b1196f3cc740d50faa388fb3640408e1ae15382be34fb5cbb8ccf574f355b7b3`
- Prompt SHA-256: `3f34e8964229e17bf678fdb0295a0b4214512a8063221444dbb90bb2e6e03fb8`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `63eea1bc6726716aeec9d0c5f47bf4224063a1ac86fd4d675f7615f584d2a70d`
- Metadata SHA-256: `20785706c746be6895ed31fc2345f379cd37d1db1f0bd95d72fc9387f408aa95`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_prior_plan_archived` | PASS | with_skill 计划明确写明全额退款计划已归档，并通过 previous_plan_archive 回链归档路径；新计划处于等待确认阶段，无活跃计划阻塞。 |
| `allows_new_active_plan` | PASS | with_skill 创建了 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，并将部分退款作为新计划范围。 |
| `records_previous_plan_archive` | PASS | 交付快照显示 frontmatter 的 previous_plan_archive 指向 docs/engineer/payment-refund/implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md。 |
| `keeps_active_entry_fixed` | PASS | 新文件实际路径为 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md；git 状态未显示对归档目录的写入。 |
| `waits_for_user_confirmation` | PASS | 输出明确要求确认计划后再进入实现阶段；git 证据仅有新计划文件，未修改代码。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f34e8964229e17bf678fdb0295a0b4214512a8063221444dbb90bb2e6e03fb8; fixture_sha256=b1196f3cc740d50faa388fb3640408e1ae15382be34fb5cbb8ccf574f355b7b3; output_sha256=8f84e4df295c782a9711879935ba19284a1cd5ff595cea8d0df999800cc9cfa1; snapshot_sha256=26b2448e2fc592a00b176a1dcabf94b9392937052d738a58c27993161580ce30
- Behavior: 正确识别并回链已归档计划，创建固定活跃入口的新计划，且等待确认后再实现。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f34e8964229e17bf678fdb0295a0b4214512a8063221444dbb90bb2e6e03fb8; fixture_sha256=b1196f3cc740d50faa388fb3640408e1ae15382be34fb5cbb8ccf574f355b7b3; output_sha256=1d886d907a3c99bb49a35261837dd0ab29926ab11ecdfde09fa21754a99d9c3d; snapshot_sha256=cf3528bcb5c54ca87c8ab426baf8e806f9a3e8a42fc75bee6b39bc4a4db6f80c
- Behavior: 创建了新计划，但未体现归档引用或等待用户确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-013-implementation-plan-archive-allows-next-plan

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-013-implementation-plan-archive-allows-next-plan`
- Test case: implementation-plan-archive-allows-next-plan
- Workspace: `workspace/eval-013-implementation-plan-archive-allows-next-plan`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认，现在要新增部分退款能力。上一轮全额退款计划已归档到 docs/engineer/payment-refund/implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md，当前没有活跃计划。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_prior_plan_archived`: 归档文件存在且 frontmatter 为 status: "Archived"；计划正文和 transcript 明确记录该归档及当前无 active plan。
- PASS `allows_new_active_plan`: 已创建 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，范围为部分退款。
- PASS `records_previous_plan_archive`: 新计划 frontmatter 的 previous_plan_archive 精确指向归档文件。
- PASS `keeps_active_entry_fixed`: 新计划位于 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md，未写入 archive 目录。
- PASS `waits_for_user_confirmation`: 计划 status 为 Draft，final 明确要求确认后再实现；workspace 未出现源代码修改。

## With Skill Behavior

with_skill 创建了正确的 Draft 活跃计划，保留归档入口并设置 previous_plan_archive；所有 input/output manifest hash 校验通过。

## Without Skill Baseline

without_skill 也创建了活跃计划，但未记录 previous_plan_archive，且未明确等待确认；仅作对照。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-013-implementation-plan-archive-allows-next-plan

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-013-implementation-plan-archive-allows-next-plan`
- Test case: implementation-plan-archive-allows-next-plan
- Workspace: `workspace/eval-013-implementation-plan-archive-allows-next-plan`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and `docs/engineer/payment-refund/implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md`.
- Fixture summary: the prior full-refund plan is archived with `status: "Archived"`, `implementation_scope: full-refund-flow`, `archived_at`, `archive_approved_by`, and `source_plan`; no active `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` exists.
- Expected output: allow a new active plan for partial refunds, require `previous_plan_archive`, keep the active entry fixed, and wait for confirmation before coding.

## Assertions

- PASS `detects_prior_plan_archived`: the skill recognizes the archived prior plan and no active-plan blocker.
- PASS `allows_new_active_plan`: planning may create a new `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` for the partial-refund scope.
- PASS `records_previous_plan_archive`: the new plan frontmatter must point `previous_plan_archive` to the archived full-refund plan.
- PASS `keeps_active_entry_fixed`: the new active plan path remains `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`, not an archive path.
- PASS `waits_for_user_confirmation`: coding waits until the new active plan is confirmed.

## With Skill Behavior

Fresh with-skill validation confirmed the archived-plan positive path. The current skill should scan the active plan path and archive directory, find no active plan, identify the archived full-refund plan as valid historical context, and proceed to write a new active plan for partial refunds. The plan must record `previous_plan_archive: docs/engineer/payment-refund/implementation-plans/archive/IMPLEMENTATION_PLAN-full-refund-flow.md`, keep the live entry at `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`, and wait for user confirmation before implementation.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic planner would likely allow a new plan because the prompt says no active plan exists, but it would not reliably require exact `previous_plan_archive` linkage metadata, validate that the archive is on the same feature path, or explicitly forbid writing the new plan inside the archive directory.

## Failures

- None.

## Next Steps

- Keep this eval focused on allowing a new active plan only after proper archival and linkage metadata.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
