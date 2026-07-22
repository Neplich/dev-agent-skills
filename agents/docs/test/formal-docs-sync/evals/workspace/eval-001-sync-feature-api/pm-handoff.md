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
  - `backfill-request.md` (Maintainer request; candidate batch not confirmed)
- scope_decision: Perform bounded discovery for a first finite API backfill batch bounded to the Identity / Sessions catalog branch and present its candidate pages and mappings for confirmation; Billing, existing Search API, and all non-API sections remain out of batch.
- downstream_owner: `Docs`
- required_output: Propose one evidence-backed nested API subtree and exact change-map entries, then wait for maintainer confirmation with zero site writes.
- exclusions: Billing, `src/api/internal/**`, `docs/site/api/search.md`, database, design, ops, product, and release documentation.
- blockers_risks: Do not move the stable Search API page; preserve unknown change-map fields.

The maintainer explicitly requested existing-system API backfill and confirmed the host repository. This handoff authorizes bounded discovery only; it does not confirm any candidate tree or write scope.
