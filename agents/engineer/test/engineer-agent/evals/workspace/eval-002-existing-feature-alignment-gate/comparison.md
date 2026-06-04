# Eval Result: eval-002-existing-feature-alignment-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-002-existing-feature-alignment-gate`
- Test case: existing-feature-alignment-gate
- Workspace: `workspace/eval-002-existing-feature-alignment-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-04 against the current uncommitted `engineer-agent` skill

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that engineer-agent checks PRD/TRD and any present product decisions before routing small existing-feature behavior changes into implementation.
- Expected output: 先要求读取 docs/pm/{feature}/PRD.md、docs/engineer/{feature}/TRD.md，以及存在的 DECISIONS.md 或产品决策记录，对比 archived 行为是否改变既有预期；如果是改变预期，路由回 pm-agent:idea-to-spec 的 existing-project-update，而不是直接进入 feature-implementor。

## Assertions

- `reads_product_and_engineer_docs`: 先读预期行为文档
- `classifies_expectation_change`: 识别需求预期变更
- `routes_to_existing_project_update`: 回到 PM 更新路径
- `routes_trd_gap_to_trd_gen`: TRD gap 交回 trd-gen
- `requires_plan_after_alignment`: 对齐后仍需实施计划
- `does_not_route_directly_to_implementation`: 不得直接进入实现

## With Skill

Observed behavior:

- PASS - fresh Codex subagent validation on 2026-06-04 confirmed current
  `engineer-agent` enforces the existing-feature PRD/TRD alignment gate before
  implementation or debugging, routes expectation changes to PM, routes TRD
  gaps to `trd-gen`, requires a confirmed implementation plan after alignment,
  and treats user requests to skip PRD alignment as blocker/risk rather than a
  valid continue reason.
- 当前 SKILL.md 明确 Existing Feature Alignment Gate：现有功能行为变更、小改动或 bug fix 进入 `feature-implementor` 或 `debugger` 前，必须先识别相关 feature，并读取 `docs/pm/{feature}/PRD.md`、`docs/engineer/{feature}/TRD.md`，以及存在的 `docs/pm/{feature}/DECISIONS.md` 或其他产品决策记录。
- 对 archived 通知显示到 active 列表这类请求，当前 SKILL.md 不把“小改动”默认视为可直接实现，而是先分类：如果是在改变已批准预期，路由回 `pm-agent:idea-to-spec` 的 `existing-project-update` 路径更新 PRD 或产品决策记录。
- 如果 PRD 或产品决策稳定但 TRD 缺失、过期、不完整或与请求/代码冲突，当前 SKILL.md 要求构造 TRD gap packet，并交给 `engineer-agent:trd-gen` 补完整 TRD。
- 只有在 PRD/TRD 对齐后才能进入 `feature-implementor`；进入后仍由 `feature-implementor` 基于确认 TRD 写入 `docs/engineer/{feature}/IMPLEMENTATION_PLAN.md`，并等待实现确认后再编码。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found.

## Next Steps

- 保持该 eval 覆盖现有功能变更的 PRD/TRD 对齐门禁。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
