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

围绕当前代码与测试说明系统、领域、组件和跨组件流程。索引提供职责和导航，正文解释结构、错误与安全边界。

`related_code` 覆盖模块和测试，组件页与流程页互相链接，API 和数据库细节引用对应维护页。

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
- 协作边界：
- 相邻模块：

## 结构与代码地图

用真实目录树或短列表标出入口、编排、数据访问和测试位置。

## 参与流程

列出本组件参与的流程并链接流程页；流程页反向链接全部参与组件。仅在本页拥有
独立流程时，用 Mermaid 表达调用方、入口、核心模块与稳定输出。

## 数据、接口与配置

说明本模块直接拥有的状态、配置和兼容边界，并链接 API / Database 权威页。

## 错误、安全与验收

记录权限、敏感信息、失败归因、超时或重试边界和防回归测试。

## 关联页面

- 上级领域与相邻组件：
- 参与流程：
- API / Database 权威页：
```
<!-- docs-scaffold:end -->
