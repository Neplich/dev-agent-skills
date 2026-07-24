---
title: 运维文档
visibility: internal
doc_type: landing
stage: ops
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 运维文档

本目录保存可执行的部署、验证、排障和回滚说明。命令、配置名和检查点
必须来自当前运行配置与验证证据。

## 部署文档

部署文档统一位于 `ops/deployment/`，按运行边界分为 Development、Docker 与
Kubernetes/Helm 三类。`deployment/index.md` 只说明支持状态、适用场景和导航；
共享环境参数由 `deployment/environment-reference.md` 维护，各部署方式在独立
子目录中维护自己的前置条件、配置注入、命令、成功标准、回滚和故障处理。
