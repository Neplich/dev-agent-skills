---
title: 运维手册模板
visibility: internal
doc_type: ops
stage: ops
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 运维手册模板

只保留当前可执行步骤。`related_code` 必须覆盖真实部署配置、自动化脚本与健康
检查；每项操作包含前置条件、明确成功标准和可执行回滚。敏感值只引用安全
存储位置，不得写入文档。

部署页面使用同一个模板正文，但按页面类型补齐以下事实，不在 skill、脚本或
测试中维护第二份模板：

- `deployment/environment-reference.md`：按功能域或服务分组；每个参数记录参数
  名、用途、类型/格式、必填性、可验证非敏感默认值、允许值/约束、适用部署
  方式、安全示例、Secret 属性与安全存储引用、生效方式和证据。必须交叉核对
  `.env.example`、配置 schema/settings、实际读取代码、Compose/Helm 映射和测试，
  并报告缺失、废弃、重命名与默认值冲突。
- Development：记录操作系统与工具版本、源码和依赖服务、初始化顺序、env 文件、
  服务启动顺序、端口、健康与成功标准、热重载、调试、日志和与容器/集群的差异。
  `image-build.md` 另记 Dockerfile/build context、target、build args、依赖来源、架构、
  开发 tag、已验证构建/加载/推送入口、内容/入口/digest 验证与缓存/registry 前置。
- Docker：记录 Docker/Compose 前置、Compose 文件/profile/依赖顺序、env 覆盖、
  secret、volume、network、port、migration/job、启停、升级、备份、恢复、回滚、
  health/log/data 成功标准；排除 namespace、release revision 和 Helm values。
  `image-sources.md` 按服务记录镜像坐标与 digest、来源类型、架构、登录引用、pull
  入口、mirror/离线选择、签名/provenance 验证和常见拉取故障。
- Kubernetes/Helm：记录集群、Helm、Ingress、StorageClass 与权限前置，namespace、
  release、values 覆盖、ConfigMap/Secret/外部 secret 映射、预检、CRD/hook/job/
  migration 顺序、install/upgrade、rollout/Pod/Service/Ingress/Job 验证和 rollback；
  不从 Compose 推断集群事实。`image-sources.md` 补充 values image 键、Chart/release
  对应、imagePullSecrets/workload identity、节点架构、离线导入和 Pod imageID 核对；
  `chart-package.md` 记录真实 Chart 树、文件职责、dependency/CRD/hook/test、lint/
  template/package/OCI 来源与 provenance；`values-reference.md` 按真实能力分组记录
  values 路径、用途、类型、默认值、必填性、约束、环境差异、敏感性、模板消费点、
  合并优先级和验证方式，禁止把敏感值放入命令行或仓库。

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

## 服务与适用范围

- 服务或组件：
- 环境：
- 依赖与所有者：

## 前置条件

列出所需版本、权限、配置、备份和外部依赖。

## 执行步骤

1. `<准备与预检>`
2. `<执行命令或操作>`
3. `<验证健康状态>`

## 检查点与观测

记录可复现的接口、日志、指标、作业或数据检查及成功标准。

## 回滚与故障处理

- 回滚触发条件：
- 回滚步骤：
- 回滚后验证：
- 常见症状与诊断入口：
```
<!-- docs-scaffold:end -->
