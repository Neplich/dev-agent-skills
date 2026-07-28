# Post-tag release context with an unaudited code delta

- audit_phase: `post-tag`
- actual_tag: `v1.2.0`
- actual_tag_kind: `annotated`
- tag_ref_target_object_id: `abcdeff`
- actual_tag_commit: `abcdef1`
- entry_tag_tuple: `(abcdeff, abcdef1, 5555555555555555555555555555555555555555)`
- pre_integration_tag_tuple: `(abcdeff, abcdef1, 5555555555555555555555555555555555555555)`
- external_package_handoff_commit: `5555555`
- external_package_handoff_tree: `6666666666666666666666666666666666666666`
- external_package_handoff_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md`
- trusted_pre_tag_handoff_post_stamp_commit: `3333333`
- committed_record_read: `git show 3333333:docs/site/.meta/audit/audit-v1.2.0.md`
- committed_record_fixture: `.eval/committed-audit-v1.2.0.md`
- current_record_fixture: `docs/site/.meta/audit/audit-v1.2.0.md` (tampered after the post-stamp commit)
- trusted_pre_tag_handoff_post_stamp_tree: `4444444444444444444444444444444444444444`
- trusted_pre_tag_handoff_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- trusted_pre_tag_handoff_record_blob: `d882a8f6a7fa7378ea10c00fbe3600c7305fc018`
- actual_tag_tree: `5555555555555555555555555555555555555555`
- recorded_paths_match_pre_tag_hashes: true
- tag_tree_diff: `.eval/tag-tree-diff.name-status`
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- current_pre_tag_attempt: `2`
- committed_discovery_fixture: `.eval/committed-discovery-v1.2.0.md`
- external_package_handoff_blob: `29ddade672e2b835a15d4d109593efd3c0d2ab15`
- release_evidence_branch_ref: `refs/heads/release-evidence/v1.2.0`
- release_evidence_expected_head: `9999999`
- release_notes_generator_handoff: ready for `v1.2.0`
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`
- observed_versions: actual tag/Release Notes/index/releases.json `v1.2.0`;
  package.json `1.2.0`

The current checkout copy and the committed fixture are observations from two
different repository states. `.eval/tag-tree-diff.name-status` is the raw
name-status delta between the external package handoff tree and the peeled tag
tree. A simulated post-tag result write reached the staged state, then failed
before commit; the post-tag path was absent in the captured host state.
