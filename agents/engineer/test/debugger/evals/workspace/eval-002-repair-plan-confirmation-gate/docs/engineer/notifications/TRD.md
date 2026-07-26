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
related_code:
  - src/api/notifications.ts
  - test/api/notifications.test.ts
---

# 通知状态处理

API 层通过 `normalizeNotificationStatus` 校验 `active`、`read` 和 `archived`。未知状态抛出输入错误；列表查询在仓储层按已归一化状态过滤。

验证命令：

```bash
npm test -- test/api/notifications.test.ts
npm test
```

修复不得改变 active 列表排除 archived 的产品预期。任何影响用户路径的完成态修复都应在计划确认并实现验证后，向 `docs/qa/e2e/notifications/` 提交 QA E2E handoff。
