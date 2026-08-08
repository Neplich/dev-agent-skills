# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-001-fix-failing-test`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff` from `agents/engineer/test/debugger/evals/workspace/eval-001-fix-failing-test`.
- Fixture SHA-256: `5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff`
- Prompt SHA-256: `466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dcc41028443385df7286f016738f0aaf1f647d06f9da1ee3865bedd33c344afe`
- Skill overlay SHA-256: `267ff29e20f38caffb753a87229899be929d0e39edb8d8216c48698de2a99ab6`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6b7f6f3c728ce188aed0a47e4a45eb3f4fe94997d76729d3cd71d8126d7fbe1a`
- Metadata SHA-256: `b2ee79c4493432ae5076e82b907d6b1be7ab09583eef30c12a61c6ba0cd38123`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `aligns_expected_behavior` | FAIL | with_skill 输出未引用 PRD.md 或 TRD.md，也未按要求对齐并说明预期行为。 |
| `classifies_requirement_alignment` | FAIL | 未在根因分析前区分 implementation_deviation、requirement_change、trd_gap 或 missing_docs。 |
| `reproduces_failure` | FAIL | 仅报告测试通过，未提供失败复现步骤或错误信息。 |
| `reports_root_cause` | FAIL | 只说明筛选条件已修改，未明确分析原实现为何导致失败。 |
| `presents_combined_analysis_and_plan` | FAIL | 未呈现根因分析与修复计划，也未等待用户确认。 |
| `blocks_e2e_before_repair_plan` | FAIL | 未说明修复计划确认前禁止新增或更新 E2E TC，也未要求引用已确认的 IMPLEMENTATION_PLAN.md。 |
| `does_not_fix_directly` | FAIL | 输出明确声称已修复、测试通过并修改了 src/api/notifications.ts。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666; fixture_sha256=5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff; output_sha256=2c64db3849c80f924eea593a380d8fc942706c07d243b94f850cfd60a215c33f; snapshot_sha256=979419988003dce818013a156de00587aa1bee4357920919a8ba007a4a60eab8
- Behavior: 同样直接修改代码并报告测试通过；未满足要求的分析、计划、E2E 阻断和确认流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666; fixture_sha256=5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff; output_sha256=8a1f3a058823a42976a455ee43631449f715a01af690abd48042635c23b0d060; snapshot_sha256=213ecfc0f050d1ec64b2660f2b8c7a5677052b704d3959c03673e292fe4c78ca
- Behavior: 直接修改代码并报告测试通过，未进行需求对齐、分类、复现或计划确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足任何一项断言要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

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
