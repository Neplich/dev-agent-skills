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
- trusted_pre_tag_handoff_record_blob: `22772710f35bef7baf16c11a4b492bf560682b7c`
- actual_tag_tree: `5555555555555555555555555555555555555555`
- tag_commit_equals_post_stamp_commit: false
- tag_tree_equals_external_handoff_tree: false
- recorded_paths_match_pre_tag_hashes: true
- tag_tree_diff: `.eval/tag-tree-diff.name-status`
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- current_pre_tag_attempt: `2`
- post_tag_release_active_attempt: none; attempt 2 is invalidated for release by final tag-tree drift
- committed_discovery_fixture: `.eval/committed-discovery-v1.2.0.md`
- external_package_handoff_blob: `871d2ca3de6e15424b433a24da42db06423de1ba`
- active_prior_lineage_digest: `sha256:33adb80c0b52f1a6ec51c2235336610b156e1d7ae818cdb554d5b48b169eee26`
- active_lineage_digest: `sha256:54422aea098062c6a08a3cd51aff818ec65ee9afbc42bcfcf69e43a45f803c41`
- lineage_rule: the tag-anchored cumulative ledger has monotonic unique attempts, one current tuple bound to the final tag tree, and does not require squash-discarded objects
- release_evidence_branch_ref: `refs/heads/release-evidence/v1.2.0`
- release_evidence_expected_head: `9999999`
- post_ff_failure_policy: CAS rollback to `9999999` only if evidence branch still equals the just-integrated result commit; concurrent movement is never overwritten
- issue_116_handoff: ready for `v1.2.0`
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`
- version_normalization: actual tag/Release Notes/index/releases.json
  `v1.2.0` and package.json `1.2.0` normalize to SemVer `1.2.0`

The tag name matches the target version. The current-path audit record was
modified after the trusted post-stamp commit and is deliberately not
authoritative; `.eval/committed-audit-v1.2.0.md` represents the exact bytes from
the stated `git show` command and must match the handoff's record blob hash.
The audit must report that difference and use the committed record. Every path
and SHA-256 already recorded by pre-tag still matches at the tag commit, but
the tag adds `src/catalog/export-v2.py` after the post-stamp commit. Therefore
the actual tree differs from the trusted handoff tree and strict tree equality
must block without a recorded-path fallback. The report includes the
name-status delta and both maintainer-selected remediation paths: correct the
host tag and rerun the same version while appending a new cumulative lineage attempt, or
abandon this version and confirm a new version before a complete pre-tag
rerun. Both reruns use the actual content intended for release as the new
`target_ref`. docs-audit records the selection but must not rewrite any release
surface or create, delete, or move a tag. The source-specific `v` prefix
difference is valid after SemVer normalization and cannot override tree
inequality.
The post-tag `blocked` result must be written to the independent
`docs/site/.meta/audit/audit-v1.2.0-post-tag.md` path. Its presence is not a
change to the current pre-tag path and must be excluded from the current-copy
comparison. The anchored pre-tag blob remains unchanged and is reused by every
post-tag rerun.

The fixture also models a persistence fault after staging the independent
blocked record. The isolated attempt must be removed; the host post-tag path
and index entry must be restored to their captured bytes/mode/type (or removed
when absent), then branch SHA, porcelain v2, raw staged/unstaged metadata and
hashes must match the pre-write fingerprint. The actual tag and both immutable
pre-tag attempts remain unchanged. No `release_verified` exists until a later
post-tag rerun durably commits, reads back, and integrates its result.
