# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- metadata_sha256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- fixture_sha256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `216827bc3e07bc68d228647a6fadcd479f48a986964f70c0c40f48052e42886f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | With_skill explicitly reports maintainer-confirmed v0.4.0, base_ref 4a1b2c3, target_ref 7c9e2af, pre-tag phase, and the locked evidence inventory. |
| `rejects_standard_doc_type` | PASS | With_skill classifies catalog-search.md as stale because doc_type: standard is outside the allowed enum. |
| `rejects_empty_related_code` | PASS | With_skill classifies catalog-export.md as stale because related_code: [] is invalid. |
| `rejects_missing_last_verified_version` | PASS | With_skill classifies catalog-status.md as stale because last_verified_version is missing. |
| `rejects_empty_owners` | PASS | With_skill classifies catalog-bulk-update.md as stale because owners: [] is invalid. |
| `accepts_valid_api_page` | FAIL | The locked fixture has all seven valid fields on catalog-items.md, but with_skill reports it as evidence-insufficient/unverified and does not confirm frontmatter validation or fact-layer entry. |
| `blocks_release_for_invalid_frontmatter` | PASS | With_skill reports blocked, retains all four invalid pages as stale, does not return ready_for_tag, and does not stamp the valid page. |
| `uses_shared_contract_source` | NOT_EXERCISED | Raw trace proves the shared frontmatter contract was read, but does not prove confirmation against a delivered check-frontmatter.mjs implementation; no such host file exists in the locked fixture. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=4faa4191aff3a2a756ffd3f8d59a093eb956d3ce93e95ece255dc72d0490c1ef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the audit entry, rejects all four invalid frontmatter cases, and blocks release; it incorrectly treats the valid API page as unverified rather than accepting it into the fact layer.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=f46d836c6682862b700738480500b624770bce0f5575863e8290fa0aabcbb5d3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline incorrectly treats the bounded diff as eliminating the affected set and does not perform the required per-page frontmatter classification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane incorrectly fails to accept catalog-items.md as valid frontmatter and entering the fact layer.
- Next: Correct the valid-page classification for catalog-items.md while preserving the blocked release result caused by the four invalid pages.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
