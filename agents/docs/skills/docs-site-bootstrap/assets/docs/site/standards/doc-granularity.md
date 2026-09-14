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

按读者任务和稳定事实边界组织页面。一个紧密主题适合单页，独立维护的子主题适合目录与索引。篇幅和文件数量提供线索，内容用途决定结构。

| 文档类型 | 组织依据 |
| --- | --- |
| Manual | 平台、业务场景、独立用户任务 |
| Product | 产品域、功能与用户任务 |
| Design | 系统、领域、子系统、组件与跨组件流程 |
| API | 业务域、路由组、独立接口或紧密接口组 |
| Database | 存储、schema、数据域、实体与关系 |
| Ops | 实际部署方式、共享参数、运行与恢复任务 |

索引说明范围、关系和导航，叶子页维护具体事实或操作。跨页面共用事实选择一个主要维护位置，通过链接复用。不同权限或生命周期的内容按实际边界分开维护。

手册任务页包含适用角色、前置条件、步骤、真实界面与截图、结果和异常处理。API 页完整说明请求、响应、错误和权限。数据库页分清物理外键和有依据的逻辑引用。设计页围绕当前代码和测试解释结构。

Development、Docker、Kubernetes/Helm 使用各自可执行 runbook。共享环境参数可写入 environment-reference.md；镜像来源、Chart 包和 values 参考根据真实支持能力建立独立页。

新增或移动页面时同步父级索引、入站链接、导航和 change-map。public/internal 各目标的引用保持可达。保留有效稳定路径，结构整理以完整授权范围和当前读者需要为依据。
