---
feature: notifications
feature_path: notifications
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-26
last_updated: 2026-07-26
---

# 通知中心

## 已确认列表规则

- active 列表只显示 `active` 和 `read` 通知。
- `archived` 通知从 active 列表排除，只能在 archive 视图查看。
- 把 archived 加入 active 属于产品预期变更，不是现有实现缺陷。

## 验收期望

- active 查询永远排除 archived。
- archive 查询只返回 archived。
