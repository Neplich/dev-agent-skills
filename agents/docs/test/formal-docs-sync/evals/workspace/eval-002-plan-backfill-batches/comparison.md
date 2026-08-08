# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3a676f73bf7941f0ab035834abd0887251dca20d52501fbcda26212974e9b01d` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `3a676f73bf7941f0ab035834abd0887251dca20d52501fbcda26212974e9b01d`
- Prompt SHA-256: `6e26676a89a16acec9866e91e19dd92a1b85a0401ad645a6160108df17d9b4b2`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2c8e08b3132af642c4bb05621cb003e26dd288906af387a3ced10de28578b14d`
- Metadata SHA-256: `7fae8c9ebc1571e6ee6485e0157870ec8eb18079ff4d13256bd1589929d19c33`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | FAIL | with_skill 输出没有执行证据证明应用 formal-docs-sync 八步合同或加载 Product/API 模块，也没有证明排除 database/design/ops 模块。 |
| `prefers_catalog_scope` | FAIL | with_skill 输出未说明先读取 feature catalog、核对 code path 存在性或将 Billing 标为 out-of-batch。 |
| `presents_batch_before_write` | FAIL | with_skill 输出只提出 Accounts 范围建议，没有在写入前展示完整三节点 parent/child tree、逐节点字段或等待确认。 |
| `keeps_unconfirmed_batch_read_only` | PASS | with_skill 输出明确未修改 Accounts API、Billing 或其他非 Product 文档；diff 仅包含 Product 页面与 Product change-map 条目。 |
| `aligns_seed_with_page` | FAIL | with_skill 输出没有实际提出完整 Accounts seed、三页 required_docs 闭包或保留 Billing 映射字段的具体方案。 |
| `handles_missing_catalog_semantically` | NOT_EXERCISED | fixture 中存在 confirmed feature catalog，因此无 catalog 的条件分支未被本轮任务触发。 |
| `creates_complete_product_tree` | PASS | delivery_snapshot 包含 Product 根、两个域、invitations、两个二级子功能 index，以及四个独立任务页。 |
| `keeps_every_task_navigable` | PASS | delivery_snapshot 中根、域、一级/二级 index 和任务页均存在逐级导航链接，未跳过中间层。 |
| `records_confirmed_non_leaf_scope` | FAIL | 部分非叶子页虽有角色、owner 和子节点，但 member-invitations 与 invitation-acceptance index 未明确列出本批排除项及相邻能力。 |
| `writes_evidence_backed_task_behavior` | PASS | 四个任务页均引用对应实现函数与 acceptance test，并记录 fixture 支持的权限、限制、状态、错误反馈和恢复路径。 |
| `updates_product_map_atomically` | PASS | change-map.yaml 新增四类 Product code glob，各自包含对应祖先闭包和叶子页；原有 Billing/support 条目及 exclude、review_policy 保留。 |
| `links_authorities_without_copying_contracts` | PASS | 每个任务页链接上级功能及 Design、API、Database、Ops 权威入口，未复制 API 或数据库契约。 |
| `runs_product_host_checks` | FAIL | with_skill 仅声称 Product 页面链接和结构校验结果，未记录 npm run test:docs、build:public、build:internal 的 cwd/退出状态，也未 handoff docs-agent:docs-audit。 |
| `blocks_audit_without_confirmed_version` | FAIL | with_skill 未列出 docs-agent:docs-audit 的完整 affected set、证据和排除项，也未明确因缺少 target_release_version 阻塞 pre-tag audit。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6e26676a89a16acec9866e91e19dd92a1b85a0401ad645a6160108df17d9b4b2; fixture_sha256=3a676f73bf7941f0ab035834abd0887251dca20d52501fbcda26212974e9b01d; output_sha256=ebd7a53b51d7face42b91b6bfb3755e62b2974aa37f2c5a466a5d7cc1124e269; snapshot_sha256=e27947cc890ef83a00bc92c4cbdb7003a2c4eba4f6b6bf1974bb4f60d437819c
- Behavior: 完成并映射 Product 页面树，任务行为和导航证据较完整；未提供所需 API 批次规划/确认流程，也未完成或完整记录宿主检查及审计阻塞交接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6e26676a89a16acec9866e91e19dd92a1b85a0401ad645a6160108df17d9b4b2; fixture_sha256=3a676f73bf7941f0ab035834abd0887251dca20d52501fbcda26212974e9b01d; output_sha256=0839b276534003c47bd91cf01f367b34518fed3a7cec7a641ad4d4607d85916f; snapshot_sha256=956652eb1de5bcdcb25097c1b748bab3e753124765a0bac98e7614eac26e4e7a
- Behavior: 完成 Product 页面树，但未更新 change-map；未修改 Accounts/Billing；检查记录不完整，Accounts 仅作粗略后续建议。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未提供 formal-docs-sync/Product/API 合同加载证据。
- 未在写入前展示完整 Accounts 候选树并等待维护者确认。
- 未按要求记录并完成三个 Product 宿主命令及审计交接。
- 部分非叶子 Product 页面缺少明确 exclusions/adjacent-scope 语义。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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
- Eval: `eval-002-plan-backfill-batches`
- Mode / types: `existing-system backfill` / API + Product

## Test Set / Fixture Version

- Fixture version: `issue-164 API information architecture + issue-160 recursive Product information architecture`
- Product evidence: two product domains; Workspace Management contains
  `invitations` as a Level 1 feature, `member-invitations` and
  `invitation-acceptance` as Level 2 features, and three independently tested
  task leaves; Analytics remains a shallow domain with one task leaf.
- API evidence: confirmed Accounts/Billing catalog and an unconfirmed
  Accounts candidate subtree with an existing protected Billing subtree.
- Fresh paired run:
  `tmp/eval-runs/pr-165-multilevel-final-clean-20260723-170550/eval-002/`
- Generation method: both generators received the same core prompt and new
  pristine fixture. Only with-skill received the Docs Agent, common contract,
  and API/Product modules. Neither generator received assertions, this
  comparison, an earlier lane, or the other lane's output.
- Judge method: a new independent `codex exec` judge first read the current 14
  assertions after generation, inspected both actual workspaces, reran Product
  acceptance tests and all host commands, and parsed the generated
  public/internal sidebar trees and local links.
- Actual validation date: `2026-07-23`

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `PARTIAL`
- without_skill：Behavior `FAIL` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| loads_scoped_api_product_contracts | FAIL | FAIL | Product/API 回填场景已实际执行，但两条 lane 均无加载合同模块的执行证据；with_skill 仅有 `skill-map.md`，结果摘要也未展示 Product/API 模块加载过程。 |
| prefers_catalog_scope | FAIL | FAIL | `result.txt` 只提出 Accounts 页面/代码建议，没有引用 catalog owner `identity-team`、验证路径存在或明确 Billing out-of-batch。 |
| presents_batch_before_write | FAIL | FAIL | 两条 lane 都先完成 Product 写入，之后才在 `result.txt` 建议 Accounts；没有写入前展示三页完整树、逐节点边界并等待确认的证据。 |
| keeps_unconfirmed_batch_read_only | PASS | PASS | 两条 lane 的 `docs/site/api/` 未新增 Accounts 页面；with_skill 的 `change-map.yaml` 保留既有 Billing 条目，Product 已确认批次正常更新。 |
| aligns_seed_with_page | FAIL | FAIL | 没有 Accounts 的实际 change-map seed；with_skill 仅在摘要中口头列出 routes/schema/tests，未保留并展示 Billing 未知字段及完整原子候选范围。 |
| handles_missing_catalog_semantically | NOT_EXERCISED | NOT_EXERCISED | fixture 明确存在 `docs/pm/feature-catalog.md`，无 catalog 分支未触发。 |
| creates_complete_product_tree | PASS | PASS | 两条 lane 均实际生成完整 Product 树：根、两个域、`invitations`、两个二级子功能 index，以及四个任务页。 |
| keeps_every_task_navigable | PASS | PASS | 两条 lane 的各级 index 均包含所需直接子链接，例如 `product/index.md` → 域 → `invitations` → 二级子功能 → 任务页。 |
| records_confirmed_non_leaf_scope | FAIL | FAIL | with_skill 的 `member-invitations/index.md` 与 `invitation-acceptance/index.md` 有角色和子节点，但没有明确本批排除项；without_skill 的非叶页面同样缺少完整 scope/exclusion 语义。 |
| writes_evidence_backed_task_behavior | PASS | PASS | 任务页均通过 `related_code` 和 acceptance test 引用证据；实现与测试覆盖 owner/admin、3 个上限、重复邀请、resend/revoke、恢复、过期/无效邀请及 dashboard empty/retry。 |
| updates_product_map_atomically | PASS | FAIL | with_skill 的 `change-map.yaml` 包含 broad、invitation、两个精确 Product glob，并为各 glob列出祖先闭包，同时保留 Billing/support 条目及未知字段；without_skill 未新增任何 Product 映射。 |
| links_authorities_without_copying_contracts | PASS | PASS | 两条 lane 的任务页均链接上级页面及 Design/API/Database/Ops 索引，未复制接口或数据库契约正文。 |
| runs_product_host_checks | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 的 `npm run test:docs` 都因缺少 `fast-glob` 未启动完成，后续宿主检查与 docs-audit handoff 因而未执行；这是 runner 依赖阻塞，不是 skill 行为失败。 |
| blocks_audit_without_confirmed_version | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 均没有 `docs-agent:docs-audit` handoff、affected set 或因缺少 `target_release_version` 而 blocked 的审计记录。 |

未满足断言（with/without 任一 FAIL）：`loads_scoped_api_product_contracts`、`prefers_catalog_scope`、`presents_batch_before_write`、`aligns_seed_with_page`、`records_confirmed_non_leaf_scope`、`updates_product_map_atomically`

基础设施阻塞说明：依赖缺失（fast-glob 等）；`runs_product_host_checks` 不构成 skill 行为回归。



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `loads_scoped_api_product_contracts`: with-skill PASS；without-skill FAIL。
  Only with-skill loaded and applied the common, API, and Product contracts.
- `prefers_catalog_scope`: both PASS. Both selected Accounts and kept Billing
  out of the candidate batch.
- `presents_batch_before_write`: with-skill PASS；without-skill FAIL。
  With-skill used the Accounts boundary for every candidate node; the baseline
  used the over-broad `src/api/**` boundary for the API root.
- `keeps_unconfirmed_batch_read_only`: both PASS. Neither lane wrote Accounts
  or changed protected API/Billing surfaces.
- `aligns_seed_with_page`: both PASS. Both proposed the complete three-page
  Accounts closure and preserved Billing metadata.
- `handles_missing_catalog_semantically`: both PASS. Both proposed bounded API
  discovery followed by confirmation.
- `creates_complete_product_tree`: both PASS. Both generated the Product root,
  two domain indexes, Invitations, two Level 2 indexes, and four task leaves.
- `keeps_every_task_navigable`: both PASS. Both generated root → domain →
  Level 1 → Level 2 → task sidebar navigation without skipping levels.
- `records_confirmed_non_leaf_scope`: with-skill PASS；without-skill FAIL。
  Only with-skill recorded audience, catalog owner, direct children, adjacent
  capability, and exclusions on every non-leaf node.
- `writes_evidence_backed_task_behavior`: both PASS. Invitation creation,
  pending invitation management, acceptance/recovery, and dashboard states
  match their exact functions and three acceptance tests.
- `updates_product_map_atomically`: both PASS. Each of the five broad/exact
  Product globs independently contains its Product ancestors, applicable task
  leaves, and four authority roots in stable order.
- `links_authorities_without_copying_contracts`: both PASS. All four task pages
  link parent and authority pages without copying contracts.
- `runs_product_host_checks`: with-skill PASS；without-skill FAIL。
  Both lanes passed 76 docs tests and both builds, and their public/internal
  sidebars include all ten Product pages with maximum nesting depth five and
  zero unresolved local links. Only with-skill recorded every command, docs
  site cwd, and final exit status as required by the assertion.
- `blocks_audit_without_confirmed_version`: with-skill PASS；without-skill
  FAIL。Only with-skill explicitly blocked `docs-agent:docs-audit` pre-tag work pending a
  maintainer-confirmed target version.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Applied the common eight-step contract and only the scoped API/Product
  modules.
- Generated ten Product pages with an independent `index.md` for every
  non-leaf node and evidence-backed behavior on each task leaf.
- Preserved the seeded per-layer change-map ancestor closures and protected
  Billing/manual entries, while keeping Accounts at zero writes.
- Used the host's arbitrary-depth sidebar generator in both views and kept all
  changed pages `last_verified_version: unverified`.
- Returned the complete `docs-agent:docs-audit` affected set but correctly blocked pre-tag audit
  on the missing `target_release_version`.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: a new pristine fixture copy with the same prompt. It did not read or
  apply the target skill, Agent README, assertions, this comparison, with-skill
  output, or a historical baseline.
- Result: 9/14 PARTIAL. It produced the recursive Product tree and valid
  mappings/pages, but failed scoped skill loading, the exact Accounts root
  proposal boundary, complete non-leaf scope, complete command/cwd/exit
  evidence, and the missing-version audit gate.
- Skill-specific uplift: +5 assertions, or +35.7 percentage points.

## Required Test Reproduction

- The independent judge ran
  `PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest tests/acceptance/test_product_tasks.py -q -p no:cacheprovider`
  in both lanes; each returned `3 passed`.
- The judge reran `npm run test:docs`, `npm run build:public`, and
  `npm run build:internal` in both lanes; each returned exit code 0, and each
  docs test run passed 76/76 tests.
- Both generated views contained all ten Product nodes at the expected
  recursive depths, and independent link parsing found zero broken links.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With-skill assertion failures: none.
- Without-skill assertion failures: `loads_scoped_api_product_contracts`,
  `presents_batch_before_write`, `records_confirmed_non_leaf_scope`, and
  `runs_product_host_checks`, and `blocks_audit_without_confirmed_version`.
- Existing VitePress asset and chunk-size warnings were non-blocking; generated
  links and both builds succeeded.

## Next Steps

- Keep the recursive sidebar test and all five mapping closures as regression
  guards for deeper future `feature_path` trees.
- Keep the shallow Analytics domain to prove that recursive support does not
  require every product domain to have the same depth.
- Keep the API read-only candidate and missing-version assertions together with
  the Product hierarchy assertions.

## Runtime Artifact Policy

- Both lanes, dependencies, generated sites, generator events, judge events,
  final outputs, verdict, and diagnostics remain under `tmp/eval-runs/` and are
  not submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, generated-site, cache, or run-status
  artifact is committed.
