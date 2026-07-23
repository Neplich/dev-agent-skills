---
feature: workspace-access
feature_path: workspace-access
parent_feature: null
feature_level: 1
version: 1.0.1
date: 2026-07-17
last_updated: 2026-07-23
status: Approved
---

# Workspace Access PRD

Workspace owners can assign an existing user one explicit role—owner, editor, or viewer. Workspace owners and platform admins can create an expiring invitation for one of those roles. A valid invitation activates that role for the authenticated accepting user, and every accepted invitation emits an audit event.

## Acceptance Criteria

- A workspace-user pair has at most one current membership.
- Missing workspaces or users are rejected before persistence.
- Each invitation belongs to an existing workspace, has a unique token hash, and expires at a recorded time.
- Only a workspace owner or platform admin can create an invitation.
- Expired invitations are rejected before membership persistence.
- Acceptance writes the membership before emitting its audit event.
- Inherited roles are outside this delivery.
