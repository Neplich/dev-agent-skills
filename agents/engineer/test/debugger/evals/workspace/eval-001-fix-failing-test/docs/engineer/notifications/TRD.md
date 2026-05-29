---
feature: "notifications"
version: "0.1.0"
date: "2026-05-29"
last_updated: "2026-05-29"
---

# Notifications TRD

## Component Boundary

`src/api/notifications.ts` owns notification list filtering for this fixture.

## Expected Behavior

`listActiveNotifications` returns notifications whose status is `unread` or
`read`. It must exclude notifications whose status is `archived`.

## Verification

Run:

```bash
npm test -- test/api/notifications.test.ts
```
