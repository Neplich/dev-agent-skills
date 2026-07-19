# Equivalent confirmed release audit entry

- audit_scope: formal documentation frontmatter contract fixtures
- audit_phase: `pre-tag`
- target_release_version: `v0.4.0`
- target_release_version_confirmation: maintainer-confirmed
- base_ref: `4a1b2c3`
- target_ref: `7c9e2af`
- diff_semantics: two-dot endpoint diff
- requested_action: run docs-audit, classify the complete affected page set, and return a release recommendation without repairing the fixture
- evidence_inventory:
  - `docs/site/standards/change-map.yaml`
  - `docs/site/api/*.md`
  - `src/catalog/routes.txt`

The maintainer explicitly confirms `target_release_version: v0.4.0`, this
bounded base/target pair, the pre-tag audit request, and the evidence inventory
as the equivalent entry basis for the fixture audit. The version was not
inferred from either ref or a branch name.
