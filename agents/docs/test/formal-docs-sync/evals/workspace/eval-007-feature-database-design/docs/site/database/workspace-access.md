---
title: Workspace Access Data
visibility: internal
doc_type: database
stage: dev
owners:
  - data-team
related_code:
  - src/workspace_access/schema.sql
last_verified_version: unverified
---

# Workspace Access Data

Each workspace membership is unique by `(workspace_id, user_id)`, and its role
is limited to `owner`, `editor`, or `viewer`. `workspace_id` is a physical
foreign key with cascading deletion; `user_id` is a service-validated logical
reference to the user domain.

Workspace invitations belong to a workspace through a physical foreign key,
use a unique token hash, and record an expiration time.
