---
title: "实施计划预期改动声明与收尾对账实施计划"
type: IMPLEMENTATION_PLAN
version: "0.1.0"
status: Draft
author: "Neplich Codex"
date: "2026-08-20"
last_updated: "2026-08-20"
generated_by: "feature-implementor"
feature: "plan-expectation-reconciliation"
feature_path: "agents/engineer-agent/skills/feature-implementor/plan-expectation-reconciliation"
parent_feature: "agents/engineer-agent/skills/feature-implementor"
feature_level: "5"
implementation_scope: "plan-expectation-reconciliation"
change_tier: "major"
related_prd: "docs/pm/agents/engineer-agent/skills/feature-implementor/plan-expectation-reconciliation/PRD.md"
related_trd: "docs/engineer/agents/engineer-agent/skills/feature-implementor/plan-expectation-reconciliation/TRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/315"
---

# 实施计划预期改动声明与收尾对账实施计划

## 1. 实施上下文

本计划承接 issue #315 及同功能路径下已批准的 PRD、TRD。目标是在
`feature-implementor` 的计划、实施证据、closeout 和 reviewer 之间建立同一组
预期与实际对账字段，并为实质偏离补充 ADR frontmatter。

### 1.1 门禁状态

| Gate | Status | Evidence |
| --- | --- | --- |
| PRD alignment | 已批准 | `docs/pm/agents/engineer-agent/skills/feature-implementor/plan-expectation-reconciliation/PRD.md` |
| TRD alignment | 已批准 | `docs/engineer/agents/engineer-agent/skills/feature-implementor/plan-expectation-reconciliation/TRD.md` |
| Feature path | 已对齐 | PRD、TRD 与本计划使用相同 `feature_path`、`parent_feature`、`feature_level`。 |
| Implementation plan | 已批准 | 维护者已批准 issue #315 实施范围。 |

### 1.2 成功标准

- 计划 checkpoint 和模板均包含六字段预期改动声明。
- implementor 采集对应实际值，closeout 逐项对账。
- 偏离按统一字段、枚举和默认拆分规则记录。
- reviewer 阻断未经解释的偏离。
- 偏离驱动 ADR 与普通 ADR 的 frontmatter 要求清晰分离。
- hotfix 保持轻量形态，声明不成为硬性上限。

## 2. 预期改动声明

| Field | Expected |
| --- | --- |
| `expected_files` | 10 个 tracked 文件：下列 6 个契约源文件、3 个过程文档、`skills-lock.json`。 |
| `expected_new_dependencies` | `0` |
| `expected_new_config` | `0` |
| `expected_new_abstractions` | `0` |
| `expected_loc_magnitude` | Skill 契约源文件净增约 150–220 行；本功能过程文档新增约 400–500 行；lock 仅机械更新 hash。 |
| `expected_tests_vs_acceptance` | 新增测试 `0`；8 个 PRD 验收点由四项静态检查与逐文件审查覆盖。 |

该声明是 closeout 问询基线，不是文件数或行数的准入上限。若实际值偏离，
必须解释并按 TRD 的偏离格式处置。

## 3. 精确文件范围

### 3.1 契约源文件

| Path | Operation | Planned Change |
| --- | --- | --- |
| `agents/engineer/skills/feature-implementor/SKILL.md` | Modify | 补计划声明、checkpoint 渲染字段、reconcile 与 closeout 对账。 |
| `agents/engineer/skills/feature-implementor/_internal/planner/INSTRUCTIONS.md` | Modify | 增加六字段模板、默认值和 hotfix 简化说明。 |
| `agents/engineer/skills/feature-implementor/_internal/_shared/output-conventions.md` | Modify | 增加逐项对账、偏离格式、默认拆分和 ADR 边界。 |
| `agents/engineer/skills/feature-implementor/_internal/reviewer/INSTRUCTIONS.md` | Modify | 增加对账与偏离完整性检查。 |
| `agents/engineer/skills/feature-implementor/_internal/implementor/INSTRUCTIONS.md` | Modify | 增加 closeout 实际值采集。 |
| `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/adr-schema.md` | Modify | 增加偏离驱动 ADR 的可选 frontmatter。 |

### 3.2 过程文档与派生状态

