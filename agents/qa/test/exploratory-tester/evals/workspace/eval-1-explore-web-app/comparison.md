# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7` from `agents/qa/test/exploratory-tester/evals/workspace/eval-1-explore-web-app`.
- Fixture SHA-256: `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7`
- Prompt SHA-256: `b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- Skill overlay SHA-256: `f90efe8186969e2f5d6c26cc6d2a76589cb8efe0e7f9452cedf25227be4cf8e9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `32b9d61e575fbee81406ffc68edbaec9418feec621754c8fca12fc2f2edd2c08`
- Metadata SHA-256: `228751d86855b3dcdb583bdc4a44c4a493c28334ed74368c030ddad805b1f314`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The with_skill report contains a charter specifying surface, timebox, heuristics, and escalation signals. |
| `assertion_2` | NOT_EXERCISED | The report claims the required QA files were read and no new cases/scripts were created, but locked evidence cannot independently prove the required read order. |
| `assertion_3` | PASS | The 15-minute timebox comes from the user prompt, and exploration is scoped to the changed surfaces and adjacent keyboard/empty-state risks. |
| `assertion_4` | PASS | The report separately lists observed issues, suspicious but unconfirmed signals, and gaps not explored, with no unconfirmed product defect asserted. |
| `assertion_5` | PASS | The report uses a chartered path, documents preflight coverage and evidence, and does not present random-click activity as exploration. |
| `assertion_6` | PASS | The handoff report includes charter, timebox, covered path, evidence basis, blocker details, and recommended next actions. |
| `deduplicates_existing_flows` | PASS | The existing TC-001 is explicitly reused; FLOW_INDEX is incrementally updated, and no duplicate TC or script is created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=defdc159a4acd6fc5bb54af12196f595070e72d90b4a9d96aea9f6b430a166e4; snapshot_sha256=5c303f089844fbd53fdce1936a9173a76c2e190e985a3fe1964b59c291ead068
- Behavior: Produced a structured exploratory handoff, updated FLOW_INDEX, reused TC-001, and correctly reported that browser execution was blocked before interaction.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=7b779f8798c81248c6d9716bc1afdf92580a43bacd0cc41713855fba1668aa75; snapshot_sha256=c50958ec45a9616b0d76349357521666d81c27061f1b07ac4517bf97ab249e7f
- Behavior: Produced a handoff report reusing TC-001 and documented the QA_BASE_URL blocker, but did not update FLOW_INDEX.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide QA_BASE_URL or a runnable target and execute the chartered filtering, empty-state, and keyboard-navigation paths.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7` from `agents/qa/test/exploratory-tester/evals/workspace/eval-1-explore-web-app`.
- Fixture SHA-256: `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7`
- Prompt SHA-256: `adb51c9508613745e4594166968ba5eae31bfca02ef3c43a040df0498e1923c7`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `afbb19ee49749967688f949ed21bb2386ea86b8301685fafced66b23325118ab`
- Skill overlay SHA-256: `253325aa58a969826ea6853544729e44f6b321de1621777385ced958992f1626`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b189077590accc8a288dd5027f94ec220abaf589b0e6787e235e77f305935bbd`
- Metadata SHA-256: `228751d86855b3dcdb583bdc4a44c4a493c28334ed74368c030ddad805b1f314`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill report includes a charter specifying surface, timebox, heuristics, and escalation signals. |
| `assertion_2` | PASS | Report states TEST_SUITE.md, FLOW_INDEX.md, and TC-001 were read; no new E2E scenario was added, and FLOW_INDEX.md was updated. |
| `assertion_3` | FAIL | The report states a 15-minute timebox, but the fixture context provides no timebox; the value is unsupported by the supplied context. |
| `assertion_4` | PASS | Report separates observed issues, suspicious but unconfirmed signals, and gaps not explored; blockers are explicitly not called product defects. |
| `assertion_5` | PASS | Report uses a chartered path covering filters, zero results, recovery, and keyboard traversal, with evidence requirements; no random-click log is presented. |
| `assertion_6` | PASS | Report contains charter, timebox, exploration path, evidence used, and recommended next actions for handoff and escalation. |
| `deduplicates_existing_flows` | PASS | The existing TC-001 flow is reused and FLOW_INDEX.md is updated; no synonymous TC or script is created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adb51c9508613745e4594166968ba5eae31bfca02ef3c43a040df0498e1923c7; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=ad399c329981be9ed249e22cacd1d28fce22bd29a6f73a4efdf60edb6add92a1; snapshot_sha256=b5aca84b351075945ea166737d83fa5dea465f68ff4ebfcfcfb421b4b997d507
- Behavior: Produced a structured blocked exploration report, reused TC-001, and updated FLOW_INDEX.md; it incorrectly introduced an unsupported 15-minute timebox.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adb51c9508613745e4594166968ba5eae31bfca02ef3c43a040df0498e1923c7; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=129c8a0c232a8704c0747fb9829589e4ce3b82ebe63303170d3462b7d4613b41; snapshot_sha256=92cd9832e53320fd850d28f628be19b23e48e110f361840877700257563ed6ce
- Behavior: Produced a blocked handoff report with a useful exploration matrix and execution recipe, but did not update QA memory and did not separate all required evidence categories.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_3 fails because the stated 15-minute timebox is not grounded in fixture context.
- Next: Derive the timebox from explicit project context, or mark it as unspecified rather than assigning a default.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7` from `agents/qa/test/exploratory-tester/evals/workspace/eval-1-explore-web-app`.
- Fixture SHA-256: `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7`
- Prompt SHA-256: `adb51c9508613745e4594166968ba5eae31bfca02ef3c43a040df0498e1923c7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2bfbb6ecc0134ec5f9998274cdf0307f307da434e743767837778ac154a53a86`
- Skill overlay SHA-256: `d11214369d847e3bf37c4f57b3d2f711860c3796c879f82ec5e4e0b0da64ec70`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b189077590accc8a288dd5027f94ec220abaf589b0e6787e235e77f305935bbd`
- Metadata SHA-256: `228751d86855b3dcdb583bdc4a44c4a493c28334ed74368c030ddad805b1f314`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill report includes an exploration charter covering changed surfaces, heuristics, escalation signals, and the blocked-state evidence plan. |
| `assertion_2` | PASS | Report records reading TEST_SUITE.md, FLOW_INDEX.md, and the existing case; notes scripts/*.spec.md is absent, reuses TC-001, and directs future reusable additions to existing TC/FLOW_INDEX/scripts without inventing a duplicate. |
| `assertion_3` | PASS | Timebox is explicitly marked unavailable because blocking occurred before execution, with retry duration deferred to the QA execution window/user context; scope prioritizes SearchPanel, FilterPills, ResultsList, and keyboard-navigation risks. |
| `assertion_4` | PASS | Report separately identifies confirmed issues, suspicious-but-unconfirmed signals, and unexplored gaps, and does not convert documented focus risk into a defect. |
| `assertion_5` | PASS | The report uses a chartered path covering filtering, empty states, transitions, keyboard boundaries, and refresh/rapid switching, while clearly stating that execution was blocked and providing evidence requirements. |
| `assertion_6` | PASS | With-skill deliverables contain charter, timebox, covered/planned exploration paths, evidence references, blocked rationale, and recommended next actions suitable for handoff. |
| `deduplicates_existing_flows` | PASS | The existing TC-001 flow is reused; the report explicitly says to update existing TC, scripts, or FLOW_INDEX for reusable paths and not create duplicate TCs. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adb51c9508613745e4594166968ba5eae31bfca02ef3c43a040df0498e1923c7; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=93b0e45a45070797a5dbaf128677148403c70ce7d2ed96cd53e3034c17b07b1b; snapshot_sha256=824435ea452d1e9a4b25547bb99d5bcaa42aef2d48a762ba8319a26debf844db
- Behavior: Produced a blocked summary report plus TC-001 execution evidence with explicit charter, context-derived timebox handling, evidence layers, coverage gaps, and deduplication guidance.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adb51c9508613745e4594166968ba5eae31bfca02ef3c43a040df0498e1923c7; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=00fe6ddd3350430b76d2acce2c50af985d96635e4faba32a8767d48d50db1ffa; snapshot_sha256=631ebcbf902b053e5ecbb20e3fb9ec3d38e176f1489fe68f8694380b56987c81
- Behavior: Produced a blocked exploratory handoff reusing TC-001 and listing planned risks, but with less explicit QA-memory/read-order and evidence classification detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Eval Result: eval-001-explore-web-app

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`
- Test case: explore-web-app
- Workspace: `workspace/eval-1-explore-web-app`
- Natural user prompt:

> 对当前可访问的目标应用进行探索测试，基于产品上下文、变更范围和环境说明发现潜在问题。

- Expected artifact: 探索测试报告，包含发现的问题列表和复现路径

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/exploratory-tester--eval-001-explore-web-app/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `184eaa5af2608524f96a97cb3aec674698e5b2340f026f0d70e0c799bc12ffaa`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 6 / FAIL 0 / NOT EXERCISED 1）
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>探索章程 | PASS | transcript 先读取技能规范，最终报告含 surface、timebox（未开始）、heuristics、escalation signal。 | FAIL | 报告虽有章程目标和路径，但未明确 timebox 与 escalation signals。 |
| `assertion_2`<br>探索记忆沉淀 | PASS | transcript 先读取 TEST_SUITE.md、FLOW_INDEX.md、TC-001；确认无 scripts、results、历史报告，且最终未新增 E2E 场景或脚本。 | PASS | transcript 也先读取 TEST_SUITE.md、FLOW_INDEX.md、cases/TC-001；未新增 E2E 场景。 |
| `assertion_3`<br>范围与时限 | PASS | 报告明确 timebox 未开始，原因是 QA_BASE_URL 缺失，并围绕 SearchPanel、FilterPills、ResultsList 及焦点风险组织 charter。 | FAIL | 报告未给出 timebox；仅说明环境阻塞，未形成来自上下文的明确时限处理。 |
| `assertion_4`<br>证据分层 | PASS | 最终报告明确分出 Observed issues、Suspicious but unconfirmed signals、Gaps not explored，且未把阻塞伪装成产品缺陷。 | FAIL | 报告没有分开的 observed issues、suspicious signals、gaps not explored 三类章节。 |
| `assertion_5`<br>探索方法 | PASS | 报告明确实际覆盖为 preflight only，并列出未执行的 UI、console、network、timing 路径；没有随机点击日志。 | PASS | 报告提供了结构化探索路径和执行记录，未使用随机操作日志替代探索方法。 |
| `assertion_6`<br>可交接产物 | PASS | 最终快照中的 test-reports-2026-08-07.md 含 Charter、Timebox、Exploration path covered、evidence/preflight evidence、Recommended next actions。 | FAIL | 报告有章程、路径和恢复建议，但未明确 timebox，且缺少完整的 evidence used 交接段落。 |
| `deduplicates_existing_flows`<br>不重复创建同义 TC | NOT EXERCISED | 由于 QA_BASE_URL 缺失，未实际发现或执行既有 TC-001 流程；因此没有触发“发现同义流程后增量更新”的条件。快照未新增同义 TC。 | NOT EXERCISED | 同样未进入应用、未发现可复用流程，去重更新条件未触发。 |

## With-Skill Behavior

with_skill 按要求完成前置读取、章程和阻塞报告；未启动浏览器，未产生运行时探索证据。

## Fresh Without-Skill Baseline

without_skill 完成基本上下文读取和章程草案，但缺少完整章程字段及分层报告结构。

## Failures

- 无。

## Not Exercised

- deduplicates_existing_flows：两条 lane 均未启动应用，未触发发现既有同义流程的条件。

## Next Steps

- 提供 QA_BASE_URL、浏览器/平台版本及同路径 TRD 与 IMPLEMENTATION_PLAN 后重试。
- 重试时执行 TC-001，并在实际发现重复流程或新增可复用场景时验证 TC、scripts 与 FLOW_INDEX 的增量更新。
- 补充运行时 UI、console、network 和截图证据，覆盖空结果、焦点切换、刷新/返回及异常响应。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
