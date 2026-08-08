# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-004-nested-feature-path-bug-alignment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0` from `agents/engineer/test/debugger/evals/workspace/eval-004-nested-feature-path-bug-alignment`.
- Fixture SHA-256: `1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0`
- Prompt SHA-256: `c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c794a9f4d25d61e50b6bf610eddf7b88ff4be58b7215ed85d280d6be8cae915f`
- Skill overlay SHA-256: `ee5b521f7d9c6fe11867036a027efeb03a84b77600d52fa7396a529de342ee2e`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ed41777f0081de6b22c8d5c1da9d06cff7a26fda1bb09b0b22361f263f5eaee`
- Metadata SHA-256: `92b34bddeb11ae5b3c6841a7115ad004679cbe8ce0c62b863a34d672cce43c83`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_nested_expected_behavior_docs` | FAIL | with_skill 引用了两个文档路径，但未说明它们对应 feature_path: chat-interface/messages/history/search。 |
| `validates_trd_related_prd` | NOT_EXERCISED | 原始 fixture 显示 related_prd 与 PRD 路径一致；候选输出未能证明执行了该隐藏校验，且不匹配分支未发生。 |
| `classifies_before_repair_plan` | PASS | 输出在提出后续补充材料前先给出 trd_gap 分类，且未进入修复计划或修复操作。 |
| `blocks_wrong_path_or_requirement_change` | NOT_EXERCISED | fixture 中 feature_path 清晰、PRD 存在、需求未变化且 TRD related_prd 匹配，因此阻断条件未发生。 |
| `does_not_fix_directly` | PASS | 输出明确说明未修改代码或测试，也未声称应用或验证修复。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94; fixture_sha256=1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0; output_sha256=ecf1e999ac15e936c1c751bd999dde326e9f41e59f51526c88803b0e2141b0e3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 读取并引用了 PRD/TRD，给出 trd_gap 分类并保持只读；但遗漏了 feature_path 对应关系的明确说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94; fixture_sha256=1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0; output_sha256=a250f8f38dd54ee8c24177c5606dd625dd11d56791dc6a8a670f14e9b376ea9e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确读取并引用了 PRD/TRD，说明预期排序，但未进行分类，也未修改代码。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 reads_nested_expected_behavior_docs：没有说明两个文档对应 feature_path: chat-interface/messages/history/search。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-004-nested-feature-path-bug-alignment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0` from `agents/engineer/test/debugger/evals/workspace/eval-004-nested-feature-path-bug-alignment`.
- Fixture SHA-256: `1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0`
- Prompt SHA-256: `c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4d48049390ab002df61765af74d4475aee31c5bcd9182a3c09d089676dc5c67c`
- Skill overlay SHA-256: `900f3a9f7889564aa652e55c72206132dc4b2c69166314535fb3c79893f86eba`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ed41777f0081de6b22c8d5c1da9d06cff7a26fda1bb09b0b22361f263f5eaee`
- Metadata SHA-256: `92b34bddeb11ae5b3c6841a7115ad004679cbe8ce0c62b863a34d672cce43c83`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_nested_expected_behavior_docs` | FAIL | With-skill output cites both documents but does not state that they correspond to feature_path: chat-interface/messages/history/search. |
| `validates_trd_related_prd` | FAIL | It does not check TRD related_prd against the PRD path or describe a trd_gap classification. |
| `classifies_before_repair_plan` | FAIL | It provides no required classification before proposing next steps. |
| `blocks_wrong_path_or_requirement_change` | PASS | Fixture evidence shows a clear feature_path, existing PRD, unchanged requirement, and matching TRD related_prd; the output proposes no repair plan, code change, or E2E update. |
| `does_not_fix_directly` | PASS | The output explicitly says it cannot reproduce or locate the defect and claims no code, test, or repair changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94; fixture_sha256=1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0; output_sha256=1ec34a18c3a78602891961919b4ec9c2e702bf8a04e66a5dff1593c9d7e00d0c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Cites both documents and avoids direct repair, but omits feature_path correspondence, related_prd validation, and required classification.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94; fixture_sha256=1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0; output_sha256=6b3844d408009aff328be3b12b5a5fade1397ac82cb5bedf5f41da98b9907c26; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Cites both documents and infers sorting behavior, but does not perform the required path/related_prd validation or classification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- With-skill output fails assertions reads_nested_expected_behavior_docs, validates_trd_related_prd, and classifies_before_repair_plan.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-004-nested-feature-path-bug-alignment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0` from `agents/engineer/test/debugger/evals/workspace/eval-004-nested-feature-path-bug-alignment`.
- Fixture SHA-256: `1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0`
- Prompt SHA-256: `c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dcc41028443385df7286f016738f0aaf1f647d06f9da1ee3865bedd33c344afe`
- Skill overlay SHA-256: `267ff29e20f38caffb753a87229899be929d0e39edb8d8216c48698de2a99ab6`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4ed41777f0081de6b22c8d5c1da9d06cff7a26fda1bb09b0b22361f263f5eaee`
- Metadata SHA-256: `92b34bddeb11ae5b3c6841a7115ad004679cbe8ce0c62b863a34d672cce43c83`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_nested_expected_behavior_docs` | FAIL | 列出了两份文档路径，但未说明它们对应 feature_path: chat-interface/messages/history/search。 |
| `validates_trd_related_prd` | FAIL | 未检查或提及 TRD 的 related_prd 指向同一路径 PRD，也未定义不匹配时的 trd_gap 分类。 |
| `classifies_before_repair_plan` | FAIL | 输出未在调查结论中使用 implementation_deviation、requirement_change、missing_docs 或 trd_gap 分类。 |
| `blocks_wrong_path_or_requirement_change` | PASS | 原始文档显示 feature_path 清晰、PRD 存在、需求未显示变化且 TRD related_prd 路径匹配；输出未进入修复计划、代码修改或 E2E 更新。 |
| `does_not_fix_directly` | PASS | 输出仅说明无法定位并请求补充代码或数据，未声称修改代码、更新测试、应用修复或验证通过。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94; fixture_sha256=1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0; output_sha256=800e503039edd5ba8b660cb75cade4d3a37d7e03e3da4407ff0a5b3472dae2e3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到仅有文档、缺少实现与测试，并保持未修改状态；同样未明确说明 feature_path、校验 related_prd 或进行规定分类。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94; fixture_sha256=1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0; output_sha256=e9ee936e5c57ed26e88a4fe0611a387dc3a8fbd21606e7aacb82e699aefaa4d2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到仅有文档、缺少实现与测试，并保持未修改状态；未完成路径元数据校验或分类。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 nested 文档行为说明、TRD related_prd 校验和修复前分类要求。
- Next: 在输出中明确引用两份文档及 feature_path，校验 related_prd，并在任何修复建议前给出规定分类。

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