| Path | Operation | Planned Change |
| --- | --- | --- |
| `docs/pm/agents/engineer-agent/skills/feature-implementor/plan-expectation-reconciliation/PRD.md` | Create | 固化 issue #315 的产品需求与验收标准。 |
| `docs/engineer/agents/engineer-agent/skills/feature-implementor/plan-expectation-reconciliation/TRD.md` | Create | 固化字段模型、对账流程与 ADR 规则。 |
| `docs/engineer/agents/engineer-agent/skills/feature-implementor/plan-expectation-reconciliation/IMPLEMENTATION_PLAN.md` | Create | 固化已批准范围、预期声明和验证步骤。 |
| `skills-lock.json` | Modify | 刷新受影响 local Skill 条目的 `computedHash`。 |

## 4. 禁止区域

- 不创建或修改 `docs/engineer/ADR-INDEX.md`。
- 不修改 `.claude-plugin/marketplace.json`、任何 `plugin.json` 或 router `SKILL.md`。
- 不修改测试、eval、README、AGENTS、cookbook 或脚本。
- 不创建额外依赖、配置、抽象层、重试、缓存、开关、钩子、监控或日志层。
- 不修改 hotfix 的轻量计划形态，不取消计划确认。

## 5. 实施步骤

### Step 1：更新计划契约

修改 public `SKILL.md` 和 planner instructions：

- 在 Mandatory Planning Checkpoint 加入六字段声明要求。
- 在 checkpoint 渲染字段清单列出声明字段名。
- 在计划模板的“预估文件数”附近写入字段、常见预期值和 hotfix 说明。

验证：六字段拼写与 PRD、TRD 完全一致，声明被描述为问询基线。

### Step 2：更新实际值采集与 closeout

修改 implementor、output conventions 和 public `SKILL.md`：

- 采集文件、依赖、配置、抽象层、行数和测试覆盖实际值。
- 逐项比较计划声明与实际值。
- 每项偏离记录规定字段和枚举。
- `scope_up` 与 `design_gap` 默认拆 Issue，并记录 `parent_issue_id`。

验证：纯 `estimate_wrong` 只留 closeout 记录，偏离不被写成自动缺陷。

### Step 3：更新 reviewer 与 ADR schema

- reviewer 检查对账已完成，所有偏离字段完整。
- ADR schema 增加七个可选字段。
- 明确偏离驱动 ADR 的条件必填场景，普通 ADR 不受影响。

验证：被接受的 `scope_up`、新依赖、新抽象层、`design_gap` 补全均被覆盖。

### Step 4：刷新派生 hash

先将全部新文件加入 index，再按 repository contract 使用的 tracked-directory
hash 算法刷新 `skills-lock.json` 中所有 `sourceType=local` 条目。

验证：未受影响条目的 hash 保持不变，受影响条目不再 stale。

## 6. 验证

按顺序执行：

```bash
uv run scripts/generate_shared_contracts.py --check
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
git diff --cached --check
```

验收时同时人工检查：

- 六字段在 public checkpoint、planner、implementor、closeout、reviewer 之间闭环；
- 偏离记录字段和枚举一致；
- ADR schema 只对偏离驱动 ADR 条件必填；
- diff 没有越过禁止区域。

## 7. Closeout 要求

实施结束后，将本节更新为实际文件数、实际新增依赖、实际新增配置、实际新增抽象层、
实际行数数量级及测试与验收点关系。逐项与 `## 2. 预期改动声明` 比较。

任何偏离必须记录 `trigger`、`expected`、`actual`、`kind`、`explanation`、
`resolution`；需要拆分时同时记录新 Issue 的 `parent_issue_id`。完成对账前不得进入交付。

## 8. 风险与处理

| Risk | Impact | Mitigation |
| --- | --- | --- |
| 声明被误作硬预算 | 合理偏离被阻止 | 明确其只触发问询和记录。 |
| 小修复流程变重 | hotfix 成本上升 | 允许简化字段，但保留确认。 |
| 普通 ADR 被额外约束 | 既有写作流程扩大 | 新字段保持可选，仅偏离驱动 ADR 条件必填。 |
| 估算误差产生过多 ADR | 决策目录被稀释 | 纯 `estimate_wrong` 只在 closeout 留一行。 |
