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
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- Skill overlay SHA-256: `9667198915198da0404e03a7d4c962d38742b19c5de4de5f0cf1473f02db2bf1`
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
| `selects_backfill_mode_and_api_contract` | PASS | With-skill output selects existing-system backfill, identifies the maintainer request, host, catalog, API template, and API-only scope; raw trace shows the corresponding source reads and no application of other type modules. |
| `derives_complete_api_candidate_tree` | PASS | The proposed tree contains the API root, Identity, Sessions, and both route leaf pages, with catalog hierarchy, route prefix/tag, owner, schema, and contract-test evidence; Billing is deferred. |
| `presents_per_node_confirmation_matrix` | PASS | The with-skill output provides a per-node matrix with parent, full path, code boundary, owner, evidence, visibility, change-map delta, exclusions, the complete tree, unresolved evidence limits, and an explicit confirmation request. |
| `proposes_exact_atomic_change_map` | PASS | The proposed YAML mappings include Identity, Sessions, and contract-test boundaries with required_docs covering both leaves and all ancestor indexes; the output specifies atomic post-confirmation updates, stable deduplication/sorting, and preservation of manual-plugin fields and unrelated mappings. |
| `preserves_stable_paths_and_scope_boundaries` | PASS | Billing, Search, and internal API paths are explicitly out of batch; database, design, ops, product, and release are excluded, and the existing Search path is explicitly retained without migration. |
| `keeps_unconfirmed_batch_read_only` | PASS | The output explicitly says the batch is unconfirmed, zero-write, no host checks were run, no pages/navigation/change map were changed, and it ends by requesting maintainer confirmation before atomic writing or verification. |
| `defaults_new_pages_to_internal_visibility` | PASS | Every newly proposed page in the matrix is marked internal; the existing API root remains both only as a stated exception to preserve the existing Search navigation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=d99acc01083ea30a9e8bd6e461f3baa8dd79505686b963124765c91be427cfc0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a complete, evidence-bound, zero-write Identity/Sessions backfill proposal and waits for maintainer confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=6883c1d0922acf88015642caeb50416386480b19aa0f48dfa101ac50171bb0dd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a useful but less complete proposal, lacking the explicit gate, per-node matrix, full ancestor change-map closure, visibility defaults, and detailed host-scope controls.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
