# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-007-feature-database-design`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `dd84eeaf9ea9452e584f740ec00a1edde6c8e5bfae2ef83da4e9e416f2e769fe`
- metadata_sha256: `23140221449282820c7da53fcdbe46ce5ee1169aff6e90986ef0dbd09c5f9120`
- fixture_sha256: `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `289a3b63a3dcdcdc4cc6c4b994a40567f085f301732b94d5ab13b0e67247a316`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | FAIL | runner_captured_trace shows database/design instruction modules were read before the host standards entry, granularity, change map, and templates; it did not read API, ops, or product rules. |
| `passes_design_closeout_gate` | NOT_EXERCISED | No formal page or change-map write occurred, so the required runtime-only closeout matrix was not exercised. |
| `creates_database_schema_domain_tree` | NOT_EXERCISED | No delivery snapshot exists for the with_skill lane; the workflow stopped before document creation. |
| `refreshes_confirmed_stable_path` | NOT_EXERCISED | No with_skill files were written; stable-path refresh was not reached. |
| `documents_current_entity_facts` | NOT_EXERCISED | No entity pages were delivered in the with_skill lane. |
| `links_relationships_bidirectionally` | NOT_EXERCISED | No relationship or entity pages were delivered in the with_skill lane. |
| `distinguishes_physical_and_logical_relations` | NOT_EXERCISED | No database documentation was delivered in the with_skill lane. |
| `creates_domain_component_flow_tree` | NOT_EXERCISED | No Design hierarchy was delivered in the with_skill lane. |
| `keeps_reciprocal_and_authority_links` | NOT_EXERCISED | No component or flow pages were delivered in the with_skill lane. |
| `keeps_cross_domain_authority_unique` | NOT_EXERCISED | No cross-domain Design pages were delivered in the with_skill lane. |
| `updates_atomic_map_and_unverified_pages` | NOT_EXERCISED | No mappings or documentation pages were written in the with_skill lane. |
| `runs_host_checks_and_handoffs_audit` | NOT_EXERCISED | The candidate correctly stopped before host checks and audit handoff because scope and delivery-diff evidence blockers remained unresolved. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=78627caf3883728821a7f0fb4d3004e9cd00d9abbb7c0181578b0abd51d100e8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Safely blocked before writing because of unresolved scope and delivery-evidence gates, but violated the required host-contract read order.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=4600758cab39ed8386bccf8f6726d47ddd3e9e76fc95ef363c987394f5e48be4; snapshot_sha256=99ed9f1ea941511e09f18de2cf4432648323ae4c3f125e3c12b71699ab95a948
- Behavior: Fresh baseline wrote the database and Design trees and refreshed the stable database page, but reported incomplete verification and did not provide the required full delivery evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- loads_only_database_design_contracts failed because the locked trace proves the required host-contract read order was not followed.
- Next: Read the host standards entry, granularity, change map, and database/design templates before loading type-specific modules.
- Next: Resolve the confirmed-scope conflict, add the missing PM handoff fields, and provide actual delivery diff evidence before resuming.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
