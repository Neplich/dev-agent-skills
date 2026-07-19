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
