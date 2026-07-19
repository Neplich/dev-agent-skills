---
title: 功能设计模板
visibility: internal
doc_type: design
stage: dev
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 功能设计模板

页面表达当前稳定设计，不保留方案讨论或实施日记。`related_code` 必须覆盖真实
模块和测试；链接权威 API 与数据库页面，不重复完整 contract。结构、流程、
错误与安全边界都应能回到代码或测试证据。

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

## 能力与边界

- 负责什么：
- 不负责什么：
- 相邻模块：

## 结构与代码地图

用真实目录树或短列表标出入口、编排、数据访问和测试位置。

## 核心流程

用 Mermaid 流程图表达调用方、入口、核心模块与稳定输出。

## 数据、接口与配置

说明本模块直接拥有的状态、配置和兼容边界，并链接权威 contract。

## 错误、安全与验收

记录权限、敏感信息、失败归因、超时或重试边界和防回归测试。
```
<!-- docs-scaffold:end -->
