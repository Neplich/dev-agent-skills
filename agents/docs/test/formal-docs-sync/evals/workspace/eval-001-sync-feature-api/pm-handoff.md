# Confirmed existing-system backfill handoff

- request_type: `formal_docs`
- change_tier: `major`
- feature_path: `agents/docs-agent/formal-docs-information-architecture`
- feature: `formal-docs-information-architecture`
- parent_feature: `agents/docs-agent`
- feature_level: `2`
- feature_path_evidence:
  - source: `docs/pm/feature-catalog.md`
    reason: The confirmed catalog records the API feature tree, owners, routes, and evidence paths.
- source_documents:
  - `docs/pm/feature-catalog.md` (Confirmed)
  - `backfill-confirmation.md` (Maintainer confirmed)
- scope_decision: Backfill one finite API batch containing the Identity / Sessions and Billing subtrees; existing Search API and all non-API sections remain out of batch.
- downstream_owner: `Docs`
- required_output: Create the confirmed nested API subtree, exact change-map entries, recursive navigation, host-check evidence, and a docs-audit handoff.
- exclusions: `src/api/internal/**`, `docs/site/api/search.md`, database, design, ops, product, and release documentation.
- blockers_risks: Do not move the stable Search API page; preserve unknown change-map fields.

The maintainer explicitly requested existing-system API backfill, confirmed the host repository, and approved the finite candidate tree recorded in `backfill-confirmation.md`.
