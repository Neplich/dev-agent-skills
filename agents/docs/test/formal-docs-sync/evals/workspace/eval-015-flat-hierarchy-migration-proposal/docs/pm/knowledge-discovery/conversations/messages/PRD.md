---
feature: conversation-messages
feature_path: knowledge-discovery/conversations/messages
version: 1.0.0
date: 2026-08-01
last_updated: 2026-08-05
status: Approved
owners:
  - knowledge-discovery
---

# 会话消息 API PRD

研究工作台需要在既有研究会话内发送消息，并读取该会话已有消息。

## Acceptance Criteria

- 工作区成员可向自己可访问的会话发送非空消息。
- 成功发送返回 `201` 及消息标识、会话标识与内容。
- 成员可按会话读取消息列表。
- 空消息返回 `422`，不可访问的会话返回 `403`。
