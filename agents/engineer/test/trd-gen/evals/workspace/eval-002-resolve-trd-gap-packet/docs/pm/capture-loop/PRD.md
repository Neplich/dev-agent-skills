---
feature: capture-loop
feature_path: capture-loop
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-26
last_updated: 2026-07-26
---

# Capture Loop

## 已确认范围

- `capture.created` 事件通过队列异步处理。
- 客户端事件 ID 是幂等键。
- 临时错误有限重试，永久错误或重试耗尽进入 dead-letter。
- pending、processed 和 failed 状态可观测。

## P0 验收

- 重复事件只产生一次业务结果。
- 临时错误遵循已记录的重试上限。
- 处理失败不会丢失原始事件和关联 ID。

## 非目标

- 改变 Capture 内容模型。
- 在 PRD 中决定具体队列实现。
