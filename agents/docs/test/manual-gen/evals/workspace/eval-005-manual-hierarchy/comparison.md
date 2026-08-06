# Skill Eval Comparison

## Evaluation Target

- Skill: `manual-gen`
- Eval: `eval-005-manual-hierarchy`
- Target behavior: 手册目录呈现平台定位、业务场景、可执行操作三个语义层次且操作可复现

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
- Blocking reason: 平台缺场景（明确处置，非 skill 行为原因）。按 #235 契约被测平台由执行前维护者确认注入；本轮维护者确认平台为 llm-wiki（wiki.jototech.cn），实测该平台缺少本 eval 场景（无导出分享功能 / 无图表创作功能），正向写入路径不可执行。按 #245（eval 测试设计收敛：单一通用测试替代按场景拆分）实施后重跑。
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），且被测平台已改为执行前维护者确认注入（#235），本结论基于旧契约，待重跑验证。


## With-Skill Behavior

- 入口门禁通过，完成 Step 1–4，候选页面树按平台层 / 业务层 / 操作层三级组织。
- 停在 Step 4 确认门禁，零写入。

## Without-Skill Baseline

- 来源：同一 prompt、同一 fixture 的独立冷启动会话，未加载 manual-gen 文档。
- 写入 4 个页面 + 3 张截图，页面树同样呈现三层结构。
- **该维度零区分度**：三层组织规则写在宿主 `standards/index.md` 与 `manual-guide.md` 模板中，
  baseline 自行读取后照做。成因属「规则天然存在于 skill 交付物」，不是缺陷——
  manual-gen 的设计原则即「模板是唯一模板源，skill 不维护第二份模板正文」。

## Failures / Gaps

- 无 skill 行为回归。
- 结构类断言在本测试集上不具判别力，观测重心应移到门禁与纪律类断言。
- 未触发：`makes_operation_layer_reproducible`、`keeps_hierarchy_navigable_and_evidence_backed`
  的写入后验证部分。

## Next Steps

- issue #235：本测试集为外部站点，宿主内不存在其前端源码，FR-M12 的 `related_code`
  「非空且可定位」无法满足，正向写入路径在该测试集上走不完。
- 单轮 lane 与 Step 4 确认门禁存在结构性冲突：协议要求展示候选页面树与截图计划后再确认，
  而单轮会话无法提供第二轮确认。要覆盖 Step 5–8 需多轮 lane 或改用宿主内应用作测试集。
- issue #234：全仓 eval 的 prompt / fixture 泄漏普查与批量整改。

## Runtime Artifact Policy

运行期产物（截图、生成页面、lane 报告、transcript）写入隔离 scratch workspace，不入库。
本文件是唯一持久化结果。
