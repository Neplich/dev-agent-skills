# BRD 生成器 (brd-gen)

## 概述

从项目描述自动生成标准化的商业需求文档 (Business Requirements Document)。

## 使用场景

- 新项目启动，需要编写商业论证
- 将商业目标正式化为文档
- 需要与利益相关方对齐项目范围、ROI 和时间线

## 快速开始

在 Claude Code 中使用：

```
帮我生成一个 BRD，项目是重新设计电商结账流程，目前支付环节流失率 40%
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| project_description | 是 | 项目描述 |
| stakeholders | 否 | 已知的利益相关方 |
| budget_context | 否 | 预算范围 |
| timeline_context | 否 | 期望时间线 |

## 输出

标准化 BRD 文档（Markdown），包含：
- 执行摘要、背景分析、SMART 目标、利益相关方分析
- 范围定义、功能需求、非功能需求
- ROI 分析、风险评估、里程碑计划

## 关联 Skill

- `brd-validator` — 校验 BRD 质量
- `brd-iteration` — 迭代更新 BRD
- `prd-gen` — 从 BRD 进一步生成 PRD
