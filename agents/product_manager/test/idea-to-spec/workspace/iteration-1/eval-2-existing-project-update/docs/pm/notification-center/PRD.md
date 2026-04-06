---
title: "Notification Center PRD"
type: PRD
version: "1.2.0"
status: Approved
author: "Eval Fixture"
date: "2026-04-06"
generated_by: "fixture"
related_docs:
  - "docs/engineer/notification-center/TRD.md"
  - "docs/pm/notification-center/DECISIONS.md"
changelog:
  - version: "1.2.0"
    date: "2026-04-06"
    changes: "Approved notification center baseline"
---

# Goals

- Deliver in-app notifications for mentions and assignments
- Support unread state and list browsing

## Current Delivery Model

- Notifications are currently fetched via polling
- The next phase moves toward event-driven delivery with polling retained as fallback during migration

## Rollout Direction

- Introduce event-driven delivery incrementally
- Keep polling fallback until delivery reliability is validated
- Update PM and engineer docs in lockstep for rollout consistency
