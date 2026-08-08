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
