# Eval Result: eval-002-battlecard-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-002-battlecard-mode`
- Test case: battlecard-mode
- Workspace: `workspace/eval-002-battlecard-mode`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: PASS

## Review Context

- Date: 2026-08-03（issue #188 Battlecard Mode 新增后 fresh 双侧验证）
- Judge: fresh Codex validation agent，双侧 candidate 冻结后独立判定（`tmp/eval-runs/issue-188-battlecard/judge/verdict.md`）

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: live 联网研究（Linear 与 Jira 官方公开页面），无静态 fixture

## Assertions

- PASS `battlecard_fields`：Linear/Jira 各产出单页 battlecard，Quick Overview / Their Pitch / Strengths / Weaknesses / Objection Handling / Landmines to Set / Landmines to Defuse / Win-Loss Themes 字段齐全；without-skill FAIL（未呈现 Their Pitch、双向 Landmines、Win/Loss Themes 等指定字段）
- PASS `no_full_brief`：未展开完整 brief 章节，只输出单页 battlecard；without-skill 同 PASS
- PASS `evidence_boundary`：标注研究日期、来源类别，逐项区分官方事实/第三方评价/推断/假设；without-skill 同 PASS
- PASS `no_battlecard_offer`：直接交付 battlecard，未再询问是否创建 battlecard；without-skill 同 PASS

## With Skill Behavior

- Battlecard Mode 生效：pm-agent `battlecard` 信号路由时直接产出两页单页 battlecard（字段齐全），不输出完整 brief，不询问是否创建 battlecard；研究日期与证据标签完整。

## Without Skill Baseline

- 来源：2026-08-03 fresh baseline（同 prompt，未读 skill）；1/4 assertions PASS（no_full_brief、evidence_boundary、no_battlecard_offer 内化，battlecard_fields 因缺指定字段 FAIL）。
- 区分度：结构契约（单页字段清单）保持 skill 增量；范围与证据边界已被 baseline 内化。

## Failures / Findings

- 无 with-skill assertion failure；无 NOT EXERCISED；Coverage FULL。
- 零区分度观察（no_full_brief/evidence_boundary/no_battlecard_offer 被 baseline 白捡）：属模型通用审慎；Battlecard Mode 的增量在固定字段清单。

## Next Steps

- 保留 Battlecard Mode 与 eval-002；后续修改这些规则时重新运行。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-188-battlecard/`（ignored 运行期目录，未提交）。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
