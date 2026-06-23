# ADR Iteration Handoff (adr-iteration, deprecated)

## 概述

ADR 由 Engineer 拥有。本 PM 资源只准备 handoff packet，不直接更新 ADR
状态或内容。

## 使用场景

- legacy 路由仍指向 `adr-iteration`
- ADR 评审、废弃、替代或内容更新需要 Engineer-owned 修订

## 快速开始

```
把 ADR-001 的状态变更请求整理成 handoff packet 并移交给 engineer-agent:trd-gen
```

## 状态流转

Proposed → Accepted → Deprecated / Superseded

## 关联 Skill

- `engineer-agent:trd-gen` — 生成或更新 Engineer-owned ADR
- `adr-validator` — 校验 ADR 质量
