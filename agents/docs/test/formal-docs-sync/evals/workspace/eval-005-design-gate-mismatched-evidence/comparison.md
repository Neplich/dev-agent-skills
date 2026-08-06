# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

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
| `blocks_on_evidence_mismatch` | PASS | PASS | 两条 lane 均明确对比 handoff/计划的 `preferences-summary` 与 PRD/TRD 的 `account-preferences`，并停止同步；证据见各自 `result.txt` 与 `PRD.md`/`TRD.md`。 |
| `design_zero_change` | PASS | PASS | 两个目标文件内容均保持原样；`.eval/actual-diff.patch` 仅包含 `src/preferences_summary.py` 新增，不包含 design 文档或 change-map 修改。 |
| `routes_to_owner` | FAIL | FAIL | with_skill 仅路由给 `pm-agent`，未明确路由 Engineer / `trd-gen`；without_skill 仅要求统一 PRD/TRD，未指定 PM owner 与 Engineer / `trd-gen` 双 owner 路由。 |

未满足断言：``routes_to_owner``


**PASS** — with-skill 3/3 assertions 通过；without-skill baseline 3/3。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 只加载 design 模块，识别 PRD/TRD/实际路径证据不一致。
- design 页面与映射零变化，并分别指出 PM 与 Engineer/trd-gen 的修复责任。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 全新 baseline 在本 fixture 上也满足 3/3，说明该阻塞信号本身足够明显。
- with-skill 的价值主要体现在稳定的 owner 和双面门禁表达。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- 保留作为明显冲突的安全网回归用例。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
