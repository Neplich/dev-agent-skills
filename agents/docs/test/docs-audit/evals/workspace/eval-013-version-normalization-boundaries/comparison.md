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
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- metadata_sha256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- fixture_sha256: `1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3cb4db02fceb3a963ab35cfa46d9bd95146e58bed4f92e90064a4aa2fe2f0404`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | With_skill normalizes the single legal `v` prefix while retaining prerelease and build metadata, and distinguishes case changes and missing build metadata as different identities. |
| `enforces_each_source_contract` | PASS | With_skill evaluates the declared sources and observed values by source, identifies missing paths, invalid raw forms, selector resolution failure, duplicate index matches, and extractor identity drift without repairing values. |
| `reports_all_version_blockers` | PASS | With_skill reports the pre-tag block and post-tag blockers, including tag state, inventory drift, missing source files, invalid observations, duplicate matches, selector failure, and complete-identity mismatches. |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | The candidate states that no complete consumable binding was formed because the input was blocked before inventory generation; therefore post-tag consumption of a bound inventory was not exercised. |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | The candidate states that key source objects are missing and that blob/hash evidence cannot be obtained; deterministic inventory-integrity evidence was therefore not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=a698c4caa7bf9233b74490146b834c2a69ab9dde9a1bc4ec1a24d497194e2b13; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks both conclusions, preserves complete version identity, evaluates source-specific failures, and reports the inventory-binding precondition.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=267a1018be1a4d3c3b640ed605cde273c904adfb7e733d343d82ed119ada47e9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline identifies many post-tag value failures but treats the pre-tag state as conditionally passing and does not establish the same inventory-binding or repository-object blockers.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
