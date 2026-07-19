# Eval Comparison — eval-010-post-tag-match

## Evaluation target

- Skill: `docs-audit`
- Scenario: post-tag match with external-package priority and fixed tag-tree fallback
- Validation time: `2026-07-20 00:43:50 +0800`
- Validation method: fresh paired reasoning from the pristine fixture; the without-skill result was frozen before any docs-audit skill, internal instructions, Docs Agent README, or comparison file was read.

## Test set / fixture

- Eval definition: `eval-010-post-tag-match`
- Fixture: `workspace/eval-010-post-tag-match`
- Candidate blob recomputed: `6bc99b264aae1474108df063c93073ce1f88d00f`
- Discovery blob recomputed: `e1da7205fda886e90828b1e60584c1946564ce92`
- Inventory digest recomputed: `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- Empty-ledger digest recomputed: `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- Current lineage digest recomputed: `sha256:207291263efab078cada72fa90060fe7318c1daadb4220a05eee92368edefa5c`
- Tag tuple: lightweight `(9f8e7d6, 9f8e7d6, 6666666666666666666666666666666666666666)`; package handoff tree is the same tree, while the recorded anchor tree is `4444444444444444444444444444444444444444` and is recovered by removing the discovery path whose preimage is absent.
- All six persisted file SHA-256 values recomputed exactly.

## Latest result

**PASS.** With skill: **10/10 assertions passed**. Without skill: **10/10 assertions passed**. Assertion lift: **0**.

The skill-applied result correctly returns `release_verified` only after the validated independent post-tag record is committed, read back, and integrated. The zero lift is material: the eval definition and fixture explicitly expose enough protocol detail for the pristine without-skill baseline to reproduce every asserted behavior.

## Assertion results

| Assertion | With skill | Without skill | Paired finding |
| --- | --- | --- | --- |
| `prefers_and_validates_external_handoff` | PASS | PASS | External package is preferred; package/artifact conflict blocks rather than falling back. |
| `falls_back_to_fixed_tag_tree_artifact` | PASS | PASS | Fixed tag-tree discovery, absent preimage reconstruction, schema/digest/convergence checks, and exactly one current attempt are explicit. |
| `reads_candidate_without_ready_from_anchor` | PASS | PASS | Candidate blob is byte-identical, contains `candidate_verified`, and does not claim `ready_for_tag`; discovery is final pre-tag authority. |
| `resolves_actual_tag_commit` | PASS | PASS | Entry and pre-integration lightweight tag tuples are identical; the protocol also preserves annotated-tag semantics. |
| `binds_tag_tree_to_validated_handoff_tree` | PASS | PASS | Commit identity differs but tree identity passes via the validated handoff tree; no commit-only shortcut is used. |
| `uses_tag_tree_object_reads_only` | PASS | PASS | Pages and required version files are evaluated from peeled-tag-tree blobs, modes, hashes, and raw version forms. |
| `normalizes_mixed_version_forms` | PASS | PASS | Four `v1.2.0` sources and package `1.2.0` normalize component-wise to `1.2.0`. |
| `returns_release_verified` | PASS | PASS | Complete consistency produces post-tag `release_verified`, not `ready_for_tag`. |
| `persists_post_tag_atomically` | PASS | PASS | Confirmed evidence branch/head, isolated single-path transaction, convergence/readback, FF CAS, guarded rollback, and cleanup are all retained. |
| `does_not_regenerate_or_restamp` | PASS | PASS | Only the independent post-tag record is written; release surfaces and stamps remain unchanged. |

## With-skill behavior

The skill makes the authority hierarchy and transaction boundary normative: external package first, fixed tag-tree fallback second, candidate never final authority, strict tree semantics despite squash, tag-tree-only source verification, and durable readback before exposing `release_verified`.

## Without-skill baseline

The fresh baseline was generated only from the eval-010 object, its metadata, and explicitly listed fixture files. It independently reproduced the same digests, blobs, tag tuple, release result, and persistence gates. It did not read or search docs-audit skill files, internal instructions, the Docs Agent README, any prior comparison, or unrelated repository content before being frozen.

## Failures

- Assertion failures: none.
- Validation contamination: none observed.
- Discriminative weakness: all 10 assertions are recoverable from the baseline-visible eval object and fixture, so this case demonstrates correctness but not measurable skill lift.

## Next steps

- Keep the result `PASS`.
- If future evaluation must measure skill lift, reduce protocol-complete wording in baseline-visible assertions/fixture context while retaining an independent judge rubric.

## Runtime artifact policy

No `with_skill/`, `without_skill/`, transcript, verdict, timing, diagnostics, or generated post-tag record was created. This durable `comparison.md` is the only eval result updated.
