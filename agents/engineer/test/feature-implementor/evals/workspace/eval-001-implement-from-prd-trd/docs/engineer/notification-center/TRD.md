---
feature: notification-center
feature_path: notification-center
parent_feature: null
feature_level: 1
status: Confirmed
related_prd: docs/pm/notification-center/PRD.md
---

# Notification Center TRD

## Components

- `src/api/notifications.ts` reads the signed-in user's notification records.
- `src/components/notification-center.tsx` renders list and empty states.
- `tests/notifications.test.ts` covers ordering, read state, and empty results.

## Implementation constraints

- Reuse the existing session and data-access layers.
- Do not introduce a new queue or external delivery provider.
- Keep read-state updates scoped to the selected notification.

## Verification

Run the notification unit tests and the existing component test suite.
