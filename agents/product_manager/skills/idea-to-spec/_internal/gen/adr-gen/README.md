# ADR Handoff Stub (adr-gen, deprecated)

## 概述

历史 PM 内部生成器已迁移为 handoff stub。新的 ADR 由
`engineer-agent:trd-gen` 在 Engineer 阶段生成，PM 不再写入 ADR 文件。

## 使用场景

- legacy 路由仍指向 `adr-gen` 时，立即停止 PM 生成
- 将已确认 PM 范围、`feature_path`、决策背景和备选方案移交给
  `engineer-agent:trd-gen`

## 快速开始

```
请把 PostgreSQL 选型 ADR 请求整理成 handoff packet 并移交给 engineer-agent:trd-gen
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| decision_context | 是 | 决策背景和内容 |
| alternatives | 否 | 已知备选方案 |
| constraints | 否 | 约束条件 |
| adr_number | 否 | ADR 编号 |

## 输出

只输出 handoff packet。目标 Engineer 产物是
`docs/engineer/{feature_path}/ADR-<NNN>-<decision-title>.md`，但本 PM stub 不写文件。

## 关联 Skill

- `engineer-agent:trd-gen` — 生成或更新 Engineer-owned ADR
- `adr-validator` — 校验已生成的 ADR 质量
