# Post-tag release context with audited-content drift

- audit_phase: `post-tag`
- actual_tag: `v1.2.0`
- actual_tag_commit: `abcdef1`
- recorded_post_stamp_HEAD: `3333333`
- tag_commit_equals_post_stamp_HEAD: false
- tag_tree_equals_post_stamp_HEAD_tree: false
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- issue_116_handoff: ready for `v1.2.0`
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`

The tag name matches the target version. However,
`.eval/tag-commit-tree.sha256`, representing SHA-256 values recomputed over
exact `git show abcdef1:<path>` bytes, proves that the tagged
`docs/site/api/catalog-status.md` differs from the pre-tag audited content.
The exact tagged bytes for that path are preserved in
`.eval/tag-commit-catalog-status.md` and hash to the manifest value.
The audit must block and require a complete pre-tag rerun rather than rewrite
any release surface or move the tag.