# Eval Result: eval-004-nested-feature-path-bug-alignment

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-004-nested-feature-path-bug-alignment`
- Test case: nested-feature-path-bug-alignment
- Workspace: `workspace/eval-004-nested-feature-path-bug-alignment`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 用户说：Message History Search 的搜索结果排序不对，这是 bug，请修一下。相关预期文档在 docs/pm/chat-interface/messages/history/search/PRD.md 和 docs/engineer/chat-interface/messages/history/search/TRD.md。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `reads_nested_expected_behavior_docs`: with_skill 的 final.md 仅写 `chat-interface/messages/history/search`，未引用要求的两个完整 PRD/TRD 路径；transcript 中虽有读取命令证据，但最终输出未满足引用要求。
- NOT EXERCISED `validates_trd_related_prd`: transcript 读取了 `related_prd` 字段且其值匹配，但没有可观测的明确校验结论；未触发不匹配分支。
- FAIL `classifies_before_repair_plan`: final.md 与 transcript 的 agent_message 均未明确分类为 `implementation_deviation`、`requirement_change`、`missing_docs` 或 `trd_gap`。
- NOT EXERCISED `blocks_wrong_path_or_requirement_change`: 实际 PRD/TRD 的 feature_path、parent_feature、feature_level 与 related_prd 均匹配，未触发路径不清、需求变化或 TRD 不一致条件。
- PASS `does_not_fix_directly`: final.md 明确表示没有源码、测试或构建入口，未声称修改代码、更新测试、应用修复或验证修复通过；workspace 文件哈希也未显示文档被修改。

## With Skill Behavior

with_skill 读取了嵌套 PRD/TRD，并确认排序规则及路径一致；但最终输出缺少完整文档路径引用和四选一分类。runtime exit_code 为 0，输入与输出哈希对应的 workspace 文档未变更。

## Without Skill Baseline

without_skill 仅读取并总结了 PRD/TRD，未引用完整路径、未校验或报告 related_prd、未分类；未修改 workspace，作为对照。

## Failures / Findings

- reads_nested_expected_behavior_docs：最终输出未引用两个完整文档路径。
- classifies_before_repair_plan：未输出规定的分类。
- Root cause: with_skill 在确认文档对齐并因缺少源码阻断后，没有把完整路径引用和强制分类写入最终输出。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-004-nested-feature-path-bug-alignment

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-004-nested-feature-path-bug-alignment`
- Workspace: `workspace/eval-004-nested-feature-path-bug-alignment`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- 日期：2026-07-30
- Fixture：`chat-interface/messages/history/search` 四级 Approved PRD/TRD，`related_prd` 同路径匹配。
- Fresh run：`tmp/eval-runs/issue-196-l2-2-debugger-20260730-220643/`
- 本轮全新 paired validation，未复用历史 baseline。

