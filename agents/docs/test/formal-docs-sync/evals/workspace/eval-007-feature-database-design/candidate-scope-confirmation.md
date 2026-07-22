# Database and design candidate scope confirmation

The maintainer reviewed and explicitly confirmed this complete write scope before execution:

```text
docs/site/database/index.md
└── primary/index.md
    └── workspace-access/index.md
        ├── relationships.md
        ├── workspaces.md
        ├── workspace-memberships.md
        └── workspace-invitations.md
docs/site/design/workspace-access.md
```

`docs/site/database/workspace-access.md` is an existing verified stable host page. This batch does not include a separately confirmed migration plan, so the page must remain at its current path and its existing change-map coverage must be preserved while the confirmed subtree is added.

| Parent | Page | Code glob | Owner | Schema / relationship evidence | Change-map delta | Exclusions |
| --- | --- | --- | --- | --- | --- | --- |
| `database/` | `primary/index.md` | `src/workspace_access/schema.sql` | data-team | primary SQL schema boundary | add database + primary indexes; preserve stable `database/workspace-access.md` mapping | other databases; stable-page migration |
| `database/primary/` | `workspace-access/index.md` | `src/workspace_access/**` | platform-team | TRD ownership and three related tables | add domain index | identity domain |
| `workspace-access/` | `relationships.md` | `src/workspace_access/**` | platform-team | schema FK plus service logical reference | add relationship overview | unsupported relations |
| `workspace-access/` | `workspaces.md` | `src/workspace_access/schema.sql` | platform-team | `workspaces` DDL | add entity page | identity fields |
| `workspace-access/` | `workspace-memberships.md` | `src/workspace_access/**` | platform-team | membership DDL, repository, service, tests | add entity page | inherited roles |
| `workspace-access/` | `workspace-invitations.md` | `src/workspace_access/**` | platform-team | invitation DDL, repository, service, tests | add entity page | email delivery implementation |
| `design/` | `design/workspace-access.md` | `src/workspace_access/service.py` | platform-team | confirmed closeout and passed tests | update design page | future hierarchy |

`workspace_memberships.workspace_id` and `workspace_invitations.workspace_id` are physical foreign keys to `workspaces.id`. `workspace_memberships.user_id` is a logical cross-domain reference supported by service validation and has no physical foreign key. All new path segments use lower kebab-case. The stable `docs/site/database/workspace-access.md` page and its existing map coverage are explicitly outside the confirmed write scope and must not be deleted, moved, or replaced without a separately confirmed migration plan.
