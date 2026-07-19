# Pre-tag release context

- audit_phase: `pre-tag`
- base_ref: `a1b2c3d`
- target_ref: `b2c3d4e`
- target_ref_commit: `b2c3d4e`
- expected_post_stamp_commit: `c3d4e5f` (ordinary commit on the host release PR branch)
- expected_post_stamp_tree: `1111111111111111111111111111111111111111`
- expected_record_path: `docs/site/.meta/audit/audit-v1.1.0.md`
- expected_record_blob_hash: persisted by the trusted pre-tag handoff after commit creation
- target_release_version: `v1.1.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.1.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.1.0`
- version_normalization: `v1.1.0` from Release Notes/index/releases.json and
  `1.1.0` from package.json both normalize to SemVer `1.1.0`
- unified_stamp_set:
  - `docs/site/api/catalog-items.md`
  - `docs/site/api/catalog-status.md`
  - `docs/site/release-notes/v1.1.0.md`
  - `docs/site/release-notes/index.md`

The maintainer confirms the target version independently of the refs. The
missing tag is expected during pre-tag audit and does not represent publication.
The `v` prefix difference is required by each source and must be normalized
before equality comparison; it is not a mismatch.
The four-page stamp and successful audit record must be introduced by the same
ordinary post-stamp commit. The committed record does not self-contain its
commit/tree identity; the trusted handoff anchors commit SHA, tree hash, record
path, and record blob hash after commit creation.
