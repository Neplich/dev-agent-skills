# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `969fba1034afbbb0a1b1ea8386f5681318bff1a8e08153fcbc8b9cc14cb9dbd3` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-009-release-product-ops`.
- Fixture SHA-256: `969fba1034afbbb0a1b1ea8386f5681318bff1a8e08153fcbc8b9cc14cb9dbd3`
- Prompt SHA-256: `8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c9bcafbf3ecc8c0e0ac28908b463b075e9d1371a95444953a8afc3d41757e192`
- Metadata SHA-256: `8deaf3ef06984a55739a36e203fd82989e4163ee4a9c31b6706c821440154ae8`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `limits_release_to_affected_product_ops` | FAIL | with_skill 的 git_status 含未跟踪的 docs/site/docs-test-gEpwSf/，超出两页及其映射的受影响集合。 |
| `reconciles_confirmed_version_facts` | PASS | with_skill 两页均记录 25 和 v1.5.0；内容未延续 10/v1.4.0，也未写入 v1.5.1。fixture/release-evidence.md 与 release-test-results.md 支持这些事实。 |
| `preserves_release_notes_surfaces` | PASS | with_skill 的 git_diff 仅涉及 product/dashboard-limits.md 和 ops/dashboard-runtime.md；未修改 Release Notes 正文、索引、元数据或导航。 |
| `keeps_release_pages_unverified` | PASS | with_skill 两页均设置 last_verified_version: unverified，并明确等待 docs audit。 |
| `runs_release_host_checks_and_handoffs` | FAIL | with_skill 仅报告 check:frontmatter、check:version 和单元测试；明确未能执行严格 affected 检查，未报告 docs/site/ 下 npm run test:docs 的通过、cwd/退出状态，也未提供 docs-agent:docs-audit 的 pre-tag handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=969fba1034afbbb0a1b1ea8386f5681318bff1a8e08153fcbc8b9cc14cb9dbd3; output_sha256=69385d6e5ec0bb569b27efb748c4079662759edfd53a332d9d3c159983b58ebb; snapshot_sha256=8b94b52ca575ee064ec84e3a75e32ebcd24001fa1e21befa2cc5d30875b3b67e
- Behavior: 正确保留 unverified 状态并同步确认的版本事实，但产生额外未跟踪目录，且未完成 npm run test:docs 和 docs-audit pre-tag handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=969fba1034afbbb0a1b1ea8386f5681318bff1a8e08153fcbc8b9cc14cb9dbd3; output_sha256=baddc0cdcc6aff45f2377160968be857c8a6d30b71e197696b82a156d1ae4fe2; snapshot_sha256=b5b9730e6e8ec886ecd894c48754cfd3e90d2cd8a7ed17f6f6d2773ce04a72d0
- Behavior: 更新了两页并核对版本事实，但错误将两页盖章为 v1.5.0，且未完成所需宿主检查与 handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 超出受影响文件集合。
- with_skill 未执行并记录 npm run test:docs，也未完成 docs-agent:docs-audit handoff。
- Next: 移除 docs/site/docs-test-gEpwSf/ 等额外产物。
- Next: 在 docs/site/ 执行并记录 npm run test:docs 的命令、cwd 和退出状态，然后将完整 affected set 与 v1.5.0 确认来源 handoff 给 docs-agent:docs-audit。

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
- Eval: `eval-009-release-product-ops`
- Review context: issue #150

## Test Set / Fixture Version

- Fixture version: `issue-150 fresh-paired group-b v1`
- Actual validation date: `2026-07-21`
- Fresh run: `tmp/eval-runs/issue-150/group-b/eval-009-release-product-ops/`
- Both lanes started from independent copies of the same pristine fixture.

## Latest Result

