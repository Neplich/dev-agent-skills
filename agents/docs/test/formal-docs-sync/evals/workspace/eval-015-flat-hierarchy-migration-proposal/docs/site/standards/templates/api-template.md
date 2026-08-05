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

页面路径来自已确认的功能域与子功能，例如
`api/<feature-domain>/<subfeature>/<route>.md`，不从源码目录名机械生成。
`api/index.md` 和各中间节点 `index.md` 只承担范围、共享约定与导航，
并直接链接所有子节点或 route 叶子页；完整 contract 不在索引中重复。
叶子页默认覆盖一条 route；只有读者任务、owner、生命周期和 contract
边界都一致时才可以合并，且每条 route 仍须有可直接定位的页内锚点。

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

合并紧密接口组时，“用途”必须链接到本页对应接口详情锚点。

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
