---
feature: workspace-access
feature_path: workspace-access
parent_feature: null
feature_level: 1
version: 1.0.1
date: 2026-07-17
last_updated: 2026-07-23
status: Confirmed
related_prd: docs/pm/workspace-access/PRD.md
related_code:
  - src/workspace_access/schema.sql
  - src/workspace_access/invitations.py
  - src/workspace_access/repository.py
  - src/workspace_access/service.py
  - src/audit/event_writer.py
---

# Workspace Access TRD

The primary database owns `workspaces`, `workspace_memberships`, and `workspace_invitations` in the workspace-access data domain. Memberships and invitations have physical foreign keys to `workspaces` with `ON DELETE CASCADE`. User identity remains owned by the separate identity domain, so `workspace_memberships.user_id` is a logical reference validated by the service rather than a physical foreign key. The service validates user identity before the repository upserts membership; invitation tokens are stored as unique hashes with explicit expiry.

`InvitationService` validates and consumes invitation tokens. It then calls
`MembershipRepository` to upsert `workspace_memberships` and calls the
separately owned `AuditWriter` after persistence. The invitation acceptance
flow crosses the workspace-access and audit-log domains. The database page owns
field and constraint details; the API page owns the HTTP contract. Invitation
records persist the target workspace role, while the accepting user's identity
comes from the authenticated service call rather than the invitation record.

The authorization boundary is fail-closed: only workspace owners and platform
admins may create invitations, and only a valid unexpired token may reach
membership persistence.
Inherited roles and future notification retries remain outside this delivery.
