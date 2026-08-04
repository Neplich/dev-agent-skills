---
title: 文档粒度
visibility: internal
doc_type: design
stage: dev
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 文档粒度

文档边界以读者任务和稳定事实边界为准，不按代码文件数量机械拆分。

## 选择单文件

满足以下条件时优先使用单文件：

- 主题只有一个稳定入口和一组紧密关联的事实；
- 页面在合理篇幅内可以完整回答读者任务；
- 子主题没有独立所有者、生命周期或导航价值。

## 选择目录

满足任一条件时使用目录并提供 `index.md`：

- 存在多个可独立阅读和维护的子域；
- 不同子域有不同证据、所有者或更新节奏；
- 单页已经妨碍定位、核验或导航。

## 约束

目录入口负责说明范围和导航，不复制子页面正文。不要按版本复制整套页面；
正式页面保留当前状态，历史由版本控制和发布说明承载。

## API 层级与拆分

- `api/index.md` 只记录全局范围、共享约定和功能域导航；功能域以及仍有子功能的中间节点都使用目录和 `index.md`。
- 父子层级依次由已确认的 `feature_path` / feature catalog、route prefix / tag、handler ownership 和 contract tests 支持；代码文件位于同一目录或页面过长都不足以单独成为拆分依据。
- 叶子页默认只覆盖一个可独立理解和维护的 route。只有读者任务、owner、生命周期和 contract 边界都一致的紧密 route 组才能合并；合并后每条 route 仍必须能从上级索引直接定位。
- 每条已确认 route 的叶子页必须完整记录方法、路径、鉴权、请求、响应、错误和证据，并能从 `api/index.md` 逐级访问。

## Database 层级与拆分

- 先以已确认的数据库实例或存储类型建立边界，再按 schema 或等效所有权边界、数据域、实体 / 表组织。存在多数据库、多 schema 或跨服务边界时不得合并成单个聚合页。
- `database/index.md`、数据库 / schema 节点和数据域 `index.md` 只记录边界、owner、关系摘要和子页导航；字段、索引和生命周期事实留在实体 / 表页。
- 关系密集的数据域必须提供 `relationships.md` 或等效关系总览。关系页链接每个实体 / 表页，实体 / 表页反向链接所属数据域、关系页、相关表、功能和 API。
- 实体 / 表页分开记录物理外键与有证据的逻辑引用；没有物理外键时不得用 ER 图或文字虚构它。

API 和 Database 路径都使用 lower kebab-case。已有稳定宿主路径不得在没有经确认的迁移计划时直接移动。首次 backfill 可分有限批次，但每批必须同时交付叶子页、所有父级 `index.md`、必要关系页、导航和 change-map 条目，形成可导航的完整子树。
