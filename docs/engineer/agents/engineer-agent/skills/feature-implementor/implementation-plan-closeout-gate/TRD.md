---
title: "IMPLEMENTATION_PLAN 收尾门禁 TRD"
type: TRD
version: "0.1.0"
status: Draft
author: "Neplich Codex"
date: "2026-06-24"
last_updated: "2026-06-25"
generated_by: "trd-gen"
feature: "implementation-plan-closeout-gate"
feature_path: "agents/engineer-agent/skills/feature-implementor/implementation-plan-closeout-gate"
parent_feature: "agents/engineer-agent/skills/feature-implementor"
feature_level: "5"
related_prd: "docs/pm/agents/engineer-agent/skills/feature-implementor/implementation-plan-closeout-gate/PRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/44"
---

# IMPLEMENTATION_PLAN 收尾门禁 TRD

## 1. 技术目标

为 `feature-implementor` 增加实施完成后的 closeout gate，确保
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` 的 frontmatter、正文状态、
实施结果和验证证据保持一致。

## 2. 影响范围

| Area | File | Change |
| --- | --- | --- |
| Public skill contract | `agents/engineer/skills/feature-implementor/SKILL.md` | 在 Phase 3 后、QA E2E handoff 前增加 closeout gate。 |
| Implementor module | `agents/engineer/skills/feature-implementor/_internal/implementor/INSTRUCTIONS.md` | 要求实现阶段收集 closeout evidence。 |
| Reviewer module | `agents/engineer/skills/feature-implementor/_internal/reviewer/INSTRUCTIONS.md` | 增加 stale implementation plan state 检查。 |
| Output conventions | `agents/engineer/skills/feature-implementor/_internal/_shared/output-conventions.md` | 增加 `IMPLEMENTATION_PLAN.md` 收尾写法。 |
| Eval contract | `agents/engineer/test/feature-implementor/evals/evals.json` | 新增回归 eval。 |
| Eval fixture | `agents/engineer/test/feature-implementor/evals/workspace/eval-010-implementation-plan-closeout-sync/` | 提供矛盾计划 fixture 和 durable `comparison.md`。 |
| Skill lock | `skills-lock.json` | 刷新受影响 skill hash。 |

## 3. Closeout Gate 设计

`feature-implementor` 完成实现、自检和验证后，需要读取本次确认过的
`IMPLEMENTATION_PLAN.md`，并检查以下内容：

| Check | Required Behavior |
| --- | --- |
| Frontmatter status | 如果实现完成，`status` 可更新为 `Implemented` 或仓库采用的等价完成态。 |
| Gate/status table | 计划正文中的门禁表必须与完成态一致，不得保留“待确认 / 未开始 / 未执行”。 |
| Implementation result | 记录已完成的文件或文档变更摘要。 |
| Deterministic checks | 记录实际命令和结果；未执行则写 skipped / blocked 原因。 |
| Skill eval evidence | 实际执行 eval 或 fresh subagent validation 后引用 durable `comparison.md`。 |
| Runtime artifact policy | 不提交 transcript、diagnostics、outputs、timing 或 run status。 |

## 4. Reviewer 检查

reviewer 需要在输出 pass 之前执行 stale-state 检查：

- `status: Implemented` 时，正文不得残留“待确认”“未开始”“待执行”“未执行”“模型 eval 尚未执行”等与完成态冲突的描述。
- 如果正文声明 eval 已完成，必须列出对应 durable `comparison.md`。
- 如果正文声明 deterministic checks 已完成，必须列出实际命令。
- 如果 eval 或检查未执行，必须说明 skipped 或 blocked 原因。

发现冲突时，reviewer 返回 blocking finding，并回到 closeout 更新步骤。

## 5. Eval 设计

新增 `eval-010-implementation-plan-closeout-sync`：

| Field | Value |
| --- | --- |
| Workspace | `workspace/eval-010-implementation-plan-closeout-sync` |
| Scenario | fixture 中已有一个 `status: Implemented` 但正文仍写“待确认 / 未开始 / 未执行”的 `IMPLEMENTATION_PLAN.md`。 |
| Expected Output | skill 必须发现 stale closeout 状态，要求同步结果和验证证据，不得直接 handoff 或 delivery。 |

核心断言：

- 检测 frontmatter 与正文状态冲突。
- 要求更新实施结果区和状态表。
- 要求记录 deterministic checks 的命令和结果。
- 要求 eval 已执行时引用 durable `comparison.md`，未执行时写明原因。
- 不提交运行期 eval 产物。

## 6. 验证策略

```bash
git diff --check
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run --with pytest pytest agents/test_eval_contract.py
```

如果实际执行 feature-implementor eval 或 fresh Codex subagent validation，需要在同一轮变更中更新对应 durable `comparison.md`。

## 7. 回滚

标准 git revert 可回滚 skill 文档、internal instructions、eval fixture、durable comparison 和 `skills-lock.json` 变更。回滚后现有实施前计划门禁仍保持不变。
