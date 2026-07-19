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
- in_scope_worktree_inventory: `.eval/in-scope-worktree-status.porcelain-v2`
- uncommitted_worktree_evidence: `.eval/actual-diff.patch` changes the legacy
  dispatcher to the table dispatcher, but is not reachable from `target_ref`

The inventory deliberately includes four independent scope intersections: a
staged code-evidence path, an unstaged affected formal page, an untracked draft
at the authorized candidate-record path, and an unstaged required version
source. None may support success, even if the maintainer does not offer it as
evidence. Passing facts must be exact ordinary blobs from the resolved
`target_ref` tree. The audit must block before creating an isolated candidate
or changing any host bytes, require every in-scope delta to be committed into
the intended release content or moved out of scope, update `target_ref`, verify
scope cleanliness, and rerun the complete pre-tag protocol from the beginning.
