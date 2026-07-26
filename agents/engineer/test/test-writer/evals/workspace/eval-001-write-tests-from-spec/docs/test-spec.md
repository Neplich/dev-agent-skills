---
feature: notifications
feature_path: notifications
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-26
last_updated: 2026-07-26
---

# NotificationService Test Spec

Status: Approved

## Test Basis

`NotificationService.create` accepts `{ recipientId, message }` and uses the injected repository.

## Required Scenarios

1. Valid input creates one notification and returns the stored record.
2. Missing `recipientId` throws `recipientId is required` without calling the repository.
3. Blank `message` throws `message is required` without calling the repository.
4. A repository error is propagated unchanged to the caller.

Use the existing `node:test` and `node:assert/strict` structure shown under `test/services/`.
