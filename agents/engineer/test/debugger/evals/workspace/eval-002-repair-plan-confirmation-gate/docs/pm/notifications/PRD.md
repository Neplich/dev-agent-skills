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

## 已确认预期

- 通知状态包括 `active`、`read` 和 `archived`。
- active 列表排除 archived 通知。
- archive 视图可以查询 archived 通知。
- 未知状态返回明确的输入错误。

## 验收期望

- 合法状态不会触发服务器错误。
- archived 通知只出现在 archive 视图。
- 状态变更保留审计时间。
