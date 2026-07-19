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
