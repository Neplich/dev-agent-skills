# Pre-tag release context

- audit_phase: `pre-tag`
- base_ref: `v1.1.0`
- target_ref: `release-head`
- target_ref_commit: `2222222`
- expected_post_stamp_commit: `3333333` (ordinary commit on the host release PR branch)
- expected_post_stamp_tree: `4444444444444444444444444444444444444444`
- expected_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- expected_record_blob_hash: persisted by the trusted pre-tag handoff after commit creation
- diff_semantics: two-dot endpoint diff
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`
- unified_stamp_set:
  - `docs/site/api/catalog-items.md` (pre-stamp `v1.1.0`)
  - `docs/site/api/catalog-status.md` (pre-stamp `unverified`)
  - `docs/site/release-notes/v1.2.0.md` (pre-stamp `unverified`)
  - `docs/site/release-notes/index.md` (pre-stamp `v1.1.0`)

The maintainer confirms `v1.2.0` independently of the refs. The target tag has
not been created, and no source in this fixture represents the release as
published. The Release Notes page and its Markdown index both carry
`last_verified_version`, so after they pass verification they join the two API
pages in the unified stamp set. A successful result must hash the exact
post-stamp file bytes, persist those hashes, and introduce the four-page stamp
plus the successful audit record in the same ordinary post-stamp commit. The
trusted pre-tag handoff anchors the committed record with commit SHA, tree hash,
record path, and record blob hash; the record does not self-contain its commit
or tree identity. Working-tree state is not an anchor.
