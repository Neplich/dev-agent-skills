# v1.2.0 pre-release documentation audit

- Phase: `pre-tag`
- Attempt: `2`
- Target release version: `v1.2.0`
- Authority ref: `refs/heads/pre-tag-handoff`
- Authority commit locator: resolve `refs/heads/pre-tag-handoff^{commit}`
- Authority tree locator: resolve `refs/heads/pre-tag-handoff^{tree}`
- Release candidate ref at review time: `release-head`
- Changed source: `src/catalog/routes.txt`
- Affected pages: `docs/site/api/catalog-items.md`, `docs/site/api/catalog-status.md`
- Release pages: `docs/site/release-notes/v1.2.0.md`, `docs/site/release-notes/index.md`
- Immediately superseded attempt: `1`

Attempt 1 covered the same release version but was superseded before tag
creation. Attempt 2 checked the catalog pages against `src/catalog/routes.txt`
and `tests/catalog.txt`, then checked the Release Notes page, index,
`.meta/releases.json`, and `package.json` for v1.2.0 consistency.

- Recorded pre-tag result: `ready_for_tag`
- Recorded at: `2026-07-19T10:05:00+08:00`
