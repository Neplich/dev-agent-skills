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
| `workspace-management/invitations` | Product feature | Invite a member; accept an invitation | `src/product/workspace_management/invitations.py`, `tests/acceptance/test_product_tasks.py` | collaboration-team |
| `analytics` | Product domain | View the activity dashboard | `src/product/analytics/dashboard.py`, `tests/acceptance/test_product_tasks.py` | insights-team |

The maintainer confirmed one finite Product backfill batch containing both
Product domains and every listed Product task. The candidate tree, pages,
mappings, links, and exclusions in `backfill-confirmation.md` are approved for
writing. Accounts is only the proposed first API module and remains unconfirmed;
Billing remains out of batch. Workspace deletion, exports, and future
role-specific branches also remain out of batch.
