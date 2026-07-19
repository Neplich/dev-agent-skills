---
title: API 文档模板
visibility: internal
doc_type: api
stage: dev
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# API 文档模板

正文只描述当前接口状态。`related_code` 必须覆盖真实路由、schema、handler
和契约测试；请求、响应、鉴权与错误都应有代码或测试证据，没有的部分删除，
不保留空表。流式或文件接口需说明结束语义、Content-Type 与下载头。

<!-- docs-scaffold:start -->
```md
---
title: {{title}}
visibility: {{visibility}}
doc_type: {{doc_type}}
stage: {{stage}}
owners:
  - {{owner}}
related_code:
  - {{related_code}}
last_verified_version: unverified
---

# {{title}}

## 接口范围

- 调用方与用途：
- 鉴权与权限：
- 稳定性或兼容边界：

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `<METHOD>` | `<path>` | `<当前用途>` | `<要求>` |

## 请求

记录 path、query、header 和 body 的真实字段、类型、必填性与约束。

## 响应与错误

列出成功响应结构、状态码和可验证错误结构。

## 证据

- 路由与处理入口：
- schema 或 contract：
- 测试：
```
<!-- docs-scaffold:end -->
