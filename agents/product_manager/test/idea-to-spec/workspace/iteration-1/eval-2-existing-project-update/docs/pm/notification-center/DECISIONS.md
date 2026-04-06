---
title: "Notification Center Decisions"
type: DECISIONS
version: "1.0.0"
status: Approved
author: "Eval Fixture"
date: "2026-04-06"
generated_by: "fixture"
related_docs:
  - "docs/pm/notification-center/PRD.md"
  - "docs/engineer/notification-center/TRD.md"
changelog:
  - version: "1.0.0"
    date: "2026-04-06"
    changes: "Initial fixture"
---

# Confirmed Decisions

- Use a hybrid transition where event-driven delivery becomes primary and polling remains fallback during migration

# Open Questions

- Retention period for notification records

# Assumptions

- Current auth model remains unchanged

# Rejected Options

- Full email notification parity in v1
- Permanent polling-only delivery for the next phase
