# Eval Result: eval-001-positioning-gap-brief

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`
- Test case: positioning-gap-brief
- Workspace: `workspace/eval-001-positioning-gap-brief`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: PASS

## Review Context

- Date: 2026-08-03（issue #188 A 维删除后 paired 回归）
- 变更：Analysis Frameworks 节已删除（L3 A 维实测确认磨平），新增 Battlecard Mode 条件模式
- Judge: fresh Codex validation agent，双侧 candidate 冻结后独立判定（`tmp/eval-runs/issue-188-regress/judge/verdict-paired.md`）

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: live 联网研究（Linear 与 Jira 官方公开页面），无静态 fixture
- With-skill evidence: `tmp/eval-runs/issue-188-regress/with_skill/competitive-brief-eval-001/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-188-regress/without_skill/competitive-brief-eval-001/candidate-output.md`

## Assertions

- PASS `positioning`：分别说明 Linear 与 Jira 的定位、目标用户和核心卖点；without-skill 同 PASS
- PASS `messaging_gap`：识别线性/强治理之间的 messaging gap 并提出可切入机会；without-skill 同 PASS
- PASS `evidence_boundary`：区分官方事实与策略推断，无法确认信息标记为假设；without-skill 同 PASS

## With Skill Behavior

- 删除 Analysis Frameworks 后仍产出完整 brief：定位、卖点、messaging gap、机会/威胁/行动项，并保留证据边界；Battlecard Mode 在 pm-agent `battlecard` 信号路由时直接产出单页 battlecard（不输出完整 brief）。

## Without Skill Baseline

- 来源：2026-08-03 fresh baseline（同 prompt，未读 skill）；3/3 assertions PASS。
- 原断言双侧零区分（baseline 已内化定位/gap/证据边界分析）；skill 增量在扩展内容（近期动态、机会、威胁、行动项）与 Battlecard Mode，删除后无行为回归。

## Failures / Findings

- 无 with-skill assertion failure；无 NOT EXERCISED；Coverage FULL。
- 零区分度观察：原 3 条断言被 baseline 全部白捡，与 #188 删除决策一致（已删内容正是 baseline 内化的框架知识）；剩余增量不在本 eval 断言范围。

## Historical Results

- 2026-07-26（删除前）：PASS（3/3 assertions，fresh same-agent judge；双侧均满足，with-skill 对事实/推断边界更系统）。该轮基于删除前 skill 内容，仅作历史记录。

## Next Steps

- 删除后后续修改 competitive-brief 时重新运行本 eval。
- 原断言已无区分度；后续评估可考虑把断言钉在 skill 特有增量（Battlecard Mode 产物、扩展结构）上。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-188-regress/`（ignored 运行期目录，未提交）。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