- Behavior result: `PASS`（with）/ `PASS`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— 依赖缺失导致宿主检查与 handoff 未执行
- Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `limits_release_to_affected_product_ops` | PASS | PASS | 两条 lane 均仅更新 `docs/site/product/dashboard-limits.md` 与 `docs/site/ops/dashboard-runtime.md`；`change-map.yaml` 仅将对应代码映射到这两页，API/database/design 未改动。 |
| `reconciles_confirmed_version_facts` | PASS | PASS | 两页分别写入上限 `25`、镜像 `registry.example/ai-hub:v1.5.0` 和 `DASHBOARD_LIMIT=25`；未写入 `v1.5.1` 计划，且与 `release-evidence.md`、代码、配置、测试记录一致。 |
| `preserves_release_notes_surfaces` | PASS | PASS | `docs/site/release-notes/index.md`、`.meta/releases.json`、导航配置及现有 Release Notes 内容保持原状；两条 lane 均未创建 Release Notes 产物，并保留了应指向独立 Release Notes 流程的边界。 |
| `keeps_release_pages_unverified` | PASS | PASS | 两页 frontmatter 均为 `last_verified_version: unverified`，没有写入 `v1.5.0` 审计盖章。 |
| `runs_release_host_checks_and_handoffs` | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 的 `npm run test:docs` 都因依赖缺失未完成，后置 pre-tag handoff 因而未执行；这是 runner 依赖阻塞，不是 skill 行为失败。 |

未触发断言：`runs_release_host_checks_and_handoffs`。

基础设施阻塞说明：依赖缺失（fast-glob 等）；对应断言不构成 skill 行为回归。



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `limits_release_to_affected_product_ops`: PASS。只修改 `product/dashboard-limits.md` 与 `ops/dashboard-runtime.md`；对应两个既有映射已准确，无 API、database、design 或无关页面扩张。
- `reconciles_confirmed_version_facts`: PASS。代码、配置和 release tests 共同证明上限 25、镜像 `registry.example/ai-hub:v1.5.0`，并排除 10、v1.4.0 与未确认 v1.5.1。
- `preserves_release_notes_surfaces`: PASS。Release Notes 正文、index、metadata、navigation 与 pristine fixture 字节一致，并明确指向 `docs-agent:release-notes-gen` #116。
- `keeps_release_pages_unverified`: PASS。两页均回读为 `last_verified_version: unverified`。
- `runs_release_host_checks_and_handoffs`: PASS。在 `docs/site` 执行 `RELEASE_VERSION=v1.4.0 npm run test:docs`，退出 0、74/74 tests；handoff 包含完整 affected set、`target_release_version: v1.5.0` 与 `release-handoff.md` 维护者确认来源。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 读取公共八步 contract 及 product/ops 两个类型模块；未加载无关类型模块。
- 先使用 lockfile 执行 `npm ci --ignore-scripts`，再运行宿主检查；版本参数只用于校验当前未改动 release metadata，不用 Git ref 推测目标版本。
- 不操作 Release Notes、tag、GitHub Release 或部署。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 来源：同一 prompt/assertions 与独立 pristine fixture 的本轮 fresh `without_skill`；在生成期间未读取目标 SKILL、Docs README、internal/shared 指令、旧 comparison 或历史输出。
- baseline 也只更新两页、保留准确映射和 Release Notes 零变化，页面保持 `unverified`，并真实通过相同 74 tests；其结构化响应包含 #117 affected set、维护者确认来源与 #116 边界。
- 结果：5/5 PASS；未复用历史 baseline。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With-skill assertion failures: none。
- Without-skill assertion failures: none。
- Comparative limitation: prompt/assertions 与 fixture 已充分显式给出范围、版本事实和 handoff 字段，fresh baseline 也能完整执行。

## Next Steps

- 保持 release mode 的 product/ops 窄范围、Release Notes 零写入、`unverified` 和明确版本确认来源作为回归门禁。
- 如需衡量 uplift，另增缺失或冲突 release evidence 的阻塞型 eval。

## Runtime Artifact Policy

- 两 lane workspace、依赖、页面副本、响应与测试日志仅位于 `tmp/eval-runs/issue-150/group-b/eval-009-release-product-ops/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。

## 磨平记录（2026-07-29）

维护者裁定本 eval 的零区分度属于模型能力进步磨平（(b) 类），批次 4 的重写已回滚。该 eval 作为 [issue #188](https://github.com/neplich/dev-agent-skills/issues/188) 的 skill 能力审查标本保留原样；在 #188 得出审查结论前不重做本 eval。
