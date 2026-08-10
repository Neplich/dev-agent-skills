# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-001-sync-feature-api`.
- Fixture SHA-256: `19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa`
- Prompt SHA-256: `cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `b75531387a8a9fcbe3680466e0062ed9ca0b3db6341639dbf81c051b7647e990`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `f8156f035dafc132a200ab0fabf455e3a12e92c380c1e7265ae20e3e3df0c170`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | PASS | With-skill trace reads the handoff, request, catalog, host standards, change map, API template, and API type instructions, and selects existing-system backfill with API scope. |
| `derives_complete_api_candidate_tree` | PASS | The with-skill output presents the five required API paths, ties hierarchy to catalog, route, owner, schema, and contract-test evidence, and defers Billing. |
| `presents_per_node_confirmation_matrix` | PASS | The with-skill output includes a complete tree, per-node matrix, mapping details, exclusions, drift, and confirmation request before writes. |
| `proposes_exact_atomic_change_map` | PASS | The proposed route mapping covers both leaves and all ancestor indexes, while schema and contract-test mappings provide the remaining exact boundaries; stable sorting, deduplication, atomic update, and preservation of manual fields are stated. |
| `preserves_stable_paths_and_scope_boundaries` | PASS | Billing, Search, non-API document types, release, and internal API paths are explicitly out of scope; Search remains unmoved and requires confirmation for future changes. |
| `keeps_unconfirmed_batch_read_only` | PASS | The output states the batch is unconfirmed, remains zero-write, does not run host checks, and does not issue a docs-agent:docs-audit handoff; the trace shows clean git status. |
| `defaults_new_pages_to_internal_visibility` | PASS | All proposed new pages are explicitly assigned visibility: internal, while the existing API root retains both visibility. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=4634533c61aef2af635afa0b7d18f22f958f45a87def7b7503bfcfd86d18db93; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a gated, evidence-backed, zero-write API backfill proposal with complete hierarchy, mappings, exclusions, and internal visibility defaults.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=7f15d429cdba8e1f21c7ce86c4843362c9596c6b5545b2ded5abda25178cf7c9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a useful read-only Sessions tree and basic API facts, but lacks the with-skill confirmation matrix, complete atomic ancestor mappings, explicit audit structure, and internal visibility default.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
