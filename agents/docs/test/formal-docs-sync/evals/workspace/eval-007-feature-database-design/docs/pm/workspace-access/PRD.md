---
feature: workspace-access
feature_path: workspace-access
parent_feature: null
feature_level: 1
version: 1.0.0
date: 2026-07-17
last_updated: 2026-07-17
status: Approved
---

# Workspace Access PRD

Workspace owners can assign an existing user one explicit role: owner, editor, or viewer.

## Acceptance Criteria

- A workspace-user pair has at most one current membership.
- Missing workspaces or users are rejected before persistence.
- Inherited roles are outside this delivery.
