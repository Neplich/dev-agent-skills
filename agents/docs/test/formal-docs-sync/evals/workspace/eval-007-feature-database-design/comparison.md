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
- Fixture SHA-256: `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81`
- Prompt SHA-256: `97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `289a3b63a3dcdcdc4cc6c4b994a40567f085f301732b94d5ab13b0e67247a316`
- Eval definition SHA-256: `dd84eeaf9ea9452e584f740ec00a1edde6c8e5bfae2ef83da4e9e416f2e769fe`
- Metadata SHA-256: `23140221449282820c7da53fcdbe46ce5ee1169aff6e90986ef0dbd09c5f9120`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | FAIL | Trace shows the candidate read docs/site/api/workspace-access.md, despite the requirement to load only database/design modules and use API pages only as link targets. |
| `passes_design_closeout_gate` | NOT_EXERCISED | The trace proves a runtime report file was created and later deleted, but does not expose its matrix content or prove the required ordering evidence. |
| `creates_database_schema_domain_tree` | PASS | Locked delivery files contain the database root, primary/database-domain indexes, relationships page, and three entity pages. |
| `refreshes_confirmed_stable_path` | PASS | The stable page remains at docs/site/database/workspace-access.md, is marked unverified, and documents current uniqueness, roles, physical workspace FKs, and logical user reference. |
| `documents_current_entity_facts` | PASS | Entity pages document current fields, constraints, indexes, ownership metadata, and lifecycle/read-write facts supported by schema, code, and tests. |
| `links_relationships_bidirectionally` | FAIL | Relationships link all three entity pages, but the Workspaces and Memberships pages do not provide the required API link, and Workspaces does not link the invitations table. |
| `distinguishes_physical_and_logical_relations` | PASS | Mermaid and prose distinguish cascading physical workspace foreign keys from the service-validated logical user_id reference. |
| `creates_domain_component_flow_tree` | PASS | Locked Design snapshots contain the root, both domains, three required components, the acceptance flow, and authorization boundary. |
| `keeps_reciprocal_and_authority_links` | PASS | Components link the acceptance flow, the flow links all three components, and Design pages link API/database authorities without duplicating their contracts. |
| `keeps_cross_domain_authority_unique` | PASS | Audit Log links the workspace-access acceptance flow as the sole authoritative cross-domain process and does not duplicate its正文. |
| `updates_atomic_map_and_unverified_pages` | PASS | All captured database/design pages and six relevant map entries are present, unverified, normalized, and include the stable page plus the confirmed subtree and cross-type closure. |
| `runs_host_checks_and_handoffs_audit` | NOT_EXERCISED | The three host commands have captured exit-0 results, but the complete link verification and docs-agent:docs-audit handoff cannot be confirmed because target release context is missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=2a591301d4576e7bf0a62d9bb65bfbc6f9b1c9d88ca021a7bea5826aeb64f8a4; snapshot_sha256=15840732834a3f6360fe57a2d2187fb0b1ace8d08d153aca112e31401fba872a
- Behavior: Delivered the requested database and Design trees with current facts, authority links, normalized mappings, and passing host checks, but violated the loading restriction and left reciprocal entity links incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=a0ac14c8fc9269410a6219184f6b3ad5a3a73b8f68dc072beca42077c74992ed; snapshot_sha256=446942bde6a4aaa86561f0ba6741ebc47aba10558fef88f27f104b81de1ef919
- Behavior: Fresh baseline reported a broad documentation sync and test pass, but provided less evidence of the required gates, current facts, atomic mappings, and handoff state.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill trace shows an API page being read despite the database/design-only loading requirement.
- Several entity pages lack the required reciprocal API and related-table links.
- Next: Restrict discovery to database/design modules and treat API pages only as link targets.
- Next: Add reciprocal API and related-table links to every entity page.
- Next: Obtain confirmed release context and complete the docs-audit handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
