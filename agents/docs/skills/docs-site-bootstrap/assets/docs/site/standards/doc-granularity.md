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

## Product 层级

Product 优先按已确认的产品功能树与 `feature_path` 组织为“产品域 → 功能 / 子功能
→ 用户任务或场景”，不按 UI 页面、角色、源码目录或篇幅机械拆分。

- `product/index.md` 只提供产品能力地图、受众入口和全局导航。
- 每个产品域以及仍包含子功能的功能节点使用目录和 `index.md`；入口页只说明
  范围、适用角色、子页面与相邻功能，不复制任务页正文。
- 一个叶子页只回答一个可独立完成或理解的任务，例如创建、配置、执行、查看
  结果或恢复失败。两个任务具有不同入口、权限、成功结果、失败反馈或恢复路径
  时必须拆页，即使合并后的篇幅仍然很短。
- 核心概念、权限与限制、故障恢复仅在跨多个任务复用且有独立维护价值时拆成
  共享页；相关任务页必须链接这些共享页。
- 角色通常是页面中的权限与可见性证据。只有角色拥有实质不同的产品入口和
  生命周期时，才建立角色专属分支。

## Design 层级

Design 优先按当前系统 / 领域 / 子系统 / 组件的稳定所有权组织，并以
`feature_path`、TRD impact scope、最终代码和测试核对边界，不按文件数量拆页。

- `design/index.md` 只提供系统设计地图、领域边界和全局导航。
- 每个领域以及仍包含子模块的设计节点使用目录和 `index.md`；入口页只说明
  职责、非目标、子页面、相邻模块和权威证据入口。
- 独立职责或维护周期不同的组件，以及跨组件控制流、数据流、安全 / 权限边界、
  错误归属或恢复机制，分别使用可独立阅读的页面。
- 组件页必须链接参与的流程；流程页必须反向链接所有参与组件。API 和数据库
  contract 只链接对应权威页，不在 Design 中复制完整字段表。
- 跨领域事实只保留一个权威页面；其他领域通过明确链接引用。
- 方案讨论、未来设计、未完成实现和实施日记不进入 `design/**`。

## 约束

目录入口负责说明范围和导航，不复制子页面正文。Product / Design 页面必须能从
各自根索引逐级定位；新建或移动稳定路径前，先确认迁移、重定向和链接修复范围。
不要按版本复制整套页面；正式页面保留当前状态，历史由版本控制和发布说明承载。

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

## Ops 部署文档粒度

`docs/site/ops/deployment/` 固定采用目录形式，因为 Development、Docker 与
Kubernetes/Helm 具有不同证据、命令、网络、存储、配置注入和回滚边界：

```text
ops/deployment/
├── index.md
├── environment-reference.md
├── development/
│   ├── index.md
│   └── image-build.md
├── docker/
│   ├── index.md
│   └── image-sources.md
└── kubernetes-helm/
    ├── index.md
    ├── image-sources.md
    ├── chart-package.md
    └── values-reference.md
```

- 根 `index.md` 只说明三类的适用场景、支持状态、选择指引和导航，不复制
  子页正文；各子目录 `index.md` 是该部署方式的权威 runbook。
- `environment-reference.md` 是三类共享的参数权威页。Development、Docker 与
  Kubernetes/Helm 页面只说明各自注入、覆盖和 secret 映射，不复制参数表。
- 每类分别维护 prerequisites、configuration、commands、success criteria、
  rollback 与 troubleshooting；不得把三类命令合并成一个聚合 runbook。
- Development 的 `image-build.md` 只描述有 Dockerfile、构建脚本或执行结果支持
  的开发验证镜像打包路径，不将其表述为正式部署流程。
- Docker 的 `image-sources.md` 与 Kubernetes/Helm 的 `image-sources.md` 分别核对
  自身 registry、repository、tag、digest、架构、鉴权引用和拉取后验证；不得因
  tag 同名推断来源或 digest 相同。
- `chart-package.md` 按宿主真实 Chart 目录说明包结构和职责；
  `values-reference.md` 按真实 values、schema、模板消费点和环境覆盖说明配置接口。
  不存在的 Chart 文件或 values 分组不得保留为空模板。
- 不支持、缺少配置或缺少执行证据的类别在候选范围中标记为 `unsupported`、
  `blocked` 或 `out-of-scope`，说明缺失证据；其他已确认类别可以继续，禁止生成
  占位命令或伪造成功状态。
- 从聚合部署页迁移时，页面移动、内部链接修复、必要导航、change-map 条目更新
  与重复内容归并必须作为同一候选原子范围展示并确认。
