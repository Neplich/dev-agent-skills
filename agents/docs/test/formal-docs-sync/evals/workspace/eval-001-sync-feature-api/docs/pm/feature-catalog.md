---
feature: inherited-api-catalog
version: 1.0.0
date: 2026-07-22
last_updated: 2026-07-22
status: Confirmed
---

# Feature Catalog

| Feature path | Parent | Code paths | Owner | API surface |
| --- | --- | --- | --- | --- |
| `identity` | root | `src/api/identity/**` | identity-team | `/api/identity/*` |
| `identity/sessions` | `identity` | `src/api/identity/sessions/**`, `tests/contract/test_sessions_api.py` | identity-team | `POST /api/identity/sessions`, `DELETE /api/identity/sessions/{session_id}` |
| `billing` | root | `src/api/billing/**`, `tests/contract/test_billing_api.py` | billing-team | `GET /api/billing/invoices` |

Identity owns the Sessions child feature. Billing is a separate top-level domain with a separate owner and lifecycle. Search is stable and outside this batch.
