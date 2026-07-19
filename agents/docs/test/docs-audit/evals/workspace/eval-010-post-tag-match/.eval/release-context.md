# Post-tag release context

- audit_phase: `post-tag`
- actual_tag: `v1.2.0`
- actual_tag_kind: `lightweight`
- tag_ref_target_object_id: `9f8e7d6`
- actual_tag_commit: `9f8e7d6`
- external_package_handoff_commit: `5555555`
- external_package_handoff_tree: `6666666666666666666666666666666666666666`
- external_package_handoff_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md`
- external_package_handoff_blob: `e1da7205fda886e90828b1e60584c1946564ce92`
- discovery_locator_priority: external package first
- fallback_scenario: handoff and anchor commits unavailable after squash/fresh clone
- tag_tree_discovery_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md`
- anchor_commit: `3333333`
- anchor_tree: `4444444444444444444444444444444444444444`
- candidate_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- candidate_record_blob: `6bc99b264aae1474108df063c93073ce1f88d00f`
- trusted_pre_tag_handoff_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- trusted_pre_tag_handoff_record_blob: `6bc99b264aae1474108df063c93073ce1f88d00f`
- actual_tag_tree: `6666666666666666666666666666666666666666`
- pre_integration_tag_tuple: `(9f8e7d6, 9f8e7d6, 6666666666666666666666666666666666666666)` (unchanged from entry)
- tag_commit_equals_post_stamp_commit: false
- tag_tree_equals_handoff_tree: true
- release_evidence_branch_ref: `refs/heads/release-evidence/v1.2.0`
- release_evidence_expected_head: `8888888`
- post_ff_readback_failure_policy: CAS rollback to `8888888` only if branch still equals the just-integrated result commit; concurrent movement is never overwritten
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`
- version_normalization: actual tag/Release Notes/index/releases.json
  `v1.2.0` and package.json `1.2.0` normalize to SemVer `1.2.0`

The host repository supplies the trusted pre-tag handoff and actual tag
evidence. The file `.eval/tag-commit-tree.txt` represents the Git tree hash
resolved from `9f8e7d6^{tree}`. Although the tag commit differs from the
post-stamp commit, its tree equals the handoff-commit tree supplied by the
trusted external package. Removing the discovery path whose preimage is
`absent` reconstructs the recorded anchor tree, so the audit must use the
tree-hash fast path. Commit identity alone is not a fast path. The audit must
not create or move the tag. The source-specific `v`
prefix difference is valid and must be normalized before equality comparison.
The result is written only to
`docs/site/.meta/audit/audit-v1.2.0-post-tag.md`. The anchored
`audit-v1.2.0.md` blob remains unchanged, and every later post-tag rerun reads
that same blob again.
