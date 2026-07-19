# eval-008-pre-tag-success Comparison

## Evaluation target

- Agent: `docs-agent`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`
- Validation time: `2026-07-20 00:23:47 +0800`
- Scope: full pre-tag candidate transaction, canonical inventory/genesis digests, actual-tag pending contract, two staged gates, anchor/discovery commits, integration readback, and post-FF CAS rollback.

## Test set and method

This is a fresh paired validation against the current 12 assertions. The
`without_skill` baseline ran first from a pristine fixture copy and read only
the current eval definition, metadata, prompt, and fixture files. It did not
read the Docs Agent README, `docs-audit` skill instructions, prior comparison,
or historical output. The `with_skill` run then started from a second pristine
fixture copy after fully reading `agents/docs/skills/docs-audit/SKILL.md`,
`agents/docs/skills/docs-audit/_internal/INSTRUCTIONS.md`, and
`agents/docs/README.md`.

## Latest result

**PASS** — `with_skill` satisfies **12/12** assertions. The fresh
`without_skill` baseline satisfies **10/12** assertions. The two skill-specific
gaps are independent canonical digest production inside the candidate schema
and the complete concurrency-safe CAS rollback contract after post-FF readback
failure.

## Canonical digest verification

The with-skill run reconstructed the exact six-field inventory rather than
trusting the fixture literals. It sorted **6 entries** by `source_id`:
`actual_tag`, `host_package`, `release_index`, `release_metadata`,
`release_notes`, and `target_version`. Each object contains exactly
`source_id`, `locator_kind`, `locator`, `selector`, `extractor`, and
`required_raw_form`; compact RFC 8259 JSON uses sorted object keys, UTF-8, no
insignificant whitespace, and no trailing newline.

- Recomputed v1.2.0 inventory digest:
  `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- Fixture inventory digest:
  `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- Recomputed empty prior-lineage digest from exact bytes `[]`:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- Fixture genesis digest:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`

Both comparisons are exact matches. The `actual_tag` entry is
`git-ref / refs/tags/v1.2.0 / tag-name / git-tag-name-v1 / vX.Y.Z`; its
pre-tag value remains `pending_expected_absent`. Tag absence is expected and
does not represent publication or a failed version comparison.

## Assertion results

| Assertion | without_skill | with_skill | Evidence summary |
| --- | --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | PASS | Keeps `base_ref: v1.1.0`, `target_ref: release-head`, and confirmed `v1.2.0` distinct; absent future tag does not block pre-tag. |
| `verifies_complete_set_and_surfaces` | PASS | PASS | Exactly **2/2 API pages** are affected and verified; #116 handoff, Release Notes, index, releases metadata, and host package facts also pass. |
| `normalizes_mixed_version_forms` | PASS | PASS | Required `v1.2.0` sources and package `1.2.0` pass source-form validation and normalize to one case-sensitive SemVer identity. |
| `records_pre_stamp_values` | PASS | PASS | Exact four values are retained: `v1.1.0`, `unverified`, `unverified`, `v1.1.0`; no `baseline_verified_version` is added. |
| `stamps_complete_set_atomically` | PASS | PASS | Exactly **4 pages** are stamped and read back together as `v1.2.0`; `.meta/releases.json` remains read-only. |
| `builds_isolated_candidate_transaction` | PASS | PASS | Candidate work occurs from the immutable target commit in an isolated worktree/branch/index; captured host state stays untouched before integration. |
| `candidate_record_has_no_ready_result` | FAIL | PASS | Baseline follows the visible happy-path schema but cannot independently reconstruct the exact six-entry canonical inventory, recompute both SHA-256 digests, or prove the literal values rather than echo them. The skill-guided candidate recomputes exact inventory/genesis digests, persists actual-tag pending, and excludes premature final authority. |
| `validates_two_complete_staged_gates` | PASS | PASS | Initial and final candidate bytes each pass raw mode/type, unfolded name-status, summary, and full binary-patch checks with no unauthorized path or hunk. |
| `confirms_anchor_commit_before_discovery` | PASS | PASS | Discovery is forbidden until target-to-anchor raw metadata/content/tree/blob and `git show` readback all pass. |
| `persists_fixed_discovery_handoff` | PASS | PASS | Fixed discovery contains anchor and candidate identities plus lineage fields without self-reference; only its 100644 blob is committed and the external package supplies handoff commit/tree/path/blob. |
| `returns_ready_only_after_integration` | FAIL | PASS | Baseline waits for FF/readback on the happy path but lacks the full post-FF failure contract. The skill requires CAS proof against the just-integrated handoff commit before rollback, target-ref restoration plus fingerprint verification, and non-overwrite/residual-ref/manual-command handling on concurrent movement. |
| `returns_ready_for_tag_not_published` | PASS | PASS | Final state means tag creation is allowed; it is not publication or `release_verified`. |

## With-skill behavior

The skill-guided run validates the full affected set and release surfaces from
the exact target tree, applies the four-page stamp only after all evidence and
version identities pass, and builds a fixed-path candidate whose positive
conclusion is only `candidate_verified`. Its exact canonical inventory and
genesis digests match the fixture values; any mismatch would instead be
`blocked` and fail this eval.

Both staged gates inspect raw modes, object types, unfolded statuses, summary,
and full binary patch. Anchor confirmation precedes discovery; the discovery
handoff is committed separately and anchored by an external package. The host
branch is fast-forwarded only if its ref and captured worktree/index
fingerprints remain unchanged. Final authority appears only after integrated
commit/tree/discovery-blob readback.

If that readback fails after fast-forward, rollback to `target_ref` is allowed
only when compare-and-swap proves the branch still equals the just-integrated
handoff commit. The process then restores and verifies every captured
fingerprint. A concurrent move is never overwritten: the result remains
`blocked`, names the residual ref/commit and exact maintainer recovery command,
and prohibits tag creation.

## Failures

- `with_skill`: none.
- `without_skill`: `candidate_record_has_no_ready_result` and
  `returns_ready_only_after_integration` fail.

## Next steps

No skill change is required. Preserve exact canonical inventory fields and
ordering, actual-tag pending semantics, genesis bytes `[]`, and the guarded
post-FF CAS rollback language in future protocol edits.

## Runtime artifact policy

No runtime artifact was written or committed. The two runs used disposable
fixture copies; this durable `comparison.md` is the only eval-008 output
updated by this validation.
