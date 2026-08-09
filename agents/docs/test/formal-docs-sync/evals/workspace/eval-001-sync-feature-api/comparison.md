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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `b75531387a8a9fcbe3680466e0062ed9ca0b3db6341639dbf81c051b7647e990`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `f8156f035dafc132a200ab0fabf455e3a12e92c380c1e7265ae20e3e3df0c170`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | NOT_EXERCISED | with_skill selects `existing-system backfill`, cites the maintainer request/catalog/host evidence, and excludes non-API module categories; raw evidence does not prove that the specific template/type modules were read. |
| `derives_complete_api_candidate_tree` | PASS | The with_skill tree contains the API, Identity, Sessions, create-session, and revoke-session paths, ties them to catalog hierarchy and route/schema/contract evidence, and leaves Billing for later due to owner/lifecycle boundaries. |
| `presents_per_node_confirmation_matrix` | FAIL | A tree, per-page evidence table, code-glob table, and change-map section are provided, but the per-node mapping does not explicitly pair every node with complete path, parent, exact code boundary, and owner; route leaves in particular lack explicit owner/code-boundary pairings. |
| `proposes_exact_atomic_change_map` | FAIL | The proposed route/schema/contract mappings cover all five candidate pages and preserve the Search mapping's unknown `review_hint`, but the output does not specify stable deduplicated ordering or explicitly preserve all unrelated/manual-plugin fields and entries. |
| `preserves_stable_paths_and_scope_boundaries` | PASS | The with_skill output keeps Billing, Search, and `docs/site/api/search.md` out of batch, excludes database/design/ops/product/release and `src/api/internal/**`, and states that no migration is needed. |
| `keeps_unconfirmed_batch_read_only` | PASS | It explicitly states zero writes, no host checks, no handoff, no next batch, and requests maintainer confirmation before proceeding. |
| `defaults_new_pages_to_internal_visibility` | PASS | It proposes `internal` visibility for all new pages, retains the existing root's `both` visibility for the established public Search page, and explains the exception. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=4e8c0828baec7086066d2199930e33dabcd36df699bc487b5726bf8730df42da; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly bounded the unconfirmed Identity/Sessions backfill and preserved read-only scope, but the per-node confirmation mapping and exact change-map preservation details are incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=7e14aec867bbf484535877566f4e7fd4f9681d8eed5b89b6e8ef619f65ed0bb2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a plausible five-page Sessions tree and left the workspace unchanged, but lacked the required complete ancestor mappings, scope/visibility detail, and explicit confirmation gate structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The confirmation matrix does not fully provide the required per-node parent/path/code-boundary/owner pairings.
- The atomic change-map proposal omits stable deduplicated ordering and explicit preservation of all unrelated/manual-plugin entries and fields.
- Next: Complete a per-node matrix/mapping that explicitly pairs every page with parent, full path, exact code boundary, owner, evidence, delta, and exclusions.
- Next: Add the stable deduplicated ordering rule and explicitly preserve all unrelated/manual-plugin change-map entries and unknown fields.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
