---
feature: ai-search
feature_path: ai-search
parent_feature: N/A
feature_level: 1
status: Confirmed
---

# AI 搜索 TRD 摘要

- 路由：`GET /api/search`
- Query：`q` 为必填非空字符串，`limit` 为 1–20 的可选整数，默认 10。
- 响应：`200 { items: SearchItem[] }`；非法输入返回 `400 { error: string }`。
- related_code：`src/search/**`、`tests/search-api.test.ts`。
