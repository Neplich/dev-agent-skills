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

## 目标

客户端离线或网络抖动时，用户创建的 Capture 事件最终可靠进入处理队列，并能看到明确状态。

## P0 要求

- 接收 `capture.created` 事件并分配幂等键。
- 临时队列错误按受控退避重试，永久错误进入 dead-letter 状态。
- 用户可区分 pending、processed 和 failed。
- 重复提交不得生成重复处理结果。

## 非目标

- 改变 Capture 内容模型。
- 提供跨组织共享。
- 在本阶段实现代码。
