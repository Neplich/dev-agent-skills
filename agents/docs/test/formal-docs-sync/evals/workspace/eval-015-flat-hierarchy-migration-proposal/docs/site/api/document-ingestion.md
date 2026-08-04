---
title: Document ingestion API
visibility: internal
doc_type: api
stage: dev
owners:
  - knowledge-platform
related_code:
  - src/api/knowledge_building/ingestion/**
last_verified_version: unverified
---

# Document ingestion API

[返回上级功能导航](./)

## 接口边界

- 功能域 / 子功能：知识建设与维护 / 文档摄取
- 调用方与用途：知识库管理端上传待处理文档
- 鉴权与权限：已认证的知识库编辑者
- owner 与生命周期：`knowledge-platform`，当前接口

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `POST` | `/api/knowledge-building/documents` | 提交摄取任务 | 编辑者 |

## 请求

请求体包含必填的 `source_uri` 字符串和目标 `collection_id`。

## 响应与错误

成功返回 `202` 及任务 `id`；无权访问目标集合时返回 `403`。

## 证据

- 功能分类与 owner：`docs/pm/feature-catalog.md`
- 路由与处理入口：`src/api/knowledge_building/ingestion/routes.py`
- schema 或 contract：路由请求模型
