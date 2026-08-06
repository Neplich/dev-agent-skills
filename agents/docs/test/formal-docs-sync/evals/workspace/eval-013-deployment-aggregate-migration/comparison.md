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
