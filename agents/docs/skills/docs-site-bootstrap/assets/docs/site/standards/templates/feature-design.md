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

页面表达当前稳定设计，不保留方案讨论、未来架构或实施日记。页面路径跟随当前
系统 / 领域 / 子系统 / 组件的稳定边界：根和非叶子 `index.md` 只写职责、边界与
导航；组件页写单一职责；跨组件流程或边界单独成页。

`related_code` 必须覆盖真实模块和测试。组件页与相关流程页双向链接；API 与
Database contract 只链接权威页，不重复完整字段表。每个页面的结构、流程、
错误与安全边界都必须能独立回到最终代码或通过的测试证据。

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

## 职责与边界

- 负责什么：
- 不负责什么：
- 相邻模块：

## 结构与代码地图

用真实目录树或短列表标出入口、编排、数据访问和测试位置。

## 参与流程

列出本组件参与的流程并链接流程页；流程页反向链接全部参与组件。仅在本页拥有
独立流程时，用 Mermaid 表达调用方、入口、核心模块与稳定输出。

## 数据、接口与配置

说明本模块直接拥有的状态、配置和兼容边界，并链接 API / Database 权威页，
不复制完整 contract。

## 错误、安全与验收

记录权限、敏感信息、失败归因、超时或重试边界和防回归测试。

## 关联页面

- 上级领域与相邻组件：
- 参与流程：
- API / Database 权威页：
```
<!-- docs-scaffold:end -->
