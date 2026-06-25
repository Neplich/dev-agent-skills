---
title: "Eval Comparison 覆盖 TRD"
type: TRD
version: "0.1.0"
status: Draft
author: "Neplich Codex"
date: "2026-06-25"
last_updated: "2026-06-25"
generated_by: "trd-gen"
feature: "eval-comparison-coverage"
feature_path: "repository-governance/eval-comparison-coverage"
parent_feature: "repository-governance"
feature_level: "2"
related_prd: "docs/pm/repository-governance/eval-comparison-coverage/PRD.md"
---

# Eval Comparison 覆盖 TRD

## 技术边界

本 TRD 只固化 eval workspace、durable comparison 和 runtime artifact 的仓库契约，不修改 specialist skill 的运行行为。

## 组件

| 组件 | 责任 |
| --- | --- |
| `agents/**/test/**/evals/evals.json` | 保存 eval item、显式 workspace 和 assertions。 |
| `agents/**/test/**/evals/workspace/**/comparison.md` | 保存 durable eval 结论。 |
| `agents/**/test/**/evals/workspace/**/eval_metadata.json` | 保存 fixture、清理规则和 deterministic runner 可检查的产物描述。 |
| `scripts/check_eval_contract.py` | 校验 eval schema、workspace、metadata 和 durable result 契约。 |
| `scripts/check_eval_artifacts.py` | 防止 runtime artifact 被提交到仓库。 |

## 实施边界

- 缺失 workspace 或 durable comparison 应由 eval contract 报错。
- runtime artifact 路径应由 artifact checker 报错。
- baseline 或 with-skill 输出的语义质量由 fresh subagent validation 或 reviewer 判断，不由 repository contract 扫描自由文本。
- 历史实施计划迁移只补本 TRD 与 PRD，不重写原计划内容。

## 验证

- `uv run scripts/check_eval_contract.py`
- `uv run scripts/check_eval_artifacts.py`
- `uv run --with pytest pytest agents/test_eval_contract.py`
