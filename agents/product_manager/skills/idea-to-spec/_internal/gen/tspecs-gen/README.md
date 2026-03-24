# 测试规格生成器 (tspecs-gen)

## 概述

从 PRD 或 TRD 自动生成结构化测试用例集，包含前置条件、步骤和预期结果。

## 使用场景

- PRD/TRD 就绪后，开发前生成测试用例
- 确保所有需求有对应的测试覆盖
- 创建 QA 交接文档

## 快速开始

```
根据这个 PRD 生成测试用例
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| source_doc | 是 | PRD、TRD 或功能描述 |
| test_level | 否 | Unit / Integration / E2E / All |
| priority_filter | 否 | P0 / P0+P1 / All |
| format | 否 | Table / Gherkin / Both |

## 输出

测试规格文档，包含：测试用例表、覆盖率摘要、需求追溯矩阵

## 关联 Skill

- `prd-gen` / `trd-gen` — 提供输入源文档
- `trace-check` — 验证需求到测试的完整追溯链
