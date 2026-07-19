# Post-tag release context with audited-content drift

- audit_phase: `post-tag`
- actual_tag: `v1.2.0`
- actual_tag_commit: `abcdef1`
- trusted_pre_tag_handoff_post_stamp_commit: `3333333`
- committed_record_read: `git show 3333333:docs/site/.meta/audit/audit-v1.2.0.md`
- committed_record_fixture: `.eval/committed-audit-v1.2.0.md`
- current_record_fixture: `docs/site/.meta/audit/audit-v1.2.0.md` (tampered after the post-stamp commit)
- trusted_pre_tag_handoff_post_stamp_tree: `4444444444444444444444444444444444444444`
- trusted_pre_tag_handoff_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- trusted_pre_tag_handoff_record_blob: `bddb69002a60bd4c622b4533407fe840ad06b624`
- actual_tag_tree: `5555555555555555555555555555555555555555`
- tag_commit_equals_post_stamp_commit: false
- tag_tree_equals_handoff_post_stamp_tree: false
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- issue_116_handoff: ready for `v1.2.0`
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`

The tag name matches the target version. The current-path audit record was
modified after the trusted post-stamp commit and is deliberately not
authoritative; `.eval/committed-audit-v1.2.0.md` represents the exact bytes from
the stated `git show` command and must match the handoff's record blob hash.
The audit must report that difference and use the committed record. However,
`.eval/tag-commit-content.sha256`, representing SHA-256 values recomputed over
exact `git show abcdef1:<path>` bytes, proves that the tagged
`docs/site/api/catalog-status.md` differs from the pre-tag audited content.
The exact tagged bytes for that path are preserved in
`.eval/tag-commit-catalog-status.md` and hash to the manifest value.
The audit must block and present both maintainer-selected remediation paths:
correct the host tag and rerun the same version while superseding the old
record, or abandon this version and confirm a new version before a complete
pre-tag rerun. docs-audit records the selection but must not rewrite any
release surface or create, delete, or move a tag.
