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

- Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `limits_release_to_affected_product_ops` | PASS | PASS | 两条 lane 均仅更新 `docs/site/product/dashboard-limits.md` 与 `docs/site/ops/dashboard-runtime.md`；`change-map.yaml` 仅将对应代码映射到这两页，API/database/design 未改动。 |
| `reconciles_confirmed_version_facts` | PASS | PASS | 两页分别写入上限 `25`、镜像 `registry.example/ai-hub:v1.5.0` 和 `DASHBOARD_LIMIT=25`；未写入 `v1.5.1` 计划，且与 `release-evidence.md`、代码、配置、测试记录一致。 |
| `preserves_release_notes_surfaces` | PASS | PASS | `docs/site/release-notes/index.md`、`.meta/releases.json`、导航配置及现有 Release Notes 内容保持原状；两条 lane 均未创建 Release Notes 产物，并保留了应指向独立 Release Notes 流程的边界。 |
| `keeps_release_pages_unverified` | PASS | PASS | 两页 frontmatter 均为 `last_verified_version: unverified`，没有写入 `v1.5.0` 审计盖章。 |
| `runs_release_host_checks_and_handoffs` | FAIL | FAIL | 两条 lane 都报告 `npm run test:docs` 因依赖缺失未完成；没有真实成功的命令/cwd/退出状态记录，也没有包含两页 affected set、确认版本来源并交给 `docs-agent:docs-audit` 的 pre-tag handoff 产物。 |

未满足断言（with/without 任一 FAIL）：``runs_release_host_checks_and_handoffs``

基础设施阻塞说明：；依赖缺失（fast-glob 等）；对应断言不构成 skill 行为回归。



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
