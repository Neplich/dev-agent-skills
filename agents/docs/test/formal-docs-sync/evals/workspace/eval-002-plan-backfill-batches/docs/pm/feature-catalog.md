---
feature: inherited-api-catalog
version: 1.0.0
date: 2026-07-15
last_updated: 2026-07-15
status: Confirmed
---

# Feature Catalog

| Feature | Code paths | Owner | API surface |
| --- | --- | --- | --- |
| Accounts | `src/api/accounts/routes.py`, `src/api/accounts/schemas.py`, `tests/contract/test_accounts_api.py` | identity-team | `/api/accounts/{account_id}` |
| Billing | `src/api/billing/routes.py` | billing-team | `/api/billing/invoices` |

The maintainer requested that backfill default to one catalog module per review batch. Accounts is the proposed first module; Billing remains out of batch.
