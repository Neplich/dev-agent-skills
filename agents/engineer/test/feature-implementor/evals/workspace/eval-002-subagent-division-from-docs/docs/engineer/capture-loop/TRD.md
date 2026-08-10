---
title: "Capture Loop Queue Retry TRD"
type: TRD
feature: capture-loop
feature_path: capture-loop
parent_feature: N/A
feature_level: 1
version: "1.0.0"
status: Approved
author: "Neplich Codex"
date: "2026-08-10"
last_updated: "2026-08-10"
related_prd: docs/pm/capture-loop/PRD.md
---

# Capture Loop 队列重试 TRD

## 技术方案

在现有内存队列服务中增加重试状态计算。处理器仍由 `event-handler.ts` 调用，队列状态由 `queue-service.ts` 维护。

临时失败最多重试三次。每次临时失败把任务更新为
`retry_scheduled`，增加 `attempts` 并记录 `nextRetryAt`；达到上限后更新为
`failed` 并保留最后一次错误。非临时失败直接进入 `failed`。

## 组件

| 组件 | 职责 | 变更 |
| --- | --- | --- |
| `src/capture-loop/queue-service.ts` | 管理队列任务状态 | 增加 `retry_scheduled` 状态、最大重试次数和下一次重试时间计算。 |
| `src/capture-loop/event-handler.ts` | 调用队列服务并处理事件结果 | 对临时失败调用队列服务的重试调度逻辑。 |
| `tests/capture-loop/queue-service.test.ts` | 验证队列状态变化 | 增加重试和上限测试。 |

## 约束

- 保持现有 TypeScript 文件结构。
- 不新增依赖。
- 不改外部 API。
- 不修改与 Capture Loop 无关的模块。

## 验证

- 运行 `npm test -- tests/capture-loop/queue-service.test.ts`，覆盖首次临时失败、达到三次上限和重试后成功。
- 运行 `npx tsc --noEmit`，确认状态类型和处理器调用保持一致。

## 风险与边界

- 本轮只计算并记录下一次重试时间，不新增后台调度器。
- 不修改外部 API、持久化方式或 Capture Loop 之外的模块。
