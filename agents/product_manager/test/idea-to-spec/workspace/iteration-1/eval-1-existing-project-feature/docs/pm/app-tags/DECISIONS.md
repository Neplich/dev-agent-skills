---
title: "App Tags Decisions"
type: DECISIONS
version: "1.0.0"
status: Draft
author: "Eval Runner"
date: "2026-04-06"
generated_by: "idea-to-spec-eval"
related_docs:
  - "docs/pm/app-tags/design.md"
  - "docs/engineer/apps-catalog/TRD.md"
changelog:
  - version: "1.0.0"
    date: "2026-04-06"
    changes: "Initial eval decision log"
---

# Confirmed Decisions

- App tags are a Portal-owned concept, not part of third-party app config
- The initial design uses a managed tag model with `app_tags` and `app_tag_bindings`
- Tag labels are unique on `normalized_name`, not raw case-sensitive text

# Open Questions

- Should admin list pages support tag filtering in phase 1 or phase 2
- How many visible tags should appear on app cards before collapsing to `+N`

# Assumptions

- The existing admin modal can absorb one more editable field group without redesign
- Frontend search will continue to combine keyword search with tag-based filtering

# Rejected Options

- Storing tags only as `string[]` directly on app records
- Storing tags inside third-party integration config
