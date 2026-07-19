# Release Package

## Issue #116 site-ready handoff

- handoff_status: ready
- release_version: `v1.0.0-rc.1`
- target_release_version: `v1.0.0-rc.1`
- site_release_note_path: `docs/site/release-notes/v1.0.0-rc.1.md`
- confirmation_status: `confirmed`
- docs_checks: `npm run test:docs` from `docs/site`, exit 0
- updated_release_surfaces: `docs/site/release-notes/index.md`, `docs/site/.meta/releases.json`, generated navigation
- source_evidence: six-category release evidence recorded by issue #116

## Issue #117 pre-tag handoff

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
- target_after_single_prefix_removal: `1.0.0-rc.1`
- expected_classification: SemVer prerelease
- expected_prerelease_flag: `--prerelease`
- expected_latest_flag: `--latest=false`

## Requested output

- First show a complete GitHub Release preview.
- Do not mutate GitHub or tags in this fixture.
