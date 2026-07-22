# Database Sync Instructions

Load this module only when the confirmed scope contains `doc_type: database`.

## Evidence Checks

Use current schema and data-access evidence to verify, as applicable:

- schema/model authority and owning read/write components;
- tables or entities, fields, types, nullability, defaults, and constraints;
- indexes, unique constraints, physical foreign keys, and logical references;
- query dependencies and actual delete/update behavior;
- migrations needed to establish current shape without turning migration
  history into the current field definition;
- data lifecycle, archive/delete rules, and sensitive-field handling;
- schema, migration, repository, and integration tests.

When no physical foreign key exists, identify the evidenced logical constraint
instead of inventing one. Conflicting runtime/schema/migration evidence blocks
the affected claim.

## Template and Output Rules

Read the database template linked from the host standards entry—normally
`docs/site/standards/templates/database.md`—and consume its single
`docs-scaffold` block for a new page. Do not copy the template into this skill.

Describe only the latest schema state and evidenced ownership, relationships,
fields, indexes, and lifecycle. Use a Mermaid ER diagram only when the evidence
supports the represented relationships. Keep database pages and their
change-map entries in the same confirmed write/read-back scope.

## Information Architecture

Identify the database instance or storage type first, then the schema or
equivalent ownership boundary, data domain, and entity/table leaves. Represent
each non-trivial database/schema and data-domain boundary with a lower
kebab-case directory and `index.md`. Never compress multiple databases,
schemas, or cross-service stores into one generic aggregate page.

Root, database/schema, and data-domain indexes only state scope, ownership,
cross-boundary constraints, relationship summaries, and child navigation.
Give each independently owned or maintained entity/table its own page. A
relationship-dense domain must also contain `relationships.md` (or a confirmed
host-equivalent) with an evidence-backed relationship overview and links to
every represented entity/table page.

Every entity/table page must link back to its data-domain index and, only when
the confirmed subtree contains one, its relationship overview. Every such page
also links its related entity/table pages and each relevant feature/API
authority page; do not treat an entity with fewer direct operations as an
exception. When the confirmed domain exposes both a feature-level API authority
and an entity-specific API authority, every entity page links the feature-level
authority and the affected entity page additionally links its specific API.
The entity-specific link never replaces the feature-level link: enumerate every
entity/table page before writing and verify that each row contains the
data-domain index, relationship overview, related entities/tables, and the
feature-level API authority. Include entities such as invitations even when
they already link their own API page. After writing, read every entity/table
page back and repeat this per-row link check; one complete entity page cannot
stand in for an omitted link on another page.
Record current fields, constraints, indexes, read/write owners,
lifecycle, and code evidence. Separate physical foreign keys from logical
references in both prose and Mermaid labels. When the schema has no physical
foreign key, name the application/store/test evidence for the logical reference
and never draw or describe it as an FK.

Before writing, present the complete database candidate tree. Pair every
database/schema node, domain index, relationship page, and entity/table page
with its parent, code glob, owner, schema/relationship evidence, change-map
delta, and exclusions. After confirmation, update the full navigable subtree,
bidirectional links, navigation, and map entries atomically. Existing stable
paths require a separately confirmed migration plan before movement.

For every affected Database `code_glob`, expand `required_docs` independently
to the complete Database closure: its affected entity/table or compatibility
pages, the Database root, database/schema root, data-domain `index.md`, the
relationship overview, pages whose reciprocal links change, and relevant API
authority pages. Repeat shared roots and indexes in every affected mapping;
never rely on a broader glob or another exact glob to supply the missing
ancestors. In a confirmed Database + Design atomic scope, this applies to every
participating invitation, repository/schema, service, audit, and broad feature
glob, even when a glob such as audit does not query the database directly: its
flow and reciprocal-link delta still carries the complete Database closure.
Verify this checklist once before writing and again during read-back.
