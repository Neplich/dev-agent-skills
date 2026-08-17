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
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- metadata_sha256: `f8156f035dafc132a200ab0fabf455e3a12e92c380c1e7265ae20e3e3df0c170`
- fixture_sha256: `19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b75531387a8a9fcbe3680466e0062ed9ca0b3db6341639dbf81c051b7647e990`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | PASS | With-skill output selects existing-system backfill, cites the maintainer handoff/request and feature catalog, and raw trace shows reading standards entry, change map, API template, and API instructions without loading non-API type templates. |
| `derives_complete_api_candidate_tree` | PASS | The output presents all five required paths, derives hierarchy from catalog, route, schema, owner, and contract evidence, and excludes Billing as a separate later-scope domain. |
| `presents_per_node_confirmation_matrix` | PASS | A complete parent/child tree, per-node matrix, mapping section, exclusions, evidence boundaries, and unresolved handler-versus-test discrepancy are presented before confirmation. |
| `proposes_exact_atomic_change_map` | PASS | Three precise route/schema/contract-test mappings each include the full five-page closure, stable deduplication/sorting, recursive navigation coverage, and preservation of the manual-plugin entry. |
| `preserves_stable_paths_and_scope_boundaries` | PASS | Billing, Search, non-API sections, internal API paths, and release scope are explicitly excluded; Search is marked read-only with no migration and no mapping changes. |
| `keeps_unconfirmed_batch_read_only` | PASS | The candidate batch is explicitly unconfirmed, no files changed per output and git evidence, host checks were not run, handoff is blocked, and the response waits for maintainer confirmation. |
| `defaults_new_pages_to_internal_visibility` | PASS | All new pages are specified as visibility: internal, with the existing API root retaining both visibility to preserve the stable public navigation path. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=745bc62d859fe0551c8272278524d0284b338223be30b6e421afd0f243853620; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a complete, evidence-backed, read-only Identity/Sessions API backfill proposal with confirmation gating and exact change-map closure.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=e0b2a3f14ba3da243e84d750119ce239a89307ab1c5fd53e5308152bbb96f2d5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identified the same five-page candidate and preserved read-only state, but provided a less complete confirmation matrix, visibility policy, hierarchy checkpoint, and atomic mapping closure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Await explicit maintainer confirmation before writing pages, navigation, or change-map entries.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
