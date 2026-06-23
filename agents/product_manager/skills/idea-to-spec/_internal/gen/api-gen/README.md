# API Handoff Stub (api-gen, deprecated)

## 概述

历史 PM 内部生成器已迁移为 handoff stub。新的 API 文档由
`engineer-agent:trd-gen` 在 Engineer 阶段生成，PM 不再写入 `API.md`。

## 使用场景

- legacy 路由仍指向 `api-gen` 时，立即停止 PM 生成
- 将已确认 PM 范围、`feature_path`、接口目标和代码证据移交给
  `engineer-agent:trd-gen`

## 快速开始

```
请基于这些 Express 路由，准备 API 文档 handoff packet 并移交给 engineer-agent:trd-gen
```

## 输入

| 参数 | 必需 | 说明 |
|------|------|------|
| api_source | 是 | 代码文件、口头描述或 OpenAPI spec |
| base_url | 否 | API 基础 URL |
| auth_method | 否 | 认证方式 |
| service_name | 否 | 服务名称 |

## 输出

只输出 handoff packet。目标 Engineer 产物是
`docs/engineer/{feature_path}/API.md`，但本 PM stub 不写文件。

## 关联 Skill

- `engineer-agent:trd-gen` — 生成或更新 Engineer-owned API 文档
- `api-validator` — 校验已生成的 API 文档质量
