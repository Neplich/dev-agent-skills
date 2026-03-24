# 版本差异比较器 (version-differ)

## 概述

比较同一文档的两个版本，生成按章节分类的结构化 diff 报告。

## 使用场景

- 审查文档两个版本之间的变更
- 为利益相关方准备变更摘要
- 审计文档演进历史

## 快速开始

```
比较 PRD v1.0.0 和 v1.2.0 的差异
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| version_a | 是 | 较早版本 |
| version_b | 是 | 较新版本 |
| focus_sections | 否 | 仅比较指定章节 |

## 关联 Skill

- `prd-iteration` / `brd-iteration` — 迭代后用 version-differ 查看变更
- `change-impactor` — 分析变更的影响范围
