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
| `analytics` | Product domain | Navigate analytics capabilities | `src/product/analytics/**`, `tests/acceptance/test_product_tasks.py` | insights-team |
| `analytics/view-dashboard` | User task leaf | View the activity dashboard | `src/product/analytics/dashboard.py::view_dashboard`, `tests/acceptance/test_product_tasks.py::test_dashboard_roles_empty_state_and_retry` | insights-team |

The maintainer confirmed one finite Product backfill batch containing the
Analytics domain and its dashboard task. The candidate tree, pages, mapping,
links, and exclusions in `backfill-confirmation.md` are approved for writing.
Accounts, Billing, and Workspace Management remain outside this batch; no API
candidate scope is requested in the current handoff.
