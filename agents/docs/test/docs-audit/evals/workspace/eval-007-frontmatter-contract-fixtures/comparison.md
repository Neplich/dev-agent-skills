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
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- metadata_sha256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- fixture_sha256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `216827bc3e07bc68d228647a6fadcd479f48a986964f70c0c40f48052e42886f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | With-skill output accepts maintainer-confirmed v0.4.0, base_ref 4a1b2c3, target_ref 7c9e2af, pre-tag phase, and the five-file evidence inventory. |
| `rejects_standard_doc_type` | PASS | With-skill output classifies catalog-search.md as stale because doc_type: standard is invalid. |
| `rejects_empty_related_code` | PASS | With-skill output classifies catalog-export.md as stale because related_code is empty. |
| `rejects_missing_last_verified_version` | PASS | With-skill output classifies catalog-status.md as stale because last_verified_version is missing. |
| `rejects_empty_owners` | PASS | With-skill output classifies catalog-bulk-update.md as stale because owners is empty. |
| `accepts_valid_api_page` | PASS | With-skill output verifies catalog-items.md and matches its GET /catalog/items, 200, and items-array claim to routes.txt. |
| `blocks_release_for_invalid_frontmatter` | PASS | With-skill output retains four stale pages, returns blocked, and does not return ready_for_tag or stamp the valid page alone. |
| `uses_shared_contract_source` | NOT_EXERCISED | Raw trace proves docs-audit read the docs-agent frontmatter contract and that docs-site-bootstrap consumes it, but does not prove the specific check-frontmatter.mjs comparison. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=4eeffb590c55540862239ba525abaeea92dac53eb0cc46ade2b73aeecdd4049a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the confirmed audit entry, validates the valid API page, identifies all four invalid frontmatter blockers, and returns blocked without mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=271c49f62dd66effd52817502ff37451dc96136b1a531004ebbbd50610652144; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also returns a no-go result but incorrectly rejects the valid catalog-items page solely because its unverified stamp is not yet versioned.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Capture explicit evidence that docs-audit and docs-site-bootstrap use the same check-frontmatter.mjs validation logic.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
