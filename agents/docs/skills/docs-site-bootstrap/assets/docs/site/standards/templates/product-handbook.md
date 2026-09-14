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

描述当前产品行为，按产品域、功能和用户任务组织页面。`related_code` 指向实际入口和测试，术语与界面保持一致。

任务页说明角色、入口、前置条件、结果、权限、限制、反馈和恢复。共享概念与相关技术事实通过链接复用。

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
- 适用边界：

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
