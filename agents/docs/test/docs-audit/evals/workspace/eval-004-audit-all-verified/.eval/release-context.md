# Pre-tag release context

- audit_phase: `pre-tag`
- base_ref: `a1b2c3d`
- target_ref: `b2c3d4e`
- target_release_version: `v1.1.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.1.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.1.0`

The maintainer confirms the target version independently of the refs. The
missing tag is expected during pre-tag audit and does not represent publication.
