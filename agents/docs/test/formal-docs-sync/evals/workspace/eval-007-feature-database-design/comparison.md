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
- target_skill_sha256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- eval_definition_sha256: `dd84eeaf9ea9452e584f740ec00a1edde6c8e5bfae2ef83da4e9e416f2e769fe`
- metadata_sha256: `23140221449282820c7da53fcdbe46ce5ee1169aff6e90986ef0dbd09c5f9120`
- fixture_sha256: `de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `289a3b63a3dcdcdc4cc6c4b994a40567f085f301732b94d5ab13b0e67247a316`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_only_database_design_contracts` | PASS | Raw trace shows the confirmed handoff, database/design instructions, and only database/design type modules were loaded; API content was used as an authority target. |
| `passes_design_closeout_gate` | NOT_EXERCISED | A runtime-only sync-report.md was added before formal writes and deleted afterward, but locked evidence does not expose its required per-page seven-field matrix content. |
| `creates_database_schema_domain_tree` | PASS | Locked delivery snapshots contain the database root, primary index, workspace-access domain index, relationships page, and all three entity pages with hierarchical links. |
| `refreshes_confirmed_stable_path` | PASS | The stable database/workspace-access.md path remains, is marked unverified, and replaces stale facts with current schema/service facts; the change map preserves and expands its mapping. |
| `documents_current_entity_facts` | PASS | Entity snapshots document current fields, constraints, indexes, ownership/read-write paths, lifecycle, membership uniqueness and roles, and invitation token uniqueness and expiry. |
| `links_relationships_bidirectionally` | PASS | The relationships Mermaid overview links all three entities, and each entity page links back to the domain, relationship overview, related entities, and API authority pages. |
| `distinguishes_physical_and_logical_relations` | PASS | The relationship page and membership/entity pages explicitly distinguish cascading physical workspace foreign keys from the service-validated logical user reference. |
| `creates_domain_component_flow_tree` | PASS | Locked snapshots contain the Design root, Workspace Access and Audit Log domains, three requested component pages, the invitation-acceptance flow, and authorization-boundary page; the flat page is a compatibility entry. |
| `keeps_reciprocal_and_authority_links` | PASS | All three component pages link the acceptance flow, the flow links all three components, and Design pages link API/database authority pages without copying their full contracts. |
| `keeps_cross_domain_authority_unique` | PASS | The acceptance flow is explicitly authoritative under Workspace Access, while Audit Log links to it without duplicating the flow body. |
| `updates_atomic_map_and_unverified_pages` | PASS | The locked map snapshot includes the stable page, corresponding database/design leaves and ancestors, reciprocal/authority pages, preserves unknown entries, and changed delivery pages use last_verified_version: unverified. |
| `runs_host_checks_and_handoffs_audit` | NOT_EXERCISED | Raw command events show test:docs, build:public, and build:internal completed successfully after link fixes. The complete affected set was prepared, but docs-agent:docs-audit handoff was blocked by missing target release-version confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=7c73e5f294fcde07a55ad9c258df2397f71a4fcf92870d781484ede74e472c16; snapshot_sha256=a2751feb68b62c63e06c6d76114b992fc3ae32116f72eaddc43b458f10e4671d
- Behavior: Delivered the requested database and design hierarchies with current facts, reciprocal authority links, map updates, and successful host checks; runtime closeout contents and final audit handoff remain unproven or blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=97f82a75c78275f5f504c11fb93e67755d5b6d9f65a9ef9273ee264808b8d9c8; fixture_sha256=de57a3e2c20f574e81d3d9803c1ae3a7c2c6c83bbead7114e75685122bb01a81; output_sha256=17ecc297339a58896447c76364f8c90b8d523d2401ddbf111a921f6d3a7ef446; snapshot_sha256=155b35823d88a1489d2344f5178665d905a8c5a11df89af7d4694d00d6cea7cd
- Behavior: Fresh baseline produced a partial-looking document tree and claimed only test:docs success, without locked evidence of the closeout matrix, complete map normalization, public/internal builds, or audit handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the missing target release version and complete the docs-agent:docs-audit handoff.
- Next: Expose or retain runtime sync-report.md content if the closeout matrix must be verified.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
