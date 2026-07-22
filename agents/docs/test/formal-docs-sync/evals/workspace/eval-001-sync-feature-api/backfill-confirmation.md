# API backfill candidate scope confirmation

The maintainer reviewed and explicitly confirmed this complete finite subtree before writing:

```text
docs/site/api/index.md
├── identity/index.md
│   └── sessions/index.md
│       ├── create-session.md
│       └── revoke-session.md
└── billing/index.md
    └── list-invoices.md
```

| Parent | Page | Code glob | Owner | Classification / route evidence | Change-map delta | Exclusions |
| --- | --- | --- | --- | --- | --- | --- |
| `api/` | `api/identity/index.md` | `src/api/identity/sessions/**` | identity-team | catalog Identity domain; `/api/identity` prefix | add root and Identity index | `src/api/internal/**` |
| `api/identity/` | `api/identity/sessions/index.md` | `src/api/identity/sessions/**` | identity-team | catalog Sessions child; `/sessions` route group | add Sessions index | other identity features |
| `api/identity/sessions/` | `create-session.md` | `src/api/identity/sessions/**` | identity-team | `POST /api/identity/sessions` plus schema/test | add leaf | revoke-only evidence |
| `api/identity/sessions/` | `revoke-session.md` | `src/api/identity/sessions/**` | identity-team | `DELETE /api/identity/sessions/{session_id}` plus test | add leaf | create-only evidence |
| `api/` | `api/billing/index.md` | `src/api/billing/**` | billing-team | catalog Billing domain; `/api/billing` prefix | add root and Billing index | payment-provider internals |
| `api/billing/` | `list-invoices.md` | `src/api/billing/**` | billing-team | `GET /api/billing/invoices` plus schema/test | add leaf | write routes |

`docs/site/api/search.md` is a stable unrelated page and remains in place. Database, design, ops, product, release, and internal API surfaces are out of batch. All new path segments are lower kebab-case.

The confirmed API subtree is `visibility: both`; every nested page must appear in both public and internal recursive navigation.
