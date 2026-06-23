# ADR 生成器 (adr-gen, deprecated)

## 概述

历史 PM 内部生成器，仅保留作兼容参考。新的 ADR 由
`engineer-agent:trd-gen` 在 Engineer 阶段生成。

## 使用场景

- 仅阅读历史规则或 schema 参考
- 新 ADR 请求应 handoff 到 `engineer-agent:trd-gen`

## 快速开始

```
请把 PostgreSQL 选型 ADR 请求移交给 engineer-agent:trd-gen
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
- `engineer-agent:trd-gen` — TRD 中的关键决策可提取为独立 ADR
