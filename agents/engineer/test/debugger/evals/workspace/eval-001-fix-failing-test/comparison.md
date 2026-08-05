# Eval Result: eval-001-fix-failing-test

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-001-fix-failing-test`
- Test case: fix-failing-test
- Workspace: `workspace/eval-001-fix-failing-test`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- Overall result: PASS

## Review Context

- Date: 2026-08-03（issue #188 A 维删除后 paired 回归）
- 变更：Common root cause patterns 根因表已删除（L3 A 维实测确认磨平）
- Judge: fresh Codex validation agent，双侧 candidate 冻结后独立判定（`tmp/eval-runs/issue-188-regress/judge/verdict-paired.md`）

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 隔离副本（`tmp/eval-runs/issue-188-regress/`），active notification 实现错误地排除 `read` 并保留 `archived`；PRD/TRD 定义 active 包含 `unread`/`read`、排除 `archived`
- With-skill evidence: `tmp/eval-runs/issue-188-regress/with_skill/debugger-eval-001/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-188-regress/without_skill/debugger-eval-001/candidate-output.md`

## Assertions

- PASS `aligns_expected_behavior`：引用 `docs/pm/notifications/PRD.md` 与 `docs/engineer/notifications/TRD.md` 说明预期；without-skill FAIL（概述了预期但未引用具体文档路径）
- PASS `classifies_requirement_alignment`：分类为 `implementation_deviation` 并排除其他类别；without-skill FAIL（未分类直接修复）
- PASS `reproduces_failure`：复现命令、退出码、actual/expected 错误信息完整；without-skill 同 PASS
- PASS `reports_root_cause`：根因定位到 `notification.status !== "read"` 谓词；without-skill 同 PASS
- PASS `presents_combined_analysis_and_plan`：一次性呈现根因/变更/验证并等一次确认；without-skill FAIL（先实施后报告）
- PASS `blocks_e2e_before_repair_plan`：计划确认前不更新 E2E，修复后 E2E 引用已确认 IMPLEMENTATION_PLAN.md；without-skill FAIL（无门禁说明）
- PASS `does_not_fix_directly`：明确尚未修改代码、停在确认门禁；without-skill FAIL（直接修复并声称通过）

## With Skill Behavior

- 删除根因表后仍完整执行：预期对齐（PRD/TRD 精确引用）→ 分类 → 复现 → 根因 → 合并呈现分析与修复计划 → 等待一次确认 → 不直接修复；E2E 与实施计划门禁完整保留。

## Without Skill Baseline

- 来源：2026-08-03 fresh baseline（同 prompt/fixture，未读 skill）；2/7 assertions PASS（复现与根因）。
- 区分度清晰：skill 保留 PRD/TRD 精确引用、预期分类、合并计划与单次确认停点、E2E/实施计划门禁、不得直接修复等协议；根因表删除无回归。

## Failures / Findings

- 无 with-skill assertion failure；无 NOT EXERCISED；Coverage FULL。
- 根因表删除后双侧区分度保持（7/7 vs 2/7），与 #188 删除决策一致（删除的是 baseline 已内化的根因知识，保留的是协议门禁）。

## Historical Results

- 2026-07-30（删除前）：PASS（7/7 assertions；without-skill 同 7/7，根因表内容被 baseline 白捡）。该轮基于删除前 skill 内容，仅作历史记录。

## Next Steps

- 删除后后续修改 debugger 时重新运行本 eval 与其他 eval（eval-005 mapped 场景等）。
- 本 eval 断言区分度良好（协议门禁类），保持现状。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-188-regress/`（ignored 运行期目录，未提交）。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
