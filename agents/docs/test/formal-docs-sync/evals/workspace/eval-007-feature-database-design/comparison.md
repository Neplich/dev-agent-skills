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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `289a3b63a3dcdcdc4cc6c4b994a40567f085f301732b94d5ab13b0e67247a316`
- Eval definition SHA-256: `dd84eeaf9ea9452e584f740ec00a1edde6c8e5bfae2ef83da4e9e416f2e769fe`
- Metadata SHA-256: `23140221449282820c7da53fcdbe46ce5ee1169aff6e90986ef0dbd09c5f9120`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | NOT_EXERCISED | The locked evidence cannot prove the required read order or module-loading restriction. |
| `passes_design_closeout_gate` | NOT_EXERCISED | The required runtime-only per-page closeout matrix is not present in the locked evidence; the claimed gate pass cannot independently prove this hidden process requirement. |
| `creates_database_schema_domain_tree` | PASS | The delivered snapshot contains the database root, primary schema, workspace-access domain, relationship page, and three entity pages with hierarchical links. |
| `refreshes_confirmed_stable_path` | PASS | The stable database path is preserved, marked unverified, and refreshed with current uniqueness, roles, physical FK, and logical-reference facts. |
| `documents_current_entity_facts` | PASS | Entity snapshots accurately reflect schema, repository/service behavior, indexes, constraints, ownership, and lifecycle evidence. |
| `links_relationships_bidirectionally` | PASS | The relationship page links all three entity pages; each entity page links its domain, relationship overview, related entities, API authority, and database authority. |
| `distinguishes_physical_and_logical_relations` | PASS | The relationship Mermaid and prose distinguish cascading physical workspace FKs from the service-validated logical user reference. |
| `creates_domain_component_flow_tree` | PASS | The Design snapshot contains root and domain indexes, InvitationService, MembershipRepository, AuditWriter, invitation-acceptance, and authorization-boundary pages. |
| `keeps_reciprocal_and_authority_links` | PASS | Components link the acceptance flow, the flow links all three components, and Design pages link API/database authority pages without duplicating complete contracts. |
| `keeps_cross_domain_authority_unique` | PASS | The acceptance flow is explicitly authoritative under workspace-access; audit-log pages link to it without duplicating its正文. |
| `updates_atomic_map_and_unverified_pages` | PASS | The locked change-map preserves existing entries and stable paths, adds the database/design closure for each relevant code glob, and marks delivered pages unverified; candidate evidence reports a zero-missing-doc readback. |
| `runs_host_checks_and_handoffs_audit` | NOT_EXERCISED | The candidate reports all three npm checks passed, but the required docs-audit handoff is explicitly blocked by missing target release-version confirmation, so the later handoff step is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=1a1411f380f4acb5acced4dbe035c4ad46b56de30424fe5f47a3e9db761c7d7e; snapshot_sha256=812dc34cf26e3eb716477d270282b502d87d8fdf64d73a5a830e6d4486334606
- Behavior: Delivered the requested database and design documentation trees with accurate current facts, reciprocal links, authority boundaries, and change-map updates; host checks were reported passed, while the final audit handoff remains blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=9cb4f30def70e50fe7c1153eeeb55923522afd95565fde2fc5439072960d21a5; snapshot_sha256=d6445ec3bad367ceb6f27f94dfce6232d444a6541b8d5fdddc3a1184f448511f
- Behavior: Delivered a similar but less complete documentation tree, omitted the public build report, and reported pytest unavailable.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the target release version and complete the docs-audit handoff.
- Next: Capture runtime closeout-matrix and read-order evidence if those process assertions must be evaluated.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
