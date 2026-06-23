# API 文档生成器 (api-gen, deprecated)

## 概述

历史 PM 内部生成器，仅保留作兼容参考。新的 API 文档由
`engineer-agent:trd-gen` 在 Engineer 阶段生成。

## 使用场景

- 仅阅读历史规则或 schema 参考
- 新 API 文档请求应 handoff 到 `engineer-agent:trd-gen`

## 快速开始

```
请基于这些 Express 路由，把 API 文档生成请求移交给 engineer-agent:trd-gen
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
- `engineer-agent:trd-gen` — 完整技术设计中包含 API 章节
