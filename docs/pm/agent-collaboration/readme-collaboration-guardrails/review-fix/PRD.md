---
title: "README 协作门禁 Review 修复 PRD"
type: PRD
version: "0.1.0"
status: Draft
author: "Neplich Codex"
date: "2026-06-25"
last_updated: "2026-06-25"
generated_by: "idea-to-spec"
feature: "review-fix"
feature_path: "agent-collaboration/readme-collaboration-guardrails/review-fix"
parent_feature: "agent-collaboration/readme-collaboration-guardrails"
feature_level: "3"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/28"
related_pr: "https://github.com/Neplich/dev-agent-skills/pull/34"
---

# README 协作门禁 Review 修复 PRD

## 背景

PR #34 review 指出，README 协作门禁主链路需要调整展示层级，并补齐 Engineer README 中 debugger 分支到 QA E2E handoff 的连接。

## Owner

本功能是 `agent-collaboration/readme-collaboration-guardrails` 的 review-fix 子项，不作为独立长期功能。

## 范围

- 主 README / README_zh 保留 6 个 Agent 的主交互图。
- 门禁关系作为主图后的补充信息呈现。
- Engineer README / README_zh 中 debugger 分支连接到 QA E2E handoff。
- 原主链路实施计划保持历史完成状态。

## 验收标准

| ID | 标准 |
| --- | --- |
| AC-01 | 主 README 的主图仍表达 6 个 Agent 的交互关系。 |
| AC-02 | 门禁关系不抢占主协作图语义。 |
| AC-03 | Engineer README 的 implementation 和 debugger 路径都进入 QA E2E handoff。 |

## 非目标

- 不修改 skill 行为。
- 不新增 eval。
- 不重写父功能实施计划。
