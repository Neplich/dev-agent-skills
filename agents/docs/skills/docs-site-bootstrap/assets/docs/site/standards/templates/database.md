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

依据 schema、迁移、读写代码和测试说明当前数据结构。实体页记录字段、索引、生命周期，关系总览展示有证据的实体联系，并与实体页互相链接。

按实际存储、schema 和数据域组织页面，索引提供边界和导航。物理外键与应用逻辑引用分别标记来源和语义。

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

[返回所属数据域](./)<!-- 仅当已确认的数据域子树包含 relationships.md 时保留： · [查看关系总览](./relationships.md) -->

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

记录由应用、仓储层或测试保证的逻辑引用，指向证据并说明应用层约束。

## 数据生命周期

说明创建、更新、归档、删除、敏感字段保护和必要迁移边界。

## 证据

- schema / model：
- 关键读写路径：
- 约束与集成测试：
```
<!-- docs-scaffold:end -->
