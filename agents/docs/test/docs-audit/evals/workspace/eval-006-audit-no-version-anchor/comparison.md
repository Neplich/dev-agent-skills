# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Test Set / Fixture Version

- Fixture version: docs-audit A2 / 2026-07-19
- Assertions: 4

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `blocks_without_target_release_version` | PASS | FAIL | with_skill 的 `result.txt` 明确为“审计结果：blocked”，并指出缺少维护者确认的 `target_release_version`；without_skill 返回“结论：未发现需要更新文档的变更”，未将阶段结果标记为 `blocked`。 |
| `allows_read_only_diagnostic` | PASS | PASS | with_skill 未执行写入或成功审计，仅报告缺少 Git 元数据；without_skill 仅依据 `.eval/actual-diff.patch`、`change-map.yaml` 和代码文件做影响诊断，未声称 `ready_for_tag` 或 `release_verified`。 |
| `does_not_persist_report_without_target` | PASS | PASS | 两个工作区均不存在 `docs/site/.meta` 目录，也不存在 `audit-7c9e2af.md` 或其他版本化审计报告。 |
| `does_not_write_version_stamp` | PASS | PASS | 两个工作区的 `docs/site/api/catalog.md` 均保持 `last_verified_version: unverified`；均不存在 `.meta/releases.json`，也未写入版本号。 |

未满足断言（with/without 任一 FAIL）：``blocks_without_target_release_version``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | 明确因目标版本缺失且未确认而 `blocked`，未返回任一成功阶段状态。 |
| `allows_read_only_diagnostic` | PASS | 仍用已确认 base/target 描述 affected page，并确认纯重构下页面事实 `verified`，但不包装为成功审计。 |
| `does_not_persist_report_without_target` | PASS | workspace 零写入；不存在 `audit-7c9e2af.md` 或其他版本化报告，没有 SHA 回退命名。 |
| `does_not_write_version_stamp` | PASS | 页面保持 `last_verified_version: unverified`，未创建或修改 `.meta/releases.json`，未推测版本。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a75-30f2-72d0-bea2-6fd9fe5ff45d`，位于 `tmp/eval-runs/117/eval-006-audit-no-version-anchor/with_skill/`。
- 候选正确应用入口 gate 与只读诊断例外，完全修正旧模型的 SHA 报告回退语义。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a78-ed4d-77e1-a925-8cac1dcb9995`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 也保持零写入且拒绝推测版本，但没有 docs-audit 的入口、报告持久化禁止与阶段状态结构。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch` 仅作只读诊断，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；无目标版本 gate 或报告持久化规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
