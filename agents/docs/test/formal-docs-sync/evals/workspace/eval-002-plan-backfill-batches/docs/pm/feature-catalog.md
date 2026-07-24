---
feature: inherited-api-product-catalog
version: 1.0.0
date: 2026-07-15
last_updated: 2026-07-22
status: Confirmed
---

# Feature Catalog

| Feature path | Level | User task / API surface | Code and acceptance evidence | Owner |
| --- | --- | --- | --- | --- |
| `accounts` | API domain | `GET /api/accounts/{account_id}` | `src/api/accounts/routes.py`, `src/api/accounts/schemas.py`, `tests/contract/test_accounts_api.py` | identity-team |
| `billing` | API domain | `GET /api/billing/invoices` | `src/api/billing/routes.py` | billing-team |
| `workspace-management` | Product domain | Navigate workspace membership capabilities | `src/product/workspace_management/**`, `tests/acceptance/test_product_tasks.py` | collaboration-team |
| `workspace-management/invitations` | Level 1 subfeature | Navigate invitation capabilities | `src/product/workspace_management/invitations/**`, `tests/acceptance/test_product_tasks.py` | collaboration-team |
| `workspace-management/invitations/member-invitations` | Level 2 subfeature | Create and manage pending member invitations | `src/product/workspace_management/invitations/member_invitations.py`, `tests/acceptance/test_product_tasks.py` | collaboration-team |
| `workspace-management/invitations/member-invitations/invite-member` | User task leaf | Invite a member | `src/product/workspace_management/invitations/member_invitations.py::invite_member`, `tests/acceptance/test_product_tasks.py::test_invitation_tasks_expose_limits_feedback_and_recovery` | collaboration-team |
| `workspace-management/invitations/member-invitations/manage-pending-invitation` | User task leaf | Resend or revoke a pending invitation | `src/product/workspace_management/invitations/member_invitations.py::manage_pending_invitation`, `tests/acceptance/test_product_tasks.py::test_pending_invitation_management_supports_resend_revoke_and_recovery` | collaboration-team |
| `workspace-management/invitations/invitation-acceptance` | Level 2 subfeature | Accept an invitation and recover from invalid or expired links | `src/product/workspace_management/invitations/invitation_acceptance.py`, `tests/acceptance/test_product_tasks.py` | collaboration-team |
| `workspace-management/invitations/invitation-acceptance/accept-invitation` | User task leaf | Accept a valid invitation or recover from invalid / expired feedback | `src/product/workspace_management/invitations/invitation_acceptance.py::accept_invitation`, `tests/acceptance/test_product_tasks.py::test_invitation_tasks_expose_limits_feedback_and_recovery` | collaboration-team |
| `analytics` | Product domain | Navigate analytics capabilities | `src/product/analytics/**`, `tests/acceptance/test_product_tasks.py` | insights-team |
| `analytics/view-dashboard` | User task leaf | View the activity dashboard | `src/product/analytics/dashboard.py::view_dashboard`, `tests/acceptance/test_product_tasks.py::test_dashboard_roles_empty_state_and_retry` | insights-team |

The maintainer confirmed one finite Product backfill batch containing both
Product domains and every listed Product task. Workspace Management contains a
confirmed Level 1 `invitations` feature, two Level 2 child features, and three
task leaves; Analytics intentionally remains shallow. The candidate tree,
pages, mappings, links, and exclusions in `backfill-confirmation.md` are
approved for writing. Accounts is only the proposed first API module and
remains unconfirmed; Billing remains out of batch. Workspace deletion, exports,
and future role-specific branches also remain out of batch.
