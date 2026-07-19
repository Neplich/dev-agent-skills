# Eval Comparison — eval-011-post-tag-mismatch

## Evaluation target

- Skill: `docs-audit`
- Scenario: post-tag mismatch with cumulative same-version lineage, tampered current copy, and unaudited tag-tree delta
- Validation time: `2026-07-20 00:43:50 +0800`
- Validation method: final fresh paired reasoning after metadata prompt/field-name synchronization; the without-skill result was frozen before any docs-audit skill, internal instructions, Docs Agent README, or prior comparison file was read.

## Test set / fixture

- Eval definition: `eval-011-post-tag-mismatch`
- Fixture: `workspace/eval-011-post-tag-mismatch`
- Canonical algorithm: `canonical-json-rfc8259-sorted-v1`; empty-ledger genesis recomputed as `sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`.
- Attempt 1 prior ledger digest recomputed from the exact seven-field tuple as `sha256:33adb80c0b52f1a6ec51c2235336610b156e1d7ae818cdb554d5b48b169eee26`.
- Attempt 2 current ledger digest recomputed from the prior ledger plus the exact six-field current tuple as `sha256:54422aea098062c6a08a3cd51aff818ec65ee9afbc42bcfcf69e43a45f803c41`.
- Committed candidate Git blob recomputed: `22772710f35bef7baf16c11a4b492bf560682b7c`; committed discovery Git blob recomputed: `871d2ca3de6e15424b433a24da42db06423de1ba`; tampered current-copy Git blob recomputed: `85ade00ff124774082442d66168104ef26530286`.
- Candidate locator tuple: `(3333333, 4444444444444444444444444444444444444444, docs/site/.meta/audit/audit-v1.2.0.md, 22772710f35bef7baf16c11a4b492bf560682b7c)`.
- External handoff locator tuple: `(5555555, 6666666666666666666666666666666666666666, docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md, 871d2ca3de6e15424b433a24da42db06423de1ba)`.
- Entry and pre-integration annotated-tag tuples both recompute from fixture facts as `(abcdeff, abcdef1, 5555555555555555555555555555555555555555)`.
- The three tree roles remain distinct: candidate anchor `4444444444444444444444444444444444444444`, integrated external handoff `6666666666666666666666666666666666666666`, and actual tag `5555555555555555555555555555555555555555`.
- Version inventory digest recomputed from the six exact locator objects sorted by `source_id`: `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`.
- Persisted SHA-256 values recompute exactly: catalog items `4699c95098a22aab06d014d404f452ec0965ef79dc7025255e822e464107a53c`, catalog status `995e20a2e7d492592fb455bcc220c9c80ea6afbdee4b28d231e980ca1ce28a7e`, Release Notes `f159690c0f8a816db8efbc2fdb2146ed73f2b04f43fdda4d79e2bd13bd746a77`, index `88fc254cad95a0a023f125419e5fc3eed7649cda6c99be890019b55d6f1cb248`, releases metadata `0a9cc1bda146381fd73264801d7510cedfbb9ff42f766e3b5b9cf9e0be7388ca`, and package `f37f1a40a628982c7ad3297df8a0b3ae5035ac8c46dab0440c9d32b6d3dfa71e`.
- Exact name-status delta: `A src/catalog/export-v2.py`.

## Latest result

**PASS.** With skill: **11/11 assertions passed**. Without skill: **11/11 assertions passed**. Assertion lift: **0**.

Both runs correctly remain `blocked`: the actual tag name and all version sources match `v1.2.0`, but the tag tree is neither the candidate anchor tree nor the validated integrated external handoff tree. The unaudited source-file addition prevents attempt 2 from becoming release-active. The zero lift is material because the eval definition and fixture expose the complete lineage, tree, remediation, and persistence requirements to the baseline.

## Assertion results

