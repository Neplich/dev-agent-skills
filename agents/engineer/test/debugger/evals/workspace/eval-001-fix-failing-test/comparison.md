# Eval Result: eval-001-fix-failing-test

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-001-fix-failing-test`
- Test case: fix-failing-test
- Workspace: `workspace/eval-001-fix-failing-test`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 测试 test/api/notifications.test.ts 失败了，帮我修复
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `aligns_expected_behavior`: transcript item_4 读取 PRD/TRD；item_6 明确说明保留 unread/read、排除 archived；final.md 引用了两份文档。
- PASS `classifies_requirement_alignment`: transcript item_6 和 final.md 在根因前明确分类为 implementation_deviation。
- PASS `reproduces_failure`: transcript item_7 实际运行测试并记录 AssertionError，actual 为 [n-1,n-3]、expected 为 [n-1,n-2]。
- PASS `reports_root_cause`: final.md 明确定位 src/api/notifications.ts:12 的过滤条件错误；workspace 文件与该定位一致。
- PASS `presents_combined_analysis_and_plan`: final.md 将根因、文件变更和验证方式合并呈现，末尾只等待一次确认；无 file_change 事件。
- FAIL `blocks_e2e_before_repair_plan`: final.md 仅写“如影响 E2E，建议后续检查”，未说明确认前不得新增/更新 E2E TC，也未要求修复后引用已确认的 IMPLEMENTATION_PLAN.md。
- PASS `does_not_fix_directly`: with_skill transcript 无 file_change 事件；with_skill input/output 哈希中的源文件与测试文件一致，实际 workspace 未被修复。

## With Skill Behavior

完成 PRD/TRD 对齐、失败复现、根因分析和修复计划，并等待确认；未直接修改代码，但遗漏 E2E 更新阻断及 IMPLEMENTATION_PLAN 引用要求。

## Without Skill Baseline

baseline 直接修改 src/api/notifications.ts 并重新运行测试通过；未进行 PRD/TRD 对齐或确认门禁。

## Failures / Findings

- blocks_e2e_before_repair_plan：未明确确认前禁止更新 E2E，也未要求后续引用已确认的 IMPLEMENTATION_PLAN.md。
- Root cause: with_skill 遵循了调试确认门禁但没有把 skill 要求的 E2E 更新前置阻断和 IMPLEMENTATION_PLAN 追溯要求写入最终计划。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-fix-failing-test

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-001-fix-failing-test`
- Test case: fix-failing-test
- Workspace: `workspace/eval-001-fix-failing-test`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- Historical result: PASS

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
