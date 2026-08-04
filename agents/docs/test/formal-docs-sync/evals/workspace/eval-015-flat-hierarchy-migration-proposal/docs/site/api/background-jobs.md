---
title: Background jobs API
visibility: internal
doc_type: api
stage: dev
owners:
  - platform-ops
related_code:
  - src/api/platform_governance/jobs/**
last_verified_version: unverified
---

# Background jobs API

[返回上级功能导航](./)

## 接口边界

- 功能域 / 子功能：平台治理与运行 / 后台任务
- 调用方与用途：平台管理端查询异步任务状态
- 鉴权与权限：平台管理员
- owner 与生命周期：`platform-ops`，当前接口

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `GET` | `/api/platform-governance/jobs/{job_id}` | 查询任务状态 | 管理员 |

## 请求

路径参数 `job_id` 为任务标识符。

## 响应与错误

成功返回任务状态；任务不存在时返回 `404`。

## 证据

- 功能分类与 owner：`docs/pm/feature-catalog.md`
- 路由与处理入口：`src/api/platform_governance/jobs/routes.py`
- schema 或 contract：路由响应模型
