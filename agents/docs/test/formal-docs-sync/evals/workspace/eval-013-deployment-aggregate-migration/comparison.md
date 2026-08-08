# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Fixture SHA-256: `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `cb68cc7396b4ed1007a2bd5b5970baa015053110168fade98a969dbebc84c1b1`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `24118b2c28e807c2d8787e545057d4e67c26fd6313bf8abe3b22a58982fbfa17`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | PASS | Locked delivery snapshot deletes docs/site/ops/deployment.md and adds deployment/index.md, environment-reference.md, and development, docker, and kubernetes-helm page trees. |
| `repairs_inbound_and_internal_links` | PASS | Locked files update both inbound links to deployment/index.md; the new root links resolve to all class pages and environment-reference.md, and no residual old aggregate links remain in the checked files. |
| `updates_change_map_without_data_loss` | PASS | Locked change-map content maps each deployment glob to root, shared environment, and class pages while preserving custom_owner_field, exclude, and the unrelated src/product mapping. |
| `updates_navigation_atomically` | PASS | With-skill evidence records npm run test:docs exit 0, git diff --check exit 0, no formal old-path remnants, and a coordinated snapshot containing navigation, moved pages, links, change-map updates, and consolidated facts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=5077aba73143ee46ad58b2537d4287c8cc783ec52d5e442329da8c295c7d1e47; snapshot_sha256=b8fb2a9995e508f6e4d33f6242c40730a14a000f80bbbce82f83a0c1d13afc87
- Behavior: Completed the migration with the full page tree, repaired links, expanded change-map entries, preserved fields, and passing documentation tests.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=d89c40f4b13f317991a77ee7fe6cfb2a0eaf54eb5e2c4b159b4a5bba10b340dc; snapshot_sha256=f671f7d7dc033436c1d9f37a04972c40a4df0ccef01fe720f7f0b0d0399a9dee
- Behavior: Deleted and split the aggregate page and repaired basic links, but mapped each category only to its class page and omitted root/shared pages from required_docs.
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
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Fixture SHA-256: `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `cb68cc7396b4ed1007a2bd5b5970baa015053110168fade98a969dbebc84c1b1`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `24118b2c28e807c2d8787e545057d4e67c26fd6313bf8abe3b22a58982fbfa17`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | PASS | delivery_snapshot 删除旧聚合页并创建根索引、共享环境参考页及 Development、Docker、Kubernetes/Helm 三类子页；根索引和子页未复制旧聚合正文。 |
| `repairs_inbound_and_internal_links` | PASS | ops/index.md 和 product/runtime.md 均改为指向 deployment/index.md；根索引及三个子页中的相对链接均可解析。 |
| `updates_change_map_without_data_loss` | PASS | 三个部署 glob 的 required_docs 均稳定包含新根索引、environment-reference.md 和对应类别页，同时保留 exclude、custom_owner_field、trigger 及 src/product 无关映射。 |
| `updates_navigation_atomically` | NOT_EXERCISED | 页面移动、链接修复、change-map 更新和重复内容归并均有交付证据，且候选报告 npm run test:docs 退出码为 0、无旧聚合链接；但 Public/Internal 递归导航配置在 fixture 中不存在，完整导航更新无法独立验证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=6b7fce31b656709a5a9d8b72b1036b03b71d85daf10d0b886d6658aca9c33f6f; snapshot_sha256=015a26a30affc04044dbe339ae43729f518b837a57b1a887b0aa8c18cdc5bb08
- Behavior: 完成聚合页迁移、三类页面拆分、链接修复及 change-map 更新；测试报告通过。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=623880000472d1854502a87297f69df5c5b855e81b36f77d4978fea89e7187bf; snapshot_sha256=3db5bbe88d5c98715d4e86ceec1fc42f672f7925e8691f605c0a79b16fac5dc8
- Behavior: 完成基础迁移、入链修复和类别映射，但未将 required_docs 扩展为根索引、共享环境页及类别页的闭包。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充或提供 Public/Internal 递归导航配置及其验证结果。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Fixture SHA-256: `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `24118b2c28e807c2d8787e545057d4e67c26fd6313bf8abe3b22a58982fbfa17`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | FAIL | with_skill reports a blocked gate and explicitly states that no batch was completed and no files were written; its delivery_snapshot is empty. |
| `repairs_inbound_and_internal_links` | FAIL | with_skill made no workspace changes, so the required inbound-link repairs and resolvable nested links were not delivered. |
| `updates_change_map_without_data_loss` | FAIL | with_skill only proposes a change-map delta and states that nothing was written; the required updated mapping is absent from its delivery evidence. |
| `updates_navigation_atomically` | FAIL | with_skill did not perform the confirmed atomic migration and did not run the documentation test; it explicitly reports no completed batch and no written changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=d8168b4c8f998e7bead5ce909b532a28009ecf50d3157e523ac123c3213a9925; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identified the confirmed batch but incorrectly stopped at a claimed missing prerequisite and made no changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=18750111e3b15d81e9663dc7eb62f0e256958cda3a4d7a8717d9475afccc2c45; snapshot_sha256=8d44595a8215d44ee3cfd795c94f9e49ca71dd1510736f3611293e8632364a98
- Behavior: Delivered the migration files, links, and change-map updates; claimed docs tests passed.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane did not execute the requested confirmed migration despite the fixture providing the handoff, deployment evidence, and test script.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Fixture SHA-256: `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `2032fa363929f7a2591d02e3cb7c7d2c88a00667a0537649e0b9a34bb8bbffa9`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | PASS | with_skill 的交付快照删除旧聚合页，创建根索引、共享环境引用页及 Development、Docker、Kubernetes/Helm 页面；共享事实集中在 environment-reference.md，分类页未复制旧聚合正文。 |
| `repairs_inbound_and_internal_links` | PASS | with_skill 快照确认 ops/index.md 和 product/runtime.md 已指向 deployment/index.md，且三个分类页与共享环境页的相对链接已更新并可由文档测试验证。 |
| `updates_change_map_without_data_loss` | PASS | with_skill 将每个部署类别映射到根索引、共享环境页和对应分类页，并保留 custom_owner_field、exclude、trigger 及 src/product 无关映射。 |
| `updates_navigation_atomically` | NOT_EXERCISED | 快照和测试证明了已交付的页面、链接及 change-map 结果，且 npm run test:docs 通过、无旧聚合链接；但锁定原始证据无法证明递归导航覆盖或这些变更是否作为同一原子操作完成。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=1a47edb5ca542c49c863438bd77ed4ff37ec7aa0798587ffb3bccdc88ff5a567; snapshot_sha256=a9a2caf558de4a03ab67a61193432123e7f44eeb54d08cbdd1bd48fdf224d586
- Behavior: 完成页面树迁移、入链修复、共享环境引用、分类 change-map 拆分与字段保留；文档测试和 diff 检查通过，后续审计因缺少目标发布版本而暂停。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=c09aea29410bd7f808678dec00d3aeb7cfbbcfe254194377e66460faf127a8d5; snapshot_sha256=8f32f279cd699e6e1c1cb02f9557cde24963b40b01f4093ce2d1459797303fd8
- Behavior: 完成了主要迁移、入链修复和分类 change-map 更新，但未把共享环境页加入各类别映射，且验证信息较少。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如需完整覆盖 updates_navigation_atomically，应提供导航配置/递归链接检查结果及原子变更过程证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Fixture SHA-256: `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `2032fa363929f7a2591d02e3cb7c7d2c88a00667a0537649e0b9a34bb8bbffa9`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | FAIL | 旧聚合页已删除且页面树已创建，但根索引及三类页面仍重复写入共享事实 APP_PORT=8080，而要求共享环境事实仅保留在 environment-reference.md。 |
| `repairs_inbound_and_internal_links` | PASS | ops/index.md、product/runtime.md 和 change-map.yaml 已更新到新路径；快照中的嵌套 Markdown 链接均指向存在的目标。 |
| `updates_change_map_without_data_loss` | PASS | required_docs 已按 Development、Docker、Kubernetes/Helm 及共享环境页拆分，并保留 custom_owner_field、exclude 及 src/product 无关映射。 |
| `updates_navigation_atomically` | NOT_EXERCISED | 最终快照支持测试通过声明且未见旧 deployment.md 链接，但锁定证据无法证明更新过程是否作为同一原子操作执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=ec78e9b246a6c142931a5df3bce7bf910dfc45f05ea09d472bd2e242048a65c5; snapshot_sha256=e46971127895eb3c6549d8affc1e4ef091bedb10f136878ee3d5d608386c5350
- Behavior: 完成页面树、链接和详细 change-map 拆分，并保留字段与排除项；但重复了共享 APP_PORT 事实。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=85f3e458c3089e2e351e62fd8bb6f574e7ff42effd1a972a2baaa7ffcfaa7fc2; snapshot_sha256=52d0bdb60aba74afeb66406556d24725f63151bf91f196694dcaca067b4ce8af
- Behavior: 完成基本迁移、入链修复和 change-map 更新，但页面与映射拆分较少。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 的根索引及三类页面重复写入应仅保留在 environment-reference.md 的共享 APP_PORT=8080 事实。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Fixture SHA-256: `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `2032fa363929f7a2591d02e3cb7c7d2c88a00667a0537649e0b9a34bb8bbffa9`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | FAIL | With_skill deletes the old aggregate and creates the required page tree, but shared facts such as APP_PORT=8080 and /healthz are repeated in the root index and class pages instead of being kept only in environment-reference.md. |
| `repairs_inbound_and_internal_links` | PASS | The snapshots update ops/index.md and product/runtime.md to deployment/index.md; all three class pages use resolving ../environment-reference.md links, and change-map paths point to the new tree. |
| `updates_change_map_without_data_loss` | PASS | With_skill adds root, shared-reference, and class-specific required_docs entries in stable order while preserving triggers, custom_owner_field, the exclude entry, and the unrelated src/product mapping. |
| `updates_navigation_atomically` | FAIL | The required path/link/change-map changes are present and no old deployment.md link remains, but duplicate aggregate facts remain, violating the required consolidation; the locked evidence also provides no independent test-command result. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=1fed21a989d172f97ff55b3c132d36208df7302671d72f6669ceee5de58323d9; snapshot_sha256=4f545a18e71002f8aec74e3e9fe6f4d9946571505d73b99d8aad21f757ad5112
- Behavior: Performs the full page-tree migration, repairs links, adds shared and class-specific mappings, and preserves change-map fields, but repeats shared aggregate facts outside the environment reference and lacks independent test-result evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=cc0f8609b140a05ebbff2f4688b3fe5d06b9ec8d168e70e36ff3589a085554e2; snapshot_sha256=fbf88a2535c003f8a6563b522eb8bee5d37a65430360c7085522cf77d031e769
- Behavior: Fresh baseline performs the path migration and basic inbound-link repair, but maps each deployment code area only to its class page and omits the shared/root pages from required_docs.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Shared deployment facts are duplicated in the root and three class pages despite the requirement that shared facts remain only in environment-reference.md.
- Atomic completion cannot be fully established from the supplied raw evidence because the claimed npm run test:docs result is not independently recorded.
- Next: Remove repeated APP_PORT and /healthz aggregate facts from the root and class pages, leaving them in environment-reference.md and linking to it.
- Next: Provide raw output from npm run test:docs and the navigation validation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Fixture SHA-256: `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `2032fa363929f7a2591d02e3cb7c7d2c88a00667a0537649e0b9a34bb8bbffa9`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | FAIL | with_skill 删除旧聚合页并创建页面树，但根索引仍重复记录 APP_PORT=8080 和 /healthz，分类页也重复部分共享事实；共享事实未仅保留在 environment-reference.md。 |
| `repairs_inbound_and_internal_links` | PASS | with_skill 更新 ops/index.md 和 product/runtime.md 的旧入链；交付快照中的嵌套页面相对链接均可解析。 |
| `updates_change_map_without_data_loss` | PASS | with_skill 按 Development、Docker、Kubernetes/Helm 分别加入根页、共享环境页和分类页，保留 exclude、custom_owner_field 及 src/product 无关映射，列表顺序稳定。 |
| `updates_navigation_atomically` | PASS | with_skill 的同一工作树变更包含页面移动、导航与入链修复、change-map 更新和内容归并；输出报告文档测试 2/2 通过且 7 个页面链接有效，快照中无旧聚合页链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=0bed717e9609bdf67b568524c0529c820e4dcfbc897b036b0a99531d7030cf34; snapshot_sha256=839c7a11f1acd36b5b357d4b1a1e4f7b37f4ec73c595121a0ea2d31773ecc200
- Behavior: 完成页面树迁移、链接修复、共享页和按类别的 change-map 更新，并保留未知字段；但仍在根页和分类页重复共享环境事实。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=9bd526989fec9746f3e368ff20227c76145fd1a4978361264fd9c5a9cb169a99; snapshot_sha256=7b4f5f12d9d5992c76c1c9242df7dffaeb2139322f2cc8350b38dd985d6d1449
- Behavior: 完成基本迁移、入链修复和分类 change-map 更新，但未加入共享环境页，也未将每类映射扩展为根页、共享页和分类页。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- migrates_aggregate_path 未满足共享环境事实集中保留在 environment-reference.md 的要求。
- Next: 移除根索引及分类页中重复的共享 APP_PORT、/healthz 等事实，仅保留导航和模式专属内容。

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
- Eval: `eval-013-deployment-aggregate-migration`
- Review context: issue #161 fresh paired rerun and fresh Codex judge

