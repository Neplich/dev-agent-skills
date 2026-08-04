---
title: Knowledge curation API
visibility: internal
doc_type: api
stage: dev
owners:
  - knowledge-platform
related_code:
  - src/api/knowledge_building/curation/**
last_verified_version: unverified
---

# Knowledge curation API

[返回上级功能导航](./)

## 接口边界

- 功能域 / 子功能：知识建设与维护 / 知识维护
- 调用方与用途：知识库管理端修订文档元数据
- 鉴权与权限：已认证的知识库编辑者
- owner 与生命周期：`knowledge-platform`，当前接口

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `PATCH` | `/api/knowledge-building/documents/{document_id}` | 修订元数据 | 编辑者 |

## 请求

路径参数为 `document_id`，请求体可包含 `title` 与 `tags`。

## 响应与错误

成功返回更新后的文档摘要；文档不存在时返回 `404`。

## 证据

- 功能分类与 owner：`docs/pm/feature-catalog.md`
- 路由与处理入口：`src/api/knowledge_building/curation/routes.py`
- schema 或 contract：路由请求模型
