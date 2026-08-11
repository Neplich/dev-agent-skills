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
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
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
| `accepts_confirmed_audit_entry` | PASS | Raw trace shows release-entry.md was read and the maintainer-confirmed v0.4.0, base_ref 4a1b2c3, target_ref 7c9e2af, pre-tag phase, and evidence inventory were accepted. |
| `rejects_standard_doc_type` | PASS | Candidate output classifies catalog-search.md as stale because doc_type: standard is invalid. |
| `rejects_empty_related_code` | PASS | Candidate output classifies catalog-export.md as stale because related_code is empty. |
| `rejects_missing_last_verified_version` | PASS | Candidate output classifies catalog-status.md as stale because last_verified_version is missing. |
| `rejects_empty_owners` | PASS | Candidate output classifies catalog-bulk-update.md as stale because owners is empty. |
| `accepts_valid_api_page` | PASS | Raw target-tree evidence shows catalog-items.md has all required frontmatter fields with valid values; the candidate reports it entering fact review and identifies insufficient API evidence rather than incorrectly stamping it. |
| `blocks_release_for_invalid_frontmatter` | PASS | The candidate retains four invalid pages as stale, reports blocked, and explicitly does not return ready_for_tag or stamp a valid subset. |
| `uses_shared_contract_source` | NOT_EXERCISED | Raw trace proves the shared frontmatter-contract.md was read and used, but does not prove comparison with docs-site-bootstrap's check-frontmatter.mjs logic. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=b26b12ec9b5a92821f43b75b4f6fa02700bde0ec643ffd1f20f40ca40aadd3e4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performs the confirmed pre-tag audit, identifies all four invalid frontmatter blockers, preserves the valid page for fact review, and returns blocked without mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=a283b981b7d713e6d02651a50cea1ab459ef2d128db1469e5721f0ca58868c90; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also reaches a no-go result and identifies the invalid pages, but provides less contract/process evidence and less precise fact-layer handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Exercise or capture evidence that docs-audit and docs-site-bootstrap use the same check-frontmatter.mjs implementation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
