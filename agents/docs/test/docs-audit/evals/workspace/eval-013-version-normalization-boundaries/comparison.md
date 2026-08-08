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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `3cb4db02fceb3a963ab35cfa46d9bd95146e58bed4f92e90064a4aa2fe2f0404`
- Eval definition SHA-256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | with_skill explicitly equates the prefixed and unprefixed Observation A values as the same complete SemVer identity, retaining prerelease and build metadata, and rejects case-changed or metadata-dropped candidates. |
| `enforces_each_source_contract` | PASS | with_skill reports each observed source failure, including raw-prefix violations, missing values, invalid package SemVer, index multiplicity, zero selector resolution, and extractor mismatch, without silently repairing values. |
| `reports_all_version_blockers` | PASS | with_skill covers the missing, malformed, ambiguous, extractor, and identity discrepancies and states that both pre-tag and post-tag checks are blocked. |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | with_skill states pre-tag cannot form a consumable canonical inventory and post-tag therefore cannot consume the same immutable identity. Per the fixture rule, this later binding check is NOT_EXERCISED. |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | with_skill states no canonical pre-tag inventory was generated. Per the fixture rule, deterministic integrity evidence cannot yet be produced, so this is NOT_EXERCISED. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=436fdcf02801a2fed6c1bb52e5909f3594ef9f52c90a7cc1ab9216f4cd1f15f4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies complete version identity, enforces source-specific raw and extraction contracts, reports the blockers, and explains that no post-tag inventory binding is available because pre-tag is blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=8ca2de0c5cb365248c64ac3123f3c7541a2bf3b13d6853460986a856ece722af; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a basic blocker list and post-tag failure conclusion, but gives less complete source-contract, identity, and inventory-binding analysis than with_skill.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | NOT_EXERCISED | with_skill correctly paused for required maintainer confirmation and review refs before producing audit conclusions; no identity judgment was made. |
| `enforces_each_source_contract` | NOT_EXERCISED | with_skill did not proceed to source-by-source validation pending the requested confirmation and refs. |
| `reports_all_version_blockers` | NOT_EXERCISED | with_skill did not produce pre-tag or post-tag blocker conclusions because the audit was blocked before review. |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | No inventory was generated; the candidate explicitly requested the missing prerequisite inputs before proceeding. |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | No inventory was generated, so deterministic integrity evidence could not yet be produced. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=ade4b80f3730f155c5b3de73909af290c5e7a6d8042fc5f97479a2aef93465ba; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly paused the interactive workflow and requested maintainer-confirmed target version plus base, target, and post-tag refs before auditing; no workspace mutation occurred.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=07d5df4837d8d6961ca49c46e141b356b449c3d393bda650e51714be17a3fd01; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced pre-tag and post-tag conclusions, identifying several fixture blockers, but did not fully establish the required source contracts and identity handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the requested maintainer confirmation and refs, then rerun the audit to exercise the remaining assertions.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | With-skill output normalizes prefixed and unprefixed forms to the same identity while preserving case, prerelease, and build metadata. |
| `enforces_each_source_contract` | PASS | It identifies source-specific raw-form failures, missing/ambiguous selector results, and the non-deterministic extractor without repairing values from other sources. |
| `reports_all_version_blockers` | PASS | It covers source-list drift, invalid target/tag/notes/package values, missing marketplace/index values, empty releases data, duplicate index matches, selector failure, comparison mismatches, and their blocked pre-tag/post-tag consequences. |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | The raw evidence shows pre-tag execution was blocked before inventory generation. The output correctly states that no bound inventory exists for post-tag consumption. |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | Because no pre-tag inventory was generated, deterministic inventory-integrity evidence cannot be produced; the output correctly reports the missing audit foundation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=8266b439f93ec76b7212332ac7617609919a4bb16d4012fe3d9de6fb06b874c3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a comprehensive read-only audit, preserves version identity semantics, identifies blockers and inventory drift, and correctly blocks both phases.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=dc10c6d5f2961be35fbb62848ac2a2494613b1d45e3c950c7a803499e09305d3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a partial, mostly post-tag anomaly review but does not establish complete per-source validation or inventory binding.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | With-skill output normalizes prefixed and unprefixed Observation A values to the same identity while preserving the case-sensitive build metadata. |
| `enforces_each_source_contract` | PASS | It evaluates each Observation B source's raw-form violation or absence, reports selector/extractor mismatches, and does not repair or substitute invalid values. |
| `reports_all_version_blockers` | PASS | It covers the fixture's missing, malformed, ambiguous, extractor, and identity-conflict blockers and concludes both pre-tag and post-tag checks are blocked. |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | Because pre-tag execution is blocked and no trusted candidate record or handoff exists, the output states that no bound pre-tag inventory is available for post-tag consumption. |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | No inventory was generated due to the pre-tag blockers, so deterministic integrity evidence cannot yet be produced; the output does not claim otherwise. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=4cc5c651dc00a432477682a23e64ff0d52b028f2c1c986ad523a2008335d47f9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the normalized identity, per-source contract violations, all blockers, and the absence of a consumable pre-tag inventory.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=2ab758a0b3f1bf439b76187eab9525729e3338f1ea7dc186fb6e171163fc68f3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognized many post-tag defects and concluded failure, but lacked complete source-by-source identity and workflow-binding analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Resolve the pre-tag blockers, generate a discoverable inventory and handoff, then rerun post-tag binding and integrity checks.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2693e17491076fba1135d0124a7b615c0e9ee9a10433dc23758069f188fcfa26`
- Skill overlay SHA-256: `c603d7558c1318dc2ab94c6a553a18ea82a33f4f323645aa19f7bdfc3da4b02d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | FAIL | With-skill output identifies the confirmed full target and rejects malformed candidates, but does not state that the valid prefixed and unprefixed observations in set A represent one equivalent complete identity. |
| `enforces_each_source_contract` | PASS | It reports per-source raw-form problems, missing/empty selector results, extractor mismatch, and explicitly rejects comparison candidates as substitutes. |
| `reports_all_version_blockers` | PASS | It covers the fixture's missing, malformed, non-unique, selector-resolution, extractor, and candidate-mismatch blockers, and marks both pre-tag and post-tag stages blocked. |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | The output states that no pre-tag handoff/candidate record exists, so there is no bound inventory available for post-tag consumption. |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | The output states that no canonical inventory digest exists because pre-tag inventory was never generated. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=ca2f50baf3529d7555fa7bc26a2c0f6c01883c231bff7f3cbd8e0932793a5e82; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks both stages, reports the observed source and extraction failures, and identifies that no post-tag-bound inventory or integrity digest exists; it omits an explicit equivalence statement for valid prefixed/unprefixed observations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=0dd6aa490b21a6931a89bc125b636b089bea45f520bac05d8a15b9a90eec63a1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reports pre-tag as passing despite the fixture's valid identity distinction and reports post-tag blockers, but omits the blocked pre-tag handoff/inventory state.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not explicitly preserve and equate the complete valid prefixed/unprefixed version identity from observation set A.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2693e17491076fba1135d0124a7b615c0e9ee9a10433dc23758069f188fcfa26`
- Skill overlay SHA-256: `c603d7558c1318dc2ab94c6a553a18ea82a33f4f323645aa19f7bdfc3da4b02d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6f3c010dbdde60de256381f298da12ba27ac671f9dba533a58464c18d69bbe20`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | 输出明确将 prefixed 与 unprefixed 形式归一化为同一版本，并保留了 rc 与 build metadata；同时识别大小写和缺失 build metadata 导致的不一致。 |
| `enforces_each_source_contract` | PASS | 输出逐项列出 target、tag、notes、index、releases、marketplace、package 的非法、缺失、非唯一或 extractor 不一致问题，并未用其他来源静默补值或修复。 |
| `reports_all_version_blockers` | PASS | 覆盖了 fixture 中的前缀错误、双前缀、缺失值、空值、非唯一 selector、0 匹配、非 SemVer、大小写/metadata identity 不一致及 extractor 不一致，并分别给出 pre-tag 与 post-tag blocked 影响。 |
| `binds_pre_and_post_tag_inventory` | FAIL | 输出说明无法绑定并消费同一份 pre-tag inventory，但没有说明 pre-tag 如何固定完整来源集合、post-tag 如何消费该绑定，也未明确禁止通过扫描多版本来源进行选择。 |
| `makes_inventory_integrity_reproducible` | FAIL | 输出给出了 refs 和工作区状态，但没有给出确定性的 inventory integrity 证据，也没有说明来源集合、定位契约或顺序变更时如何阻止阶段成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=06f747d8604216332d0f39e470f6fb14a9806eab403efff782fa5c4140836d11; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别版本 identity、逐来源失败和 pre/post 阻断条件，保持工作区未修改；但缺少 inventory 绑定机制说明及确定性的完整性证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=419e1a7da7b913f1d9d1fe87d28313d57e771a282914e6c1c1269c41f1d9d209; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了大部分 post-tag 版本错误并保持工作区未修改，但将 pre-tag 结论判为条件通过，未建立完整、可复现的 inventory 绑定与完整 blocker 审计。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未满足同一 pre-tag inventory 在 post-tag 消费及禁止扫描挑选的说明要求。
- 未提供可独立重算的 inventory integrity 证据及篡改阻断规则。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3a4b2d479eb82f158ff553c0de29c5500ea8c145d26001e791b067066084b30c`
- Skill overlay SHA-256: `d0676af2589cdd9cf03815afd90d790a2c8a481c8a6fd7b57fcb75ac8689ba58`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6f3c010dbdde60de256381f298da12ba27ac671f9dba533a58464c18d69bbe20`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | with_skill 识别 prefixed/unprefixed 形式可归一为同一 SemVer，并保留了完整的 prerelease 与 build metadata。 |
| `enforces_each_source_contract` | PASS | with_skill 逐项指出 target、tag、notes、index、releases、marketplace、package 的缺失或非法观测，并指出 selector resolution 为 0、extractor 不匹配，未静默修复或跨来源补值。 |
| `reports_all_version_blockers` | PASS | with_skill 覆盖了前缀错误、缺失 v、缺失索引、空值、缺失 marketplace、非法 package、候选 identity 不一致、重复匹配、解析为 0 和 extractor 不一致，并说明 pre-tag 与 post-tag 均 blocked。 |
| `binds_pre_and_post_tag_inventory` | FAIL | with_skill 说明缺少 pre-tag handoff/candidate record，但没有说明 pre-tag 固定完整来源集合、post-tag 消费同一绑定，或禁止通过扫描多版本来源来重新选择。 |
| `makes_inventory_integrity_reproducible` | FAIL | with_skill 没有给出确定性的 inventory integrity 证据，也没有说明来源集合、定位契约或顺序被改变时如何阻止阶段成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=7540cf48d51449f934019fbd9d0452d1b86a565b58b085ae1af94e97845af167; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 更严格地将缺少 handoff、来源文件和发布后证据判为 blocked，并覆盖了观测集 B 的失败项，但遗漏了来源绑定和 inventory integrity 要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=4605776cda035b6d0e50fc699a0220399c235d65e36dc3e4853e2d4ef5f5da65; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并报告了主要 pre-tag/post-tag 版本来源问题，但未建立绑定库存或可重算的完整性机制。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- binds_pre_and_post_tag_inventory 未说明同一绑定来源集合如何贯穿 pre-tag 与 post-tag，也未禁止扫描挑选多版本来源。
- makes_inventory_integrity_reproducible 未提供确定性 inventory integrity 证据及篡改阻断规则。
- Next: 明确记录并固定 pre-tag 的完整来源集合、定位契约与顺序，post-tag 仅消费该绑定。
- Next: 提供可独立重算的 inventory integrity 证据，并规定完整性变化时阻止阶段成功。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3a4b2d479eb82f158ff553c0de29c5500ea8c145d26001e791b067066084b30c`
- Skill overlay SHA-256: `d0676af2589cdd9cf03815afd90d790a2c8a481c8a6fd7b57fcb75ac8689ba58`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6f3c010dbdde60de256381f298da12ba27ac671f9dba533a58464c18d69bbe20`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `28de521676f44fb26d98a8943e30e638b7117fde8c52e2e6bdc9323fd9003961`
- Runtime SHA-256: `e054983e5b847c0b5102be505d299683dafcc043b1cc5f0db5fafb24d083ee5b`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | FAIL | with_skill does not establish prefixed and unprefixed forms as one complete identity; it instead calls Observation A inconsistent and omits an explicit identity-preserving normalization. |
| `enforces_each_source_contract` | FAIL | with_skill lists several bad observations but does not evaluate each source's raw-form, selector, and extractor contract or explicitly rule out cross-source repair. |
| `reports_all_version_blockers` | FAIL | with_skill omits blocker details including the index match count, releases selector resolution count, extractor drift, and both comparison-candidate identity differences, so it does not cover all fixture categories and impacts. |
| `binds_pre_and_post_tag_inventory` | FAIL | with_skill says no trusted pre-tag authority exists and mentions a future same-binding review, but does not explain a fixed complete source inventory consumed by post-tag verification. |
| `makes_inventory_integrity_reproducible` | FAIL | with_skill provides no deterministic inventory-integrity evidence or mutation-detection rule for changed sources, locators, selectors, extractors, or ordering. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=a0ea94fea936baf7100db9c7a910046392a46c659eeb9d9b3d434e94b519c5db; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Concludes both lanes are blocked and identifies missing documentation/runtime evidence plus several Observation B failures, but omits required identity, per-source contract, inventory-binding, and integrity results.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=d5be2ee64fd077471ad8f38627f16a36720b03d82e9b3c40283a4671260a4b40; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline identifies many observed version failures and the pre/post outcomes, but lacks complete source-contract, binding, and reproducible-integrity analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- All five with_skill assertions are materially unsatisfied; the output is incomplete for the requested semantic audit despite correctly reporting blocked outcomes and no workspace mutation.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6f3c010dbdde60de256381f298da12ba27ac671f9dba533a58464c18d69bbe20`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `a6701d093076bc07d26c7e813151915b2b1a25f501428e58ba88c24bfe3d6c6e`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | With-skill output correctly normalizes prefixed and unprefixed Observation A values to the same complete identity, retaining prerelease and build metadata. |
| `enforces_each_source_contract` | PASS | With-skill output identifies source-specific raw-form violations, missing/ambiguous selector results, invalid SemVer, and extractor mismatch without silently repairing or cross-filling values. |
| `reports_all_version_blockers` | PASS | With-skill output covers the fixture's missing, malformed, ambiguous, extractor, and identity-mismatch blockers and marks both pre-tag and post-tag phases blocked. |
| `binds_pre_and_post_tag_inventory` | FAIL | It states that pre-tag authority is missing and the post-tag chain cannot be bound, but does not explain how pre-tag fixes the complete source inventory, how post-tag consumes that same binding, or that scanning among multiple versions is forbidden. |
| `makes_inventory_integrity_reproducible` | FAIL | The output provides Git tree and cleanliness observations but no deterministic inventory-integrity evidence and no explicit rule that altered source membership, locator contracts, or ordering would block phase success. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=2ac2469d507d9ee7d8408db16295205a740f87d71edac26238982f10ac545a7a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks both phases and identifies the fixture's source-level failures, but omits the required binding and reproducible inventory-integrity behavior.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=e19760e37accf7995cd3938f386e54007189c2873bf2d7e460eb46dc28f20d3f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies many post-tag blockers and preserves the full version identity, but declares pre-tag passed despite missing binding/inventory evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not explain or demonstrate binding one complete pre-tag source inventory to post-tag verification.
- The with_skill output lacks deterministic inventory-integrity evidence and tamper-detection rules.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6f3c010dbdde60de256381f298da12ba27ac671f9dba533a58464c18d69bbe20`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | FAIL | With-skill output does not explicitly establish prefixed/unprefixed equivalence while preserving the complete prerelease and build identity. |
| `enforces_each_source_contract` | FAIL | It reports several raw-value failures and the extractor mismatch, but does not provide a complete per-source selector/extractor validity judgment or explicitly reject cross-source supplementation/silent repair. |
| `reports_all_version_blockers` | FAIL | It covers most Observation B failures but omits both comparison candidates and their identity mismatches. |
| `binds_pre_and_post_tag_inventory` | FAIL | It lists declared and observed sources but does not explain that post-tag verification consumes the same fixed pre-tag inventory or prevent multi-version source selection. |
| `makes_inventory_integrity_reproducible` | FAIL | No deterministic inventory-integrity evidence or explicit tamper-detection/blocking rule is provided. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=a1fe8b987dbd86dc75d3e1fdc346419cd64fcb5ce9235571d56a998558fbadf0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly concludes both pre-tag and post-tag checks are blocked and identifies most observed failures, but omits several required semantic audit results.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=a994edefa177f8ddc99911760edbeaeec2f370db0a5947272c8ca7770305517b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the overall blocked status and many version failures, but lacks complete source-contract and inventory-binding detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output omits required identity, per-source contract, complete blocker, inventory-binding, and reproducible-integrity findings.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6f3c010dbdde60de256381f298da12ba27ac671f9dba533a58464c18d69bbe20`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | with_skill 将带 v 与不带 v 的 Observation set A 值归入同一完整版本，并明确保留大小写与 +Build.7 构建元数据；与 fixture 第 21–22 行一致。 |
| `enforces_each_source_contract` | FAIL | with_skill 列出了 Observation set B 的多项非法值及 extractor identity 不匹配，但没有逐来源核验 selector、locator 和 extractor 契约，也未明确证明未跨来源补值或静默修复；fixture 第 9–17、25–36 行要求的逐来源契约审计未完整呈现。 |
| `reports_all_version_blockers` | PASS | with_skill 覆盖了 target、tag、notes、index 缺失与重复、releases 空值和解析数为 0、marketplace 缺失、package 非 SemVer、比较候选差异及 extractor 不匹配，并给出 pre-tag 不放行与 post-tag blocked 结论；对应 fixture 第 25–36 行。 |
| `binds_pre_and_post_tag_inventory` | FAIL | with_skill 没有说明 pre-tag 如何固定完整来源集合、post-tag 如何消费同一绑定集合，也没有说明多版本来源不得通过扫描挑选；fixture 明确区分 pre_tag_declared_source_ids 与 post_tag_observed_source_ids（第 4–7 行）。 |
| `makes_inventory_integrity_reproducible` | FAIL | with_skill 未提供确定性的 inventory integrity 证据（如可重算的来源集合、定位契约或顺序完整性证明），也未说明这些内容改变时如何阻止阶段成功。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=4a047bf803bda88c340a32987e87701ee79fd5e56369f9207131d5b68ed3a06b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别完整版本 identity 和大部分发布后 blocker，并得出不放行结论；未覆盖逐来源契约闭环、绑定来源集合和可重算完整性证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=9f0f6a43a7a7dac543a30e1f84824f281272172745722d1fd5da4de7b35e4542; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 Observation set A 的前缀差异和 Observation set B 的主要失败，但承认预发布仅有聚合观察值，未完成逐源闭环。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- enforces_each_source_contract
- binds_pre_and_post_tag_inventory
- makes_inventory_integrity_reproducible
- Next: 补充逐来源 selector、locator、extractor 与 raw-form 核验及禁止补值/静默修复的结论。
- Next: 明确固定 pre-tag 来源集合并让 post-tag 复核消费同一绑定，禁止扫描挑选多版本来源。
- Next: 提供可独立重算的 inventory integrity 证据，并定义集合、契约或顺序变化时的阻断规则。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6f3c010dbdde60de256381f298da12ba27ac671f9dba533a58464c18d69bbe20`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | with_skill 将带 v 与不带 v 的版本归一化为同一完整 identity，并保留 rc.1 与 +Build.7；同时拒绝大小写、构建元数据和预发布部分不同的候选。 |
| `enforces_each_source_contract` | PASS | with_skill 逐项列出 target、tag、notes、index、releases、marketplace、package 的观测问题，指出缺失、非法 raw form、selector 解析为 0、非唯一匹配及 extractor identity 不一致，未将其他来源值作为补值。 |
| `reports_all_version_blockers` | PASS | with_skill 覆盖了 fixture 中的缺失、非法格式、大小写/前缀错误、identity 差异、selector 非唯一或无解析结果、extractor 不一致及 pre-tag 来源集合问题，并分别判定 pre-tag 与 post-tag blocked。 |
| `binds_pre_and_post_tag_inventory` | FAIL | with_skill 指出 pre-tag 缺少可验证 handoff，但没有说明应如何固定完整来源集合、如何让 post-tag 消费同一绑定，或为何多版本来源不能通过扫描挑选。 |
| `makes_inventory_integrity_reproducible` | FAIL | with_skill 仅指出 extractor identity 不一致会破坏可复现性；没有给出确定性的 inventory integrity 证据，也没有说明来源集合、定位契约或顺序变更时的阻断规则。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=582eefc3872decc8188039db14b9d6123afc0c1fe9fc12d6f50f3e36095ee39c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 更完整地识别并阻断 pre-tag/post-tag 证据问题，但未满足来源绑定和 inventory integrity 可复现性要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=268fab184efced03c3c678997644aa1ae17fed5fdc378736e78ee2c55baa0bea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了主要 post-tag 版本问题，但将 pre-tag 判为通过且未充分逐源审查。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未说明 pre-tag 固定来源集合与 post-tag 同绑定复核机制。
- with_skill 未提供确定性的 inventory integrity 证据及其篡改阻断规则。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-013-version-normalization-boundaries`
- Scenario: 多来源版本 identity、selector 边界与跨阶段 inventory 完整性
- Review context: issue #177 sub-batch 4b

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 22:48:16 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-audit/round-1/`
- Assertions: 5，全部实际触发

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `preserves_complete_version_identity` | PASS | PASS | 两条产物均确认 `v1.2.0-rc.1+Build.7` 为完整 identity，并指出前缀、大小写、预发布标识和 build metadata 不能被丢失或视为等价（with_skill: `result.txt:5,7,17`；without_skill: `result.txt:6-8,23`）。 |
| `enforces_each_source_contract` | PASS | PASS | 均按来源识别 raw form、selector/extractor 和缺失值问题；未用其他来源补值，也未静默修复非法值（with_skill: `result.txt:7,12-16`；without_skill: `result.txt:8,16-25`）。 |
| `reports_all_version_blockers` | PASS | PASS | 两条产物均覆盖大小写/前缀非法、缺失、非 SemVer、selector 解析失败、重复匹配、extractor 不一致及 identity 差异，并分别给出发布前和发布后的失败结论（with_skill: `result.txt:8,12-18`；without_skill: `result.txt:10,14-27`）。 |
| `binds_pre_and_post_tag_inventory` | FAIL | FAIL | 产物仅列出 pre-tag 的 6 个来源和 post-tag 的 7 个来源，没有说明 pre-tag 如何固化完整来源集合，也没有说明 post-tag 消费同一绑定；with_skill: `result.txt:6`，without_skill: `result.txt:5`。 |
| `makes_inventory_integrity_reproducible` | FAIL | FAIL | 产物提到 selector 数量、匹配数量和 extractor identity，但没有给出可独立重算的 inventory integrity 证据，也没有说明来源集合、定位契约或顺序被篡改时如何阻止阶段成功（with_skill: `result.txt:13-14,18`；without_skill: `result.txt:19-25,27`）。 |

