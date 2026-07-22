---
feature: workspace-access
feature_path: workspace-access
parent_feature: null
feature_level: 1
version: 1.0.0
date: 2026-07-17
last_updated: 2026-07-17
status: Confirmed
related_prd: docs/pm/workspace-access/PRD.md
related_code:
  - src/workspace_access/schema.sql
  - src/workspace_access/repository.py
  - src/workspace_access/service.py
---

# Workspace Access TRD

The primary database owns `workspaces`, `workspace_memberships`, and `workspace_invitations` in the workspace-access data domain. Memberships and invitations have physical foreign keys to `workspaces` with `ON DELETE CASCADE`. User identity remains owned by the separate identity domain, so `workspace_memberships.user_id` is a logical reference validated by the service rather than a physical foreign key. The service validates user identity before the repository upserts membership; invitation tokens are stored as unique hashes with explicit expiry.
