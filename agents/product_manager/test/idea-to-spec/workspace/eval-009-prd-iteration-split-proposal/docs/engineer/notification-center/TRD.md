---
title: "notification-center — Technical Requirements Document"
type: TRD
feature: "notification-center"
feature_path: "notification-center"
parent_feature: "N/A"
feature_level: "1"
version: "1.1.0"
status: Confirmed
author: "Notification Engineering Team"
date: "2026-07-21"
last_updated: "2026-07-28"
---

# TRD: Notification Center

## Architecture

Polling-based delivery worker with a notification store, subscription service,
and channel gateway.

## Constraints

- Polling worker interval configurable per priority class.
- Channel gateway isolates email, in-app, and webhook adapters.
