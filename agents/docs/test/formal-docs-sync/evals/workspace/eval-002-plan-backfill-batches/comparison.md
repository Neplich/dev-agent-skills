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
| loads_scoped_api_product_contracts | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 均无加载合同模块的执行证据；with_skill 仅有 `skill-map.md`，结果摘要也未展示 Product/API 模块加载过程。 |
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
| runs_product_host_checks | FAIL | FAIL | with_skill 明确报告 `npm run test:docs` 因 `fast-glob` 无法启动，未证明三个宿主命令通过；without_skill 只报告相对链接校验，缺少三条命令及 docs-audit handoff 证据。 |
| blocks_audit_without_confirmed_version | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 均没有 `docs-agent:docs-audit` handoff、affected set 或因缺少 `target_release_version` 而 blocked 的审计记录。 |

未满足断言（with/without 任一 FAIL）：`prefers_catalog_scope`、`presents_batch_before_write`、`aligns_seed_with_page`、`records_confirmed_non_leaf_scope`、`updates_product_map_atomically`、`runs_product_host_checks`

基础设施阻塞说明：；依赖缺失（fast-glob 等）；对应断言不构成 skill 行为回归。



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
