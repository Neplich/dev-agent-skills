---
title: Workspace governance API
visibility: internal
doc_type: api
stage: dev
owners:
  - platform-ops
related_code:
  - src/api/platform_governance/workspaces/**
last_verified_version: unverified
---

# Workspace governance API

[返回上级功能导航](./)

## 接口边界

- 功能域 / 子功能：平台治理与运行 / 工作区治理
- 调用方与用途：平台管理端列出工作区状态
- 鉴权与权限：平台管理员
- owner 与生命周期：`platform-ops`，当前接口

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `GET` | `/api/platform-governance/workspaces` | 查询工作区 | 管理员 |

## 请求

可选 query 参数 `status` 用于筛选工作区状态。

## 响应与错误

成功返回工作区摘要数组；非管理员返回 `403`。

## 证据

- 功能分类与 owner：`docs/pm/feature-catalog.md`
- 路由与处理入口：`src/api/platform_governance/workspaces/routes.py`
- schema 或 contract：路由响应模型
