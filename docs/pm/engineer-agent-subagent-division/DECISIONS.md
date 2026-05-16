---
title: "Engineer Agent 编码阶段 sub-agent 分工决策记录"
type: DECISIONS
version: "1.0.0"
status: Draft
author: "AI Assistant"
date: "2026-05-15"
generated_by: "idea-to-spec"
feature: "engineer-agent-subagent-division"
last_updated: "2026-05-15"
related_docs:
  - "docs/pm/engineer-agent-subagent-division/PRD.md"
changelog:
  - version: "1.0.0"
    date: "2026-05-15"
    changes: "初始版本"
---

# Engineer Agent 编码阶段 sub-agent 分工决策记录

## 已确认决策

| ID | 决策 | 理由 |
| --- | --- | --- |
| D-001 | MVP 聚焦复杂 Engineer Agent 编码任务。 | Issue 描述的核心问题是复杂编码任务会挤占主进程上下文。 |
| D-002 | 主进程保留需求、设计约束、仓库规则、实现边界和交付判断。 | 该能力的核心价值是让主进程持续掌握高层上下文，用于最终整合和风险处理。 |
| D-003 | 满足触发条件时，实现和验收由两个不同 sub-agent 承担。 | 分离实现与验收可以降低同一上下文损耗同时影响编码和验收判断的风险。 |
| D-004 | 简单单文件修改、纯解释、纯代码阅读和用户明确不拆分的任务不触发该机制。 | 该机制应提升复杂任务质量，不应增加小任务的流程负担。 |
| D-005 | 第一版 eval 覆盖“文档驱动实现 + 独立验收”的真实场景。 | 真实场景能验证 Engineer Agent 是否会在复杂任务中主动安排分工。 |

## 假设

| ID | 假设 | 如果假设不成立的影响 |
| --- | --- | --- |
| A-001 | Engineer Agent 的运行环境支持当前会话中的 sub-agent 能力。 | 如果不支持，需要降级为结构化 handoff 指令，而不是实际委派执行。 |
| A-002 | 现有 specialist skill 可以在不修改 marketplace 公开结构的情况下更新。 | 如果需要调整 marketplace metadata，范围会扩大到 registry 和 lockfile。 |
| A-003 | 一个代表性 eval 足以先验证 MVP 行为。 | 如果不足，需要为 `debugger` 和 `project-bootstrap` 路径补充更多 eval。 |

## 待确认问题

| ID | 问题 | Owner | 截止点 | 结论 |
| --- | --- | --- | --- | --- |
| Q-001 | `project-bootstrap` 是否纳入 MVP，还是在 `feature-implementor` 和 `debugger` 后再处理？ | PM / Engineer maintainer | 实施前 | 待确认 |
| Q-002 | 默认触发 sub-agent 分工的复杂度阈值应如何定义？ | Engineer maintainer | 实施前 | 待确认 |
| Q-003 | 当本地确定性测试和验收 sub-agent 都可用时，验收应在测试前还是测试后执行？ | Engineer maintainer | 实施前 | 待确认 |

## 已排除方案

| ID | 方案 | 排除理由 |
| --- | --- | --- |
| R-001 | 所有 Engineer Agent 请求都强制拆分 sub-agent。 | 会给简单任务增加不必要开销，也会削弱“选择最窄可用路径”的原则。 |
| R-002 | 只在 dispatcher prompt 中增加一句最终提醒。 | 单点提示不够稳定，难以覆盖 specialist 行为和 eval 回归。 |
