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

以真实部署配置、脚本和执行结果编写可用步骤。操作包含前置条件、成功标准、恢复和回滚；凭据使用安全存储引用。

按实际 Development、Docker、Kubernetes/Helm 支持能力选择内容。共享参数页核对 .env.example、配置 schema、实际读取和注入点；每个参数保留类型、必填性、默认值、约束、生命周期与环境信息。

Development 说明源码启动与验证构建；Docker 说明 Compose、网络、卷、迁移和恢复；Kubernetes/Helm 说明集群权限、values、ConfigMap/Secret、Chart、发布顺序与 rollout。镜像来源记录坐标、digest、架构、鉴权引用和验证方式。

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
