---
feature: ai-search
feature_path: ai-search
parent_feature: N/A
feature_level: 1
status: Approved
---

# AI 搜索 PRD 摘要

- 用户可以通过非空 `q` 查询词搜索知识条目。
- 最大返回数量为 20；本版本不包含写入、删除或管理能力。
- 预期接口为 `GET /api/search`，非法空查询返回 400。