## Assertion Results

- PASS `reads_nested_expected_behavior_docs`：引用 PRD/TRD 并核对 `feature_path`、`parent_feature`、`feature_level`。
- PASS `validates_trd_related_prd`：确认 `related_prd` 同路径，并说明不匹配时分类 `trd_gap`。
- PASS `classifies_before_repair_plan`：在任何计划前记录 `implementation_deviation` 候选，因缺少实现与复现证据而等待确认。
- PASS `blocks_wrong_path_or_requirement_change`：路径/PRD/需求问题回 PM，TRD 字段不一致回 `trd-gen`，均阻断计划、代码与 E2E。
- PASS `does_not_fix_directly`：未修改代码、测试或声称修复。

## With-Skill Behavior

候选精确核对四级文档关系；在缺少实现、失败测试和复现命令时不猜根因，但仍在允许的四类中记录实现偏离候选，并停在证据收集阶段。

## Without-Skill Baseline

来源为本轮隔离子代理基于同一 prompt/fixture 的新候选，未读取 skill、Engineer README 或 with-skill。baseline 完成路径与阻断核对，但明确表示当前不属于四种分类中的任何一种，改用“缺少复现与实现证据”，因此 `classifies_before_repair_plan` 失败；其余 4/5 通过。

## Failures

- With-skill：无。
- Baseline：`classifies_before_repair_plan` FAIL。

## Latest Result

- Behavior result: PASS
- Coverage result: PARTIAL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


未覆盖说明：`classifies_before_repair_plan` 仅以候选形式触发——with-skill 记录了 `implementation_deviation` 候选但因 fixture 缺少实现与复现证据而停在证据收集阶段，未完整执行分类决策。fixture 补充失败样例后该断言才能完整覆盖。

## Next Steps

保留该用例覆盖嵌套 feature path 与证据不足时的分类边界；后续可在 fixture 增加最小排序实现和失败样例，使 `implementation_deviation` 从候选变为可确认结论。

## Runtime Artifact Policy

paired candidates、verdict 与诊断只保存在 ignored runtime 目录，不提交。
