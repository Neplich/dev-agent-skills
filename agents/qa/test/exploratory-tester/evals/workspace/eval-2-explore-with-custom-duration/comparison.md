# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3` from `agents/qa/test/exploratory-tester/evals/workspace/eval-2-explore-with-custom-duration`.
- Fixture SHA-256: `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3`
- Prompt SHA-256: `95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- Skill overlay SHA-256: `f90efe8186969e2f5d6c26cc6d2a76589cb8efe0e7f9452cedf25227be4cf8e9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `234873760fb9d0649d16f54118fbf0383fa2955b9451730f9429892d78a6d7e0`
- Metadata SHA-256: `4befffc2e8037477b9995f3ded3869d8476cd9a66637621d7f8e8d3fc8c6fed3`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill output records the target URL, 5-minute timebox, intended exploration charter, changed-surface risk, environment/DNS evidence, and unverified behaviors. |
| `assertion_2` | NOT_EXERCISED | The run was blocked before independent E2E execution. Raw evidence confirms TEST_SUITE.md and FLOW_INDEX.md were addressed and no active TC existed, but cannot prove the complete required read order or execution confirmation. |
| `version_entry_and_subagent` | NOT_EXERCISED | The candidate correctly recorded that platform version was missing and execution was blocked, but no TC execution, subagent use, or entry-point selection occurred. |
| `assertion_3` | NOT_EXERCISED | No browser session occurred, so console, network, crash, and anomaly-layer classification were not exercised. |
| `assertion_4` | NOT_EXERCISED | The candidate provided blocker evidence and a FLOW_INDEX reference, but actual E2E execution paths were unavailable because DNS blocked the workflow. |
| `assertion_5` | PASS | The candidate records the toast/validation masking risk and gives follow-up steps: restore the hostname, record browser/platform version, and rerun the exploration. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=8f4ee6babb293ecca431ca4d8cbeb3c6bfe725819d7dc39056d4ba4da5b61163; snapshot_sha256=0bd32c6db39131786cdbaf96430215727e8c034b5d6306199cf1ce34817b8d0d
- Behavior: Performed a documented preflight, recorded charter, changed surface, risk, and DNS blocker, updated FLOW_INDEX.md, and correctly deferred execution-dependent checks.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=de65a25d4863064eac5eff05c28ae2b9e7cb21edfa22b7315e9916fcf5412ef2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline detected DNS blockage, summarized scope and risks, and stopped without execution or workspace changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore or provide a reachable QA hostname, record the browser/platform version, then execute the planned E2E exploration and capture TC/results plus console/network/crash evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3` from `agents/qa/test/exploratory-tester/evals/workspace/eval-2-explore-with-custom-duration`.
- Fixture SHA-256: `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3`
- Prompt SHA-256: `95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `afbb19ee49749967688f949ed21bb2386ea86b8301685fafced66b23325118ab`
- Skill overlay SHA-256: `253325aa58a969826ea6853544729e44f6b321de1621777385ced958992f1626`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `234873760fb9d0649d16f54118fbf0383fa2955b9451730f9429892d78a6d7e0`
- Metadata SHA-256: `4befffc2e8037477b9995f3ded3869d8476cd9a66637621d7f8e8d3fc8c6fed3`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The report records the requested URL, 5-minute timebox, charter priorities, changed surface, environment details, and unverified assumptions. |
| `assertion_2` | PASS | It records the feature-update scenario, existing suite/flow review, absence of active TCs/reusable flows/prior results, and no expansion because execution was blocked. |
| `version_entry_and_subagent` | PASS | It marks platform version as blocked, records the qa-agent → exploratory-tester route, and explains the harness → browser connector → standalone fallback order. |
| `assertion_3` | PASS | The report separates no observed product issue, suspicious but unconfirmed toast risk, and uncovered product areas. |
| `assertion_4` | PASS | It provides the preflight execution path, exact curl evidence, source-document references, and a linked report. |
| `assertion_5` | PASS | It documents toast/validation risk and provides concrete retry, environment, evidence-capture, and escalation steps. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=0c9645d164cb6aea7ab4699920f72434e7ad4eff0da6e73f9e12c3f369ab9541; snapshot_sha256=456c5a2deefd65148e4fb818f4efc61011c097070737a09fed5f793ce91a01e0
- Behavior: Correctly blocked execution on DNS and missing platform version, produced a structured exploratory QA report with charter, evidence, classifications, gaps, routing, and next steps.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=08a1951817ca5fe757b495d9111ebbfc5dd129602b8ef99c3ec8cdfa1911026f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline reported DNS blockage and listed intended follow-up checks, but provided no charter, structured evidence report, or explicit execution-routing details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore QA connectivity and record the browser/platform version, then rerun the five-minute charter.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3` from `agents/qa/test/exploratory-tester/evals/workspace/eval-2-explore-with-custom-duration`.
- Fixture SHA-256: `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3`
- Prompt SHA-256: `95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2bfbb6ecc0134ec5f9998274cdf0307f307da434e743767837778ac154a53a86`
- Skill overlay SHA-256: `d11214369d847e3bf37c4f57b3d2f711860c3796c879f82ec5e4e0b0da64ec70`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `234873760fb9d0649d16f54118fbf0383fa2955b9451730f9429892d78a6d7e0`
- Metadata SHA-256: `4befffc2e8037477b9995f3ded3869d8476cd9a66637621d7f8e8d3fc8c6fed3`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 记录了目标 URL、5 分钟时限、feature-update 场景、改动面、覆盖章程、环境缺失项和未验证范围。 |
| `assertion_2` | PASS | with_skill 报告确认读取 TEST_SUITE、FLOW_INDEX 及历史 QA 状态，确认 feature-update；在无可复用 case/flow、未能启动 UI 的前提下，仅更新 FLOW_INDEX，并明确 live flow 确认后再新增 case/script。 |
| `version_entry_and_subagent` | PASS | with_skill 明确记录平台版本和执行入口缺失，因此在执行前 blocked；同时记录无 repo harness、浏览器 connector，未声称执行任何 TC。 |
| `assertion_3` | PASS | with_skill 将无确认缺陷、可疑但未确认信号和未覆盖区域分开记录，并明确 console/network 证据尚未探索。 |
| `assertion_4` | PASS | with_skill 提供了探索报告和 FLOW_INDEX evidence references，记录了 preflight、URL 尝试及阻塞原因，而非随机操作清单。 |
| `assertion_5` | PASS | with_skill 提供了阻塞风险、认证/版本/执行入口缺失等 notes，并给出恢复环境、提供账号和入口、补充证据及新增 case/script 的后续步骤。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=d9042be89f0e4d8646ce7491fdf15101d98b5222a0ebbace948361658ecf7b94; snapshot_sha256=008d00c463d002f948eba5f58fe667e523eb9cb85e3887583e111ed7bbc2803e
- Behavior: Performed documented preflight, identified the execution blocker, separated confirmed/unconfirmed/uncovered areas, created report evidence, and updated FLOW_INDEX without fabricating UI results.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=f097aef54cfa54b916f522b3e77eb54d06ec80b545a12650fbb4645b82e3bd9f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline reported DNS blocking and did not produce structured preflight, report references, or QA artifact updates.
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

# Eval Result: eval-002-explore-with-custom-duration

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`
- Test case: explore-with-custom-duration
- Workspace: `workspace/eval-2-explore-with-custom-duration`
- Natural user prompt:

