# Capture Loop 队列重试 TRD

## 技术方案

在现有内存队列服务中增加重试状态计算。处理器仍由 `event-handler.ts` 调用，队列状态由 `queue-service.ts` 维护。

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