| Assertion | With skill | Without skill | Paired finding |
| --- | --- | --- | --- |
| `reads_anchored_record_not_tampered_copy` | PASS | PASS | Both use the `3333333`-anchored candidate blob, report the different current-copy blob as tampered, reject its forged fields, and exclude the independent post-tag path from that comparison. |
| `accepts_correct_tag_name_but_checks_tree` | PASS | PASS | Both preserve matching `v1.2.0`, distinguish anchor tree `444...` from integrated handoff tree `666...`, and reject actual tag tree `555...` because it differs from the external handoff tree. |
| `validates_cumulative_attempt_lineage` | PASS | PASS | Genesis, prior, and current digests recompute exactly; attempts are monotonic and unique, the current entry omits its self-referential handoff blob, the external package supplies it, and only the current tuple could become release-active if final tree binding passed. |
| `rejects_unaudited_tag_delta` | PASS | PASS | The sole added path `src/catalog/export-v2.py` causes strict tree inequality despite exact equality of all six persisted content hashes; name-status evidence is retained and no per-path fallback is allowed. |
| `normalizes_mixed_version_forms` | PASS | PASS | Actual tag, target, Release Notes, index, and release metadata use valid `v1.2.0`; package uses valid `1.2.0`; all normalize to `1.2.0` but cannot override tree drift. |
| `invalidates_pre_tag_handoff` | PASS | PASS | The tag is not bound to the validated integrated handoff/release tree, so existing `ready_for_tag` cannot upgrade and the phase result remains `blocked`. |
| `offers_two_maintainer_remedies` | PASS | PASS | Both preserve immutable old blobs and offer either host-side correction/removal of the bad tag followed by a same-version full pre-tag rerun with a superseding cumulative attempt, or abandonment of `v1.2.0` followed by confirmation of a new version and full pre-tag rerun. |
| `allows_pre_tag_reentry_after_selection` | PASS | PASS | Re-entry requires a selected remedy plus host-side deletion or movement of the invalid tag and a recorded tag state; while it still resolves to the target version, post-tag stays blocked, but prior existence is not permanent blocking. |
| `persists_blocked_in_separate_post_tag_record` | PASS | PASS | After all checks, the blocked evidence belongs only in `audit-v1.2.0-post-tag.md`, including attempt/lineage, tuple and tree inequality, raw mode/type/object/name-status/full-patch evidence, and both remedies; candidate and discovery blobs remain unchanged. |
| `restores_failed_blocked_persistence` | PASS | PASS | Both remove the isolated attempt, restore or remove the host path/index from captured bytes/mode/type, use guarded CAS rollback only when the evidence branch still points to the just-integrated commit, verify branch/porcelain/raw diffs/hashes, preserve the tag and pre-tag lineage, and prohibit success when restoration cannot be proved. |
| `does_not_rewrite_or_operate_tag` | PASS | PASS | docs-audit only adjudicates and records; neither run rewrites stamped pages, Release Notes, index, releases metadata, GitHub Release content, or creates/deletes/moves a tag. |

## With-skill behavior

The current skill makes the external package the preferred locator, validates its handoff commit/tree/path/blob and committed discovery, reads the candidate only from the anchor commit or a byte-identical tag-tree blob, and makes strict final tree binding decisive. It also supplies the exact independent post-tag transaction, guarded rollback, immutable-lineage, and maintainer-remediation boundaries used by the passing result.

## Without-skill baseline

The fresh baseline was generated only from the eval-011 object, its metadata, and explicitly listed fixture files. Before being frozen it did not read or search docs-audit skill files, internal instructions, the Docs Agent README, any prior comparison, or unrelated repository content. It independently recomputed the canonical digests, Git blobs, inventory digest, locator/tag tuples, persisted hashes, one-path delta, blocked result, both maintainer remedies, and persistence-failure restoration behavior.

## Failures

- Assertion failures: none.
- Validation contamination: none observed.
- Discriminative weakness: all 11 assertions remain recoverable from the baseline-visible eval object and corrected fixture, so this case demonstrates protocol correctness but no measurable skill lift.

## Next steps

- Keep the result `PASS`.
- If future evaluation must measure skill lift, separate the judge-only protocol rubric from baseline-visible fixture prose.

## Runtime artifact policy

No `with_skill/`, `without_skill/`, transcript, verdict, timing, diagnostics, or generated post-tag record was created. This durable `comparison.md` is the only eval result updated by this validation.
