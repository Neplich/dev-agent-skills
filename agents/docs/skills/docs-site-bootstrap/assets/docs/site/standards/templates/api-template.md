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

根据 route、schema、handler 和测试说明当前接口。正文覆盖请求、响应、鉴权、错误与证据；流式或文件接口说明结束语义、Content-Type 和下载头。

按业务域与可独立理解的接口组织页面，索引提供范围和导航。紧密接口组可共用页面，每条接口具有可直接定位的锚点。

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

[返回上级功能导航](./)

## 接口边界

- 功能域 / 子功能：
- 调用方与用途：
- 鉴权与权限：
- owner 与生命周期：
- 稳定性或兼容边界：

## 接口清单

| 方法 | 路径 | 用途 | 权限 |
| --- | --- | --- | --- |
| `<METHOD>` | `<path>` | `<当前用途>` | `<要求>` |

合并紧密接口组时，“用途”链接到本页对应接口详情锚点。

## 请求

记录 path、query、header 和 body 的真实字段、类型、必填性与约束。

## 响应与错误

列出成功响应结构、状态码和可验证错误结构。

## 证据

- 功能分类与 owner：
- 路由与处理入口：
- schema 或 contract：
- 测试：
```
<!-- docs-scaffold:end -->
