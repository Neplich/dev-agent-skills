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
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- metadata_sha256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- fixture_sha256: `1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3cb4db02fceb3a963ab35cfa46d9bd95146e58bed4f92e90064a4aa2fe2f0404`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | FAIL | The with_skill output preserves the full target identity and rejects case, prerelease, and build-metadata changes, but it never states that the prefixed and unprefixed observations in set A map to the same complete identity. |
| `enforces_each_source_contract` | PASS | It gives source-by-source observations and blockers, rejects malformed raw values, and reports the extractor mismatch without silently filling values from other sources. |
| `reports_all_version_blockers` | PASS | It reports the missing, malformed, duplicate, unresolved, and extractor-contract blockers and gives blocked conclusions for both pre-tag and post-tag stages. |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | The output states that no pre-tag handoff, candidate audit record, or consumable binding exists, so post-tag consumption of a generated inventory was not reached. |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | The output states that no normalized digest or candidate record exists, so deterministic inventory-integrity evidence could not yet be produced. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=7d9f9b29a8a3a6ed40d531b21f94be6ed5cd02db2f446506f5c1000474945677; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a detailed blocked pre-tag/post-tag audit with per-source failures, but omits the set-A prefixed/unprefixed identity conclusion.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=1c86d157d2d7fcd2f82e1f019cb0ff7864aa486b14da8ccd39ee0c0394d6f640; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also reports the major post-tag blockers and mentions set A, but lacks the with_skill audit's stronger repository and inventory-binding analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- preserves_complete_version_identity
- Next: Explicitly map the prefixed and unprefixed set-A observations to the same complete, case-sensitive identity while retaining the raw-form distinction.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
