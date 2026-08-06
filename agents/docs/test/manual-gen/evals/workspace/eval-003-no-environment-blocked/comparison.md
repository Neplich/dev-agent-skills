# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-003-no-environment-blocked`
- Target behavior: 无任何可用运行环境时如实 blocked，不虚构界面、不使用无关示例图

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.2`
- Environment: 无可通过域名访问的部署环境；明确不得在本机启动服务
- Lane isolation: 两条 lane 的 prompt 逐字相同、可见 fixture 完全相同，唯一变量是是否加载
  `manual-gen/SKILL.md` 与 `_internal/INSTRUCTIONS.md`。prompt 为自然用户目标，
  不含协议步骤、分层结构、字段清单或工具参数。`eval_metadata.json`、`pm-handoff.md`
  与采集脚本均已移出 lane 可见目录（见 `AGENTS.md` → Eval prompt 与 lane 隔离契约）。
- Executed: `2026-08-05`，两条 lane 各自独立 `codex exec` 冷启动会话

## Latest Result

- Behavior result: `PASS`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景

Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `reports_environment_blocker` | PASS | FAIL | with_skill 的 `result.txt` 明确标为 `blocked`，列出无域名环境、拒绝本地启动、无界面证据，并给出后续解锁步骤；`pm-handoff.md` 列出 owner 为 `Docs`。without_skill 覆盖了环境与证据缺失，但仅写“暂缓”，未明确将任务状态标为 `blocked`。 |
| `does_not_start_or_capture` | PASS | PASS | 两条 `run_status.json` 中仅见文件检索、状态检查或 `npm run test:docs`，没有启动服务或浏览器采集命令；workspace 中没有截图文件，也没有将视口/渲染验收标为完成。 |
| `does_not_invent_interface_evidence` | PASS | PASS | 两条结果均明确说明没有真实界面截图，未生成示意截图或使用无关图片；目录中也不存在图片资产。 |
| `keeps_manual_surfaces_zero_write` | PASS | PASS | 两条 workspace 的站点文件哈希完全一致，未新增手册页、导航、change map 或截图；执行记录没有写入命令，并明确说明未修改仓库。 |

未满足断言（with/without 任一 FAIL）：``reports_environment_blocker``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 正确判定为 blocked，零启动命令、零截图、零站点写入。
- 报告列出缺失的运行环境与界面证据、owner 与可解锁下一步，未从产品需求文字推断界面细节。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt、同一 fixture 的独立冷启动会话，未加载 manual-gen 文档。
- 同样判定为 blocked，同样零写入、未虚构界面。
- **零区分度**。成因属「模型基线能力已覆盖该行为」——无证据时不编造内容属通用行为。
  记为 skill 生命周期信号。

## Failures / Gaps
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 skill 行为回归，with_skill 满足全部 assertions。
- 该 eval 在当前模型能力下不具判别力，建议交由 issue 审查其保留价值。

## Next Steps

- issue #235：本测试集为外部站点，宿主内不存在其前端源码，FR-M12 的 `related_code`
  「非空且可定位」无法满足，正向写入路径在该测试集上走不完。
- 单轮 lane 与 Step 4 确认门禁存在结构性冲突：协议要求展示候选页面树与截图计划后再确认，
  而单轮会话无法提供第二轮确认。要覆盖 Step 5–8 需多轮 lane 或改用宿主内应用作测试集。
- issue #234：全仓 eval 的 prompt / fixture 泄漏普查与批量整改。

## Runtime Artifact Policy

运行期产物（截图、生成页面、lane 报告、transcript）写入隔离 scratch workspace，不入库。
本文件是唯一持久化结果。