## Test Set / Fixture Version

- Fixture: legacy aggregate deployment page, inbound links, three-class evidence summary and old change map
- Actual validation date: `2026-07-22`

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `migrates_aggregate_path` | FAIL | FAIL | with_skill 仍存在 `docs/site/ops/deployment.md`；without_skill 虽创建页面树，但根索引及分类页仍重复 `APP_PORT`、健康检查等旧聚合正文（如 `deployment/index.md:21-25`、`docker/index.md:12-17`）。 |
| `repairs_inbound_and_internal_links` | FAIL | PASS | with_skill 的 `ops/index.md`、`product/runtime.md` 仍链接 `deployment.md`；without_skill 的站内链接均指向新页面且相对目标存在。 |
| `updates_change_map_without_data_loss` | FAIL | FAIL | with_skill 的三个 `required_docs` 仍指向旧聚合页；without_skill 保留了未知字段和 exclude，但未将共享 `environment.md` 纳入各类别映射。 |
| `updates_navigation_atomically` | FAIL | FAIL | with_skill 保留旧链接且 `npm run test:docs` 失败；without_skill 链接已更新，但同一测试命令仍因缺少 `scripts/deployment-migration.test.mjs` 失败。 |

未满足断言（with/without 任一 FAIL）：``migrates_aggregate_path``、``repairs_inbound_and_internal_links``、``updates_change_map_without_data_loss``、``updates_navigation_atomically``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Moved shared `APP_PORT` facts to the environment authority, repaired Ops/Product inbound links, split maps by class and preserved `exclude`, unknown fields and unrelated entries.
- Limited the migration to evidence retained by the fixture; it did not invent image, Chart, values or exact command child pages from a summary.
- Kept changed pages `unverified` and returned the `docs-agent:docs-audit` handoff blocked on a confirmed target version.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: fresh lane from the same pristine fixture and prompt without the target skill, Agent README, comparisons or with-skill output.
- It also passed 2/2 structural migration tests, but used broader unsupported phrases such as a current Chart, approved workflow and previous Helm revision; with-skill maintained the stricter evidence boundary.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures.
- Runtime provenance used lane transcripts and reports; a separate immutable input manifest was not retained.

## Next Steps

- 修复四条 with-skill 失败（确认范围、迁移闭包、历史页面处理与写后证据）后，使用同一 prompt/fixture 重新执行 paired eval；重跑前保持 `FAIL`。

## Runtime Artifact Policy

- Paired lanes, transcripts, reports, generated pages and judge verdict remain under `tmp/eval-runs/issue-161-rerun/` and are not submitted.
- Only this comparison is durable.
