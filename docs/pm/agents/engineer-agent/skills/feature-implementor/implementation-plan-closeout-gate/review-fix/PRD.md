---
title: "IMPLEMENTATION_PLAN 收尾门禁 Review 修复 PRD"
type: PRD
version: "0.1.0"
status: Draft
author: "Neplich Codex"
date: "2026-06-24"
last_updated: "2026-06-25"
generated_by: "idea-to-spec"
feature: "review-fix"
feature_path: "agents/engineer-agent/skills/feature-implementor/implementation-plan-closeout-gate/review-fix"
parent_feature: "agents/engineer-agent/skills/feature-implementor/implementation-plan-closeout-gate"
feature_level: "6"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/44"
related_pr: "https://github.com/Neplich/dev-agent-skills/pull/45"
---

# IMPLEMENTATION_PLAN 收尾门禁 Review 修复 PRD

## 背景

PR #45 已实现 `feature-implementor` 的 implementation plan closeout gate。
PR review 进一步指出新增 eval 的 durable `comparison.md` 缺少真实 baseline
结果或 blocked / skipped 原因。本地 review 同时指出实施计划 closeout 证据应记录
最终 PASS 的 subagent 验证结果。

本修复只补齐 durable 证据链，不改变 closeout gate 的产品范围。

## 目标

1. 让新增 eval 的 `Without Skill / Baseline` section 不再只是描述假设风险。
2. 让实施计划 closeout 记录最终 PASS 的 fresh subagent validation。
3. 保持两个 durable evidence 文件对 baseline、validation 和 runtime artifact policy 的表述一致。

## 非目标

- 不修改 `feature-implementor` skill 行为。
- 不新增新的 eval item。
- 不提交 runtime transcript、diagnostics、outputs、timing 或 run status。
- 不重写 PR #45 的主实施计划范围。

## 功能需求

| ID | Feature | Description | Priority | Acceptance Criteria |
| --- | --- | --- | --- | --- |
| FR-001 | Baseline Evidence | `eval-010` 的 durable comparison 必须记录 baseline 结果，或明确 baseline 被 blocked / skipped 的原因。 | P0 | `Without Skill / Baseline` section 不再只有假设风险。 |
| FR-002 | Final Validation Evidence | closeout gate 实施计划必须记录最终 PASS 的 fresh subagent validation。 | P0 | 实施计划中可看到最终 subagent id、PASS 结论和测试命令摘要。 |
| FR-003 | Evidence Consistency | `IMPLEMENTATION_PLAN.md` 与 `comparison.md` 的 validation / baseline / runtime artifact policy 表述一致。 | P1 | 两份文档不会互相矛盾。 |

## 验收标准

| ID | Criteria | Verification |
| --- | --- | --- |
| AC-01 | PR review thread 的 baseline 缺口被直接处理。 | 人工 review `comparison.md`。 |
| AC-02 | 本地 review 提到的最终 PASS subagent 证据已写回实施计划。 | 人工 review `IMPLEMENTATION_PLAN.md`。 |
| AC-03 | 仓库确定性检查通过。 | 运行 repository / eval contract 和 pytest。 |
