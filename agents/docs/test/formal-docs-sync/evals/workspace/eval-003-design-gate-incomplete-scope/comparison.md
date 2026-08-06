# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-003-design-gate-incomplete-scope`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

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
| `blocks_on_incomplete_scope` | PASS | FAIL | with_skill 明确指出 `SCOPE-02` 为 TODO、属于本次交付，Owner 为 Engineer，并要求完成代码与对应测试后重新提供 closeout 证据；without_skill 虽识别 TODO 和交付未关闭，但未明确给出 owner、完成代码与验证后重新提交 closeout 的阻断要求。 |
| `design_zero_change` | PASS | PASS | 两条 lane 的 `.eval/actual-diff.patch` 均仅包含 `src/preferences_summary.py`；设计页与 change-map 的 SHA-1 均分别为 `dfcee25...` 与 `bed32d5...`，保持一致。with_skill 报告也明确为“Changed docs: 无”。 |
| `no_tentative_design` | PASS | PASS | 两条 lane 均未修改设计正文；实际 diff 没有 `docs/site/design/preferences-summary.md` 或设计性新增内容，也未将紧凑摘要描述为当前状态。 |

未满足断言（with/without 任一 FAIL）：``blocks_on_incomplete_scope``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 只加载 design 模块，识别实施计划仍有未完成范围。
- design 页面与 change-map 均零变化，并将解锁动作交回 Engineer / feature-implementor owner。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 同样停止写入，但未明确指名 Engineer / feature-implementor owner。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- design closeout gate 变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
