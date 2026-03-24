# ADR 生成器 (adr-gen)

## 概述

自动生成标准化的架构决策记录 (Architecture Decision Record)。

## 使用场景

- 做出或需要记录重要技术决策
- 评估不同技术方案的优劣
- 需要为未来参考建立决策历史

## 快速开始

```
帮我写一个 ADR，记录为什么选择 PostgreSQL 而不是 MongoDB
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| decision_context | 是 | 决策背景和内容 |
| alternatives | 否 | 已知备选方案 |
| constraints | 否 | 约束条件 |
| adr_number | 否 | ADR 编号 |

## 输出

标准 ADR 文档，包含：标题、状态、上下文、决策、后果、备选方案对比

## 关联 Skill

- `adr-validator` — 校验 ADR 质量
- `adr-iteration` — 更新 ADR 状态（Proposed → Accepted 等）
- `trd-gen` — TRD 中的关键决策可提取为独立 ADR
