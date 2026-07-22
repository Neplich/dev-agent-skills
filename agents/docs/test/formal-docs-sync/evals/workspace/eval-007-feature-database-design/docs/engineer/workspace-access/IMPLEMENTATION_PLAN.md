---
feature: workspace-access
feature_path: workspace-access
parent_feature: null
feature_level: 1
version: 1.0.0
date: 2026-07-17
last_updated: 2026-07-17
status: Confirmed
implementation_scope: workspace-membership-delivery
---

# Workspace Access Implementation Plan

Maintainer confirmation: confirmed for implementation and closeout.

| ID | Scope | Status |
| --- | --- | --- |
| SCOPE-01 | Add workspace, membership, and invitation schema with current constraints and indexes | Complete |
| SCOPE-02 | Add physical workspace foreign keys and validate the logical user reference before membership upsert | Complete |
| SCOPE-03 | Add membership and invitation repository/service paths and tests | Complete |

## Required Tests

- `test_workspace_domain_schema_constraints`
- `test_assign_role_validates_logical_user_reference`
- `test_invitation_requires_existing_workspace`

## Closeout

All scope is complete. `.eval/actual-diff.patch` covers every related code path and `.eval/test-results.md` records all required tests as passed. No TODO, deferred item, stub, or residual in-scope work remains.
