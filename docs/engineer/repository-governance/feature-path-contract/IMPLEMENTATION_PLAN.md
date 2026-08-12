---
title: "feature_path 自主拆分与结构治理实施计划"
type: IMPLEMENTATION_PLAN
version: "1.0.0"
status: Implemented
author: "Neplich Claude"
date: "2026-08-03"
last_updated: "2026-08-03"
generated_by: "feature-implementor"
feature: "feature-path-contract"
feature_path: "repository-governance/feature-path-contract"
parent_feature: "repository-governance"
feature_level: "2"
implementation_scope: "feature-path-structure-governance"
previous_plan_archive: "docs/engineer/repository-governance/feature-path-contract/archive/IMPLEMENTATION_PLAN-feature-path-contract.md"
related_prd: "docs/pm/repository-governance/feature-path-contract/PRD.md"
related_trd: "docs/engineer/repository-governance/feature-path-contract/TRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/197"
related_pr: "https://github.com/Neplich/dev-agent-skills/pull/218"
changelog:
  - version: "1.0.0"
    date: "2026-08-03"
    changes: "补录 #197 L2b 拆分机制与结构治理的已交付范围"
---

# feature_path 自主拆分与结构治理实施计划

## 1. 实施上下文

本计划为补录。issue #197（PRD/TRD 多级 `feature_path` 自主拆分与结构梳理机制）属契约面 `major` 变更，按仓库「变更分级契约」应先产出完整实施计划并确认后再实施；实际执行以 issue 内已确认设计与维护者逐轮确认为范围依据直接实施，review（PR #218 P1 意见）指出后按门禁要求补录本计划，状态经维护者批准（2026-08-03，PR #218 对话内）转为 Implemented，plan gate 以事后确认闭环。

## 2. 已交付范围

| 范围 | 内容 |
| --- | --- |
| L2b 拆分机制 | `gen-conventions.md` L2 拆分为 L2a（同目录支撑文档）/L2b（子 feature_path 拆分评估）；四类信号（>500 行、独立领域 ≥3、US·FR ≥15、语义子功能边界）；提案-确认制 |
| 迭代接入 | `prd-iteration`、`trd-iteration`、`trd-gen` 接入 L2b 评估；`prd-iteration` 在更新时初始化/reconcile `child_features`（先推导子路径，为空才写 `N/A`） |
| 结构治理 | 新增 `_internal/analysis/structure-governance` 模块：六角色目录只读全量梳理，HTML 报告写仓库外 `mktemp -d`，对话内给摘要 |
| 路由 | `pm-agent` 新增 `document_structure_governance` request_type；`idea-to-spec/SKILL.md` Phase 0 lane 表与 `skill-map.md` 同步登记 |
| 索引契约 | `prd-schema.md` 定义 `child_features` 字段；`prd-gen` 生成子 PRD 时同步父索引；reparenting 移动同步旧父/新父双侧索引 |
| 角色边界 | trd-gen 只做 TRD 侧镜像；PM 侧索引更新与 PM 目录移动交回 `idea-to-spec`；活跃计划对齐交 `feature-implementor` |
| 契约文档 | `feature-path-contract` PRD/TRD 扩展 L2b 与结构治理契约 |
| eval | 新增 `eval-009-prd-iteration-split-proposal`、`eval-016-route-document-structure-governance`，fresh subagent 验证均 PASS/FULL |

## 3. 验证证据

- 四项契约检查（repository / eval / eval-artifacts / doc）全部 PASS；完整 pytest 213/213 PASS。
- 两个新 eval 经规范 fresh subagent 验证（显式 with_skill → 全新 baseline → judge）：Behavior PASS、Coverage FULL；eval-009 baseline 1/5、eval-016 baseline 3/5。
- PR #218 外部 review 全部意见逐条处置完毕。

## 4. 流程偏差记录

本次实施未先产出活跃计划即开工，不符合 `major` 变更的 plan gate；本计划为 review 指出后的补录。后续契约面 `major` 变更必须先有计划再实施。
