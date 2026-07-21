---
feature: dependency-inventory
feature_path: dependency-inventory
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-21
last_updated: 2026-07-21
---

# 依赖维护状态审计

## 当前状态

服务仍依赖早期引入的网络请求与 UUID 工具。`package.json` 是已确认的生产依赖版本来源。

## 目标

- 识别已废弃、停止维护或明显过时的直接依赖。
- 说明缺少安全维护对运行时的影响。
- 给出受支持的替代包或平台内建能力迁移建议。

## 范围

- 审查 `package.json` 中的直接生产依赖。
- 区分废弃状态、已知漏洞和普通版本落后。
- 安全审查仅输出替换计划，不实施迁移。

## 验收期望

- 每项结论引用具体依赖与版本。
- 废弃依赖说明维护状态与暴露面。
- 建议包含替代方向和迁移优先级。
