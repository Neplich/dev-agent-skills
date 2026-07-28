# 架构证据

- `services/gateway/src/workflow-events.ts` 将 workflow_finished 事件转换为统一附件模型。
- `packages/contracts/src/message-file.ts` 是 Web 与 Gateway 共用的文件字段契约。
- 兼容路径保留旧文本消息渲染，避免无附件响应回归。
