# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-006-design-gate-all-passed`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `PASS` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| passes_completion_gates | PASS | PASS | 两条 lane 的 `PRD.md` 为 Approved、`TRD.md` 为 Confirmed、实施计划为 Confirmed；SCOPE-01/02 均 Complete；`actual-diff.patch` 覆盖 `src/preferences_summary.py`；`test-results.md` 中三项计划测试均 PASSED。 |
| stops_at_scope_confirmation | PASS | PASS | 两条 lane 均展示候选页面 `docs/site/design/preferences-summary.md`、代码路径 `src/preferences_summary.py`、证据、排除项和阻断项，并明确等待维护者确认；`actual-diff.patch` 未包含页面或 change-map 修改。 |
| current_state_only | PASS | PASS | 两条 lane 的源码与测试共同证明固定顺序 `language → timezone → theme`、省略空值、compact 复用相同非空值；候选描述未添加无证据的未来行为或实施结果。 |

本轮无 FAIL 断言。



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 七项 design closeout 证据全部通过后仍停在候选范围确认，不提前写入。
- 候选内容仅使用最终代码与通过测试支持的当前事实，并保持后续 `unverified` 纪律。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 全新 baseline 在该明确 fixture 上同样满足 3/3。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- closeout 条件或候选确认协议变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
