# Eval Result: eval-003-professional

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-003-professional`
- Test case: Professional Design System
- Workspace: `workspace/eval-003-professional`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 2/2 assertions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed PM handoff and approved PRD for an enterprise analytics visual system
- Expected output: 面向企业软件的专业视觉系统文档，强调可信和可访问性，并在设计交接处停止

## Assertions

- PASS `assertion_1`: with_skill 明确覆盖 WCAG AA 对比度与企业数据层级。
- PASS `assertion_2`: with_skill 只交付视觉规范，没有输出实现代码。

## With Skill

- 实际执行 Design System Data 检索后生成视觉系统，覆盖 WCAG 4.5:1/3:1、表格、图表、告警、状态与反模式。
- 仅交付设计规范和工程 handoff 要点，不进入实现。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 visual-design skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 2/2 assertions，覆盖 WCAG 与数据层级并保持设计止点；相较 with_skill，reference-driven rationale 和企业数据组件完整度较弱。

## Failures

- 无 assertion failure。
- 当前 assertions 对 skill 增益的区分度有限，增益主要体现在设计依据和组件覆盖深度。

## Next Steps

- 保留该 eval 对可访问性、企业数据组件和不落代码边界的覆盖。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics were generated only in an ignored scratch workspace and are not committed.
