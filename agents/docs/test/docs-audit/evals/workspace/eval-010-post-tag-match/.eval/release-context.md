# Post-tag release context

- audit_phase: `post-tag`
- actual_tag: `v1.2.0`
- actual_tag_commit: `9f8e7d6`
- recorded_post_stamp_HEAD: `3333333`
- tag_commit_equals_post_stamp_HEAD: false
- tag_tree_equals_post_stamp_HEAD_tree: false
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`

The host repository supplies the actual tag evidence. The file
`.eval/tag-commit-tree.sha256` represents SHA-256 values recomputed over the
exact bytes returned by `git show 9f8e7d6:<path>` for every recorded path. The
audit must use this general content-binding path and must not create or move
the tag.
