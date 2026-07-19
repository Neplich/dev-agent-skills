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

只陈述已经存在的产品行为。`related_code` 必须覆盖支撑当前能力的真实入口与
测试；术语与当前界面和接口保持一致。按用户角色说明权限、限制、失败反馈与
恢复路径，不写规划中的能力。

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

## 受众与范围

- 面向角色：
- 适用场景：
- 能力边界：

## 核心概念

定义读者必须理解的对象、角色、状态和约束。

## 用户流程

用 Mermaid 流程图表达进入功能、完成配置、执行任务和查看结果。

## 权限、限制与异常

说明不同角色可见操作、输入限制、失败反馈与恢复路径。

## 关联资料

- 功能设计：
- API 或数据说明：
- 运维说明：
```
<!-- docs-scaffold:end -->
