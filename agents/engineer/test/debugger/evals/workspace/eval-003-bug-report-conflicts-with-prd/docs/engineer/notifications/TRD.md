---
type: TRD
feature: notifications
feature_path: notifications
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-26
last_updated: 2026-07-26
related_prd: docs/pm/notifications/PRD.md
---

# 通知列表过滤

active 查询条件为 `status IN ('active', 'read')`，archive 查询条件为 `status = 'archived'`。该技术行为与 PRD 一致。
两个查询在仓储层独立构造，不会把 archive 结果合并进 active 响应。
