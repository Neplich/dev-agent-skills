---
feature: inherited-product-catalog
version: 1.0.0
date: 2026-07-15
last_updated: 2026-07-22
status: Confirmed
---

# Feature Catalog

| Feature path | Level | User tasks | Code and acceptance evidence | Owner |
| --- | --- | --- | --- | --- |
| `workspace-management` | Product domain | Navigate workspace membership capabilities | `src/product/workspace_management/**`, `tests/acceptance/test_product_tasks.py` | collaboration-team |
| `workspace-management/invitations` | Feature | Invite a member; accept an invitation | `src/product/workspace_management/invitations.py`, `tests/acceptance/test_product_tasks.py` | collaboration-team |
| `analytics` | Product domain | View the activity dashboard | `src/product/analytics/dashboard.py`, `tests/acceptance/test_product_tasks.py` | insights-team |

The maintainer confirmed one finite Product backfill batch containing both
domains and every listed task. The candidate tree, pages, mappings, links, and
exclusions in `backfill-confirmation.md` are approved for writing. Billing,
workspace deletion, exports, and future role-specific branches remain out of
batch.
