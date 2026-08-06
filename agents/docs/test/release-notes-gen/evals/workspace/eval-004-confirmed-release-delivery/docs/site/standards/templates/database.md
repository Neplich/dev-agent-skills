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

## 范围与所有权

- 数据域：
- schema 权威入口：
- 读写所有者：

## 实体关系

用 Mermaid ER 图记录当前实体关系。

## 表与字段

| 表 / 实体 | 字段 | 类型 | 约束 | 说明 |
| --- | --- | --- | --- | --- |
| `<entity>` | `<field>` | `<type>` | `<constraint>` | `<meaning>` |

## 索引与关系

记录真实索引、外键、逻辑引用、删除策略和查询依赖。

## 数据生命周期

说明创建、更新、归档、删除、敏感字段保护和必要迁移边界。
```
<!-- docs-scaffold:end -->
