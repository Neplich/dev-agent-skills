# Eval Result: eval-001-fix-failing-test

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-001-fix-failing-test`
- Workspace: `workspace/eval-001-fix-failing-test`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）- 2026-08-03 #188 删除后 paired 回归（with-skill 7/7 / without-skill 2/7，judge 独立判定）
- Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- 日期：2026-08-03（#188 删除后 paired 回归）
- Fixture：active notification 实现错误地排除 `read` 并保留 `archived`（隔离副本 `tmp/eval-runs/issue-188-regress/`）
- With-skill evidence: `tmp/eval-runs/issue-188-regress/with_skill/debugger-eval-001/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-188-regress/without_skill/debugger-eval-001/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-188-regress/judge/verdict-paired.md`


## Historical Results

# Eval Result: eval-001-fix-failing-test

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-001-fix-failing-test`
- Workspace: `workspace/eval-001-fix-failing-test`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- 日期：2026-07-30
- Fixture：active notification 实现错误地排除 `read` 并保留 `archived`。
- Fresh run：`tmp/eval-runs/issue-196-l2-2-debugger-20260730-220643/`
- 本轮重新生成 with-skill 与 without-skill 候选，未复用历史 baseline。

## Assertion Results

- PASS `aligns_expected_behavior`：引用 PRD/TRD，明确 active 包含 unread/read、排除 archived。
- PASS `classifies_requirement_alignment`：根因分析前分类为 `implementation_deviation`。
- PASS `reproduces_failure`：记录测试命令、退出码、实际/预期数组及 AssertionError。
- PASS `reports_root_cause`：定位错误过滤条件及其双向影响。
- PASS `presents_combined_analysis_and_plan`：根因与 standard 修复计划一次呈现，只等待一次实施确认。
- PASS `blocks_e2e_before_repair_plan`：计划确认前禁止更新 E2E，后续交接要求引用已确认 IMPLEMENTATION_PLAN。
- PASS `does_not_fix_directly`：未修改代码、测试或 E2E，也未声称验证修复通过。

## With-Skill Behavior

候选按无显式 `change_tier` 的 `standard` 路径，一次完成预期对齐、真实复现、根因分析和最小修复计划，并停在唯一一次实施确认门禁。

## Without-Skill Baseline

来源为本轮隔离子代理基于同一 prompt 与 fixture 新生成的 baseline，未读取 debugger skill、Engineer README 或 with-skill 输出。baseline 同样完成预期对齐、分类、复现、根因、合并计划、确认与 E2E 门禁，满足 7/7 assertions。

## Failures

- With-skill：无。
- Baseline：无；本用例本轮没有拉开 skill 与通用响应的行为差异。

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- Overall result: PASS

## Next Steps

保留该用例验证新契约“分析与计划一次呈现、动代码前一次确认”；如需衡量增益，应减少 prompt/fixture 对门禁细节的直接提示。

## Runtime Artifact Policy

候选、verdict 与诊断仅保存在上述 ignored runtime 目录，不提交到 git；长期仅更新本 `comparison.md`。

## 2026-08-03 变更后回归（issue #188）

- 变更：删除 Common root cause patterns 根因表（A 维实测确认磨平）。
- 验证：删除后 paired 回归（fresh 双侧，judge 独立判定）：with-skill 7/7 PASS、without-skill 2/7 PASS（PRD/TRD 精确引用、分类、合并计划、确认停点、E2E/计划门禁保持明确区分）。
- 验证：L3 A 维 with/without 实测确认磨平（judge 独立判定，证据 `tmp/eval-runs/issue-188-l3/`）；删除后以原 eval prompt + fixture 重跑 with-skill，fresh judge 逐条判定原断言全部 PASS（7/7 PASS），Behavior result **PASS**，**无回归**（证据 `tmp/eval-runs/issue-188-regress/`）。
