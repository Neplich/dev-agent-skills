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
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
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
| `accepts_confirmed_audit_entry` | PASS | With-skill output accepts maintainer-confirmed v0.4.0, explicit base_ref 4a1b2c3, target_ref 7c9e2af, pre-tag phase, requested audit, and evidence inventory. |
| `rejects_standard_doc_type` | PASS | catalog-search.md is classified stale because doc_type: standard is outside the allowed enumeration. |
| `rejects_empty_related_code` | PASS | catalog-export.md is classified stale because related_code is an empty array. |
| `rejects_missing_last_verified_version` | PASS | catalog-status.md is classified stale because last_verified_version is absent. |
| `rejects_empty_owners` | PASS | catalog-bulk-update.md is classified stale because owners is an empty array. |
| `accepts_valid_api_page` | PASS | catalog-items.md is classified verified, and the output relates its declared GET /catalog/items behavior to src/catalog/routes.txt evidence. |
| `blocks_release_for_invalid_frontmatter` | PASS | The with-skill result is blocked; all four invalid pages remain stale, no ready_for_tag result is returned, and unified stamping is explicitly withheld. |
| `uses_shared_contract_source` | NOT_EXERCISED | The locked evidence does not independently prove use of docs-agent's frontmatter-contract.md or consistency with docs-site-bootstrap's check-frontmatter.mjs; those sources are absent from the fixture and not directly evidenced. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=17cfa997123693abe495c654472a553d9e360ffaecb1677295f22918b5a688cd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the confirmed audit entry, identifies all four invalid frontmatter cases, verifies the valid API page against code evidence, and blocks release without stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=ae412db7e3eb280fc105610f3684d98ce17757d436988314799ff57b81dc90a6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline incorrectly treats the affected page set as empty and recommends release despite the documented frontmatter defects.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide direct locked evidence of frontmatter-contract.md and check-frontmatter.mjs if the shared-contract-source assertion must be exercised.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
