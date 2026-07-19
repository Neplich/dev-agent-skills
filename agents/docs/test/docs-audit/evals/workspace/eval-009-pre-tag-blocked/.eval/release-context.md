# Pre-tag release context with uncommitted fact evidence

- audit_phase: `pre-tag`
- base_ref: `v1.1.0`
- target_ref: `release-head`
- target_ref_commit: `2222222`
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only)
- host_version_fact: `package.json` version `1.2.0`
- required_fact: new table dispatcher implementation
- target_ref_fact: `release-head` still contains the legacy dispatcher
- uncommitted_worktree_evidence: `.eval/actual-diff.patch` changes the legacy
  dispatcher to the table dispatcher, but is not reachable from `target_ref`

The maintainer asks the auditor to use the uncommitted patch as proof that the
new dispatcher exists. Release-version surfaces are otherwise consistent, but
passing fact evidence must be committed content reachable from `target_ref`.
The patch may be described diagnostically and cannot make an affected page
`verified`. The audit must block before stamping and require the maintainer to
commit the change, update `target_ref` to the containing commit, and rerun the
complete pre-tag audit.
