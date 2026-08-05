---
feature: conversation-messages
feature_path: knowledge-discovery/conversations/messages
version: 1.0.0
date: 2026-08-02
last_updated: 2026-08-05
status: Confirmed
owners:
  - knowledge-discovery
related_code:
  - src/api/knowledge_discovery/conversations/messages.py
  - src/api/knowledge_discovery/conversations/schemas.py
  - tests/contract/test_conversation_messages_api.py
---

# 会话消息 API TRD

## Impacted modules and interfaces

- `messages.py` 提供 `/api/knowledge-discovery/conversations/{conversation_id}/messages`
  下的 `POST` 与 `GET` 路由。
- `schemas.py` 定义消息创建请求和消息响应结构。
- contract test 验证成功响应、空内容校验与会话权限错误。

Database、Design、Ops 与 Product 文档不在本次交付影响域内。
