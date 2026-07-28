# Consumption Regression Comparison

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-008-mapped-notification-update`
- Workspace: `workspace/eval-008-mapped-notification-update`

## Test Set / Fixture Version

- Evaluation date: `2026-07-28`
- Schema: `evals.json` v1.0
- Fixture: mapped notification source, `change-map.yaml`, an `unverified` notification API page, and `channels.txt` with email as the only enabled channel.
- Run: fresh Codex evaluator with a separately isolated, newly generated `without_skill` baseline.

## Latest Result

**PASS** — all 3 assertions passed. With-skill precisely followed the change map, verified the current channel from code, reported the webhook documentation drift, and treated `unverified` documentation as lowest trust.

## With-Skill Behavior

- 从 `src/notifications/` 反查 `change-map.yaml`，只读取命中的 `docs/site/api/notifications.md`。
- 以 `src/notifications/channels.txt` 的 email-only 事实作为 ground truth，没有用文档覆盖代码。
- 结构化说明 webhook 分歧、SMS delta 与影响范围，不虚构供应商、接口或数据模型。
- 正确停在一个产品范围决策点。

## Without-Skill Baseline

- 来源：本次 fresh 严格隔离子代理，使用相同 prompt 与 fixture，未读取或应用目标 skill、PM Agent README、内部指令或历史 comparison。
- baseline 也正确使用映射、降低 `unverified` 文档信任并回代码核证；fixture 的事实线索本身较强。baseline 仅作为对照，不影响 with-skill 对三条 assertions 的直接满足。

## Failures

- 无 assertion failure 或 baseline blocker。
- PR #163 新增的部署完整性收尾在本场景不触发：这里只消费 `docs/site` 证据，没有完成 Docs content batch、bootstrap、Release Notes 或构建入口变更；未发现回归。

## Next Steps

- 保留本用例作为 change-map、代码 ground truth 与文档信任模型的回归覆盖。
- 后续可加入无关站点页面，进一步验证精准读取边界。

## Runtime Artifact Policy

- with/without responses、verdict、timing 与 diagnostics 仅保留在 `tmp/eval-runs/idea-to-spec-v0.3.4/`，不提交到 git。
