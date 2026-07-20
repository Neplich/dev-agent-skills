---
title: AI 搜索 API
visibility: both
doc_type: api
stage: release
owners:
  - ai-platform
related_code:
  - src/search/routes.ts
  - tests/search-api.test.ts
last_verified_version: unverified
---

# AI 搜索 API

## 接口范围

`GET /api/search` 为 AI Hub 提供只读知识搜索，不包含写入、删除或管理能力。

## 请求

- `q`：必填非空字符串。
- `limit`：可选整数，范围 1–20，默认 10。

## 响应与错误

- 成功：`200 { items: SearchItem[], limit: number }`。
- 查询为空：`400 { error: "q is required" }`。

## 证据

- `src/search/routes.ts`
- `tests/search-api.test.ts`
