---
feature: notifications
feature_path: notifications
parent_feature: null
feature_level: 1
status: Confirmed
related_prd: docs/pm/notifications/PRD.md
---

# Notifications List TRD

## Current implementation

`src/api/notifications.ts` builds the active-list query. The current filter
omits the archived-state exclusion.

## Required correction

Add the archived-state exclusion without changing pagination or read-state
handling.

## Verification

Run the notification API tests covering active, read, and archived records.
