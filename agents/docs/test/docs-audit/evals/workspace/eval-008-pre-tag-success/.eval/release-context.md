# Pre-tag release context

- audit_phase: `pre-tag`
- base_ref: `v1.1.0`
- target_ref: `release-head`
- target_ref_commit: `2222222`
- expected_anchor_commit: `3333333` (ordinary commit on the isolated temporary branch)
- expected_anchor_tree: `4444444444444444444444444444444444444444`
- expected_record_path: `docs/site/.meta/audit/audit-v1.2.0.md`
- expected_record_blob_hash: `38be5ead4d55f0e800444abf16991005a8b2b44f`
- expected_discovery_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md`
- expected_handoff_commit: `5555555`
- expected_handoff_tree: `6666666666666666666666666666666666666666`
- expected_discovery_blob_hash: persisted by the external release handoff package
- diff_semantics: two-dot endpoint diff
- target_release_version: `v1.2.0`
- target_release_version_confirmation: maintainer-confirmed
- matching_tag_status: absent
- issue_116_handoff: ready
- release_notes: `docs/site/release-notes/v1.2.0.md`
- release_notes_index: `docs/site/release-notes/index.md`
- release_metadata: `docs/site/.meta/releases.json` (read-only audit surface)
- host_version_fact: `package.json` version `1.2.0`
- version_normalization: `v1.2.0` from the target version, Release
  Notes/index/releases.json and `1.2.0` from package.json both normalize to
  SemVer `1.2.0`
- version_source_inventory: each source declares `source_id`, `locator_kind`,
  immutable `locator`, exact `selector`, versioned deterministic `extractor`,
  and `required_raw_form`; the index uses `entry[v1.2.0].version`, releases.json
  uses JSON Pointer `/latest`, and package.json uses `/version`
- actual_tag inventory entry: `refs/tags/v1.2.0` / `tag-name` /
  `git-tag-name-v1` / `vX.Y.Z`, persisted as `pending_expected_absent`
- inventory_digest_algorithm: `canonical-json-rfc8259-sorted-v1`
- inventory_digest: `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- empty_prior_lineage_digest: `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- unified_stamp_set:
  - `docs/site/api/catalog-items.md` (pre-stamp `v1.1.0`)
  - `docs/site/api/catalog-status.md` (pre-stamp `unverified`)
  - `docs/site/release-notes/v1.2.0.md` (pre-stamp `unverified`)
  - `docs/site/release-notes/index.md` (pre-stamp `v1.1.0`)

The maintainer confirms `v1.2.0` independently of the refs. The target tag has
not been created, and no source in this fixture represents the release as
published. The Release Notes page and its Markdown index both carry
`last_verified_version`, so after they pass verification they join the two API
pages in the unified stamp set. A successful candidate must hash the exact
post-stamp file bytes and persist those hashes with the complete producer
schema. Its only positive conclusion is `candidate_verified`; it has no
`ready_for_tag`, success time, containing commit/tree, or post-commit result.
Working-tree state is not an anchor. The source-specific `v` prefix difference
is valid and must be normalized before equality comparison.

The audit builds the candidate in an isolated worktree from the immutable
target commit. After writing the four stamp files and initial record it stages
only those five paths and checks raw old/new mode, object type, unfolded
name-status, summary, and full binary patch. After atomically replacing the
final candidate record, it repeats the identical gate over the exact final
bytes. Both gates reject rename/copy/delete/type changes, mode-only changes,
executable bits, symlinks, gitlinks, path swaps, extra hunks, and extra paths.
Only after the anchor commit passes the same committed convergence, tree, blob,
and git-show checks may the audit write the fixed discovery handoff. That file
contains `ready_for_tag`, result time, anchor commit/tree, candidate path/blob,
post-commit confirmation, and its own path preimage. A second commit adds only
this 100644 discovery blob; the external release package records that handoff
commit/tree/path/blob. The host branch may accept the temporary branch only by
normal fast-forward while its branch, worktree, and index fingerprints still
match the captured state. Integration and readback are the final gate before
the issue #120 handoff.
