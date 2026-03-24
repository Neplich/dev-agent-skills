# 迭代协调器 (iteration-coordinator)

## 概述

当变更影响多个文档时，协调跨文档的迭代更新，确保文档间一致性。

## 使用场景

- 一个变更影响多个文档（如范围变更影响 BRD、PRD、TRD）
- `change-impactor` 识别出多个需要更新的文档后
- 需要确保所有项目文档在变更后保持同步

## 快速开始

```
我们要从 session 认证迁移到 JWT，帮我更新所有相关文档
```

## 工作流程

1. 运行 `change-impactor` 评估影响
2. 按依赖顺序排列文档（上游优先）
3. 逐个运行迭代 skill + 校验
4. 最终运行 `trace-check` 检查一致性

## 关联 Skill

- `change-impactor` — 影响分析（第一步）
- `prd-iteration` / `brd-iteration` / `adr-iteration` — 各文档迭代
- `trace-check` — 最终一致性检查
- `flow` — 生成类工作流（iteration-coordinator 是迭代类工作流）
