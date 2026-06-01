---
feature: "notifications"
version: "0.1.0"
date: "2026-05-29"
last_updated: "2026-05-29"
---

# Notifications PRD

## Requirement

The active notification list must include only notifications that are actionable
for the user.

## Acceptance Criteria

- Active notifications include `unread` and `read` notifications.
- Active notifications exclude `archived` notifications.
- Archived notifications remain available for archive views, but not for the
  active notification API.
