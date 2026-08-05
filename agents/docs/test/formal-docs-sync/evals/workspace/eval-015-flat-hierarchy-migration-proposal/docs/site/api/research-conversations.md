---
title: Research conversations API
visibility: internal
doc_type: api
stage: dev
owners:
  - knowledge-discovery
related_code:
  - src/api/knowledge_discovery/conversations/**
last_verified_version: unverified
---

# Research conversations API

[返回上级功能导航](./)

## 接口边界

- 功能域 / 子功能：知识发现与应用 / 研究会话
- 调用方与用途：研究工作台创建会话
- 鉴权与权限：已认证的工作区成员
- owner 与生命周期：`knowledge-discovery`，当前接口

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `POST` | `/api/knowledge-discovery/conversations` | 创建研究会话 | 成员 |

## 请求

请求体包含必填的 `title` 和 `workspace_id`。

## 响应与错误

成功返回 `201` 及会话 `id`；工作区不可访问时返回 `403`。

## 证据

- 功能分类与 owner：`docs/pm/feature-catalog.md`
- 路由与处理入口：`src/api/knowledge_discovery/conversations/routes.py`
- schema 或 contract：路由请求模型
