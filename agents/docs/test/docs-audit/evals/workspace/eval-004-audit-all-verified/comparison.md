# eval-004-audit-all-verified Comparison

## Evaluation target

- Agent: `docs-agent`
- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`
- Validation time: `2026-07-20 00:23:47 +0800`
- Scope: complete affected-set verification, canonical version-source inventory and genesis digests, unified stamping, candidate/anchor/discovery transaction, and integration-gated `ready_for_tag`.

## Test set and method

This is a fresh paired validation against the current 6 assertions. The
`without_skill` baseline ran first from a pristine fixture copy and read only
the current eval definition, metadata, prompt, and fixture files. It did not
read the Docs Agent README, `docs-audit` skill instructions, prior comparison,
or historical output. The `with_skill` run then started from a second pristine
fixture copy after fully reading `agents/docs/skills/docs-audit/SKILL.md`,
`agents/docs/skills/docs-audit/_internal/INSTRUCTIONS.md`, and
`agents/docs/README.md`.

## Latest result

**PASS** — `with_skill` satisfies **6/6** assertions. The fresh
`without_skill` baseline satisfies **4/6** assertions. The skill-specific delta
is the complete canonical candidate producer schema and the mandatory
anchor/discovery/handoff/integration success chain.

## Canonical digest verification

The with-skill run reconstructed the exact six-field inventory rather than
trusting the fixture literals. It sorted **6 entries** by `source_id`:
`actual_tag`, `host_package`, `release_index`, `release_metadata`,
`release_notes`, and `target_version`. Each object contains exactly
`source_id`, `locator_kind`, `locator`, `selector`, `extractor`, and
`required_raw_form`; compact RFC 8259 JSON uses sorted object keys, UTF-8, no
insignificant whitespace, and no trailing newline.

- Recomputed v1.1.0 inventory digest:
  `sha256:109170c373e9aab353ff234d73d7fb28ca70e464cab3d2019dfa79928365a787`
- Fixture inventory digest:
  `sha256:109170c373e9aab353ff234d73d7fb28ca70e464cab3d2019dfa79928365a787`
- Recomputed empty prior-lineage digest from exact bytes `[]`:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- Fixture genesis digest:
  `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`

Both comparisons are exact matches. The `actual_tag` entry is
`git-ref / refs/tags/v1.1.0 / tag-name / git-tag-name-v1 / vX.Y.Z`; its
pre-tag value remains `pending_expected_absent`, so expected absence is not a
version mismatch and does not represent publication.

## Assertion results

| Assertion | without_skill | with_skill | Evidence summary |
| --- | --- | --- | --- |
| `verifies_complete_affected_set` | PASS | PASS | The endpoint diff matches `src/catalog/**`; both required API pages are included and their method, path, auth, query, success, error, streaming, and file claims match the route evidence. Exactly **2/2 affected pages** are `verified`, with zero unresolved gaps. |
| `stamps_all_pages_together` | PASS | PASS | Exactly **4 pages** form the unified stamp set: two API pages, v1.1.0 Release Notes, and the Markdown index. They are updated and read back together as `v1.1.0` only after the complete set passes. |
| `verifies_release_metadata_read_only` | PASS | PASS | `.meta/releases.json` agrees with the target version and remains read-only; no candidate delta includes it. |
| `normalizes_mixed_version_forms` | PASS | PASS | Required `v1.1.0` sources and package `1.1.0` pass source-form validation and normalize to the same case-sensitive SemVer identity. |
| `persists_candidate_producer_schema` | FAIL | PASS | The baseline can repeat the supplied digest literal but cannot reconstruct the exact six-entry/six-field canonical inventory or prove the genesis digest, and it lacks the full identity, per-page blob/hash, lineage, dual-gate, and no-premature-success producer contract. The skill-guided result recomputes both digests exactly and requires the complete fixed-path candidate with conclusion only `candidate_verified`. |
| `anchors_candidate_then_discovers_success` | FAIL | PASS | The baseline does not make committed raw metadata/content/tree/blob confirmation, fixed discovery, handoff-only commit, external package, normal fast-forward integration, and integrated readback one indivisible success gate. The skill does. |

## With-skill behavior

The skill keeps `base_ref`, `target_ref`, and the maintainer-confirmed target
version independent, accepts the absent future tag for pre-tag, verifies all
facts from target-tree ordinary blobs, and keeps `.meta/releases.json`
read-only. It builds the four-page stamp and fixed candidate only in an
isolated worktree/branch/index. The candidate records the complete producer
schema, actual-tag pending contract, exact recomputed inventory and prior
lineage digests, and only `candidate_verified`—never `ready_for_tag`, success
time, containing commit/tree, or post-commit confirmation.

The initial and atomically replaced final candidate each pass the complete raw
metadata, unfolded name-status, summary, and full binary-patch gate. Only then
is the anchor committed and checked. The fixed discovery is written only after
anchor confirmation, then committed as the sole handoff delta and anchored by
the external package. `ready_for_tag` is returned only after normal
fast-forward integration and integrated readback, and is explicitly not a
publication result.

## Failures

- `with_skill`: none.
- `without_skill`: `persists_candidate_producer_schema` and
  `anchors_candidate_then_discovers_success` fail.

## Next steps

No skill change is required. Preserve the exact canonical digest input schema,
actual-tag pending entry, genesis bytes `[]`, and anchor/discovery/integration
ordering in future edits.

## Runtime artifact policy

No runtime artifact was written or committed. The two runs used disposable
fixture copies; this durable `comparison.md` is the only eval-004 output
updated by this validation.
