---
title: "变更分级契约实施计划"
type: IMPLEMENTATION_PLAN
version: "0.1.0"
status: "Implemented"
author: "Neplich Claude Code"
date: "2026-07-05"
last_updated: "2026-07-05"
generated_by: "feature-implementor"
feature: "change-tier-contract"
feature_path: "repository-governance/change-tier-contract"
parent_feature: "repository-governance"
feature_level: "2"
implementation_scope: "change-tier-contract"
related_prd: "docs/pm/repository-governance/change-tier-contract/PRD.md"
related_trd: "docs/engineer/repository-governance/change-tier-contract/TRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/55"
changelog:
  - version: "0.1.0"
    date: "2026-07-05"
    changes: "初始版本，落地变更分级契约与各门禁分级引用并记录验证结果"
---

# 变更分级契约实施计划

## 1. 实施上下文

本计划实施 GitHub issue #55：在 `AGENTS.md` 定义 `hotfix` / `standard` / `major`
三级变更分级契约（`change_tier`），作为所有角色门禁强度的唯一引用来源，并让
`feature-implementor` 的 plan / closeout / archive gate、QA E2E 门禁与 `pm-agent`
入口分类按 `change_tier` 取强度。

本次变更的 `change_tier` 自判为 `major`：影响 `AGENTS.md` 契约面和多个角色的
skill 文档，按契约维持完整实施计划流程。

来源文档：

- PRD：`docs/pm/repository-governance/change-tier-contract/PRD.md`
- TRD：`docs/engineer/repository-governance/change-tier-contract/TRD.md`
- Issue：`https://github.com/Neplich/dev-agent-skills/issues/55`

## 2. 当前门禁状态

| 门禁 | 状态 | 证据 |
| --- | --- | --- |
| PRD 对齐 | 已完成 | `docs/pm/repository-governance/change-tier-contract/PRD.md`（Approved） |
| TRD 对齐 | 已完成 | `docs/engineer/repository-governance/change-tier-contract/TRD.md` |
| 实施计划 | 已实施 | 本文件 `status: "Implemented"` |
| 契约与文档修改 | 已完成 | 见第 3 节文件清单 |
| 验证 | 已完成 | 见第 6 节 |

## 3. 范围

### 3.1 计划文件变更

| 路径 | 操作 | 目的 |
| --- | --- | --- |
| `AGENTS.md` | 修改 | 新增「变更分级契约」章节（唯一定义源）；QA E2E 门禁条目改为引用分级契约取强度。 |
| `agents/engineer/skills/feature-implementor/SKILL.md` | 修改 | plan gate 与 closeout / archive 确认按 `change_tier` 取强度；QA handoff 携带 resolved `change_tier`。 |
| `agents/engineer/skills/feature-implementor/_internal/planner/INSTRUCTIONS.md` | 修改 | 计划记录 resolved `change_tier`；`hotfix` 轻量计划形态与一次确认；预期变更不得按 `hotfix` 规划。 |
| `agents/engineer/skills/feature-implementor/_internal/reviewer/INSTRUCTIONS.md` | 修改 | closeout 检查清单增加分级强度检查项。 |
| `agents/qa/skills/qa-agent/SKILL.md` | 修改 | E2E 门禁按 `change_tier` 取强度；handoff 声明 resolved tier 与所选强度。 |
| `agents/product_manager/skills/pm-agent/SKILL.md` | 修改 | 入口判级职责与 #52 `change_tier` handoff packet 字段衔接。 |
| `docs/pm/repository-governance/change-tier-contract/PRD.md` | 新增 | 需求定义。 |
| `docs/engineer/repository-governance/change-tier-contract/TRD.md` | 新增 | 技术方案与设计决策。 |
| `docs/engineer/repository-governance/change-tier-contract/IMPLEMENTATION_PLAN.md` | 新增 | 本计划。 |
| `skills-lock.json` | 修改 | 重算 `feature-implementor`、`pm-agent`、`qa-agent` 的 `computedHash`。 |

### 3.2 明确不做

- 不修改 `scripts/check_repository_contract.py` 等契约脚本：`hotfix` 轻量计划
  形态不引入新落盘结构（TRD D-002）。
- 不实现 #52 PM 收口本体，不实现 #54 archive gate 本体；只留衔接措辞。
- 不改变 skill eval 的 Fresh Sub-Agent 门禁。
- 不在本次提交中新增 `hotfix` 场景 eval 用例（PRD FR-008，P1），作为后续工作
  单独补充；见 TRD 第 8 节。

## 4. 实施步骤

1. `AGENTS.md` 新增「变更分级契约」章节：等级表、判定入口、门禁强度表、
   Fresh Sub-Agent 门禁排除说明 → 验证：`rg "变更分级契约" AGENTS.md`。
2. QA E2E 门禁条目改写：预期对齐门禁按 `change_tier` 取强度；"小功能也不能
   跳过"改为"任何等级都不能跳过实施计划门禁，`hotfix` 可用轻量计划形态"
   → 验证：证据要求未被削弱。
3. `feature-implementor` SKILL.md、planner、reviewer 增加分级引用段落，不重写
   原有 gate → 验证：只引用 `AGENTS.md` 契约，不复制等级表。
4. `qa-agent`、`pm-agent` SKILL.md 增加分级引用与 #52 衔接措辞 → 验证：同上。
5. 新增 PRD / TRD / 本计划三份文档 → 验证：frontmatter 满足仓库契约。
6. 重算 `skills-lock.json` 受影响 skill 的 `computedHash` → 验证：
   `check_repository_contract.py` 通过。
7. 运行三个契约脚本与 CI 同款 pytest → 验证：全部通过。

## 5. 风险与缓解

| 风险 | 缓解 |
| --- | --- |
| 各 gate 复制分级定义导致漂移 | 各处只加一小段引用，等级表只存在于 `AGENTS.md`。 |
| `hotfix` 被滥用跳过预期对齐 | 契约明确预期变化一律按 `standard` 或 blocked 回 PM；planner 与 qa-agent 各自重申。 |
| #52 / #54 未落地导致措辞失效 | 两阶段判定入口 + archive gate 条件引用。 |

## 6. 实施收尾

### 6.1 验证结果

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| 仓库契约 | `uv run scripts/check_repository_contract.py` | 通过 |
| eval 契约 | `uv run scripts/check_eval_contract.py` | 通过 |
| eval 产物策略 | `uv run scripts/check_eval_artifacts.py` | 通过 |
| CI 同款 pytest | `uv run --with pytest pytest agents/product_manager/test/idea-to-spec agents/qa/test/test_qa_run_eval.py agents/designer/test/test_designer_run_eval.py agents/devops/test/test_devops_run_eval.py agents/test_eval_contract.py` | 通过（72 passed, 3 subtests passed） |

### 6.2 剩余风险与后续工作

- eval 覆盖（FR-008，P1）未在本次范围：`hotfix` 轻量链路放行、`standard`
  完整门禁、`hotfix` 名义滥用阻断三类用例待后续补充，执行时按 Fresh
  Sub-Agent 门禁重新生成 `without_skill` baseline 并更新 `comparison.md`。
- `hotfix` 轻量计划的具体形态（追加 scope 条目或简化模板）由各功能 TRD 阶段
  确定；若未来引入新落盘结构，需同步 `check_repository_contract.py` 校验规则。
- #52 落地时需把 `change_tier` 写入 handoff packet 结构并启用 PM entry gate
  fast lane；#54 落地时按 `hotfix` 档合并确认口径实现 archive gate。
