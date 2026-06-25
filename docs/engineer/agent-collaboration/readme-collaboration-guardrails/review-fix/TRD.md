---
title: "README 协作门禁 Review 修复 TRD"
type: TRD
version: "0.1.0"
status: Draft
author: "Neplich Codex"
date: "2026-06-25"
last_updated: "2026-06-25"
generated_by: "trd-gen"
feature: "review-fix"
feature_path: "agent-collaboration/readme-collaboration-guardrails/review-fix"
parent_feature: "agent-collaboration/readme-collaboration-guardrails"
feature_level: "3"
related_prd: "docs/pm/agent-collaboration/readme-collaboration-guardrails/review-fix/PRD.md"
---

# README 协作门禁 Review 修复 TRD

## 技术边界

本 TRD 只覆盖 PR #34 review 修复对应的 README 文档调整，不修改 skill、eval、contract 或锁文件。

## 文件触点

| 文件 | 责任 |
| --- | --- |
| `README.md` | 保留 6-Agent 主交互图，并将门禁关系作为补充图。 |
| `README_zh.md` | 同步中文说明。 |
| `agents/engineer/README.md` | 将 debugger 分支接入 QA E2E handoff。 |
| `agents/engineer/README_zh.md` | 同步中文 Engineer flow。 |

## 实施边界

- Review-fix 是父功能子项，不创建独立长期 feature。
- 本迁移只补 PRD/TRD 和路径字段，原实施计划内容保持历史事实。

## 验证

- `git diff --check`
- README Mermaid 语义人工检查。
