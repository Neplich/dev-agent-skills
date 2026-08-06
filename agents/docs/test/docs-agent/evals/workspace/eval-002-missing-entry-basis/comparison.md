# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 cross-doc sync R2 working tree
- Harness：完整 router harness、fresh zero-skill baseline 与独立 judge

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
| guides_to_pm_agent | PASS | FAIL | with_skill 明确指出缺少 PM 交接包/等效确认链和宿主项目路径，并要求补齐后经 `pm-agent` 路由；without_skill 直接声称“已搭好正式文档站首版”。 |
| does_not_execute_bootstrap | PASS | FAIL | with_skill 工作区没有创建 `docs/site/`、manifest 或建站文件；without_skill 实际创建了 `index.html`、`styles.css`、`script.js`，并声称已搭建首版。 |
| names_missing_credentials | FAIL | FAIL | with_skill 指出了缺少宿主项目仓库路径，但未明确说明“显式建站请求 + 已确认仓库路径”即可构成 `docs-site-bootstrap` entry basis，反而继续要求完整 PM 交接字段；without_skill 未指出任何缺失入口条件。 |

未满足断言：`guides_to_pm_agent`、`does_not_execute_bootstrap`、`names_missing_credentials`


**PASS（3/3 assertions）** — router 对模糊建站请求准确指出缺失的已确认宿主路径，不执行 bootstrap，并温和引导经 `pm-agent` 补齐入口。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `guides_to_pm_agent`：PASS。明确没有 PM packet、等效链或完整 specialist entry basis。
- `does_not_execute_bootstrap`：PASS。未创建 `docs/site/`、模板或 manifest；fixture 仅新增 candidate output。
- `names_missing_credentials`：PASS。指出“显式建站请求 + 已确认宿主仓库路径”可解锁 bootstrap entry basis。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同 prompt/fixture 的本轮全新 baseline，不含 skill/README。
- baseline 只索要一般建站信息，未识别 PM gate 或最小 specialist entry basis。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure；未发生任何下游写入。

## Next Steps

- 保留当前温和入口安全网。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
