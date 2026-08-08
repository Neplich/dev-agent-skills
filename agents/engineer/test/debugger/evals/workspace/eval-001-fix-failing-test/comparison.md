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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c794a9f4d25d61e50b6bf610eddf7b88ff4be58b7215ed85d280d6be8cae915f`
- Skill overlay SHA-256: `ee5b521f7d9c6fe11867036a027efeb03a84b77600d52fa7396a529de342ee2e`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a64fd90ac10a25e027c288e912b74561949edde0e4324959b4f6359f344c4587`
- Metadata SHA-256: `b2ee79c4493432ae5076e82b907d6b1be7ab09583eef30c12a61c6ba0cd38123`
- Executor SHA-256: `28de521676f44fb26d98a8943e30e638b7117fde8c52e2e6bdc9323fd9003961`
- Runtime SHA-256: `e054983e5b847c0b5102be505d299683dafcc043b1cc5f0db5fafb24d083ee5b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `aligns_expected_behavior` | PASS | With-skill output explicitly cites both PRD.md and TRD.md and states active notifications include unread/read and exclude archived. |
| `classifies_requirement_alignment` | PASS | It classifies the issue as implementation_deviation before presenting the root cause. |
| `reproduces_failure` | PASS | It gives the test command, actual IDs ["n-1", "n-3"], and expected IDs ["n-1", "n-2"]. |
| `reports_root_cause` | PASS | It identifies the incorrect status !== "read" condition in src/api/notifications.ts:12 and explains its effect. |
| `presents_combined_analysis_and_plan` | PASS | The response combines analysis and a concrete repair plan, then requests one confirmation before modifying and validating. |
| `blocks_e2e_before_repair_plan` | PASS | The plan states no E2E files will be modified, and raw Git evidence shows no E2E or other workspace writes. |
| `does_not_fix_directly` | PASS | It presents a proposed fix and explicitly waits for confirmation; it does not claim code or tests were modified or validated. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666; fixture_sha256=5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff; output_sha256=0b5dccef253e8c84d8ff4512338c9df04da770070c16cf7e448e4b5d539a85e5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Aligns behavior to PRD/TRD, classifies the deviation, reproduces and explains the failure, presents a repair plan, preserves a clean Git state, and waits for confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666; fixture_sha256=5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff; output_sha256=75750998249acc79fb06e6d8a6b35100ee579fb98eb17923a6c0e30af39fe967; snapshot_sha256=979419988003dce818013a156de00587aa1bee4357920919a8ba007a4a60eab8
- Behavior: Claims the bug was fixed and tests passed, with a source-file worktree modification, but provides no requirements alignment, classification, reproduction, or confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c794a9f4d25d61e50b6bf610eddf7b88ff4be58b7215ed85d280d6be8cae915f`
- Skill overlay SHA-256: `ee5b521f7d9c6fe11867036a027efeb03a84b77600d52fa7396a529de342ee2e`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6b7f6f3c728ce188aed0a47e4a45eb3f4fe94997d76729d3cd71d8126d7fbe1a`
- Metadata SHA-256: `b2ee79c4493432ae5076e82b907d6b1be7ab09583eef30c12a61c6ba0cd38123`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `a6701d093076bc07d26c7e813151915b2b1a25f501428e58ba88c24bfe3d6c6e`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `aligns_expected_behavior` | PASS | 引用了 PRD/TRD，并在修复计划中说明仅保留 unread/read，排除 archived。 |
| `classifies_requirement_alignment` | PASS | 明确分类为 implementation_deviation。 |
| `reproduces_failure` | PASS | 提供了测试命令、实际 ID 结果和预期 ID 结果。 |
| `reports_root_cause` | PASS | 明确指出 src/api/notifications.ts:12 使用 status !== "read" 导致过滤条件错误。 |
| `presents_combined_analysis_and_plan` | PASS | 同一输出中同时呈现根因和修复计划，并仅在开始修改前请求一次确认。 |
| `blocks_e2e_before_repair_plan` | FAIL | 未明确说明修复计划经确认前不得新增或更新 E2E TC，也未说明后续 E2E 文档补充必须引用已确认的 IMPLEMENTATION_PLAN.md。 |
| `does_not_fix_directly` | PASS | 未声称已修改代码、更新测试、应用修复或验证通过；工作区和 git diff 均为空。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666; fixture_sha256=5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff; output_sha256=34ea3954bf266441363a2bec9f6ae86b3991e92d29b4a66e454fe94857eb3413; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了需求对齐、分类、复现、根因分析和修复计划，并等待用户确认；未修改工作区。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666; fixture_sha256=5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff; output_sha256=c7f73f6dee64e72cb700226c74f9a5447dac3fac5a0d7ddcd17ec10357ae0bb1; snapshot_sha256=979419988003dce818013a156de00587aa1bee4357920919a8ba007a4a60eab8
- Behavior: 直接修改了实现并声称测试通过，未提供需求对齐、复现、根因或确认流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出遗漏了 E2E 更新前置阻断和 IMPLEMENTATION_PLAN.md 引用要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4d48049390ab002df61765af74d4475aee31c5bcd9182a3c09d089676dc5c67c`
- Skill overlay SHA-256: `900f3a9f7889564aa652e55c72206132dc4b2c69166314535fb3c79893f86eba`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6b7f6f3c728ce188aed0a47e4a45eb3f4fe94997d76729d3cd71d8126d7fbe1a`
- Metadata SHA-256: `b2ee79c4493432ae5076e82b907d6b1be7ab09583eef30c12a61c6ba0cd38123`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `aligns_expected_behavior` | FAIL | with_skill 输出未引用 docs/pm/notifications/PRD.md 或 docs/engineer/notifications/TRD.md。 |
| `classifies_requirement_alignment` | FAIL | with_skill 输出未区分 implementation_deviation、requirement_change、trd_gap 或 missing_docs。 |
| `reproduces_failure` | FAIL | with_skill 输出未提供复现步骤或错误信息。 |
| `reports_root_cause` | FAIL | with_skill 输出未给出根因分析。 |
| `presents_combined_analysis_and_plan` | FAIL | with_skill 输出仅声称已修复，未合并呈现根因分析与修复计划，也未说明等待一次用户确认。 |
| `blocks_e2e_before_repair_plan` | FAIL | with_skill 输出未说明修复计划确认前阻断 E2E 更新，也未要求后续 E2E 文档引用已确认的 IMPLEMENTATION_PLAN.md。 |
| `does_not_fix_directly` | FAIL | with_skill 输出明确声称“已修复”并报告验证通过；其 git evidence 也显示 src/api/notifications.ts 已修改。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666; fixture_sha256=5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff; output_sha256=531fee06708d92942763db775099e5885800897d14fa1fb0e3b205c4532e02df; snapshot_sha256=979419988003dce818013a156de00587aa1bee4357920919a8ba007a4a60eab8
- Behavior: 同样直接修改实现并声称测试通过；未满足任一流程性输出要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=466181e7694b25aaf0cac9d93d523254287de12a8ec17c132e46918754d64666; fixture_sha256=5c2aa809e84372707ac261c141dd4e1423c9e30cd9e6ea24a75c119a154d7dff; output_sha256=2d0507bac0f01ebfad4990af65882f2e01b6bad85ae075a69fa6adbf7d91b2dd; snapshot_sha256=213ecfc0f050d1ec64b2660f2b8c7a5677052b704d3959c03673e292fe4c78ca
- Behavior: 直接修改实现并声称测试通过，未遵循文档对齐、分析、计划和确认流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足任何一项断言。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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
