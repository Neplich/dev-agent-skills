# Post-tag release context with mismatch

- audit_phase: `post-tag`
- actual_tag: `v1.2.1`
- actual_tag_commit: `abcdef1`
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- issue_116_handoff: ready for `v1.2.0`
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`

The host created `v1.2.1`, which does not match the target version recorded by
the pre-tag audit. The audit must report the conflict rather than rewrite any
release surface or move the tag.
