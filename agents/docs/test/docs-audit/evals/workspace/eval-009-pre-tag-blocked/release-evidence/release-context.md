# Pre-tag release context with uncommitted fact evidence

- audit_phase: `pre-tag`
- base_ref: `v1.1.0`
- target_ref: `release-head`
- target_ref_commit: resolve the immutable commit from `release-head^{commit}`
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only)
- host_version_fact: `package.json` version `1.2.0`
- required_fact: new table dispatcher implementation
- target_ref_fact: `release-head` still contains the legacy dispatcher
- in_scope_worktree_inventory: `release-evidence/in-scope-worktree-status.porcelain-v2`
- uncommitted_worktree_evidence: `release-evidence/actual-diff.patch` changes the legacy
  dispatcher to the table dispatcher, but is not reachable from `target_ref`
