# Equivalent confirmed release audit entry

- audit_scope: formal documentation frontmatter contract fixtures
- pending_release_version: `v0.4.0`
- base: `4a1b2c3`
- target: `7c9e2af`
- diff_semantics: two-dot endpoint diff
- requested_action: run docs-audit, classify the complete affected page set, and return a release recommendation without repairing the fixture
- evidence_inventory:
  - `docs/site/standards/change-map.yaml`
  - `docs/site/api/*.md`
  - `src/catalog/routes.txt`

The maintainer confirms this bounded base/target pair, pending-release context,
audit request, and evidence inventory as the equivalent entry basis for the
fixture audit.
