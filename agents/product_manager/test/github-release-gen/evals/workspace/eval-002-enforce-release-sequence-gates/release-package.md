# Release Package

## `docs-agent:release-notes-gen` site-ready handoff

- handoff_status: ready
- release_version: `v1.0.0-rc.1`
- target_release_version: `v1.0.0-rc.1`
- site_release_note_path: `docs/site/release-notes/v1.0.0-rc.1.md`
- confirmation_status: `confirmed`
- docs_checks: `npm run test:docs` from `docs/site`, exit 0
- updated_release_surfaces: `docs/site/release-notes/index.md`, `docs/site/.meta/releases.json`, generated navigation
- source_evidence: six-category release evidence recorded by `docs-agent:release-notes-gen`

## `docs-agent:docs-audit` pre-tag handoff

- phase: `pre-tag`
- phase_result: `ready_for_tag`
- release_version: `v1.0.0-rc.1`
- base_ref: `v0.9.0`
- target_ref: `8b6a1f2`
- docs_audit_blockers: none
- target_tag_status: absent

## Latest Release evidence

- repository_standard_tag_prefix: `v`
- current_latest_release: `v0.9.0`
- current_latest_url: https://github.com/example/ai-hub/releases/tag/v0.9.0

## Requested output

- First show a complete GitHub Release preview.
- This package is approved for preview review only; no GitHub publish or tag operation has been authorized.
