# TRD 生成器 (trd-gen)

## 概述

从 PRD 或技术描述自动生成标准化的技术需求文档 (Technical Requirements Document)。

## 使用场景

- 将产品需求转化为技术设计方案
- 记录架构决策、数据模型和 API 合约
- 需要在开发前建立技术蓝图

## 快速开始

```
帮我生成一个 TRD，基于这个 PRD 来设计支付微服务的技术方案
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| technical_context | 是 | 技术上下文（PRD、功能描述等） |
| tech_stack | 否 | 偏好的技术栈 |
| constraints | 否 | 性能指标、基础设施约束 |
| existing_architecture | 否 | 现有系统架构 |

## 输出

标准化 TRD 文档（Markdown），包含：
- 架构概览（含 Mermaid 图）、技术选型
- 数据模型（含 ER 图）、API 设计
- 系统交互序列图、量化 NFR 指标
- 安全设计、部署架构、测试策略

## 关联 Skill

- `trd-validator` — 校验 TRD 质量
- `prd-gen` — 先生成 PRD，再用 trd-gen 做技术设计
- `adr-gen` — 记录 TRD 中的关键技术决策
- `tspecs-gen` — 从 TRD 生成测试用例
