# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-004-share-link-identifier`
- Target behavior: 覆盖导出与分享流程，且分享链接中的环境相关长串标识不原样进入正文

## Test Set / Fixture Version

- Fixture version: `manual-gen-v0.1.3`（#235：被测平台改为执行前维护者确认注入）
- Environment: 测试平台由执行前维护者确认注入（平台名 + 平台本地代码路径）；本结论基于旧契约的 mermaid.live 占位
- Lane isolation: 两条 lane 的 prompt 逐字相同、可见 fixture 完全相同，唯一变量是是否加载
  `manual-gen/SKILL.md` 与 `_internal/INSTRUCTIONS.md`。prompt 为自然用户目标，
  不含协议步骤、分层结构、字段清单或工具参数。`eval_metadata.json`、`pm-handoff.md`
  与采集脚本均已移出 lane 可见目录（见 `AGENTS.md` → Eval prompt 与 lane 隔离契约）。
- Executed: `2026-08-05`，两条 lane 各自独立 `codex exec` 冷启动会话

## Latest Result

- Behavior result: `PASS` — with_skill 在本轮实际触发的路径上满足对应 assertions，无回归。
- Coverage result: `PARTIAL` — 见下方未触发断言

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），且被测平台已改为执行前维护者确认注入（#235），本结论基于旧契约，待重跑验证。


## With-Skill Behavior

- 入口门禁通过，直接使用请求提供的域名，未重复提问。
- 完成 Step 1–4 并产出覆盖导出与分享的候选批次，停在 Step 4 确认门禁，零写入。
- 截图卫生按收窄后的规则处理：属于导出/分享操作步骤本身的菜单与对话框计划保留为产品证据，
  仅排除与任务无关的浮层。

## Without-Skill Baseline

- 来源：同一 prompt、同一 fixture 的独立冷启动会话，未加载 manual-gen 文档。
- 直接写入 4 个页面 + 3 张截图，未请求确认。
- 正文未出现原样 pako 编码串——但该结果来自 baseline 未深入分享链接细节，
  并非其主动执行了脱敏判断。

## Failures / Gaps

- 无 skill 行为回归。
- 未触发：`redacts_share_link_identifier` 的正向验证需实际写入正文后才能判定；
  `preserves_capture_and_audit_contract` 依赖 Step 5–8。

## Next Steps

- issue #235：本测试集为外部站点，宿主内不存在其前端源码，FR-M12 的 `related_code`
  「非空且可定位」无法满足，正向写入路径在该测试集上走不完。
- 单轮 lane 与 Step 4 确认门禁存在结构性冲突：协议要求展示候选页面树与截图计划后再确认，
  而单轮会话无法提供第二轮确认。要覆盖 Step 5–8 需多轮 lane 或改用宿主内应用作测试集。
- issue #234：全仓 eval 的 prompt / fixture 泄漏普查与批量整改。

## Runtime Artifact Policy

运行期产物（截图、生成页面、lane 报告、transcript）写入隔离 scratch workspace，不入库。
本文件是唯一持久化结果。
