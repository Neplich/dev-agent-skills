# Pre-tag release context

- audit_phase: `pre-tag`
- base_ref: `a1b2c3d`
- target_ref: `b2c3d4e`
- target_ref_commit: `b2c3d4e`
- expected_anchor_commit: `c3d4e5f` (ordinary commit created on the isolated temporary branch)
- expected_anchor_tree: `1111111111111111111111111111111111111111`
- expected_record_path: `docs/site/.meta/audit/audit-v1.1.0.md`
- expected_record_blob_hash: persisted by the fixed discovery handoff after anchor confirmation
- expected_discovery_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.1.0.md`
- expected_handoff_commit: `d4e5f6a`
- expected_handoff_tree: `2222222222222222222222222222222222222222`
- target_release_version: `v1.1.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.1.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.1.0`
- version_normalization: `v1.1.0` from Release Notes/index/releases.json and
  `1.1.0` from package.json both normalize to SemVer `1.1.0`
- version_source_inventory: each source declares `source_id`, `locator_kind`,
  immutable `locator`, exact `selector`, versioned deterministic `extractor`,
  and `required_raw_form`; the index uses `entry[v1.1.0].version`, releases.json
  uses JSON Pointer `/latest`, and package.json uses `/version`
- actual_tag inventory entry: `refs/tags/v1.1.0` / `tag-name` /
  `git-tag-name-v1` / `vX.Y.Z`, persisted as `pending_expected_absent`
- inventory_digest_algorithm: `canonical-json-rfc8259-sorted-v1`
- inventory_digest: `sha256:109170c373e9aab353ff234d73d7fb28ca70e464cab3d2019dfa79928365a787`
- empty_prior_lineage_digest: `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- unified_stamp_set:
  - `docs/site/api/catalog-items.md`
  - `docs/site/api/catalog-status.md`
  - `docs/site/release-notes/v1.1.0.md`
  - `docs/site/release-notes/index.md`

The maintainer confirms the target version independently of the refs. The
missing tag is expected during pre-tag audit and does not represent publication.
The `v` prefix difference is required by each source and must be normalized
before equality comparison; it is not a mismatch.
The four-page stamp and candidate record are built only in an isolated
worktree. The candidate record carries the complete producer schema and the
conclusion `candidate_verified`; it never carries `ready_for_tag`, success
time, its containing commit/tree, or a post-commit result. The first staged
gate checks the initial record and stamp delta, and the second checks the exact
final candidate bytes after atomic replacement. Only after the anchor commit
passes the committed raw metadata/content/tree/blob confirmation may the audit
write `docs/site/.meta/audit/handoffs/pre-tag-v1.1.0.md`. That discovery file
carries the anchor commit/tree and candidate path/blob plus the post-commit
confirmation; the external package carries its own handoff commit/tree/path/blob.
The temporary branch may be fast-forward integrated only if the host branch,
index, and worktree fingerprints still match their captured state. Only the
integrated discovery record authorizes `ready_for_tag`.
