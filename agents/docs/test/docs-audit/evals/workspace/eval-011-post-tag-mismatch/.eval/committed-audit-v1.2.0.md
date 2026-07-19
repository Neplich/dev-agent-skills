# Formal documentation audit

- schema_version: `1.0`
- attempt: `2`
- phase: `pre-tag`
- base_ref_commit: `1111111`
- target_ref_commit: `2222222`
- target_release_version: `v1.2.0` (maintainer-confirmed)
- diff_semantics: two-dot endpoint diff
- prior_attempt_lineage: `[(attempt=1, commit=111aaaa, tree=111bbbb, record_path=docs/site/.meta/audit/audit-v1.2.0.md, record_blob=111cccc, handoff_blob=111dddd, previous_lineage_digest=sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945)]`
- prior_lineage_digest: `sha256:33adb80c0b52f1a6ec51c2235336610b156e1d7ae818cdb554d5b48b169eee26`
- immediately_superseded_attempt: `1`

## Impact

- Raw changed files: `M src/catalog/routes.txt`
- Change-map matches: `src/catalog/** -> docs/site/api/catalog-*.md`; no mapping delta.
- Affected set: `docs/site/api/catalog-items.md`, `docs/site/api/catalog-status.md`
- Unified stamp set: affected set plus `docs/site/release-notes/v1.2.0.md` and `docs/site/release-notes/index.md`

## Per-page evidence

- `docs/site/api/catalog-items.md`: target mode/type/blob `100644/blob/a111`; pre/post stamp `v1.1.0` -> `v1.2.0`; claims `catalog item route and response`; target-ref evidence `src/catalog/routes.txt@100644/blob/c111`, `tests/catalog.txt@100644/blob/d111`; final `verified`; post-stamp SHA-256 `4699c95098a22aab06d014d404f452ec0965ef79dc7025255e822e464107a53c`.
- `docs/site/api/catalog-status.md`: target mode/type/blob `100644/blob/a222`; pre/post stamp `unverified` -> `v1.2.0`; claims `catalog status route`; target-ref evidence `src/catalog/routes.txt@100644/blob/c111`, `tests/catalog.txt@100644/blob/d222`; final `verified`; post-stamp SHA-256 `995e20a2e7d492592fb455bcc220c9c80ea6afbdee4b28d231e980ca1ce28a7e`.
- `docs/site/release-notes/v1.2.0.md`: target mode/type/blob `100644/blob/a333`; pre/post stamp `unverified` -> `v1.2.0`; claims `release contents`; target-ref evidence `src/catalog/routes.txt@100644/blob/c111`, `tests/catalog.txt@100644/blob/d222`; final `verified`; post-stamp SHA-256 `f159690c0f8a816db8efbc2fdb2146ed73f2b04f43fdda4d79e2bd13bd746a77`.
- `docs/site/release-notes/index.md`: target mode/type/blob `100644/blob/a444`; pre/post stamp `v1.1.0` -> `v1.2.0`; claims `unique v1.2.0 index entry`; target-ref evidence `docs/site/release-notes/v1.2.0.md@100644/blob/a333`; final `verified`; post-stamp SHA-256 `88fc254cad95a0a023f125419e5fc3eed7649cda6c99be890019b55d6f1cb248`.

## Version sources

- Digest algorithm: `canonical-json-rfc8259-sorted-v1`; inventory entries sorted by `source_id`, exact six-field objects, UTF-8 compact JSON, SHA-256.
- Inventory digest: `sha256:bd935efb92eedfb3facbfe867542687802159c700fa73dee1d2a896deac041a8`
- `actual_tag`: locator_kind `git-ref`; locator `refs/tags/v1.2.0`; selector `tag-name`; extractor `git-tag-name-v1`; required_raw_form `vX.Y.Z`; pre_tag_value `pending_expected_absent`.
- `target_version`: locator_kind `handoff`; locator `issue-116`; selector `target_release_version`; extractor `handoff-field-v1`; required_raw_form `vX.Y.Z`; raw_value `v1.2.0`; normalized `1.2.0`; comparison `passed`.
- `release_notes`: locator_kind `git-file`; locator `docs/site/release-notes/v1.2.0.md`; selector `heading[h1].release-version`; extractor `markdown-release-heading-v1`; required_raw_form `vX.Y.Z`; raw_value `v1.2.0`; target mode/type/blob `100644/blob/a333`; SHA-256 `f159690c0f8a816db8efbc2fdb2146ed73f2b04f43fdda4d79e2bd13bd746a77`; normalized `1.2.0`; comparison `passed`.
- `release_index`: locator_kind `git-file`; locator `docs/site/release-notes/index.md`; selector `entry[v1.2.0].version`; extractor `markdown-release-index-v1`; required_raw_form `vX.Y.Z`; raw_value `v1.2.0`; target mode/type/blob `100644/blob/a444`; SHA-256 `88fc254cad95a0a023f125419e5fc3eed7649cda6c99be890019b55d6f1cb248`; normalized `1.2.0`; comparison `passed`.
- `release_metadata`: locator_kind `git-file`; locator `docs/site/.meta/releases.json`; selector `/latest`; extractor `json-pointer-rfc6901-v1`; required_raw_form `vX.Y.Z`; raw_value `v1.2.0`; target mode/type/blob `100644/blob/fb4bd3ca352abb9a59ae1c1894aaca9582dad5ab`; SHA-256 `0a9cc1bda146381fd73264801d7510cedfbb9ff42f766e3b5b9cf9e0be7388ca`; normalized `1.2.0`; comparison `passed`.
- `host_package`: locator_kind `git-file`; locator `package.json`; selector `/version`; extractor `json-pointer-rfc6901-v1`; required_raw_form `X.Y.Z`; raw_value `1.2.0`; target mode/type/blob `100644/blob/99f37ebf0f908c587d03ba0ed3e9dcc3512ffe11`; SHA-256 `f37f1a40a628982c7ad3297df8a0b3ae5035ac8c46dab0440c9d32b6d3dfa71e`; normalized `1.2.0`; comparison `passed`.

## Candidate convergence

- Initial staged inventory: four stamp paths `M` at unchanged `100644/blob`; candidate fixed path `M` at unchanged `100644/blob`; rename/copy disabled; no `R/C/D/T`, mode-only, symlink, gitlink, path swap, or unauthorized path; full binary patch valid; zero unauthorized delta.
- Final staged inventory after atomic record replacement: identical allowed paths/status/mode/type inventory; summary and full binary patch reviewed; zero unauthorized delta.
- Stamp read-back: all four pages equal `v1.2.0`.

## Conclusion

- Blocking items: none at pre-tag time
- Candidate conclusion: `candidate_verified`
- Reproducible commands: endpoint diff, raw/name-status/summary/binary staged checks, host docs checks, exact Git-object reads.
- This record contains no final success, containing commit/tree identity, success time, or post-commit confirmation.
