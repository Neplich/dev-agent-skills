---
title: "Feature Implementor 计划门禁历史实施计划"
type: IMPLEMENTATION_PLAN
feature: "feature-implementor-plan-gate"
version: "0.1.0"
status: Legacy
author: "Neplich Codex"
date: "2026-05-29"
last_updated: "2026-06-25"
legacy_of: "agents/engineer-agent/skills/feature-implementor"
legacy_reason: "Historical implementation plan superseded by feature-implementor PRD plan gate requirements"
superseded_by: "docs/pm/agents/engineer-agent/skills/feature-implementor/PRD.md"
---

# Feature Implementor 计划门禁实施计划

## 背景

GitHub issue #20 记录了 Engineer skills 中的一个流程缺口：小功能更新和轻量 bug 修复有时会绕过实施计划门禁。目标行为是先完成实施计划，再由用户确认，确认后才进入代码实施。

## 来源需求

- `feature-implementor` 在进入实施前先使用 implementation planner。
- 所有实现任务都需要产出或更新 `docs/engineer/{feature}/IMPLEMENTATION_PLAN.md`。
- 实施计划负责判断本次范围是否需要拆分 implementation / validation sub-agent。
- 小改动可以不拆 sub-agent，但不能跳过实施计划和用户确认。
- `debugger` 在确认 bug 根因后，先输出 bug 分析汇报，再询问用户是否产出修复实施计划。
- 修复实施计划写完后，需要用户确认，确认后才能应用修复。

## 文件变更清单

1. 修改 `agents/engineer/skills/feature-implementor/SKILL.md`
   - 解决 planner 加载和 implementation plan 确认之间的内部矛盾。
   - 将实施计划明确为所有功能实现任务的统一前置门禁。
   - 区分“不拆复杂 sub-agent”和“不写实施计划”两个概念。
   - 要求用户确认实施计划后，才允许加载 implementor 行为。

2. 修改 `agents/engineer/skills/feature-implementor/_internal/planner/INSTRUCTIONS.md`
   - 明确小改动也需要产出可持久化的实施计划。
   - 要求实施计划记录是否需要拆分 sub-agent 的判断。
   - 要求主流程在展示实施计划后停止，等待用户确认。

3. 修改 `agents/engineer/skills/feature-implementor/_internal/implementor/INSTRUCTIONS.md`
   - 要求输入必须包含用户已确认的实施计划。
   - 如果实施计划尚未展示或尚未确认，阻止进入实施。

4. 修改 `agents/engineer/skills/debugger/SKILL.md`
   - 在根因确认后增加门禁。
   - 要求先输出 bug 分析汇报，再进入修复计划判断。
   - 询问用户是否产出修复实施计划。
   - 要求修复实施计划确认后，才能应用修复。

5. 修改 `agents/engineer/test/feature-implementor/evals/evals.json`
   - 增加小改动 eval，覆盖实施计划产出、sub-agent 拆分判断、用户确认和不得直接实施。
   - 增加小 bug fix 进入 `feature-implementor` 的 eval，覆盖单文件修复仍需实施计划和用户确认。

6. 修改 `agents/engineer/test/debugger/evals/evals.json`
   - 更新现有 bug 修复 eval，覆盖 bug 分析汇报和修复实施计划门禁。

## 验证方式

- 运行 `uv run scripts/check_repository_contract.py`。
- 运行 `uv run scripts/check_eval_contract.py`。
- 运行 `uv run scripts/check_eval_artifacts.py`。
- 涉及 skill 或 eval 行为变更后，先询问是否运行受影响的模型 eval，用户确认后再执行。

## 实施顺序

1. 更新 `feature-implementor` 公开入口和内部 planning 指导。
2. 更新 `debugger` 根因分析后的修复计划门禁。
3. 更新 eval 定义，固定新的门禁行为。
4. 运行确定性仓库校验。
