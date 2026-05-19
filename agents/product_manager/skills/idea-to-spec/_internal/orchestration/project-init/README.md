# 项目初始化 (project-init)

## 概述

为新项目生成标准化的文档目录结构和文档骨架。

## 使用场景

- 新项目启动，需要文档骨架
- 为现有项目设置标准化文档结构
- 引导项目进入文档管理工作流

## 快速开始

```
初始化项目文档，项目名 smart-checkout，类型是 Web 应用
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| project_name | 是 | 项目名称 |
| project_type | 否 | webapp / mobile / api / library / data-pipeline |
| description | 否 | 项目简述 |
| team | 否 | 团队成员和角色 |

## 关联 Skill

- `brd-gen` / `prd-gen` — 填充 PM 文档骨架
- `engineer-agent:trd-gen` — PRD 确认后编写 Engineer TRD
- `flow` — 定义完整工作流
