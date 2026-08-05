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

- Behavior result: `PASS` — with_skill 在本轮实际触发的路径上满足对应 assertions，无回归。
- Coverage result: `FULL` — 本 eval 的全部 assertion 场景均已触发。

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## With-Skill Behavior

- 正确判定为 blocked，零启动命令、零截图、零站点写入。
- 报告列出缺失的运行环境与界面证据、owner 与可解锁下一步，未从产品需求文字推断界面细节。

## Without-Skill Baseline

- 来源：同一 prompt、同一 fixture 的独立冷启动会话，未加载 manual-gen 文档。
- 同样判定为 blocked，同样零写入、未虚构界面。
- **零区分度**。成因属「模型基线能力已覆盖该行为」——无证据时不编造内容属通用行为。
  记为 skill 生命周期信号。

## Failures / Gaps

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
