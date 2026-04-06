---
title: "App Tags Feature Design"
type: PRD
version: "0.1.0"
status: Draft
author: "Eval Runner"
date: "2026-04-06"
generated_by: "idea-to-spec-eval"
related_docs:
  - "docs/pm/app-tags/DECISIONS.md"
  - "docs/engineer/apps-catalog/TRD.md"
changelog:
  - version: "0.1.0"
    date: "2026-04-06"
    changes: "Working PM draft from eval run"
---

# Scope And Goals

Add app-level tagging so administrators can classify apps and end users can
discover apps by tag in the frontend catalog.

## Goals

- Allow admins to create and assign tags during app editing
- Surface tags on app cards in the frontend catalog
- Support app discovery through explicit tag filtering

## Non-Goals

- Global tag analytics dashboard
- Tag-driven recommendation engine
- Third-party-config-driven tags

# Data Model Direction

The preferred v1 design introduces a managed tag model:

- `app_tags`
- `app_tag_bindings`

This supports rename, deletion, filter stability, and shared taxonomy
management.

# Interaction Direction

## Admin

- App create/edit uses searchable multi-select plus inline new tag creation
- Tag deletion with existing bindings requires a confirmation modal listing
  impacted apps

## Frontend

- App cards display tag chips
- Users can filter by tag and combine tag filtering with keyword search

# Remaining Work

- Confirm phase split for admin tag management page
- Confirm search semantics between keyword-only and keyword-plus-tag filter
- Expand this working draft into `PRD.md` after all sections are confirmed
