# Confirmed Product backfill batch

- Mode: `existing-system backfill`
- Product tree:
  - `product/index.md`
    - `analytics/index.md`
      - `view-dashboard.md`
- Owner: `insights-team`.
- Reader task: view dashboard activity and recover from an empty or failed load.
- Evidence: confirmed feature catalog, current implementation, and acceptance tests.
- Mapping:
  - `src/product/analytics/**` -> `product/index.md`, `analytics/index.md`, and `view-dashboard.md`.
- Links: the task is reachable from `product/index.md` through `analytics/index.md`;
  the task page links its parent and relevant authority indexes without copying contracts.
- Exclusions: workspace management, billing, exports, future behavior, and all non-Product writes.
- Stable paths: no Product leaf path exists yet, so no migration or redirect is required.
- Confirmation: the maintainer confirms this three-page tree, mapping, links, navigation, and exclusions as one finite batch.
