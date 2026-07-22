---
title: 数据库文档模板
visibility: internal
doc_type: database
stage: dev
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 数据库文档模板

只描述最新 schema 当前状态。`related_code` 必须覆盖真实 schema、迁移与关键
数据访问代码；记录真实索引、外键、逻辑引用和删除策略，不存在物理外键时
明确逻辑约束位置。历史迁移过程不混入当前字段定义。

页面按 `database/<database-or-schema>/<data-domain>/` 组织。根索引、数据库 /
schema 索引和数据域 `index.md` 只记录边界、owner、关系摘要和导航。
关系密集的数据域使用 `relationships.md` 记录有证据的关系总览，每个实体 /
表使用独立页记录字段、约束、索引、读写 owner 和生命周期。关系页与
实体 / 表页必须双向链接，并把物理外键与逻辑引用分开标记。

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

[返回所属数据域](./) · [查看关系总览](./relationships.md)

## 范围与所有权

- 数据库 / schema：
- 数据域：
- schema 权威入口：
- 读写所有者：

## 相关页面

- 相关实体 / 表：
- 相关功能与 API：

## 实体关系

实体页只摘要记录与本实体直接相关的已验证关系；完整 Mermaid ER 图放在数据域关系总览，且只在证据支持时使用。

## 表与字段

| 表 / 实体 | 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- | --- |
| `<entity>` | `<field>` | `<type>` | `<constraint>` | `<meaning>` |

## 索引

记录当前主键、唯一索引、普通索引和对应查询用途。

## 物理外键

记录 schema 中真实存在的外键、引用页面和删除 / 更新策略；没有时明确写“无物理外键”。

## 逻辑引用

记录没有物理外键但由应用、仓储层或测试保证的引用，并指向证据；不得用 FK 语义表述。

## 数据生命周期

说明创建、更新、归档、删除、敏感字段保护和必要迁移边界。

## 证据

- schema / model：
- 关键读写路径：
- 约束与集成测试：
```
<!-- docs-scaffold:end -->
