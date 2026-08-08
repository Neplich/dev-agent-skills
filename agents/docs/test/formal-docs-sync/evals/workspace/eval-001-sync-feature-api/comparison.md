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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
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
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | PASS | 明确判定为 existing-system backfill，声明仅加载 api，并列出 host standards、change map、API template 与 API 证据；未应用其他类型模块。 |
| `derives_complete_api_candidate_tree` | PASS | 包含 API、Identity、Sessions 两级索引及两个 route leaf，并以 catalog、路由、schema、owner 和 contract tests 支撑层级；Billing 明确留后续批次。 |
| `presents_per_node_confirmation_matrix` | FAIL | 有 evidence bindings 和 mapping section，但没有为 docs/site/api/index.md 提供对应的逐节点 evidence binding，且部分节点的代码边界不够精确。 |
| `proposes_exact_atomic_change_map` | FAIL | 提出覆盖完整祖先索引和两个叶页的 required_docs，并保留 manual-plugin 未知字段；但未说明列表稳定去重排序。 |
| `preserves_stable_paths_and_scope_boundaries` | PASS | 明确排除 Billing、Search、database、design、ops、product、release 与 src/api/internal/**，并声明不迁移 Search；没有隐式扩大稳定路径范围。 |
| `keeps_unconfirmed_batch_read_only` | PASS | 明确 pending_scope_confirmation、confirmed_batch:none、Changed docs:none，声明零写入、不运行 host checks，并等待维护者确认后再写入。 |
| `defaults_new_pages_to_internal_visibility` | FAIL | 明确所有新增页面 visibility 为 internal；但没有解释该收紧依据及例外条件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=b79c717205a5ed39810aaef97e9bb02f4362073601e276ecfa0ca267ba40e8dd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择了受确认门控的 API backfill，提出完整 Identity/Sessions 候选树并保持零写入，但逐节点矩阵、change-map 细节和 visibility rationale 不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=a614b05f6bbdc9563c015700a99577fd495543e4c63ba09e23a48ef4bb1db88e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出相同的 Sessions 页面树和基本接口证据，但 visibility 建议沿用 both，change-map 与范围门控细节较弱。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- presents_per_node_confirmation_matrix: API 根索引缺少逐节点绑定，部分代码边界不够精确。
- proposes_exact_atomic_change_map: 未提出稳定去重排序约束。
- defaults_new_pages_to_internal_visibility: 未解释 internal 默认值的依据与例外。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `b75531387a8a9fcbe3680466e0062ed9ca0b3db6341639dbf81c051b7647e990`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `f8156f035dafc132a200ab0fabf455e3a12e92c380c1e7265ae20e3e3df0c170`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | NOT_EXERCISED | The with_skill output visibly selects existing-system backfill and an API-only Sessions proposal, but locked evidence cannot prove the required read order or exact source-loading process. |
| `derives_complete_api_candidate_tree` | PASS | It presents the complete API tree through API, Identity, Sessions, and both route leaves, ties levels to catalog/code/route/contract evidence, and defers Billing. |
| `presents_per_node_confirmation_matrix` | PASS | It provides a tree, per-page table, mapping section, exclusions, unresolved authentication/version details, and waits for confirmation; parent and per-node delta pairing is partly implicit rather than fully explicit. |
| `proposes_exact_atomic_change_map` | PASS | The proposed sessions glob and contract-test mapping each require all five pages, describe atomic confirmation/write behavior, and preserve manual-plugin unknown fields and unrelated mappings. |
| `preserves_stable_paths_and_scope_boundaries` | PASS | Billing, Search, internal APIs, and non-API sections are explicitly excluded; it states no migration is needed and requests confirmation before any path movement. |
| `keeps_unconfirmed_batch_read_only` | PASS | It states no batch is confirmed, no files or mappings were written, no next batch or host checks were run, and the audit handoff is blocked pending confirmation. |
| `defaults_new_pages_to_internal_visibility` | FAIL | The candidate does not specify internal visibility for any proposed new page or explain a visibility-default rule. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=edb056300ac2ea5fb896f44a2e850dd099e5dc2d4ab340e1bfec87f9014c6c16; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Strong bounded API backfill proposal with complete candidate tree, atomic mapping, exclusions, and confirmation gate, but no internal visibility defaults.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=f8ae6df66406037b1c8146fa92890dcb0e3c1b00dc0c0b4436da918925ef28ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline identifies the Sessions subtree and zero-write confirmation gate, but omits ancestor mappings, detailed atomic closure, and visibility handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- defaults_new_pages_to_internal_visibility
- Next: Add internal visibility to every proposed new page and mapping, with the host-default rationale and any explicit exception.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `b75531387a8a9fcbe3680466e0062ed9ca0b3db6341639dbf81c051b7647e990`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `f8156f035dafc132a200ab0fabf455e3a12e92c380c1e7265ae20e3e3df0c170`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | NOT_EXERCISED | With-skill output explicitly selects `existing-system backfill` and proposes only the API subtree, but locked evidence cannot prove the required read/non-read process. |
| `derives_complete_api_candidate_tree` | PASS | The complete five-node Sessions tree is present, supported by catalog, route, owner, schema, and contract-test evidence; Billing is excluded as a separate batch. |
| `presents_per_node_confirmation_matrix` | FAIL | The output has a tree and partial page/evidence table, but does not provide per-node parent, complete path, exact code boundary, proposed delta, and exclusions in a cross-mappable confirmation structure. |
| `proposes_exact_atomic_change_map` | FAIL | The proposed mappings cover the five pages and preserve manual/Search entries, but omit the required explicit stable dedupe/sort behavior and do not fully present the required atomic route-mapping details. |
| `preserves_stable_paths_and_scope_boundaries` | PASS | Billing, Search, internal API, database, design, ops, product, and release documentation are explicitly excluded; Search is described as stable and not migrated or changed. |
| `keeps_unconfirmed_batch_read_only` | PASS | The output states no files or change map were modified, confirmation is pending, no build or handoff occurred, and only read-only checks were run. |
| `defaults_new_pages_to_internal_visibility` | FAIL | The candidate output never specifies `internal` visibility for proposed new pages or mappings. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=8f6f2c57996ff6ae6d9a000bc5d53ed2b41a9dcfa6e6f62960c9e5c9bb6068c0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly limits the proposed batch and preserves read-only scope, but omits required confirmation-matrix detail, exact atomic-map guarantees, and internal visibility defaults.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=d33eed82fc54347a0725dfafa3cd8574f92c56773617e07c800a732698457f55; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a fresh baseline with a plausible Sessions proposal, but is less complete and less explicit about scope and confirmation gating.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- presents_per_node_confirmation_matrix
- proposes_exact_atomic_change_map
- defaults_new_pages_to_internal_visibility
- Next: Add a fully cross-mappable per-node confirmation matrix and mapping section.
- Next: Specify internal visibility for every proposed new page.
- Next: Document atomic page/map update semantics, stable deduplicated ordering, and complete route/navigation mapping.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `f8156f035dafc132a200ab0fabf455e3a12e92c380c1e7265ae20e3e3df0c170`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | NOT_EXERCISED | The with_skill output states existing-system backfill, accepted entry basis, and api as the loaded type module, but locked evidence cannot prove the required read order or that database/design/ops/product modules were not read or applied. |
| `derives_complete_api_candidate_tree` | PASS | The with_skill output presents the complete five-node API tree, ties nodes to catalog hierarchy, owner, routes, schemas, handlers, and contract tests, and excludes Billing for later review. |
| `presents_per_node_confirmation_matrix` | FAIL | The table covers all five pages but does not provide the required per-node parent pairing, complete exact code boundary for every node, proposed change-map delta, and exclusions in a cross-correspondable matrix/mapping structure. |
| `proposes_exact_atomic_change_map` | FAIL | The proposed mappings cover the five-page closure and preserve the manual-plugin review_hint, but the output omits the required stable deduplicated ordering behavior and does not explicitly preserve all unrelated change-map entries. |
| `preserves_stable_paths_and_scope_boundaries` | PASS | The with_skill output explicitly excludes Billing, existing docs/site/api/search.md, database, design, ops, product, release-notes, and src/api/internal/**; it states Search remains unchanged and proposes no migration. |
| `keeps_unconfirmed_batch_read_only` | PASS | It marks the gate blocked pending maintainer confirmation, reports no changed docs, says host checks were not run, emits no docs-audit handoff, and requests confirmation before atomic writes. |
| `defaults_new_pages_to_internal_visibility` | FAIL | The with_skill output does not assign internal visibility to proposed new pages or explain the default/exception policy. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=6f517ac1b32b2e3c34ea089bc7f24fa7ca4fa10c002409e76908fe2cd96d6c17; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a read-only, confirmation-gated five-page Identity/Sessions proposal with strong API evidence, exclusions, and full proposed mapping closure, but misses required matrix detail and internal visibility policy.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=29f249e3f0b48418fab86fb1e7f43c26e7e4adbe80bf78eeef4e622913e9255e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline identifies the five-page Identity/Sessions batch and some API evidence, but lacks explicit backfill gating, complete ancestor change-map closure, detailed confirmation matrix, exclusions, and visibility policy.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- presents_per_node_confirmation_matrix: required per-node mapping fields and cross-correspondable matrix coverage are incomplete.
- proposes_exact_atomic_change_map: stable deduplicated ordering and preservation of all unrelated entries are not fully stated.
- defaults_new_pages_to_internal_visibility: no internal visibility default is proposed or justified.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `e71fe1ba5d6339777690bef42456f363050aa1a29a7cf722a403bab61da88105`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | NOT_EXERCISED | With-skill output visibly selects existing-system backfill and API-only loading, but locked evidence cannot prove the complete read-order/exclusion requirement. |
| `derives_complete_api_candidate_tree` | PASS | Provides the complete API, Identity, Sessions, create-session, and revoke-session tree, with catalog hierarchy, routes, owners, schemas/tests, and Billing deferred. |
| `presents_per_node_confirmation_matrix` | PASS | Provides a per-page table, full tree, code boundaries, owners, route/catalog evidence, mapping section, discrepancies, exclusions, and requests maintainer confirmation before writing. |
| `proposes_exact_atomic_change_map` | PASS | Maps routes, schemas, and contract tests to all five ancestor/leaf pages, including recursive navigation impact, while preserving plugins/manual/** unknown fields and unrelated entries. |
| `preserves_stable_paths_and_scope_boundaries` | PASS | Explicitly excludes Billing, Search, internal API, database, design, ops, product, and release scope; states the existing Search page and mapping remain unchanged. |
| `keeps_unconfirmed_batch_read_only` | PASS | States zero writes, no host checks, and no handoff, and stops pending one explicit confirmation of the complete Sessions subtree and mappings. |
| `defaults_new_pages_to_internal_visibility` | FAIL | The with-skill proposal does not specify visibility for candidate or mapped new pages, so it does not establish the required internal default or exceptions. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=d6c58b790f443880676c7d88916fcea44920d4eac5e12875998fe4ae906cadc5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a detailed zero-write Sessions subtree proposal with evidence, exclusions, atomic mappings, and confirmation gating, but omits new-page visibility defaults; read-order claims are not independently provable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=25fcdaf0d11f553eafb081af332c6de7f873e2eff6119cc674188a17dffefc88; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identifies a limited Identity/Sessions batch and waits for confirmation, but omits the API root ancestor, per-node confirmation matrix, full atomic ancestor mappings, explicit discrepancies, and visibility policy.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- New candidate-page visibility is not specified as internal by default.
- Next: Add internal visibility to each proposed new page and explain that no public/both visibility is warranted absent explicit host requirements.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-001-sync-feature-api`.
- Fixture SHA-256: `a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032`
- Prompt SHA-256: `cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `e71fe1ba5d6339777690bef42456f363050aa1a29a7cf722a403bab61da88105`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | NOT_EXERCISED | 输出明确提出 API backfill 并限制为 API 范围，但锁定 raw evidence 无法证明实际读取顺序或未读取其他类型模板。 |
| `derives_complete_api_candidate_tree` | FAIL | 完整树和 Billing 排除均出现，但未充分以 feature catalog 父子关系、owner、route prefix/tag、schema 与 contract tests 解释层级。 |
| `presents_per_node_confirmation_matrix` | FAIL | 有完整树和页面/代码范围表，但缺少逐节点 parent、owner、分类或 route 证据、change-map delta 与逐节点 exclusions 的可交叉映射。 |
| `proposes_exact_atomic_change_map` | FAIL | 三类 Sessions 来源均映射到五个页面，且保留 manual review_hint；但未明确稳定去重排序、页面与 map 原子更新，也未明确保留所有既有 trigger、exclude 和无关条目。 |
| `preserves_stable_paths_and_scope_boundaries` | PASS | 明确排除 Billing、Search 页面及路径迁移、internal、database、design、ops、product、release，并说明不移动既有 Search 页面。 |
| `keeps_unconfirmed_batch_read_only` | PASS | 明确候选范围尚未确认、本轮不改文件，并停在维护者确认五页子树及映射之后。锁定 git evidence 也显示无写入或提交。 |
| `defaults_new_pages_to_internal_visibility` | FAIL | 输出未为新增候选页面或映射声明 internal visibility，也未说明默认收紧依据或例外。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032; output_sha256=4b762c2e180b0c0bb72f401e06d4eec6296778461f8bfae96fe23bbcac9db3a2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确停留在未确认批次的只读提案阶段，给出完整 Sessions 页面树、接口事实和较完整的 change-map 草案，但遗漏逐节点映射字段、稳定更新约束和 visibility 默认值。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032; output_sha256=b2a16f3ad64798ab4ead37cf76238ca3be37691384713211bfd1506469a92cb1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出 API/Sessions 批次并保持不写入，但粒度、映射和证据结构较简略，未提供完整逐节点确认矩阵。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未充分说明候选层级所依据的 catalog、owner、route、schema 和 contract-test 证据。
- 未提供满足要求的逐节点 confirmation matrix/mapping section。
- change-map 草案遗漏稳定去重排序、页面/map 原子更新及既有 trigger/exclude 全量保留的明确承诺。
- 未声明新增页面默认 visibility 为 internal。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-001-sync-feature-api`.
- Fixture SHA-256: `a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032`
- Prompt SHA-256: `cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `e71fe1ba5d6339777690bef42456f363050aa1a29a7cf722a403bab61da88105`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | FAIL | with_skill 选择了 existing-system backfill 并识别维护者请求与 feature catalog，但未明确说明以 host standards entry、change map、API template 和 API type module 作为读取依据，也未明确排除其他类型模板。 |
| `derives_complete_api_candidate_tree` | PASS | with_skill 给出了 api/index.md、identity/index.md、identity/sessions/index.md 及 create-session.md、revoke-session.md 的完整树，并以 catalog、route、owner、schema、handler 和 contract tests 解释拆分；Billing 被排除在本批之外。 |
| `presents_per_node_confirmation_matrix` | FAIL | with_skill 提供了页面表和 mapping section，但未逐节点配对 parent、完整代码边界、owner、proposed delta 等全部字段，未展示 api/index.md 的逐节点确认项，也未明确列出 unresolved discrepancies。 |
| `proposes_exact_atomic_change_map` | FAIL | with_skill 的 required_docs 覆盖两个叶子及祖先索引，并保留 manual-plugin/Search 条目不变；但未明确稳定去重排序规则，也未显式复述并保留 manual-plugin 的 review_hint、trigger、exclude 字段。 |
| `preserves_stable_paths_and_scope_boundaries` | PASS | with_skill 明确将 Billing、既有 docs/site/api/search.md、src/api/internal/** 及 database、design、ops、product、release 排除，并声明不迁移或重命名现有页面。 |
| `keeps_unconfirmed_batch_read_only` | PASS | with_skill 明确候选页面树和 change-map 尚待维护者确认，未修改站点文件；确认后才进入写入和测试阶段，未提前 handoff。 |
| `defaults_new_pages_to_internal_visibility` | FAIL | with_skill 未说明候选新增页面的 visibility 为 internal，也未给出默认收紧依据或例外规则。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032; output_sha256=55a186eac564eb3ad70d20b71ef5dc3b0b2630398bf753e3f68a49351447f1c5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确停留在未确认的 existing-system backfill 前期梳理阶段，给出完整 Sessions 候选树和较完整 change-map，但遗漏 host/API 模板读取声明、逐节点矩阵细节、稳定映射规则和 internal visibility。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032; output_sha256=e1234ed2a8b0030eda2434250fda930085c27adc397472e1eb2484de158fee67; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出了有限 Sessions 范围并保持零写入，但页面路径错误为 create.md/revoke.md，缺少完整树、逐节点确认矩阵、visibility 和充分的边界说明。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 selects_backfill_mode_and_api_contract。
- with_skill 未满足 presents_per_node_confirmation_matrix。
- with_skill 未满足 proposes_exact_atomic_change_map。
- with_skill 未满足 defaults_new_pages_to_internal_visibility。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-001-sync-feature-api`.
- Fixture SHA-256: `a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032`
- Prompt SHA-256: `cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- Metadata SHA-256: `e71fe1ba5d6339777690bef42456f363050aa1a29a7cf722a403bab61da88105`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | FAIL | With-skill output selects existing-system backfill and cites the request, handoff, catalog, and site, but does not state loading the host standards entry, change map, or API template, nor explicitly confirm those non-API templates were not read or applied. |
| `derives_complete_api_candidate_tree` | FAIL | It lists the required five pages and supports them with catalog paths, routes, owner, schema, and contract-test evidence, while deferring Billing; however, route tag evidence is not stated. |
| `presents_per_node_confirmation_matrix` | FAIL | The page table has only page, role, and evidence, and the mapping section has change-map entries. It does not provide per-node parent, exact code boundary, owner, classification/route evidence, delta, and exclusions for every domain, subfeature, index, and leaf. |
| `proposes_exact_atomic_change_map` | FAIL | The route, schema, and contract-test mappings cover the five-page tree and preserve the manual-plugin fields, but the output does not state stable deduplicated sorting of mappings/navigation or explicitly preserve all unrelated entries. |
| `preserves_stable_paths_and_scope_boundaries` | FAIL | It keeps Billing and Search out of batch and explicitly excludes database, design, ops, product, and release documentation, but does not explicitly exclude src/api/internal/** or state the required migration-plan-and-confirmation rule for any stable-path move. |
| `keeps_unconfirmed_batch_read_only` | FAIL | It clearly says no documents or change map are written and waits for confirmation before creation, but does not explicitly state that no next batch, post-write host checks, or docs-agent:docs-audit handoff will occur. |
| `defaults_new_pages_to_internal_visibility` | PASS | It assigns visibility: internal to new pages and keeps the existing API root both-visible because the existing external Search page remains in scope for that root. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032; output_sha256=11161bded73630a85cd31368c0e218e82be9fad772da28eb2071f2a299fc0a09; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: The candidate selects the correct Identity/Sessions backfill and page paths, adds richer evidence and mappings, preserves existing Search/manual-plugin context, and pauses before writes, but omits several required per-node, exclusion, and confirmation-boundary details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=a02cecead0666327de493458ce5b7665c4330c17675060cfa33039c7bc6f5032; output_sha256=4ca78b03d9e770f30a2c191b37277e80501b4d504ccfee8590cc220140b63de0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline proposes a narrower four-page subtree with create.md/revoke.md names, incomplete ancestor/change-map coverage, and no visibility or explicit read-only handoff safeguards.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- With-skill output fails six assertions due to omitted required evidence or safeguards; the without-skill lane was used only as comparison context.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-001-sync-feature-api`
- Review context: PR #164 second-round review for skill-specific eval discrimination

## Test Set / Fixture Version

- Fixture: current pristine `workspace/eval-001-sync-feature-api` snapshot for issue #159
- Scenario: an existing-system API backfill request authorizes bounded discovery for the Identity / Sessions catalog branch but does not confirm candidate pages, hierarchy, mappings, navigation, or writes
- Evidence set: PM handoff, bounded-discovery request, feature catalog, host standards and change map, route/schema/handler code, contract tests, existing stable Search page, and Billing as an out-of-batch control
- Actual validation date: `2026-07-22`
- Isolation: fresh `codex exec` copied the same fixture without historical comparison into independent with-skill and without-skill lanes; the start manifests matched, both end manifests remained identical to their starts, and a third fresh `codex exec` judge reviewed the final assertions and both outputs

## Latest Result

- Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | FAIL | FAIL | 两者都提出 API 回填，但未明确引用 host standards、change map、API template/type module，也未证明未读取 database/design/ops/product 模块；with_skill 仅列出 API 证据（`with_skill/result.txt:13-24`），without_skill 还引入了 `docs/pm/feature-catalog.md` 映射（`without_skill/result.txt:43-48`）。 |
| `derives_complete_api_candidate_tree` | FAIL | FAIL | 两者都列出了完整五节点树（`result.txt:3-11`），但未用 catalog 父子关系、route prefix/tag、owner、schema、contract tests 完整解释层级，也未明确说明不是按源码文件机械拆分。 |
| `presents_per_node_confirmation_matrix` | FAIL | FAIL | 两者没有逐 domain、subfeature、index、route leaf 的 confirmation matrix；仅有树状图和 change-map。缺少逐节点的完整 page path、代码边界、owner、分类证据、delta 和 exclusions 配对。 |
| `proposes_exact_atomic_change_map` | FAIL | FAIL | with_skill 的 `required_docs` 覆盖五个页面（`with_skill/result.txt:26-53`），但未明确递归导航、原子更新、稳定去重排序及保留 `plugins/manual/**` 全部字段；without_skill 的映射遗漏 API/Identity/Sessions ancestor index，并额外加入 `docs/pm/feature-catalog.md`（`without_skill/result.txt:23-49`）。 |
| `preserves_stable_paths_and_scope_boundaries` | FAIL | FAIL | 两者都排除了 Billing、Search 和内部 API（with `:56`；without `:51`），但未明确排除 database/design/ops/product/release，也未完整声明既有 `search.md` 及其 change-map 映射保持不动，或提供迁移计划要求。 |
| `keeps_unconfirmed_batch_read_only` | PASS | PASS | 两者均明确“不写入站点”、要求维护者确认后再写入（with `:1,58`；without `:1,51`）。实际目录仅有 `result.txt` 和 `run_status.json`，没有页面、change-map、index、导航或 handoff 产物。 |
| `defaults_new_pages_to_internal_visibility` | FAIL | FAIL | 两者均未为候选页面或映射声明 `visibility: internal`，也未解释 `both/public` 例外。 |

未满足断言（with/without 任一 FAIL）：``selects_backfill_mode_and_api_contract``、``derives_complete_api_candidate_tree``、``presents_per_node_confirmation_matrix``、``proposes_exact_atomic_change_map``、``preserves_stable_paths_and_scope_boundaries``、``defaults_new_pages_to_internal_visibility``



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `selects_backfill_mode_and_api_contract`: with skill PASS; without skill FAIL. The skill lane selected `existing-system backfill`, accepted the bounded-discovery entry basis, and loaded only the host API contract; the baseline did not establish mode or progressive-loading semantics.
- `derives_complete_api_candidate_tree`: both PASS. Both lanes derived the API root, Identity and Sessions indexes, and the create/revoke route leaves from catalog, route, owner, schema, and contract-test evidence while keeping Billing for a later batch.
- `presents_per_node_confirmation_matrix`: with skill PASS; without skill FAIL. The skill lane's node matrix and mapping section jointly paired every node with parent, path, code boundary, owner, evidence, mapping delta, and exclusions; the baseline could not pair ancestor indexes with proposed mapping deltas.
- `proposes_exact_atomic_change_map`: with skill PASS; without skill FAIL. The skill lane's route mapping included both leaves plus the Sessions, Identity, and API ancestor indexes and preserved unrelated entries and unknown fields; the baseline mapped only leaf pages.
- `preserves_stable_paths_and_scope_boundaries`: both PASS. Both lanes preserved Search and its mappings and excluded Billing, internal API, non-API surfaces, stable-path migration, and later batches.
- `keeps_unconfirmed_batch_read_only`: both PASS. Both lanes waited for explicit candidate-batch confirmation, produced zero workspace changes, and did not run write-after checks or hand off to docs-audit.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Read `formal-docs-sync` entry and common instructions, the API type module, the host standards entry, API template, change map, implementation evidence, tests, and the shared frontmatter contract; no non-API type module was loaded.
- Chose existing-system backfill rather than feature delivery and treated the maintainer request as discovery authorization rather than write confirmation.
- Proposed one coherent Identity / Sessions subtree with all ancestor indexes and two independently locatable route leaves.
- Presented the full candidate scope and an ancestor-aware atomic change-map delta, preserved manual unknown fields and stable Search mappings, and kept Billing and all non-API surfaces out of batch.
- Stopped before writes, host checks, the next batch, or a `docs-agent:docs-audit` handoff.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: fresh `without_skill` lane from the same final prompt and identical pristine fixture; it did not read the target skill, Docs Agent README, internal/shared skill instructions, historical comparison, or with-skill output.
- The baseline correctly derived the five-node Identity / Sessions tree, protected Search and out-of-batch surfaces, and stayed read-only.
- It did not select the formal-docs-sync backfill mode or API-only progressive-loading path, did not complete the per-node confirmation mapping for ancestor indexes, and omitted all ancestor indexes from the proposed change-map `required_docs`.
- Baseline result: **3/6**.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With-skill assertion failures: none.
- Baseline failures: mode/progressive loading, per-node candidate confirmation mapping, and ancestor-aware atomic change-map coverage.
- Infrastructure blockers: none. The recurring local Codex model-cache warning did not prevent either lane or the judge from completing and did not affect semantic evidence.

## Next Steps

- Keep the bounded-discovery request distinct from candidate confirmation so future regressions cannot pass by copying a prompt-prescribed tree.
- Preserve the ancestor-index mapping assertion; it is the strongest observed discriminator between skill-guided synchronization and the generic baseline.

## Runtime Artifact Policy

- Source copy, both isolated lanes, candidate outputs, manifests, workspace diffs, and fresh judge verdict remain under `tmp/eval-runs/issue-159-review2-20260722-v2/` and are not submitted.
- Only this `comparison.md` is durable; no transcript, candidate output, verdict, timing, diagnostics, dependency directory, or generated site is tracked.
