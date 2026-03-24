# PRD 生成器 (prd-gen)

## 概述

从产品描述自动生成标准化的产品需求文档 (Product Requirements Document)。

## 使用场景

- 新功能或产品需要定义产品需求
- 将非正式的需求描述标准化
- 从 BRD 的业务目标转化为可执行的产品需求

## 快速开始

```
帮我生成一个 PRD，要给 SaaS 应用添加社交登录功能（Google、GitHub）
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| product_description | 是 | 产品/功能描述 |
| target_users | 否 | 目标用户画像 |
| related_brd | 否 | 关联的 BRD 文档 |
| constraints | 否 | 技术或业务约束 |

## 输出

标准化 PRD 文档（Markdown），包含：
- 背景动机、目标与非目标、用户画像
- 用户故事与验收标准、功能需求、非功能需求
- 用户流程、UI/UX、数据模型、API
- 发布计划、风险评估

## 关联 Skill

- `prd-validator` — 校验 PRD 质量
- `prd-iteration` — 迭代更新 PRD
- `trd-gen` — 从 PRD 生成技术设计文档
- `idea-to-spec` — 先用对话探索想法，再用 prd-gen 正式化
