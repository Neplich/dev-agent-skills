# API 文档生成器 (api-gen)

## 概述

从代码、路由定义或口头描述自动生成结构化 API 文档。

## 使用场景

- 为已有 API 补充文档
- 设计新 API 时生成规范文档
- 将非正式 API 笔记转为标准文档

## 快速开始

```
帮我为这些 Express 路由生成 API 文档
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| api_source | 是 | 代码文件、口头描述或 OpenAPI spec |
| base_url | 否 | API 基础 URL |
| auth_method | 否 | 认证方式 |
| service_name | 否 | 服务名称 |

## 输出

结构化 API 文档，包含：概述、认证、端点详情、数据模型、错误码、curl 示例

## 关联 Skill

- `api-validator` — 校验 API 文档质量
- `trd-gen` — 完整技术设计中包含 API 章节
