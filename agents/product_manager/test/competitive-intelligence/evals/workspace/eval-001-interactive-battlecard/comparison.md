# Eval Result: eval-001-interactive-battlecard

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-intelligence`
- Eval: `eval-001-interactive-battlecard`
- Test case: interactive-battlecard
- Workspace: `workspace/eval-001-interactive-battlecard`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that competitive-intelligence creates an evidence-aware interactive battlecard plan.
- Expected output: 面向销售的 battlecard 输出，包含竞品卡片、功能/定价/定位对比、近期变化、反驳话术和证据来源说明。

## Assertions

- `battlecard`: 形成 battlecard 结构
- `sales_context`: 面向销售场景
- `freshness`: 处理近期变化

## With Skill

Observed behavior:

- 当前 skill 明确产出交互式 HTML battlecard，包含竞品卡片、横向矩阵、功能/定价/定位、近 90 天发布、talk tracks、objection handling 和 freshness 说明，满足断言。

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 实际运行若缺少本方公司信息，应先确认 seller context 或显式使用占位。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
