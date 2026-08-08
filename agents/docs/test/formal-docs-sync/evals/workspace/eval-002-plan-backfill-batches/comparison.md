# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45`
- Prompt SHA-256: `8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `9176713527a4959d0641a1feea488e487885b76c3aa23f11bb3b81f29825c3ae`
- Eval definition SHA-256: `be4dca3fd3a1f9f483cdce9c1cd23eedce67742046720ec2fe530fb1b240c258`
- Metadata SHA-256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill Git evidence changes only Analytics Product pages and change-map; Accounts, Billing, and unrelated paths are untouched. |
| `creates_complete_product_tree` | PASS | Locked delivery snapshot contains product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md. |
| `keeps_every_task_navigable` | FAIL | Analytics index links the task and the task links its parent, but product/index.md contains plain text stating Analytics is reached through internal navigation without an actual link. |
| `writes_evidence_backed_task_behavior` | PASS | The task page records allowed roles, empty state, load failure retry, unauthorized recovery, and binds them to dashboard.py::view_dashboard and the named acceptance test. |
| `updates_product_map_atomically` | PASS | Final Git evidence includes all three Analytics required_docs and preserves existing Billing and support entries, including triggers, excludes, and review_policy fields. |
| `runs_product_host_checks` | FAIL | The output records all three docs-site host checks with cwd docs/site and exit 0, and all three pages retain last_verified_version: unverified; however the root-to-Analytics navigation link is absent, so navigation resolution is incomplete. |
| `blocks_audit_without_confirmed_version` | PASS | The audit handoff is explicitly blocked, lists the batch, affected docs, evidence, exclusions, and target_release_version: missing; it does not claim audit readiness or infer a version. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=ac30ae9227f11b82d06a35d296220343d8767b459e7e4fe642e9b22da0e48f52; snapshot_sha256=2f59080876003ee128f9f3b6253d2c8e5eaa8dfa88fcb04ffb0f80680d32179d
- Behavior: Delivered the confirmed Analytics three-page tree and mapping, with evidence-backed task behavior and a correctly blocked audit handoff, but omitted the required root navigation link.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=12599600c13bc6c93ce714f315811aae6e9ab968cb4053c9c67e3aaf3982b8ee; snapshot_sha256=796267faee13160336978a3a5f383e7a3bcb2e638962746cd04c65072088267b
- Behavior: Fresh baseline also delivered Analytics pages and mapping, but provided less explicit evidence-backed behavior and audit gating.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- product/index.md does not contain an actual navigable link to the Analytics domain.
- The host-check requirement is not fully satisfied because the root navigation link is missing.
- Next: Add a Markdown link from docs/site/product/index.md to docs/site/product/analytics/index.md or its directory.
- Next: Re-run the docs host checks after repairing root navigation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45`
- Prompt SHA-256: `8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `be4dca3fd3a1f9f483cdce9c1cd23eedce67742046720ec2fe530fb1b240c258`
- Metadata SHA-256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill git evidence changes only Product Analytics pages and the change map; Accounts, API root, Billing, and unrelated files remain unchanged. |
| `creates_complete_product_tree` | PASS | Delivery snapshot contains product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md. |
| `keeps_every_task_navigable` | PASS | Snapshots show root→Analytics→dashboard links and the task page links back to Analytics, with node-scoped content. |
| `writes_evidence_backed_task_behavior` | PASS | Dashboard page records owner/admin/analyst visibility, empty state, load failure, retry, and unauthorized recovery, citing the implementation and acceptance test. |
| `updates_product_map_atomically` | PASS | Git evidence includes the three-page Analytics required_docs mapping while preserving existing Billing and support mapping fields, triggers, and exclusions. |
| `runs_product_host_checks` | PASS | With-skill output records all three docs-site commands with cwd docs/site/ and exit 0; all three pages retain last_verified_version: unverified and links are resolvable. |
| `blocks_audit_without_confirmed_version` | PASS | Audit handoff lists the completed Analytics batch, affected pages/map, evidence, exclusions, and target_release_version missing with status blocked. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=bf606403d2518738249a63d1ff571a48c627e84feaea1fa2b784203e8fed5c64; snapshot_sha256=42eff437d1114d91563061ff830f77db697fd38e13e493d5c1e9ca4b7f6ab430
- Behavior: Completed the confirmed Analytics documentation tree and mapping, preserved excluded areas, recorded host checks, and blocked audit pending release-version confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=07f0f3e6852dee0a9f2dbd9691e482c60008df9492dfd7893f9ece403898a543; snapshot_sha256=1825da37a88ca28edbdd93e1d6ca1ae8d15fc4e5835616d803da3583580a232e
- Behavior: Produced the three Analytics pages and claimed checks, but omitted the required change-map update and audit handoff details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45`
- Prompt SHA-256: `8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `be4dca3fd3a1f9f483cdce9c1cd23eedce67742046720ec2fe530fb1b240c258`
- Metadata SHA-256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill diff adds only Analytics Product documentation and mapping; no Accounts, Billing, or unrelated fixture files are changed, and existing mapping entries remain unchanged. |
| `creates_complete_product_tree` | PASS | With-skill status and manifest show product/index.md plus analytics/index.md and view-dashboard.md. |
| `keeps_every_task_navigable` | PASS | Locked delivery evidence for the created pages shows root-to-domain, domain-to-task, and task-to-parent links with node-scoped descriptions. |
| `writes_evidence_backed_task_behavior` | FAIL | With-skill output lists supporting evidence files but does not provide locked evidence that the task page records all required visibility, empty-state, retry, and unauthorized-recovery claims with implementation and acceptance-test locations. |
| `updates_product_map_atomically` | PASS | With-skill diff adds the Analytics glob with all three required Product pages; existing Billing and support mappings are unchanged, including their triggers, excludes, and other fields. |
| `runs_product_host_checks` | PASS | With-skill output records all three commands run from docs/site with exit status 0, states all three pages retain last_verified_version: unverified, and successful builds provide host/navigation validation. |
| `blocks_audit_without_confirmed_version` | PASS | With-skill handoff explicitly marks status blocked, lists the affected pages and map, supporting evidence, exclusions, completed batch, missing target_release_version, and maintainer confirmation dependency. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=8a2fb4cfce32432ad2f6aaf68ffc595ddea9d23c67543c0546f3382761acf3f3; snapshot_sha256=6062077a354905babcd177a5bd3d833d1c0e155e78489e5fe27a048f0df2ce60
- Behavior: Implemented the confirmed Analytics Product batch, preserved excluded areas, recorded host checks, and correctly blocked release audit pending a maintainer-confirmed version; task-page behavior evidence is not established by the locked record.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=9105462cd71586b660233f47fd5beee63e025bb2082b6ebb614ea8d234e4bfab; snapshot_sha256=fe509db0656624a3ef67722d26d47fa7a2ea5efdf2da8cdbdab230d05c6f0b9a
- Behavior: Created the Analytics tree and mapping, but claimed broad verification without an audit handoff or confirmed-version block; generated navigation artifacts remained.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- writes_evidence_backed_task_behavior is not substantiated by the locked with-skill evidence.
- Next: Provide the created dashboard task page content or equivalent locked evidence showing each required claim mapped to dashboard.py and the named acceptance test.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45`
- Prompt SHA-256: `8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `be4dca3fd3a1f9f483cdce9c1cd23eedce67742046720ec2fe530fb1b240c258`
- Metadata SHA-256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill Git evidence shows changes only to the Product pages/map and no Accounts, Billing, API root, or existing Billing file changes. |
| `creates_complete_product_tree` | PASS | Delivery snapshot contains product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md. |
| `keeps_every_task_navigable` | PASS | Product links Analytics, Analytics links the dashboard task, and the task links its parent; scope and direct-child descriptions are present. |
| `writes_evidence_backed_task_behavior` | PASS | The task page documents all three allowed roles, ready/empty states, load-failure retry, unauthorized recovery, and references the dashboard implementation and acceptance test. |
| `updates_product_map_atomically` | PASS | Git evidence includes the Analytics three-page required_docs mapping; the Billing and support entries retain their existing triggers, excludes, and policies. |
| `runs_product_host_checks` | PASS | With-skill output records all three required commands run from docs/site with exit 0; all three pages retain last_verified_version: unverified and their links target existing pages. |
| `blocks_audit_without_confirmed_version` | PASS | Audit handoff lists the completed Analytics batch, affected pages/map, evidence, exclusions, and target_release_version missing with status blocked. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=23dd99549d44a4478504e27e8314bd37cf4729480f4972640add38abe75f2541; snapshot_sha256=08cc692b74f2b460bb0eb420c0e5c502d5db08a2cf27f6daebd5d7fb225cce83
- Behavior: Produced the confirmed Analytics-only tree and mapping, documented evidence-backed behavior, reported host checks, and explicitly blocked audit pending target release confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=8c76d84a928656a60e5327baf7b5c2563335c466cda3d895d9bdc1cf642edd04; snapshot_sha256=75eebd011c38cca6a4287e3154b2462654cce0c7e3098e630fef6617809e7843
- Behavior: Produced the requested Analytics tree and mapping and reported host checks, but omitted the required audit handoff and did not report acceptance-test success.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45`
- Prompt SHA-256: `8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e338138030b22a6ae7490409e1775199fdfb2000266aaae4be515f4b6517895c`
- Skill overlay SHA-256: `b34598ef98f82f331a2854f425e5c9d02ef08aad3dbdc8d0e1449576a18d9737`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `be4dca3fd3a1f9f483cdce9c1cd23eedce67742046720ec2fe530fb1b240c258`
- Metadata SHA-256: `5fd28d9378e7eecda587e4671ac17460a0dd3663cff48d75fd068b1dc2cb5f0c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_unconfirmed_batch_read_only` | PASS | with_skill 的状态与 diff 仅新增 Analytics Product 页面及对应映射；Accounts、Billing 和其他既有条目未修改。 |
| `creates_complete_product_tree` | PASS | 交付快照包含 product/index.md、product/analytics/index.md 和 view-dashboard.md，形成三层树。 |
| `keeps_every_task_navigable` | PASS | 根页链接 Analytics，Analytics 页链接 dashboard 任务，任务页反向链接 Analytics；各页范围和直接子节点描述符合要求。 |
| `writes_evidence_backed_task_behavior` | PASS | 任务页记录 owner/admin/analyst 权限、空状态、加载失败重试及未授权恢复建议，并通过 related_code 关联 dashboard 实现和 acceptance tests。 |
| `updates_product_map_atomically` | PASS | 快照包含 Analytics 三层 required_docs 映射；Billing 与 support 条目的 trigger、exclude、review_policy 等既有字段保持不变。 |
| `runs_product_host_checks` | PASS | with_skill 明确记录 cwd 为 docs/site/，test:docs、build:public、build:internal 均 exit 0；三页为 unverified，页面链接可解析。 |
| `blocks_audit_without_confirmed_version` | FAIL | with_skill 表示等待 target_release_version 后再交 docs-audit，但未在交接中列出完整 affected set、完整排除项和已覆盖批次，也未明确标记为 blocked。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=3e0db27d03cbd69e3d9a2662bae395db9784cd43a70fd0149beb54c4144b40fd; snapshot_sha256=2e1101eba5f7e9be8a469f0aff3ee31bbe89bf8ebf081c3454d1f68320f0d421
- Behavior: 正确完成 Analytics 三层文档、导航、证据映射、范围隔离和三项宿主检查；审计交接未完整满足要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8abbeebf58a017f34c7b7989f0280e2daf82af8f4daf404a0ba21c98f5540049; fixture_sha256=d39e08e3921dea4ed3620111c7989cda61f1e85ab306939032821affe0218f45; output_sha256=009339be1ba498f90de09d419abaed095c9a2a32ae0e85c2b034f6ffb6cf1ce6; snapshot_sha256=666534d81e73982a77737fc285ba11ac81bebf179550db7e1a65c682eb15af66
- Behavior: 完成了基本 Analytics 页面和映射，但未充分记录任务证据，也未记录完整宿主检查或审计阻塞交接。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 的 docs-agent:docs-audit handoff 缺少完整 affected set、完整排除项、已覆盖批次及明确 blocked 状态。
- Next: 补充完整审计交接清单，并将因缺少 target_release_version 的状态明确标为 blocked。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ff2978a19218daf3ee17d1aeea66d5a3b52bc2f5ad798c16064946bfe89814a4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `ff2978a19218daf3ee17d1aeea66d5a3b52bc2f5ad798c16064946bfe89814a4`
- Prompt SHA-256: `b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ae90c79234e240e94a1c4163f10473b4638ab357414478ae34e4410e752613b8`
- Skill overlay SHA-256: `9b8e63e6228c18764bc0faabd4879064df2cdca45e6372e693a249916edd894b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `674e177d87a50f0f05a1583dadd978460365e1f4229b5f205a9f834e5a46d21f`
- Metadata SHA-256: `bad705c6a3981db437dc55d6c99d8a43af658e9de678271ac7ab24dcbf326198`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | 锁定证据未证明 formal-docs-sync 公共合同或 Product/API 模块加载顺序。 |
| `prefers_catalog_scope` | PASS | 候选输出给出 Analytics 产品同步、Accounts 为 identity-team，并保留 Billing；路径与 fixture catalog 一致。 |
| `presents_batch_before_write` | FAIL | 列出了三页候选树、代码和 owner，但未列出明确的排除项。 |
| `keeps_unconfirmed_batch_read_only` | PASS | 明确声明 Accounts 零写入；git 状态和 diff 仅显示 Product 页面及 Product 映射变更。 |
| `aligns_seed_with_page` | FAIL | 只提出 src/api/accounts/** 映射和页面树，未明确给出覆盖三个 required_docs 的映射条目。 |
| `creates_complete_product_tree` | PASS | 明确列出并同步 product/index.md、analytics/index.md、view-dashboard.md。 |
| `keeps_every_task_navigable` | NOT_EXERCISED | 锁定 with_skill 输出未提供页面内容或导航链接证据。 |
| `writes_evidence_backed_task_behavior` | NOT_EXERCISED | 锁定 with_skill 输出未展示任务页行为内容及实现/验收测试逐项定位。 |
| `updates_product_map_atomically` | PASS | git 状态显示三层 Product 页面和 change-map.yaml 变更；diff 未显示 Billing 或无关映射变更。 |
| `runs_product_host_checks` | FAIL | 记录了 test:docs，但未执行或记录 build:public、build:internal 的 cwd 与退出状态。 |
| `blocks_audit_without_confirmed_version` | FAIL | 输出未提供 docs-agent:docs-audit handoff、affected set 或因缺少 target_release_version 的 blocked 状态。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=ff2978a19218daf3ee17d1aeea66d5a3b52bc2f5ad798c16064946bfe89814a4; output_sha256=7a93686291d2683947298f86a2f4cf8120fec5ea9614ce98c477b2a4fca85ad4; snapshot_sha256=a98a4a27660477e6059832f2e95d57e03335ea619c25af1ddecc911694d48873
- Behavior: 正确落地 Analytics 并保持 Accounts 零写入，报告候选 API 树和部分检查；缺少完整排除项、required_docs、页面导航/行为证据、两项构建检查及审计 handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=ff2978a19218daf3ee17d1aeea66d5a3b52bc2f5ad798c16064946bfe89814a4; output_sha256=920659f65efe031121fe5f89c1ba5dd7ce9f15731f322269fcf8dab69ca93818; snapshot_sha256=93b40a2b8b5502946701e091f5066a6dcb0f1f5b13785f9d586224c73dc18165
- Behavior: 完成 Analytics 三层页面和 Product 映射，并保持 Accounts 未写入；报告较简略，未覆盖候选 API 树细节及审计要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 候选 API 批次报告缺少明确排除项。
- Accounts 映射未明确列出三个 required_docs。
- 未记录 build:public 和 build:internal。
- 未提供缺少 target_release_version 时 blocked 的 docs-agent:docs-audit handoff。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc`
- Prompt SHA-256: `b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ae90c79234e240e94a1c4163f10473b4638ab357414478ae34e4410e752613b8`
- Skill overlay SHA-256: `9b8e63e6228c18764bc0faabd4879064df2cdca45e6372e693a249916edd894b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `674e177d87a50f0f05a1583dadd978460365e1f4229b5f205a9f834e5a46d21f`
- Metadata SHA-256: `bad705c6a3981db437dc55d6c99d8a43af658e9de678271ac7ab24dcbf326198`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `5568d3e6f0cce47c83a23dfe1d385eed4c71cf991b770afb6cbef93b0e4e8cce`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | 锁定证据未能证明具体公共合同的加载过程或读取顺序。 |
| `prefers_catalog_scope` | PASS | Analytics 使用 insights-team；Accounts 使用 identity-team，并引用真实代码与验收测试路径；Billing 保持批次外。 |
| `presents_batch_before_write` | PASS | 报告展示 api/index.md → api/accounts/index.md → api/accounts/get-account.md，并列出代码证据、owner、映射、排除项和 unconfirmed 状态。 |
| `keeps_unconfirmed_batch_read_only` | PASS | git 状态和 diff 仅包含 Product Analytics 页面及 Product 映射；Accounts、API root、Billing 页面均未修改。 |
| `aligns_seed_with_page` | PASS | Accounts 建议映射覆盖 src/api/accounts/** 及三个 required_docs，并保留既有 Billing 映射、排除越界页面。 |
| `creates_complete_product_tree` | PASS | 交付快照包含 product/index.md、product/analytics/index.md 和 view-dashboard.md 三层页面。 |
| `keeps_every_task_navigable` | PASS | Product 根链接 Analytics，Analytics index 链接 dashboard 任务，任务页链接 Analytics 与产品根页面。 |
| `writes_evidence_backed_task_behavior` | PASS | 任务页引用 dashboard.py 与 acceptance test，并记录 owner/admin/analyst 可见性、empty、加载失败 retry 和越权恢复。 |
| `updates_product_map_atomically` | PASS | 快照同时包含 Analytics 三层页面和 src/product/analytics/** 的三层映射；Billing 与 support 映射内容未变。 |
| `runs_product_host_checks` | FAIL | 未记录 npm run build:public 或 npm run build:internal；npm run test:docs 仅报告初次因 committed base 无法解析而失败，不能证明三项宿主检查通过。 |
| `blocks_audit_without_confirmed_version` | PASS | 报告明确将 docs-audit handoff 标为 blocked，指出缺少已确认 target_release_version，并提供候选批次、证据与排除项，未声称 ready。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=fc628e4ef7173aacdb296d4fd8e271f74eca8de2b94f4a3d20cf2360b61a895c; snapshot_sha256=afdb5750b17dc481b495a1802a1957b750c193f29b8c1b9ca87a5e8c2d3a540c
- Behavior: 正确完成已确认的 Analytics Product 三层文档，保持 Accounts 只读并提供完整候选树、证据和阻塞 handoff；但宿主检查记录不完整且 test:docs 未通过。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=9b3bdc37cd928367ca63c30e0fbfe1e631752ac4d9ada1871d1db28cc060bb1b; snapshot_sha256=2e4a9e39d1596a4f58621e178a44351c02d69a36469cbfe2ae8673654029e3e0
- Behavior: 完成 Analytics 文档和基础映射，并提出 Accounts 建议，但未展示完整 Accounts 候选树、证据边界或 blocked audit handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未完成或未证明 npm run test:docs、npm run build:public、npm run build:internal 三项宿主检查通过。
- Next: 补充并成功记录 docs/site 下三项宿主检查及导航链接解析结果。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc`
- Prompt SHA-256: `b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ae90c79234e240e94a1c4163f10473b4638ab357414478ae34e4410e752613b8`
- Skill overlay SHA-256: `9b8e63e6228c18764bc0faabd4879064df2cdca45e6372e693a249916edd894b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `674e177d87a50f0f05a1583dadd978460365e1f4229b5f205a9f834e5a46d21f`
- Metadata SHA-256: `bad705c6a3981db437dc55d6c99d8a43af658e9de678271ac7ab24dcbf326198`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `942fbce8d1515dca58a012d1d8ca6b0fbd7278cbfa2c66f483e7e29f04d649b4`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | 候选输出说明加载了 product 与仅用于 Accounts 只读规划的 api 模块，但锁定证据无法证明 formal-docs-sync 公共合同的实际应用过程。 |
| `prefers_catalog_scope` | PASS | Analytics 使用 insights-team，Accounts 建议使用 identity-team；候选引用的代码、测试和既有 Billing 路径均存在，Git 证据显示 Billing 映射未改动。 |
| `presents_batch_before_write` | PASS | 候选展示了 api/index.md、api/accounts/index.md、api/accounts/get-account.md，并列出代码证据、契约测试、identity-team、建议映射、排除项和待确认状态。 |
| `keeps_unconfirmed_batch_read_only` | PASS | Git 状态和 diff 仅包含 Product Analytics 三页及其映射；没有 Accounts、API root 或 Billing 页面变更。 |
| `aligns_seed_with_page` | PASS | 候选建议映射为 src/api/accounts/**，required_docs 覆盖 API root、Accounts index 和 get-account leaf；Git diff 保留既有 Billing 映射。 |
| `creates_complete_product_tree` | PASS | Git 证据包含 docs/site/product/index.md、analytics/index.md 和 view-dashboard.md 三层页面。 |
| `keeps_every_task_navigable` | PASS | 交付快照显示 Product 根链接 Analytics，Analytics index 链接 dashboard 任务，任务页反向链接 Analytics 父页。 |
| `writes_evidence_backed_task_behavior` | PASS | 任务页记录 owner/admin/analyst 可见性、empty 状态、加载失败 retry 和越权恢复，并分别引用 dashboard 实现与 acceptance test。 |
| `updates_product_map_atomically` | PASS | Git diff 同时包含 Analytics 三层页面及 src/product/analytics/** 的三层 required_docs 映射；交付快照显示既有 Billing 和 support 条目保持不变。 |
| `runs_product_host_checks` | FAIL | 候选记录了 docs/site 下的 frontmatter、version 和文档测试，但未记录 npm run build:public 或 npm run build:internal；npm run test:docs 还明确为 exit 1。 |
| `blocks_audit_without_confirmed_version` | PASS | 候选列出 Analytics 已覆盖批次、Accounts 未确认候选、证据与排除范围，并明确 docs-audit 暂阻塞，指出缺少 target_release_version，未声称 ready 或推断版本。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=2e702a0bba2ef10f420c220818435f8a1a01ac89d4cdc9fa5c40df1cca7222f6; snapshot_sha256=2db94c30c404fc6b9773111bc04bbf045da18d1cdc574397b4d44c14f57fb8be
- Behavior: 正确完成已确认 Analytics 批次并保持 Accounts 只读，提供完整候选树、证据和审计阻塞信息；缺少 public/internal build 记录且 test:docs 失败。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=ecd0521d247e779d889ddf61141f25f338247445fcb6b34588100010e3cdfa15; snapshot_sha256=ba4da5007779b0bb42517ae3f3c4d7191712276ad983d1d47f622a6514e0c1dd
- Behavior: 完成 Analytics 三页和映射，但仅给出简略 Accounts 建议，未提供完整合同范围、证据、阻塞审计和宿主检查细节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- runs_product_host_checks 未记录 npm run build:public 和 npm run build:internal，且 npm run test:docs 为 exit 1。
- Next: 补跑并记录 docs/site 下 npm run test:docs、npm run build:public、npm run build:internal 的退出状态，并解决 test:docs 的 affected-check 阻塞。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc`
- Prompt SHA-256: `b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ae90c79234e240e94a1c4163f10473b4638ab357414478ae34e4410e752613b8`
- Skill overlay SHA-256: `9b8e63e6228c18764bc0faabd4879064df2cdca45e6372e693a249916edd894b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `674e177d87a50f0f05a1583dadd978460365e1f4229b5f205a9f834e5a46d21f`
- Metadata SHA-256: `bad705c6a3981db437dc55d6c99d8a43af658e9de678271ac7ab24dcbf326198`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `88e3dd18c44d213fbbe3d124e36d721a91510f2326cd5b3ec31b4c12fbb87e67`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | The locked output names product and api modules, but cannot prove application of the public contract or the required load order. |
| `prefers_catalog_scope` | FAIL | Accounts is proposed with owner '尚未确认', contradicting the catalog's identity-team owner requirement. |
| `presents_batch_before_write` | FAIL | The candidate tree and evidence are shown, but the required identity-team owner is omitted. |
| `keeps_unconfirmed_batch_read_only` | PASS | Git status/diff show only Product pages and change-map changes; no Accounts, API root, or Billing writes. |
| `aligns_seed_with_page` | PASS | The proposed src/api/accounts/** mapping and three-node API tree are listed; Billing mapping content is unchanged in the diff. |
| `creates_complete_product_tree` | PASS | All three required Product pages are present in the delivery snapshot. |
| `keeps_every_task_navigable` | PASS | Root links Analytics, Analytics links the task, and the task links back to Analytics. |
| `writes_evidence_backed_task_behavior` | PASS | The task page documents roles, empty state, retry behavior, and access recovery, with implementation and acceptance-test references. |
| `updates_product_map_atomically` | PASS | Git evidence contains the three Analytics required_docs and leaves existing Billing/support trigger, exclude, and policy fields unchanged. |
| `runs_product_host_checks` | FAIL | The output records npm run test:docs but does not record execution or exit status for npm run build:public and npm run build:internal. |
| `blocks_audit_without_confirmed_version` | FAIL | It notes no confirmed target_release_version and defers audit, but does not explicitly provide the required blocked docs-audit handoff with a complete affected set, evidence, exclusions, and covered batches. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=0a0027d5b8dc701fa101f6e06444b64fee68919210f0632f23c0c3fbeef67a56; snapshot_sha256=e3c46ff4550776f7b16cbf8a34d1aee9e11654707852f82cd4a86e7eccf2d54e
- Behavior: Correctly created and evidenced the Analytics tree, preserved unconfirmed Accounts as read-only, and documented a proposed API tree, but omitted the catalog owner, two required builds, and a fully explicit blocked audit handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=26c98e386b7e1b337eb55e8c038a701aa31d8034adddc0d2910dbe1f5aa3a0d5; snapshot_sha256=83d97bb80632273ea832aebfe53b95f99cb1caa8e9ef4d8ac67c330a72cb0f30
- Behavior: Created the Analytics Product tree and mapping, omitted Accounts writes, and reported partial checks; it did not present the scoped API planning evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Accounts owner is reported as unconfirmed instead of identity-team.
- The required public and internal build checks are not recorded.
- The docs-audit handoff is not explicitly blocked with the complete required contents.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc`
- Prompt SHA-256: `b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ae90c79234e240e94a1c4163f10473b4638ab357414478ae34e4410e752613b8`
- Skill overlay SHA-256: `9b8e63e6228c18764bc0faabd4879064df2cdca45e6372e693a249916edd894b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `674e177d87a50f0f05a1583dadd978460365e1f4229b5f205a9f834e5a46d21f`
- Metadata SHA-256: `bad705c6a3981db437dc55d6c99d8a43af658e9de678271ac7ab24dcbf326198`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | Raw evidence does not prove contract/module load order or process selection. |
| `prefers_catalog_scope` | PASS | With-skill output identifies Analytics as insights-team-owned and Accounts as identity-team-owned, cites real route/schema/test paths, and the diff leaves Billing unchanged. |
| `presents_batch_before_write` | FAIL | The candidate lists the Accounts page tree and pending status but omits the complete code boundary, mapping increment, exclusions, and full evidence details. |
| `keeps_unconfirmed_batch_read_only` | PASS | Git evidence shows only Analytics product pages, product root, and the Analytics mapping changed; no Accounts, API root, or Billing files changed. |
| `aligns_seed_with_page` | FAIL | The candidate proposes Accounts pages but does not provide the required src/api/accounts/** mapping with the three required_docs or demonstrate preservation of Billing mapping fields. |
| `creates_complete_product_tree` | PASS | Delivery snapshot contains product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md. |
| `keeps_every_task_navigable` | PASS | Root links Analytics, Analytics index links the dashboard task, and the task links its parent; page scopes are separated appropriately. |
| `writes_evidence_backed_task_behavior` | PASS | The task page documents owner/admin/analyst visibility, empty state, load failure and retry, unauthorized recovery, and cites the dashboard implementation and acceptance test. |
| `updates_product_map_atomically` | PASS | Git evidence includes all three Analytics pages and three required_docs under src/product/analytics/**; the existing Billing and unrelated mappings remain present and unchanged. |
| `runs_product_host_checks` | FAIL | The candidate does not record npm run test:docs, npm run build:public, and npm run build:internal with docs/site cwd and exit statuses. |
| `blocks_audit_without_confirmed_version` | FAIL | The candidate says release-version confirmation is pending, but does not provide the required complete docs-agent:docs-audit handoff with affected set, evidence, exclusions, and covered batches. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=855d26b89c5d03d2867bc50d79c88e0c055c5131d1278598fada36a001a7a8b1; snapshot_sha256=591c88aff0ad0e21451cacf43fa540a8122960851a5a21dde3576ed682f0b76d
- Behavior: Correctly delivered the confirmed Analytics batch and kept Accounts read-only, but omitted required Accounts mapping detail, exact host checks, and a complete blocked audit handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=c9ca36b58ababc7a19b2ba822ee9ac77dda8aa639cf7b1ee1ae2e9e262ca473f; snapshot_sha256=cdc83e971cabc4fec947d790d19e64acc6d4ff6029722492a528600a58375e78
- Behavior: Completed the Analytics tree and mapping, but reported weaker verification and only a brief Accounts suggestion.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Accounts candidate reporting is incomplete and lacks the required proposed mapping details.
- Required docs-site host commands and their cwd/exit statuses are not recorded.
- The docs-audit handoff is incomplete despite correctly awaiting release-version confirmation.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc`
- Prompt SHA-256: `b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ae90c79234e240e94a1c4163f10473b4638ab357414478ae34e4410e752613b8`
- Skill overlay SHA-256: `9b8e63e6228c18764bc0faabd4879064df2cdca45e6372e693a249916edd894b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `674e177d87a50f0f05a1583dadd978460365e1f4229b5f205a9f834e5a46d21f`
- Metadata SHA-256: `7c4a4d5707dfe6fb5343f4ca9d8c5c5615fe50505393af0e7f27402bea165131`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | Locked evidence does not prove the hidden contract application or module load order. |
| `prefers_catalog_scope` | PASS | With-skill output identifies Analytics as insights-team and Accounts as identity-team, cites existing source paths, and reports only Analytics/Product and mapping changes; Billing remains unchanged. |
| `presents_batch_before_write` | FAIL | The candidate tree and evidence boundaries are shown, but the report does not enumerate the mapping increment and exclusion items required in the proposed batch. |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill git evidence shows only Analytics Product pages and its mapping changed; no Accounts, API root, or Billing files were modified. |
| `aligns_seed_with_page` | FAIL | The report mentions the Accounts tree and source evidence but does not provide the proposed Accounts mapping with the three required_docs or verify preservation of existing Billing mapping fields. |
| `creates_complete_product_tree` | PASS | The output lists product/index.md, product/analytics/index.md, and product/analytics/view-dashboard.md, and raw status shows the Analytics pages added. |
| `keeps_every_task_navigable` | FAIL | The output lists the pages but omits the required root-to-domain-to-task and task-to-parent navigation result, which is not present in the locked with-skill diff evidence. |
| `writes_evidence_backed_task_behavior` | FAIL | The report summarizes roles, empty state, load failure, and recovery, but does not locate each claim to the dashboard implementation and corresponding acceptance test. |
| `updates_product_map_atomically` | PASS | With-skill diff adds the three Analytics required_docs under src/product/analytics/** and preserves the existing Billing/support mapping content; status shows no unrelated tracked changes. |
| `runs_product_host_checks` | FAIL | The report records passing frontmatter/version checks, script tests, and public/internal builds, plus test:docs failure, but does not record the required cwd and complete exit-status details or navigation-link resolution. |
| `blocks_audit_without_confirmed_version` | FAIL | It correctly says the release version is unverified and audit is pending, but does not provide a docs-agent:docs-audit handoff listing the complete affected set, evidence, exclusions, and covered batches. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=c9ec471a6ef41dab5a5a593570b27e1ebdb19887bb683cc5f8c94e2c43673466; snapshot_sha256=9db37c2d3bcaa2b736fb8fe844992bcfe2b46a0484b0354cb96c66ba32d03688
- Behavior: Correctly scoped and wrote the confirmed Analytics Product batch while leaving Accounts untouched and reporting missing release-version/runtime checks, but omitted several required planning, navigation, evidence-location, and audit-handoff details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=2b8a7fe4bde7b735f51ce790a2bb722fd696ec458c15d85eadc92b1a770255cd; snapshot_sha256=02f117221d1df0e21afda4e0c4115e01067ab36e8854b10995142a0c073b8fc8
- Behavior: Completed the confirmed Analytics Product write and basic build claims, but lacked strict affected verification and detailed Accounts planning evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill report omits required Accounts mapping details, complete candidate-batch exclusions, navigation verification, claim-to-source/test locations, required cwd/exit-status records, and the complete docs-audit handoff.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc`
- Prompt SHA-256: `b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3f67e4da977602f7c82a15dd20c25b54ae7441a76825b33ffdd46aea1e7684ac`
- Skill overlay SHA-256: `3e6d162c4517cefa50603d7572bc00f46efa0486f62e30e79ca7e042764ffe18`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fb2c03c1c61801384ea8a8b915a4111095a3ffbddae1a3d23002b4f6fa03a339`
- Metadata SHA-256: `7c4a4d5707dfe6fb5343f4ca9d8c5c5615fe50505393af0e7f27402bea165131`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | 输出提到加载 product/api 模块，但锁定证据无法证明 formal-docs-sync 公共合同或读取顺序。 |
| `prefers_catalog_scope` | FAIL | 未显示使用 feature catalog，且 Accounts owner 建议为 platform-team，与 catalog 中的 identity-team 不一致。 |
| `presents_batch_before_write` | FAIL | 展示了完整 Accounts 树和大部分范围信息，但 owner 使用 platform-team 而非 catalog 的 identity-team；锁定证据也无法证明是在写入前展示并等待确认。 |
| `keeps_unconfirmed_batch_read_only` | PASS | git diff 和交付快照显示未创建或修改 Accounts 页面、API root、Billing 页面或既有 Billing 映射，仅写入确认的 Analytics 页面和映射。 |
| `aligns_seed_with_page` | PASS | 输出提出 src/api/accounts/** 到 api root、Accounts index 和 get-account leaf 的三层映射；git diff 显示既有 Billing 条目未改变。 |
| `creates_complete_product_tree` | PASS | 交付快照包含 docs/site/product/index.md、product/analytics/index.md 和 product/analytics/view-dashboard.md。 |
| `keeps_every_task_navigable` | PASS | 交付页面内容显示 Product 根链接 Analytics，Analytics index 链接 dashboard 任务，任务页链接父级和产品入口。 |
| `writes_evidence_backed_task_behavior` | PASS | 任务页记录 owner/admin/analyst 可见性、空状态、加载失败重试和越权恢复，并引用 dashboard.py 与对应 acceptance test。 |
| `updates_product_map_atomically` | NOT_EXERCISED | 最终映射包含三层 Product required_docs 且既有条目在 diff 中保留，但锁定证据无法证明写入过程具有原子性。 |
| `runs_product_host_checks` | FAIL | 未完整记录要求的三条命令及各自 docs/site cwd；且 npm run test:docs 明确失败，因此不能满足三项宿主检查通过并记录的要求。 |
| `blocks_audit_without_confirmed_version` | FAIL | 输出正确说明缺少 target_release_version 且 audit 阻塞，但未提供要求的完整 affected set、证据、排除项和已覆盖批次 handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=c8f38d7088a9dae61f66240c581f7aa0a42ae115f5fa8c140a64f6c1f41613a9; snapshot_sha256=6fb9de73045eb77617e20a240b35de111ae5be78680be97e3ff30bdcb4f8e876
- Behavior: 正确完成确认的 Analytics 文档树、导航、证据记录和只读 Accounts 规划，但 owner、检查记录及 audit handoff 存在缺失或不一致。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=d35d2d4dd60e004e27e59177ab1125b603dbb0e531a481051a46fbdba59aa4ce; snapshot_sha256=e4d11ea1466c7e87f51e4d5962d7e62b6df870dc378a41460d35cf900eed7a27
- Behavior: 完成 Analytics 三页和映射，但仅简要提出 Accounts 建议，检查记录较少。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Accounts owner 建议与 feature catalog 不一致，且未证明使用 catalog。
- 未完整满足 docs/site 宿主检查命令、cwd 和退出状态记录要求，test:docs 失败。
- Docs audit handoff 缺少完整 affected set、证据、排除项和已覆盖批次。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-002-plan-backfill-batches`.
- Fixture SHA-256: `5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc`
- Prompt SHA-256: `b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fb2c03c1c61801384ea8a8b915a4111095a3ffbddae1a3d23002b4f6fa03a339`
- Metadata SHA-256: `7c4a4d5707dfe6fb5343f4ca9d8c5c5615fe50505393af0e7f27402bea165131`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | 候选输出和锁定原始证据无法证明合同应用或模块加载顺序。 |
| `prefers_catalog_scope` | NOT_EXERCISED | 结果与 catalog 范围一致，但锁定证据无法证明读取或优先使用 catalog 的过程。 |
| `presents_batch_before_write` | FAIL | 展示了三条 Accounts 路径及部分接口信息，但未列出完整的代码边界、证据、映射增量、排除项和明确待确认状态清单。 |
| `keeps_unconfirmed_batch_read_only` | PASS | with_skill 的 git 状态和 diff 仅包含 Product Analytics 页面及其映射；Accounts、API root、Billing 均未修改。 |
| `aligns_seed_with_page` | PASS | 候选提出 src/api/accounts/**，并给出 api root → accounts index → get-account leaf 的完整候选树；Billing 保持未变。 |
| `creates_complete_product_tree` | PASS | 原始 delivery snapshot 包含 product/index.md、product/analytics/index.md 和 view-dashboard.md 三层页面。 |
| `keeps_every_task_navigable` | PASS | Product 根链接 Analytics，Analytics index 链接 dashboard，任务页反向链接父级；快照中的链接路径可逐级解析。 |
| `writes_evidence_backed_task_behavior` | PASS | 任务页覆盖 owner/admin/analyst 可见性、empty 状态、加载失败与 retry 恢复，并引用 dashboard 实现和对应 acceptance test；源代码与测试支持这些主张。 |
| `updates_product_map_atomically` | PASS | with_skill diff 新增 Analytics 三层 required_docs 映射；原始完整 change-map 快照保留 Billing 与 support 条目的既有字段。 |
| `runs_product_host_checks` | FAIL | 候选仅报告 frontmatter、版本检查、76 个测试和导航结果，未记录指定 npm run test:docs、build:public、build:internal 的 cwd 与退出状态。 |
| `blocks_audit_without_confirmed_version` | NOT_EXERCISED | 候选未声明 audit ready，也未提供 audit handoff；缺少 target_release_version 的后续审计步骤按规则视为未 exercised。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=f024b18c5f591e5875115bb2e3143e0442e06c4f1296c045f8f265df04bda7a1; snapshot_sha256=349ce72462df294e95433b254e21d687eee899592b98d93af7f3f13d523ccce2
- Behavior: 正确落地完整 Analytics Product 子树、证据和映射，并保持 Accounts/Billing/API 未修改；候选树说明不完整，且未记录全部指定宿主命令。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b8f7f74c6c12ed6bb9af4605da763d91c23adace1924488d63c8891befcc5b22; fixture_sha256=5b1e95e619c9723c58ca7dc9fa4d41f3bd1c9ea83686d95dfbf069b376eed8fc; output_sha256=b5ab72573d6d4829ab24ef5c4820c989eb0fd2e9e53f8629a1ce26aa8198f25f; snapshot_sha256=cd999067e2266f45c8eea2d2780eaad8c9e8837c0fad4f900520585e8db24ad4
- Behavior: 完成了 Analytics 三层页面和映射，并保持 Accounts 未写入，但未提供完整候选树细节或指定宿主检查结果。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- presents_batch_before_write 未列出完整的代码边界、证据、映射增量、排除项和待确认状态。
- runs_product_host_checks 未记录三个指定命令的 cwd 与退出状态。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2c8e08b3132af642c4bb05621cb003e26dd288906af387a3ced10de28578b14d`
- Metadata SHA-256: `7fae8c9ebc1571e6ee6485e0157870ec8eb18079ff4d13256bd1589929d19c33`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | NOT_EXERCISED | Locked evidence contains no readable skill/process trace proving contract load order or module exclusions. |
| `prefers_catalog_scope` | NOT_EXERCISED | The catalog and source files are present, but the locked evidence does not prove the selection and path-checking process. |
| `presents_batch_before_write` | FAIL | The with_skill output suggests one Accounts endpoint but does not present the complete root/domain/leaf tree with the required per-node fields or explicitly wait for confirmation. |
| `keeps_unconfirmed_batch_read_only` | PASS | Git evidence shows no Accounts, API root, or Billing page/map changes; Product pages and confirmed Product mappings were added. |
| `aligns_seed_with_page` | FAIL | No Accounts change-map seed or complete required_docs proposal is shown; the output only mentions routes, schemas, and contract tests. |
| `handles_missing_catalog_semantically` | NOT_EXERCISED | A confirmed feature catalog exists, so the no-catalog branch is not exercised. |
| `creates_complete_product_tree` | PASS | The delivery snapshot contains product/index.md, both domain indexes, invitations and both second-level indexes, and all four required task pages. |
| `keeps_every_task_navigable` | PASS | The delivered links form the required root-to-domain-to-feature-to-task paths without skipped intermediate indexes. |
| `records_confirmed_non_leaf_scope` | FAIL | Several non-leaf pages provide navigation and some scope, but the root and lower-level indexes do not consistently state the required audience/owner, adjacent capability, and batch exclusions for each node. |
| `writes_evidence_backed_task_behavior` | PASS | Task pages cite the corresponding implementation functions and acceptance tests and cover the required permissions, limits, states, feedback, and recovery behavior. |
| `updates_product_map_atomically` | FAIL | Mappings have appropriate Product globs and ancestor closures, but the merged change-map order places Product entries before existing API Billing entries rather than maintaining stable code-glob ordering. |
| `links_authorities_without_copying_contracts` | PASS | Each delivered task page links its parent and Design/API/Database/Ops authority indexes without duplicating contract text or creating role-based duplicate trees. |
| `runs_product_host_checks` | NOT_EXERCISED | The output reports frontmatter/version checks and acceptance tests, but complete test:docs plus both builds, cwd/exit records, visibility/link verification, and docs-audit handoff are unavailable; it does not claim they passed. |
| `blocks_audit_without_confirmed_version` | NOT_EXERCISED | No audit handoff evidence is present, and the candidate does not claim pre-tag audit readiness. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6e26676a89a16acec9866e91e19dd92a1b85a0401ad645a6160108df17d9b4b2; fixture_sha256=3a676f73bf7941f0ab035834abd0887251dca20d52501fbcda26212974e9b01d; output_sha256=ea44aad3f66d4a120fb531c4720ed02ffad712ebdbe00e0fb2225f5eacc410ab; snapshot_sha256=73d0cedc968b8991d9f454490be86aabfd3b01b0c23bfbec0c25554bdabdd583
- Behavior: Created the full confirmed Product tree with evidence-backed task pages and mappings, kept Accounts unmodified, but omitted the complete Accounts confirmation tree and had scope/order and validation gaps.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6e26676a89a16acec9866e91e19dd92a1b85a0401ad645a6160108df17d9b4b2; fixture_sha256=3a676f73bf7941f0ab035834abd0887251dca20d52501fbcda26212974e9b01d; output_sha256=be516dbe646c86d6877d52a7a80d28464be6baa6e30b506ec66c78cf61b80273; snapshot_sha256=5a3dde1d2addce5964778ac7f298a1ae6d0eee2b4d884b655d3ef8c2a645aedd
- Behavior: Completed the Product tree and mappings, but provided less precise Accounts planning and only partial validation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Missing complete Accounts root/domain/leaf batch presentation and per-node scope fields.
- Missing proposed Accounts change-map seed with complete page closure.
- Incomplete non-leaf Product scope metadata.
- Change-map entries are not stably code-glob sorted.
- Next: Provide the complete Accounts candidate tree and wait for maintainer confirmation.
- Next: Add the Accounts seed proposal with required_docs and preserved Billing metadata.
- Next: Complete non-leaf scope metadata and stable change-map ordering.
- Next: Run the full host checks when Git/temp-directory operations are available, then hand off a blocked audit pending target_release_version.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2c8e08b3132af642c4bb05621cb003e26dd288906af387a3ced10de28578b14d`
- Metadata SHA-256: `7fae8c9ebc1571e6ee6485e0157870ec8eb18079ff4d13256bd1589929d19c33`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `loads_scoped_api_product_contracts` | FAIL | With-skill evidence shows only skill visibility, not ordered application of formal-docs-sync, Product/API modules, or exclusion of database/design/ops contracts. |
| `prefers_catalog_scope` | FAIL | The output proposes the Accounts route and owner but does not show catalog-driven selection, path existence checks, or Billing explicitly marked out-of-batch. |
| `presents_batch_before_write` | FAIL | No pre-write complete API parent/child tree, per-node evidence, delta, exclusions, or confirmation wait is recorded. |
| `keeps_unconfirmed_batch_read_only` | PASS | With-skill git status/diff shows no Accounts or API-root changes and preserves existing Billing entries; only confirmed Product pages and Product mappings changed. |
| `aligns_seed_with_page` | FAIL | No Accounts seed was written or fully proposed with the required three-page closure and preserved Billing metadata. |
| `handles_missing_catalog_semantically` | NOT_EXERCISED | The fixture contains a confirmed feature catalog, so the no-catalog branch is not applicable. |
| `creates_complete_product_tree` | PASS | The with-skill delivery snapshot contains the Product root, both domains, invitations, both second-level indexes, and all four required task pages. |
| `keeps_every_task_navigable` | PASS | Snapshot links establish the required root-to-domain-to-feature-to-task paths, with direct-child navigation at each index. |
| `records_confirmed_non_leaf_scope` | FAIL | Most non-leaf pages state scope, owners, children, and exclusions, but the Product root lacks the required explicit audience, adjacent capability, and batch-exclusion semantics. |
| `writes_evidence_backed_task_behavior` | PASS | Task pages cite implementation functions and acceptance tests; fixture code/tests support the documented permissions, limits, feedback, recovery, and dashboard behavior. |
| `updates_product_map_atomically` | PASS | The Product change-map adds broad, nested, and exact Product globs with ancestor-closed required_docs while preserving existing Billing/support entries and fields. |
| `links_authorities_without_copying_contracts` | PASS | Every task page links its parent and Design/API/Database/Ops indexes without duplicating interface or database contracts. |
| `runs_product_host_checks` | FAIL | The output reports checks blocked and provides no records for the three required npm commands, visibility/link verification, or docs-audit handoff. |
| `blocks_audit_without_confirmed_version` | FAIL | No docs-agent:docs-audit handoff is recorded, and the required blocked status, affected set, evidence, exclusions, and missing target_release_version are absent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6e26676a89a16acec9866e91e19dd92a1b85a0401ad645a6160108df17d9b4b2; fixture_sha256=3a676f73bf7941f0ab035834abd0887251dca20d52501fbcda26212974e9b01d; output_sha256=88f96463db26037288c7fca61aeddaa631cd27002a3a65a6171a9de252b74934; snapshot_sha256=9b39bd9dc9a05df603834637c1c7ca11c8959cbb0269eefac3c9c81bb985d7f7
- Behavior: Correctly implemented the confirmed Product tree and evidence-backed task content while leaving Accounts unmodified, but omitted the required API candidate/confirmation workflow and audit/test handoff evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6e26676a89a16acec9866e91e19dd92a1b85a0401ad645a6160108df17d9b4b2; fixture_sha256=3a676f73bf7941f0ab035834abd0887251dca20d52501fbcda26212974e9b01d; output_sha256=74ab505d196f960bf3fc278207f68c6c665fe6c40f25c98a1c626b43b6382240; snapshot_sha256=1d9f111df4b33c71b4982603c16db2fa20203aec1b8d9f93ba0e9507ea9be527
- Behavior: Implemented the Product tree and basic mapping, but provided weaker scope/evidence and only partial validation; it also omitted the required API planning workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Required scoped skill-contract loading and API planning evidence is absent.
- Required complete pre-write Accounts tree and confirmation wait are absent.
- Product root scope semantics are incomplete.
- Required host-check command records and blocked docs-audit handoff are absent.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
