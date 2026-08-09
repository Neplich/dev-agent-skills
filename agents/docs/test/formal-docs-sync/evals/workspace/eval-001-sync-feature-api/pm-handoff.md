# Confirmed existing-system backfill handoff

- request_type: `formal_docs`
- change_tier: `major`
- feature_path: `documentation/api-backfill`
- feature: `formal-docs-information-architecture`
- parent_feature: `documentation`
- feature_level: `2`
- feature_path_evidence:
  - source: `docs/pm/feature-catalog.md`
    reason: The confirmed catalog records the API feature tree, owners, routes, and evidence paths.
- source_documents:
  - `docs/pm/feature-catalog.md` (Confirmed)
  - `backfill-request.md` (Maintainer request; candidate batch not confirmed)
- scope_decision: The maintainer is considering the Identity / Sessions catalog branch for the first API backfill batch. Candidate pages, hierarchy, mappings, and navigation changes have not been confirmed. Billing, the existing Search API page, and non-API sections are not part of this request.
- downstream_owner: `Docs`
- required_output: An evidence-backed proposal for a finite first API backfill batch that the maintainer can review.
- exclusions: Billing, `src/api/internal/**`, `docs/site/api/search.md`, database, design, ops, product, and release documentation.
- blockers_risks: `docs/site/api/search.md` is an existing stable page, and the current change map contains additional fields owned by the manual-plugin entry; accidental path or mapping churn could affect existing navigation.

The maintainer requested analysis of a first existing-system API backfill batch and confirmed the host repository. No candidate page set or write scope has been approved.
