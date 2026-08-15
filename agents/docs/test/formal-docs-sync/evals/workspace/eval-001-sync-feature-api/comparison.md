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
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `ce743547e06014367140716bb2c97c1db58eb733e797662e8b4bd6eca00be3ee`
- metadata_sha256: `f8156f035dafc132a200ab0fabf455e3a12e92c380c1e7265ae20e3e3df0c170`
- fixture_sha256: `19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b75531387a8a9fcbe3680466e0062ed9ca0b3db6341639dbf81c051b7647e990`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_backfill_mode_and_api_contract` | PASS | PASS：with_skill 明确选择 existing-system backfill，引用维护者请求、既有 host 与 feature catalog，并列出 standards entry、change-map、API template、API module；未读取其他类型模块。 |
| `derives_complete_api_candidate_tree` | PASS | PASS：候选树完整包含 API、Identity、Sessions 两级索引及两个 route leaf，并以 catalog、route、owner、schema 与 contract test 证据支撑；Billing 明确留待后续。 |
| `presents_per_node_confirmation_matrix` | FAIL | FAIL：虽有树、矩阵和 mapping section，但未明确列出 unresolved discrepancies；叶子节点矩阵还使用了 `.../create-session.md` 与 `.../revoke-session.md` 的缩略路径。 |
| `proposes_exact_atomic_change_map` | FAIL | FAIL：映射覆盖五页闭包、两个 leaf、全部 ancestor index、递归导航及未知字段保留；但 `required_docs` 实际顺序并非稳定路径排序，却声称已稳定排序。 |
| `preserves_stable_paths_and_scope_boundaries` | PASS | PASS：明确将 Billing、Search 及其既有映射置于批次外并保持稳定路径，且排除 internal、database、design、ops、product、release；未提出隐式迁移。 |
| `keeps_unconfirmed_batch_read_only` | PASS | PASS：with_skill 输出 pending confirmation、zero-write、未运行 checks、未提前 handoff；git evidence 与 delivery snapshot 也显示无写入。 |
| `defaults_new_pages_to_internal_visibility` | FAIL | FAIL：新增页面均标为 internal，既有 API 根/Search 保持 both；但未解释 internal 默认的收紧依据及例外。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=8d51fd2ccae14078e15c2d412ebb75acc0e73e36ade7de744cea2559b1a7fb55; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成有边界的 API backfill 只读候选规划，识别完整五页树并等待确认，但矩阵、排序和 visibility 说明存在缺口。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cd2f08c41a6ec95815793c80de00d9c220026a6632090c7da71f54b61e0f767a; fixture_sha256=19be975a76919e1880464ff6b63104dc042d768be1d80c006b73e28d58ffabfa; output_sha256=92f4fdc84f2641c42831898ed7d92ade62bcc42f6fd966a5d4142caabc1adc34; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样提出五页候选树并保持零写入，但缺少逐节点确认矩阵、完整原子 change-map 闭包、显式同步决策和 internal visibility 处理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 逐节点确认矩阵未明确 unresolved discrepancies，且叶子路径在矩阵中不完整。
- change-map required_docs 声称稳定排序但实际列表顺序不满足该要求。
- 未解释新增页面默认 internal 的依据与 existing both 的例外。
- Next: 补全每个节点的完整页面路径及 unresolved discrepancies 字段。
- Next: 将每个 required_docs 列表按明确且一致的稳定排序输出。
- Next: 说明新增页面默认 internal 的证据依据，并标明既有 both 页面是保持现状的例外。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
