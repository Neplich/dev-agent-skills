---
title: List invoices
visibility: both
doc_type: api
stage: dev
owners:
  - billing-team
related_code:
  - src/api/billing/routes.py
last_verified_version: unverified
---

# List invoices

[返回 Billing API](./)

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `GET` | `/api/billing/invoices` | 列出账单发票 | 当前路由未配置鉴权 |

## 请求

当前接口没有 path、query 或 request body 参数。

## 响应与错误

- 成功响应：`200`，body 为 `{ "items": [] }`。
- 当前路由未定义业务错误结构。

## 证据

- 路由与处理入口：`src/api/billing/routes.py`
