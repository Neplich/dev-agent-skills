---
title: "README 协作门禁 PRD"
type: PRD
version: "0.1.1"
status: Draft
author: "Neplich Codex"
date: "2026-06-25"
last_updated: "2026-09-01"
generated_by: "idea-to-spec"
feature: "readme-collaboration-guardrails"
feature_path: "agent-collaboration/readme-collaboration-guardrails"
parent_feature: "agent-collaboration"
feature_level: "2"
child_features:
  - "agent-collaboration/readme-collaboration-guardrails/review-fix"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/28"
changelog:
  - version: "0.1.1"
    date: "2026-09-01"
    changes: "按 skill 最新约定补齐 frontmatter 字段（child_features、changelog）"
---

# README 协作门禁 PRD

## 背景

GitHub issue #28 要求 README 层面准确表达 Agent 协作门禁，避免用户把 PRD/TRD 对齐、IMPLEMENTATION_PLAN 确认和 QA E2E handoff 误解为 specialist 内部细节。

## Owner

本功能归属 `agent-collaboration`。PM 范围负责定义 README 应呈现的跨 Agent 协作规则；Engineer 范围负责按现有 README 结构落地文档更新。

## 范围

- 主 README 保留 7 个 Agent 的协作关系，并补充现有功能变更、bug fix 和用户可见实现的关键门禁。
- Engineer README 展示 TRD 确认、实施计划确认、实现或 debug、测试与 QA E2E handoff 的关系。
- 中英文 README 保持语义一致。

## 验收标准

| ID | 标准 |
| --- | --- |
| AC-01 | README 不把 PRD/TRD 对齐和 IMPLEMENTATION_PLAN 确认隐藏为 specialist 内部步骤。 |
| AC-02 | Engineer README 的实现和 debug 路径都能进入 QA E2E handoff。 |
| AC-03 | README 只描述协作门禁，不复制 specialist SKILL.md 的完整规则。 |
| AC-04 | 英文和中文 README 的主流程语义一致。 |

## 非目标

- 不修改 specialist skill 行为。
- 不新增 eval。
- 不刷新 `skills-lock.json`。
