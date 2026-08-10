# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-013-version-normalization-boundaries`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970` from `agents/docs/test/docs-audit/evals/workspace/eval-013-version-normalization-boundaries`.
- Fixture SHA-256: `1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970`
- Prompt SHA-256: `e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `3cb4db02fceb3a963ab35cfa46d9bd95146e58bed4f92e90064a4aa2fe2f0404`
- Eval definition SHA-256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | With-skill output normalizes prefixed and unprefixed values while retaining prerelease, build metadata, and case-sensitive identity distinctions. |
| `enforces_each_source_contract` | PASS | With-skill output evaluates the listed raw forms, missing values, selector counts, and extractor mismatch without repairing or cross-filling sources. |
| `reports_all_version_blockers` | PASS | With-skill output reports all fixture blocker categories and concludes both pre-tag and post-tag are blocked. |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | The pre-tag audit is blocked before an inventory is generated; the output explicitly states that no same-source binding is available for post-tag consumption. |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | Because no inventory was generated before blocking, deterministic inventory-integrity evidence cannot be produced. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=2e96cbeda8f43950ecdc700975f3d4dfc89d0ed3f4827505f5ef36361e55a24a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserves version identity, enforces source contracts, reports all blockers, and appropriately stops before inventory-dependent post-tag checks.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=b8f10c5079b179daf1f01d43fa64b65cdabeaa4dd60446ab7cc2344dc5734134; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a plausible baseline audit and reports many post-tag discrepancies, but lacks the stronger inventory and gate handling shown by with_skill.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide a valid pre-tag inventory and binding evidence to exercise post-tag inventory consumption.
- Next: Provide reproducible integrity evidence for the bound inventory to exercise tamper detection.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