未满足断言（with/without 任一 FAIL）：``binds_pre_and_post_tag_inventory``、``makes_inventory_integrity_reproducible``



## Leakage Surface Analysis

重做前，prompt、assertions 和 `version-cases.md` 直接给出前缀算法、完整 expected identity、case/build 判定、全部 blocker、六字段 inventory、canonical serialization、预计算 digest 和 pre/post producer-consumer 答案。

重做后，fixture 只保留 source locator table、pre/post observed source ids 和 observation sets，不给 expected identity、valid/invalid 标签、canonical rules、digest 或阶段裁定。

## Redesign

- prompt 只要求分别给出两阶段 identity、全部 blocker、持久化证据与结论。
- assertions 改为完整 identity、source contract、全量 blocker、跨阶段 inventory binding 和 reproducible integrity 五个语义结果。
- 删除预计算 digest、canonical 答案、invalid 原因标签和 producer/consumer 指令。
- 增加 phase-boundary 变体：pre-tag declared source ids 缺少 future `tag`，post-tag observations 才出现该来源。
- 保留多版本 index 的双匹配、absent JSON Pointer 与 unknown extractor 原始观测。
- 将历史 issue locator 替换为 `docs-agent:release-notes-gen`。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `preserves_complete_version_identity` | PASS | PASS | 两臂均保留 prerelease、build metadata 与大小写。 |
| `enforces_each_source_contract` | PASS | PASS | 两臂均逐来源拒绝 raw-form、selector 与 extractor 问题。 |
| `reports_all_version_blockers` | PASS | PASS | 两臂均覆盖缺失、非法、歧义和 identity 不一致类别。 |
| `binds_pre_and_post_tag_inventory` | PASS | FAIL | skill arm要求 pre-tag 固定 future tag pending source；baseline 将 tag 当作 post-tag 新增来源。 |
| `makes_inventory_integrity_reproducible` | PASS | FAIL | skill arm给出 canonical JSON、稳定排序、digest 重算和篡改阻塞；baseline 只有字段列表。 |

## Fresh Validation Method

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 两臂锁定前只读取同一 prompt 和 `version-cases.md`，未读取 assertions、expected output、旧 comparison 或对方输出。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm隔离这些内容。
- fresh judge 在 SHA-256 锁定后才读取 assertions。
- with-skill SHA-256：`210a4836d46b095ef9ad18943784c5dcc55df4c9693a46a1351010c3bdab11b3`；without-skill：`e053ee70e2330b8c7b5138a57bdb1ce189170489dd169b5d182bf2fd8a068d9b`。

## Failures And Limitations

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- with-skill 无失败；Coverage FULL。
- source table 仍暴露 raw forms、selector 和 extractor，所以 baseline 可恢复 3/5；区分度来自跨阶段 future-tag binding 与 canonical integrity。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。
