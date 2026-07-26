# Eval Result: eval-001-interactive-battlecard

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-intelligence`
- Eval: `eval-001-interactive-battlecard`
- Test case: interactive-battlecard
- Workspace: `workspace/eval-001-interactive-battlecard`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 3/3 assertions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed seller context and an official-source competitive pack for Notion, Superhuman Docs, and Airtable
- Expected output: 面向销售的 battlecard 输出，包含竞品卡片、功能/定价/定位对比、近期变化、反驳话术和证据来源说明。

## Assertions

- PASS `battlecard`: with_skill 提供跨竞品矩阵和逐竞品卡片。
- PASS `sales_context`: with_skill 包含 objections、talk tracks、landmine questions 和定位建议。
- PASS `freshness`: with_skill 标注 2026-04-27 至 2026-07-26 的 90 天窗口，并提示实时核验易变事实。

## With Skill

- 生成自包含的交互式 HTML，提供 tabs、逐卡官方链接和 fact/inference 标签。
- 2026-07-26 fresh validator 核验官方定价、更新和品牌迁移资料；没有把 Airtable 窗口内未确认的发布事件虚构为产品发布。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 competitive-intelligence skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 3/3 assertions，包含矩阵、竞品段落、objections 和 freshness；相较 with_skill，交互性、销售落地性和证据标注较弱。

## Failures

- 无 assertion failure。
- 竞品事实具有时效性，后续实际使用仍需按输出提示实时复核。

## Next Steps

- 保留 seller context、官方来源、近 90 天窗口和 fact/inference 边界。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, generated HTML, outputs, and diagnostics were kept only in an ignored scratch workspace and are not committed.
