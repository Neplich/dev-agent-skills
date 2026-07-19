# Pre-tag release context

- audit_phase: `pre-tag`
- base_ref: `v1.1.0`
- target_ref: `release-head`
- target_ref_commit: `2222222`
- post_stamp_HEAD: `3333333`
- diff_semantics: two-dot endpoint diff
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`

The maintainer confirms `v1.2.0` independently of the refs. The target tag has
not been created, and no source in this fixture represents the release as
published. A successful result must hash the exact post-stamp file bytes and
atomically persist those hashes and the stamp read-back in the same audit
record before returning `ready_for_tag`.
