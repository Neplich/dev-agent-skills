---
title: Workspace Access Data
visibility: internal
doc_type: database
stage: dev
owners:
  - data-team
related_code:
  - src/workspace_access/schema.sql
last_verified_version: v0.9.0
---

# Workspace Access Data

Each workspace can contain duplicate rows for a user. Roles are arbitrary strings and both identifiers have physical foreign keys.
