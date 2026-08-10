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
- Fixture SHA-256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `216827bc3e07bc68d228647a6fadcd479f48a986964f70c0c40f48052e42886f`
- Eval definition SHA-256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- Metadata SHA-256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | With_skill explicitly accepted the maintainer-confirmed v0.4.0, base_ref 4a1b2c3, target_ref 7c9e2af, pre-tag phase, and evidence inventory. |
| `rejects_standard_doc_type` | PASS | With_skill classified catalog-search.md as stale because doc_type: standard is invalid. |
| `rejects_empty_related_code` | PASS | With_skill classified catalog-export.md as stale because related_code: [] is invalid. |
| `rejects_missing_last_verified_version` | PASS | With_skill classified catalog-status.md as stale because last_verified_version is missing. |
| `rejects_empty_owners` | PASS | With_skill classified catalog-bulk-update.md as stale because owners: [] is invalid. |
| `accepts_valid_api_page` | PASS | With_skill marked catalog-items.md verified, stated its frontmatter was valid, and checked its claim against src/catalog/routes.txt. |
| `blocks_release_for_invalid_frontmatter` | PASS | With_skill returned blocked, retained four stale pages in scope, and stated that no unified stamp was produced and no tag should be created. |
| `uses_shared_contract_source` | NOT_EXERCISED | The raw trace proves frontmatter-contract.md was read, but does not prove consistency with a delivered check-frontmatter.mjs implementation; the locked fixture also lacks that host implementation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=568a97406ca216cbcaa15e87bac2e1a19e597c4bd909f5de3d71a398b99e0f9d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepted the confirmed audit entry, classified all four invalid pages as stale, accepted the valid catalog-items page, and blocked release without stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=a6b6b1ca26f010edc5a07c5b5bc3ebe4e572fb02522e33d658b5650e5aa0d38d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also blocked release and found the four invalid pages, but incorrectly treated catalog-items.md as failing because last_verified_version was unverified.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide locked evidence of the delivered check-frontmatter.mjs logic if the shared-contract consistency assertion must be exercised.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
