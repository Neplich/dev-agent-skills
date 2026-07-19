# Pre-tag release context with an unrelated staged delta

- audit_phase: `pre-tag`
- base_ref: `v1.1.0`
- target_ref: `release-head`
- target_ref_commit: `2222222`
- post_stamp_commit: `5555555`
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only)
- host_version_fact: `package.json` version `1.2.0`
- unrelated_preexisting_staged_path: `src/catalog/debug-trace.txt`

All page facts and release-version surfaces are consistent. The post-stamp
commit includes the authorized four-page `last_verified_version` stamp and
audit record, but it also includes the unrelated staged source change shown in
`.eval/post-stamp-diff.patch`. The full commit must therefore be blocked even
though the fact audit and stamping operation otherwise succeed.
