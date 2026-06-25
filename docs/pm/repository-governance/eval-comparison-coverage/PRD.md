---
title: "Eval Comparison 覆盖 PRD"
type: PRD
version: "0.1.0"
status: Draft
author: "Neplich Codex"
date: "2026-06-25"
last_updated: "2026-06-25"
generated_by: "idea-to-spec"
feature: "eval-comparison-coverage"
feature_path: "repository-governance/eval-comparison-coverage"
parent_feature: "repository-governance"
feature_level: "2"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/23"
---

# Eval Comparison 覆盖 PRD

## 背景

GitHub issue #23 指出，skill eval 的长期结论应由 durable `comparison.md` 承载。缺少显式 workspace 或 durable comparison 时，维护者无法稳定判断某个 eval 是否被当前 skill 行为覆盖。

## Owner

本功能归属 `repository-governance`。PM 范围负责定义 eval 证据覆盖要求；Engineer 范围负责用仓库检查和测试固定这些要求。

## 范围

- 每个 eval item 都应有显式 workspace。
- 每个 eval workspace 都应有 durable `comparison.md` 作为长期结论入口。
- `eval_metadata.json` 只描述可复用输入、fixture、清理规则和 deterministic runner 能真实生成或检查的运行期产物。
- runtime artifact 不进入 git，包括 transcript、outputs、diagnostics、timing、run status 和自动生成 comparison。

## 验收标准

| ID | 标准 |
| --- | --- |
| AC-01 | 新增或更新 eval item 时，仓库检查能发现缺失 workspace 或 durable comparison 的情况。 |
| AC-02 | `comparison.md` 是长期结论入口，PR 评论或对话中的 eval 结论应与 durable comparison 一致。 |
| AC-03 | deterministic checker 不把模型运行期 artifact 当作应提交文件。 |
| AC-04 | 无 deterministic runner 的 eval 不声明 runner output，只保留 durable comparison 和必要 metadata。 |

## 非目标

- 不要求一次性重跑所有历史模型 eval。
- 不把 baseline 自由文本语义交给 repository contract 做机器判定。
- 不修改具体 skill 行为。
