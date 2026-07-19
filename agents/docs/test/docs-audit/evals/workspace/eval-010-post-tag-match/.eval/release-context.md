# Post-tag release context

- audit_phase: `post-tag`
- actual_tag: `v1.2.0`
- actual_tag_commit: `9f8e7d6`
- trusted_pre_tag_handoff_post_stamp_commit: `3333333`
- committed_record_read: `git show 3333333:docs/site/.meta/audit/audit-v1.2.0.md`
- trusted_pre_tag_handoff_post_stamp_tree: `4444444444444444444444444444444444444444`
- trusted_pre_tag_handoff_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- trusted_pre_tag_handoff_record_blob: `38be5ead4d55f0e800444abf16991005a8b2b44f`
- actual_tag_tree: `4444444444444444444444444444444444444444`
- tag_commit_equals_post_stamp_commit: false
- tag_tree_equals_handoff_post_stamp_tree: true
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`

The host repository supplies the trusted pre-tag handoff and actual tag
evidence. The file `.eval/tag-commit-tree.txt` represents the Git tree hash
resolved from `9f8e7d6^{tree}`. Although the tag commit differs from the
post-stamp commit, its tree equals the tree hash stored by the trusted handoff,
so the audit must use the tree-hash fast path. Commit identity alone is not a
fast path. The audit must not create or move the tag.
