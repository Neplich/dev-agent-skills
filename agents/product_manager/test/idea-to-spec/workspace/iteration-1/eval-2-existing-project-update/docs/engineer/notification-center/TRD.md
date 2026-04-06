---
title: "Notification Center TRD"
type: TRD
version: "1.1.0"
status: Approved
author: "Eval Fixture"
date: "2026-04-06"
generated_by: "fixture"
related_docs:
  - "docs/pm/notification-center/PRD.md"
  - "docs/pm/notification-center/DECISIONS.md"
changelog:
  - version: "1.1.0"
    date: "2026-04-06"
    changes: "Approved technical baseline"
---

# Architecture

The current implementation polls `/notifications` every 30 seconds.
The next iteration introduces an event-driven delivery path while preserving polling as migration fallback.

## Constraints

- Auth service is session based
- Delivery path is tied to current notification storage table

## Update Impact

- Event production and delivery contracts need to be introduced
- Rollout must preserve fallback behavior while event reliability is verified