> 对用户指定的目标应用进行 5 分钟探索测试，按探索章程验证 changed surface、相邻风险和证据分层

- Expected artifact: 5 分钟探索测试报告

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/exploratory-tester--eval-002-explore-with-custom-duration/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `309d7645fa902999f9cc011ad12d0dc566cf30afa564d27b0c546cf8e149fa0b`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 6 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>上下文驱动范围 | PASS | 最终快照中的 FLOW_INDEX.md 和阻塞报告包含目标 URL、5 分钟时长、changed surface、具体启发式、阻塞原因及未验证范围；transcript 记录了读取环境和改动面。 | FAIL | transcript/candidate 仅记录目标、改动面和风险，未形成完整探索章程，缺少明确的升级信号和未验证前提记录。 |
| `assertion_2`<br>独立探索确认 | PASS | transcript 在任何运行前读取 TEST_SUITE.md、FLOW_INDEX.md、PRD 和环境/改动信息；最终快照确认无 cases、scripts、results。阻塞后实际更新了 FLOW_INDEX.md，未创建 TC/script。 | PASS | transcript 读取了 TEST_SUITE.md、FLOW_INDEX.md、PRD、环境和改动面；最终快照确认没有可读的 cases/scripts/results，且未声称扩充用例。 |
| `version_entry_and_subagent`<br>版本、执行入口与 subagent | PASS | TEST_SUITE.md 明确平台版本缺失；transcript 及最终阻塞报告明确因此 blocked、未启动计时，并记录 repo harness → Chrome/browser connector → Playwright fallback 顺序及 subagent 执行约定。 | FAIL | 虽读取到版本缺失并执行 curl 探测，但 transcript/candidate 未确认规定的执行入口顺序、选择理由或默认 subagent 执行约定。 |
| `assertion_3`<br>异常分层 | PASS | 最终阻塞报告明确区分 Observed issues（None）、Suspicious but unconfirmed signals（toast 风险）和 Gaps not explored；transcript 证明未进行 UI/运行时操作。 | PASS | candidate 明确将 DNS/HTTP 000 作为 L0 环境证据，并区分文档证据与没有 UI/日志证据，未把未确认信号升级为缺陷。 |
| `assertion_4`<br>证据输出 | PASS | 最终阻塞报告包含实际覆盖路径（preflight only）、读取的 QA/PM/环境文件、目标 URL 和阻塞原因；transcript 还提供了实际读取命令及文件变更 trace。 | PASS | transcript 提供实际 rg/sed/curl 命令，candidate 给出目标 URL、DNS/HTTP 000 结果及 implementation/changed-surface.md 证据引用，不是随机操作清单。 |
| `assertion_5`<br>风险交接 | PASS | 最终阻塞报告包含具体风险 notes（toast 可能遮蔽校验错误）及三项重试/补齐版本、TRD、IMPLEMENTATION_PLAN 的下一步建议。 | PASS | candidate 记录保存/取消、未保存状态、账户联动和 toast 风险，并建议提供可解析地址或浏览器环境后重测。 |

## With-Skill Behavior

with_skill 完成了阻塞前置检查、章程、证据分层和风险交接；未伪造运行结果。最终快照确认 FLOW_INDEX 与阻塞报告确实落盘。

## Fresh Without-Skill Baseline

without_skill 未完成版本/执行入口/subagent 前置要求，但进行了可审计的环境探测；仅作为 baseline 对照。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 补充确切平台/浏览器版本及可达 QA 地址后重跑 5 分钟探索。
- 补齐或确认对应 TRD 与 IMPLEMENTATION_PLAN，并在发现可复用场景时生成匹配 TC/script。
- fixture-manifest.json 的五个初始 fixture 在两条 lane 中一致；with_skill 的 FLOW_INDEX 差异是已验证的运行后更新，非初始 fixture 差异。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
