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
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | FAIL | Raw trace item_11 directly reads API pages with sed, contrary to the requirement that API pages only serve as link targets and API rules not be loaded/applied. |
| `passes_design_closeout_gate` | NOT_EXERCISED | The locked trace proves a runtime report was created before formal writes and later removed, but does not expose its page-level matrix contents, timestamp, or changed-path snapshot. |
| `creates_database_schema_domain_tree` | FAIL | The database root links directly to `primary/workspace-access/` and the stable page, but does not link `database/primary/index.md`; the intermediate index is therefore not linked level-by-level from the root. |
| `refreshes_confirmed_stable_path` | PASS | The stable database path is retained, marked `last_verified_version: unverified`, and redirected to the current detailed subtree with updated unique membership, supported roles, physical workspace FKs, and logical user reference facts. |
| `documents_current_entity_facts` | PASS | All three entity pages contain current fields, constraints, indexes, owners in frontmatter, lifecycle information, membership uniqueness and role checks, invitation token uniqueness, and `expires_at`. |
| `links_relationships_bidirectionally` | PASS | The relationship page contains the Mermaid overview and links all three entity pages; each entity page links its domain, relationships, related tables, stable page, and API page. |
| `distinguishes_physical_and_logical_relations` | PASS | The Mermaid diagram and prose distinguish CASCADE physical workspace foreign keys from the service-validated logical `user_id` reference. |
| `creates_domain_component_flow_tree` | PASS | Locked delivery files include the Design root, Workspace Access and Audit Log indexes, all three requested component pages, invitation-acceptance flow, authorization boundary, and the legacy flat compatibility page. |
| `keeps_reciprocal_and_authority_links` | PASS | All three component pages link the acceptance flow; the flow links all three components; Design links the API and database authority pages without reproducing their full contracts. |
| `keeps_cross_domain_authority_unique` | PASS | Audit Log index and event-writer link to the Workspace Access-owned acceptance flow and do not duplicate its process body. |
| `updates_atomic_map_and_unverified_pages` | PASS | The locked change map preserves the manual entry, retains the stable page, adds the database/design hierarchy, reciprocal pages, authority pages, and separate invitation/repository/schema/service/audit mappings with unverified changed pages. |
| `runs_host_checks_and_handoffs_audit` | NOT_EXERCISED | Trace shows `npm run test:docs`, `npm run build:public`, and the corrected `npm run build:internal` exiting 0, but the required docs-agent:docs-audit handoff is explicitly blocked pending a confirmed release version, so the later handoff step was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=a0cac5d2d31eb165b91c2f1d7c9b5ecf1b4f0f42e1e0621e273044a17f23d467; snapshot_sha256=65ed35b84276bf34ced20d2617ec1e8780969b0c9a979a8bdbbae4e55f797f86
- Behavior: Delivered a substantially complete database/design documentation tree, refreshed the stable database path, distinguished physical and logical relationships, normalized mappings, and ran the documented site checks; however, it violated the load-scope assertion and omitted the required root-to-primary index link.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=70cdd1a91038a07017750b580b61e4a4fad487e1ac3f63b515180f9deaaee663; snapshot_sha256=b59ca1f76cf06ce200ba77db1ba390c7a42c8f87621767f3733dc3d137f176e5
- Behavior: Fresh baseline delivered much of the requested page content and navigation, but its change map remained a broad/incomplete mapping and it provided no comparable closeout-gate or audit-handoff evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill trace shows API pages were directly read.
- The database root does not link the required intermediate `database/primary/index.md` level.
- Next: Confirm the intended API-page loading boundary and add the missing database root link to `database/primary/index.md`.
- Next: After PM confirms `target_release_version`, perform the docs-agent:docs-audit handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
