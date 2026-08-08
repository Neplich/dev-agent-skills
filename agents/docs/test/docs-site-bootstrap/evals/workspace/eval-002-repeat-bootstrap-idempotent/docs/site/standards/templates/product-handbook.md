---
title: 产品手册模板
visibility: internal
doc_type: product
stage: dev
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 产品手册模板

只陈述已经存在的产品行为。页面路径跟随已确认的产品功能树：根和非叶子
`index.md` 只写范围与导航，叶子页只覆盖一个用户任务或场景。`related_code`
必须覆盖支撑当前能力的真实入口与测试；术语与当前界面和接口保持一致。

任务页按用户角色说明入口、前置条件、成功结果、权限、限制、失败反馈与恢复
路径，并链接相关 Design、API、Database、Ops 权威页，不复制 contract。跨任务
概念或权限仅在具有独立维护价值时拆成共享页。不写规划中的能力，也不把多个
独立任务重新合并成大型 handbook。

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

## 任务与适用范围

- 面向角色：
- 用户目标：
- 入口与前置条件：
- 不覆盖：

## 完成任务

按当前产品入口描述完成该任务的步骤；只有真实流程需要时才使用 Mermaid。

## 权限与限制

说明角色可见性、授权边界、输入限制和不可用条件，并链接复用的概念或权限页。

## 结果、失败反馈与恢复

说明成功结果、用户可见失败反馈、可重试条件和恢复步骤。

## 关联资料

- 上级功能与相邻任务：
- Design：
- API / Database：
- Ops：
```
<!-- docs-scaffold:end -->
