---
title: Graph search API
visibility: internal
doc_type: api
stage: dev
owners:
  - knowledge-discovery
related_code:
  - src/api/knowledge_discovery/graph/**
last_verified_version: unverified
---

# Graph search API

[返回上级功能导航](./)

## 接口边界

- 功能域 / 子功能：知识发现与应用 / 图谱检索
- 调用方与用途：研究工作台检索关联实体
- 鉴权与权限：已认证的工作区成员
- owner 与生命周期：`knowledge-discovery`，当前接口

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `POST` | `/api/knowledge-discovery/graph/search` | 检索关联实体 | 成员 |

## 请求

请求体包含必填的 `query`，可选 `limit` 最大为 50。

## 响应与错误

成功返回实体与关系数组；空查询返回 `422`。

## 证据

- 功能分类与 owner：`docs/pm/feature-catalog.md`
- 路由与处理入口：`src/api/knowledge_discovery/graph/routes.py`
- schema 或 contract：路由请求模型
