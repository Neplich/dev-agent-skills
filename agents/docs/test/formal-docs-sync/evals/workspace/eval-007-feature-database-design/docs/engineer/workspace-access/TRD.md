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

`workspace_memberships` owns the role assignment. Workspace and user records remain in separately owned stores, so the service validates both identities before the repository upserts the membership. No physical foreign keys are introduced by this feature.
