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
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `dd84eeaf9ea9452e584f740ec00a1edde6c8e5bfae2ef83da4e9e416f2e769fe`
- metadata_sha256: `23140221449282820c7da53fcdbe46ce5ee1169aff6e90986ef0dbd09c5f9120`
- fixture_sha256: `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `289a3b63a3dcdcdc4cc6c4b994a40567f085f301732b94d5ab13b0e67247a316`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | PASS | Trace shows standards entry, granularity, change map, database/design templates, and only database/design type instructions loaded; API pages were read as authority targets. |
| `passes_design_closeout_gate` | NOT_EXERCISED | A runtime sync-report file-change event exists, but its locked content and required per-page matrix/timing evidence are not available in the delivery snapshot or raw evidence. |
| `creates_database_schema_domain_tree` | PASS | Locked delivery files contain the database root, primary database, workspace-access domain, relationships, and all three entity pages with links. |
| `refreshes_confirmed_stable_path` | PASS | The stable database path remains, its obsolete facts are replaced with current facts, it is marked unverified, and the broad workspace-access mapping is preserved. |
| `documents_current_entity_facts` | FAIL | Entity pages record current fields, role checks, uniqueness, indexes, ownership, and lifecycle facts supported by schema, code, and tests. |
| `links_relationships_bidirectionally` | FAIL | The relationships page links the entity pages, but the entity pages do not each link the required API workspace-access authority page; several also omit reciprocal links to all related entity pages. |
| `distinguishes_physical_and_logical_relations` | PASS | Mermaid and prose distinguish the two cascading physical workspace foreign keys from the service-validated logical user reference. |
| `creates_domain_component_flow_tree` | PASS | Locked delivery files contain the Design root, both domains, all three components, the acceptance flow, authorization boundary, and the flat compatibility page. |
| `keeps_reciprocal_and_authority_links` | PASS | All three component pages link the acceptance flow, the flow links all three components, and Design pages link API/database authority without duplicating full contracts. |
| `keeps_cross_domain_authority_unique` | PASS | Audit Log links to the workspace-access acceptance flow and does not duplicate its process; the acceptance flow is the sole detailed authority. |
| `updates_atomic_map_and_unverified_pages` | PASS | The locked change map preserves unknown/manual entries, adds exact source mappings with sorted closures, retains the stable page, covers the database/design subtree and reciprocal links, and all delivered pages are unverified. |
| `runs_host_checks_and_handoffs_audit` | NOT_EXERCISED | Raw command events show test:docs, build:public, and build:internal ultimately passed and internal navigation was inspected, but the audit handoff is explicitly blocked with target_release_version missing; completion of that later handoff step is therefore not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=069ee9a676b316d78571e5bfce36c7a00f4525c6351eed789148f6c9e908c706; snapshot_sha256=72fc8da393c9e12f7982f684fe0eef6ed89648f5e41c29a3f91218db26bb808b
- Behavior: Delivered a substantially complete database/design hierarchy with current facts, authority distinctions, reciprocal design flow links, normalized mappings, and real host checks; the entity-link contract is incomplete and closeout/handoff evidence is partial.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=318415604a6ba586f02f2f4366e076e9f9872358418c0ad0a6524d2bdc680e16; snapshot_sha256=b04838b28473eefa6ff71704b0bb35cad1b0342f0e91b642cb37a6f51c361619
- Behavior: Fresh baseline reports broad document synchronization and partial validation in concise prose, without the with_skill lane's detailed gate, scope, mapping, and handoff evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- links_relationships_bidirectionally: entity pages do not each provide the required API workspace-access link and complete reciprocal related-table links.
- Next: Add the required API workspace-access and complete related-table links to every entity page.
- Next: Provide the confirmed release version and complete the docs-audit handoff.
- Next: Expose the locked sync-report content if closeout-gate scoring is required.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
