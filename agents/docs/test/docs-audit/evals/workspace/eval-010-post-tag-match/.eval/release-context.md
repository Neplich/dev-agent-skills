# Post-tag release context

- audit_phase: `post-tag`
- actual_tag: `v1.2.0`
- actual_tag_kind: `lightweight`
- tag_ref_target_object_id: `9f8e7d6`
- actual_tag_commit: `9f8e7d6`
- external_package_handoff_commit: `5555555`
- external_package_handoff_tree: `6666666666666666666666666666666666666666`
- external_package_handoff_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md`
- external_package_handoff_blob: `40ba49cc285bc393db948e1560c0a1136cd500a2`
- direct_handoff_object_resolution: available
- fresh_clone_handoff_object_resolution: missing
- fresh_clone_anchor_object_resolution: missing
- tag_tree_discovery_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md`
- anchor_commit: `3333333`
- anchor_tree: `4444444444444444444444444444444444444444`
- candidate_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- candidate_record_blob: `7427efa7a68e8aa531b2559bf75a5a38ce59d2b1`
- trusted_pre_tag_handoff_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- trusted_pre_tag_handoff_record_blob: `7427efa7a68e8aa531b2559bf75a5a38ce59d2b1`
- actual_tag_tree: `6666666666666666666666666666666666666666`
- entry_tag_tuple: `(9f8e7d6, 9f8e7d6, 6666666666666666666666666666666666666666)`
- pre_result_tag_tuple: `(9f8e7d6, 9f8e7d6, 6666666666666666666666666666666666666666)`
- tag_commit_equals_post_stamp_commit: false
- release_evidence_branch_hint: `refs/heads/release-evidence/v1.2.0`
- release_evidence_branch_confirmation: absent
- release_evidence_expected_head: absent
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- release_notes_generator_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`
- observed_versions: actual tag/Release Notes/index/releases.json `v1.2.0`;
  package.json `1.2.0`

The file `.eval/tag-commit-tree.txt` is the raw result of resolving
`9f8e7d6^{tree}`. The direct-handoff scenario exposes the package objects. The
fresh-clone scenario exposes the same tag tree and committed paths but not the
handoff or anchor commit objects. No release-evidence branch choice has been
confirmed by a maintainer.
