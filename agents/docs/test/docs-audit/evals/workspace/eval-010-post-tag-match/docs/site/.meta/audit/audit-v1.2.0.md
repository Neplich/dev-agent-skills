# v1.2.0 pre-release documentation audit

- Phase: `pre-tag`
- Attempt: `1`
- Target release version: `v1.2.0`
- Base commit locator: resolve `pre-tag-handoff^{commit}`
- Release candidate commit locator: resolve `release-head^{commit}`
- Audited package tree locator: resolve `refs/release-evidence/v1.2.0^{tree}`
- Changed source: `src/catalog/routes.txt`
- Affected pages: `docs/site/api/catalog-items.md`, `docs/site/api/catalog-status.md`
- Release pages: `docs/site/release-notes/v1.2.0.md`, `docs/site/release-notes/index.md`

The catalog item and status pages were checked against
`src/catalog/routes.txt` and `tests/catalog.txt`. Their version markers, the
Release Notes page and index, `.meta/releases.json`, and `package.json` all
represent release `v1.2.0` (the package uses `1.2.0`).

- Recorded pre-tag result: `ready_for_tag`
- Recorded at: `2026-07-19T10:05:00+08:00`
