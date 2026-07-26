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

若产品希望 active 包含 archived，必须先由 `pm-agent:idea-to-spec` 的 existing-project-update 路径更新 PRD 或产品决策，再同步本 TRD，并由 `feature-implementor` 形成确认的 `IMPLEMENTATION_PLAN.md`。
