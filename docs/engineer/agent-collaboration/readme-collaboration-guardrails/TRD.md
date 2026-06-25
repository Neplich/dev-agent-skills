---
title: "README 协作门禁 TRD"
type: TRD
version: "0.1.0"
status: Draft
author: "Neplich Codex"
date: "2026-06-25"
last_updated: "2026-06-25"
generated_by: "trd-gen"
feature: "readme-collaboration-guardrails"
feature_path: "agent-collaboration/readme-collaboration-guardrails"
parent_feature: "agent-collaboration"
feature_level: "2"
related_prd: "docs/pm/agent-collaboration/readme-collaboration-guardrails/PRD.md"
---

# README 协作门禁 TRD

## 技术边界

本 TRD 只覆盖 README 文档结构和跨 Agent 协作图，不修改 `SKILL.md`、eval、仓库脚本或锁文件。

## 文件触点

| 文件 | 责任 |
| --- | --- |
| `README.md` | 展示英文 6-Agent 协作关系和关键门禁。 |
| `README_zh.md` | 同步中文协作关系和关键门禁。 |
| `agents/engineer/README.md` | 展示英文 Engineer 典型工作流。 |
| `agents/engineer/README_zh.md` | 同步中文 Engineer 典型工作流。 |

## 实施边界

- README 的 Mermaid 图应表达协作关系，不引入新的运行时规则。
- 现有功能变更和 bug fix 的门禁说明必须与 Engineer / QA 已有 skill 契约一致。
- 本迁移只补 PRD/TRD 归属并保留历史计划，不重写已完成 README 变更。

## 验证

- Markdown 中 Mermaid 流程语义人工检查。
- `git diff --check`
- 仓库 contract 和 eval artifact 检查。
