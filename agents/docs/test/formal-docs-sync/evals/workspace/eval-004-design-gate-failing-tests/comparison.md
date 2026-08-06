# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-004-design-gate-failing-tests`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `blocks_on_failing_tests` | PASS | PASS | 两条 lane 的 `.eval/test-results.md` 均明确记录 `test_compact_summary_handles_empty_values` 为 `FAILED`；报告均说明测试门禁失败、停止同步。 |
| `design_zero_change` | PASS | PASS | 两条 lane 的 `.eval/actual-diff.patch` 仅包含 `src/preferences_summary.py`；`preferences-summary.md` 与 `change-map.yaml` 均保持原内容，未产生设计文档变更。 |
| `names_missing_evidence` | PASS | FAIL | with_skill 指名失败测试，指出 `src/preferences_summary.py` 由工程负责修复，并要求必需测试通过后再同步；without_skill 未指名当前 owner，也未明确重新执行全部计划测试并重新进入 design 收口门禁。 |

未满足断言：``names_missing_evidence``


**PASS** — with-skill 3/3 assertions 通过；without-skill baseline 2/3。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 只加载 design 模块，核对并复现 required test failure。
- design 页面与 change-map 保持零变化，明确由 Engineer / test owner 修复并重跑后解锁。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 停止写入，但缺少明确 owner 与完整解锁路径。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- design 测试门禁或 fixture 变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
