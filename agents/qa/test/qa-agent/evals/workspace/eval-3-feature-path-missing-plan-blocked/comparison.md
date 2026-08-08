# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc` from `agents/qa/test/qa-agent/evals/workspace/eval-3-feature-path-missing-plan-blocked`.
- Fixture SHA-256: `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc`
- Prompt SHA-256: `094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bf605f953dcf46f19d2e331c4596d99cf4c0c84b7fc1582467970e0cc18f8ccd`
- Skill overlay SHA-256: `61d94a4bf111e70ade2232cb9d882f35a6012c6ae7909aa0b8f48602aadf3860`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ffa490cd1f58367914b109adc50e94706c92cbf66e7c95942ae329d3f9a191c7`
- Metadata SHA-256: `aa798ca118679678c2fef882d4726badd357a387202dcb387aceaa4b86696bd0`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_same_feature_path` | PASS | with_skill 明确识别 `account/profile/preferences`，指出同路径 PRD/TRD 均为 Confirmed，并保留现有 QA E2E 目录；workspace_manifest 也确认四个同路径材料未被修改。 |
| `specialist_gate_pointer` | PASS | with_skill 选择 `spec-based-tester` 作为后续 E2E 验证责任方，明确缺少 `IMPLEMENTATION_PLAN.md`、测试平台和运行环境，因此当前不能执行；git_status 和 git_diff 均为空，未创建、更新或运行 E2E 资产。 |
| `keeps_single_route` | PASS | with_skill 选择单一的 `spec-based-tester` QA 路由，并将实施计划补齐描述为前置阻塞条件；没有并行调用多个 QA skill，也没有执行实现修复或 specialist 协议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=29631206d05f125703591d3a877ffa27deb83f8776294e7762198ec65e651d8b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 feature path，选择 spec-based-tester，指出实施计划及运行条件缺失并在门禁处停止，未产生工作区变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=61ddf52d3adb7bb2748b5e27c806091ff323264a404b2f071cbfa83218af8605; snapshot_sha256=03a49eca18df71c5a3109d7b519c3a457f88e2b8f30796f92d4914206ce774ab
- Behavior: 识别材料不足和 E2E 无法执行，但修改了 QA 测试套件与流程索引，未体现 specialist 门禁和单一路由。
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

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc` from `agents/qa/test/qa-agent/evals/workspace/eval-3-feature-path-missing-plan-blocked`.
- Fixture SHA-256: `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc`
- Prompt SHA-256: `094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a20bd075e7e1649c2f9f1462392950229b31be9ed570a4e240d839bf872da003`
- Skill overlay SHA-256: `46ffa1a74f0eaa93e8e4995713b7c67a998b633e4325098596292dae49b6afe3`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `850613bb7e4be55053e2a4ef8d2c3adf6cfe9e1ff2df8dc4182acbf3737eb282`
- Metadata SHA-256: `aa798ca118679678c2fef882d4726badd357a387202dcb387aceaa4b86696bd0`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_same_feature_path` | PASS | with_skill 明确使用 feature_path `account/profile/preferences`，指出同路径 PRD/TRD，并引用同路径 QA E2E 目录中的 TEST_SUITE.md 与 FLOW_INDEX.md。 |
| `specialist_gate_pointer` | FAIL | 虽声明选择 `spec-based-tester` 并提及 QA memory、平台版本、执行入口、PRD/TRD、IMPLEMENTATION_PLAN 和账号信息，但明确展开了 IMPLEMENTATION_PLAN 缺失导致硬门禁阻塞及后续补充协议，违反不得复述缺计划阻塞/交接/执行协议的要求。 |
| `keeps_single_route` | PASS | with_skill 选择单一且最窄的 `spec-based-tester` 路由，未并行调用多个 QA skill，也未进入实现修复。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=d29c948d3648a8f9c1dcb9fbd09000e118005522297851da03e9113d397b8eb2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择了单一 spec-based-tester 路由并正确识别同路径材料，但展开复述了缺少 implementation plan 的阻塞及后续执行前置条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=2c0dc6f9f83e4e7c449ebed981b22d6263ba62abc340eb70cf39e57284443ea0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了正确的功能承接范围和材料不足，但未声明 specialist 或其权威门禁指针。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- specialist_gate_pointer：with_skill 输出展开了缺计划后的硬门禁阻塞和后续补充/执行协议。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc` from `agents/qa/test/qa-agent/evals/workspace/eval-3-feature-path-missing-plan-blocked`.
- Fixture SHA-256: `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc`
- Prompt SHA-256: `094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fce4a3d76c9b69c96fdd86c3a44479dd8a12dd392536b124aa25210a7efca146`
- Skill overlay SHA-256: `5682fc1ffcb4eb879c1789588b290db4ff6dc8f83dc85473fb6c12c8ad0ebd72`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `850613bb7e4be55053e2a4ef8d2c3adf6cfe9e1ff2df8dc4182acbf3737eb282`
- Metadata SHA-256: `aa798ca118679678c2fef882d4726badd357a387202dcb387aceaa4b86696bd0`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_same_feature_path` | PASS | With-skill output identifies spec-based testing, confirms same-path PRD/TRD, and references the existing QA directory. |
| `specialist_gate_pointer` | FAIL | It names spec-based-tester and notes missing implementation plan, platform version, and executable entry, but does not point to the specialist's authoritative E2E memory, credentials, execution entry, or the full blocked-condition gate. |
| `keeps_single_route` | PASS | It selects only the spec-based-tester route and stops at the prerequisite-material gate without parallel QA routes, implementation, or execution. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=f4c9b8cd6772b3db0d10f6d0b3d2d0ee09d96aa07e3f79d6ba3b99c0e32f8490; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Selected spec-based-tester, stopped on missing prerequisites, and made no workspace changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=70fc838a64c6c8c386b1b1bafd340742272f4e27517582522f915bca8dffbe84; snapshot_sha256=9976230027181bcc2ab0f189b210380e823d9f729a4cdcee71080d47af5254c3
- Behavior: Expanded the QA suite and flow index, attempted execution, and reported three blocked cases.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill route omits required specialist authority and gate pointers.
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

# Eval Result: eval-003-feature-path-missing-plan-blocked

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`
- Test case: feature-path-missing-plan-blocked
- Workspace: `workspace/eval-3-feature-path-missing-plan-blocked`
- Natural user prompt:

> 用户说：account/profile/preferences 已经开发完成，请基于 docs/pm/account/profile/preferences/PRD.md 和 docs/engineer/account/profile/preferences/TRD.md 更新并执行 E2E 验收。docs/qa/e2e/account/profile/preferences/ 目录也存在。

- Expected artifact: QA 路由决策必须识别 feature_path account/profile/preferences，读取同路径 PRD/TRD 和 QA 功能树，但因为缺少 docs/engineer/account/profile/preferences/IMPLEMENTATION_PLAN.md 而 blocked，不创建、更新或执行 E2E acceptance TC

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/qa-agent--eval-003-feature-path-missing-plan-blocked/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `dc46f6e9c1ab17c986802148894541b71552a8bbd96ec33756b90f15b25e1a45`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 2 / FAIL 1 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_same_feature_path`<br>同路径上下文 | PASS | transcript item_2 明确将请求归类为基于 PRD/TRD 的文档化 E2E 验收；item_1/3/5 读取同路径 PRD、TRD、FLOW_INDEX、TEST_SUITE，并确认 feature_path 为 account/profile/preferences。最终快照保留四个同路径文件。 | PASS | transcript item_1/2 读取同路径 PRD、TRD、FLOW_INDEX、TEST_SUITE；快照保留相同四个文件，PRD/TRD 中的 feature_path 与 QA 路径均一致。 |
| `specialist_gate_pointer`<br>Specialist 权威门禁指针 | FAIL | 虽然 transcript item_2 和最终 candidate.md 选择了 spec-based-tester，但输出没有完整声明该 specialist 的权威 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 门禁适用；并且 item_6/candidate.md 详细展开了缺少 IMPLEMENTATION_PLAN、禁止创建/更新/执行 TC、技能缺失等阻塞与交接协议。断言明确规定展开复述即 FAIL。 | FAIL | candidate.md 未声明选中的 specialist，也未提供 required gate pointer；仅说明缺少 IMPLEMENTATION_PLAN 并复述阻塞条件。该无条件路由输出要求缺失，判 FAIL。 |
| `keeps_single_route`<br>单一路由 | PASS | transcript item_2 只选择一个最窄 route：spec-based-tester；没有并行调用多个 QA skill、执行 specialist 协议、修改实现或修复代码。item_1/3/5 仅为文档读取和缺失文件检查。 | FAIL | transcript 与 candidate.md 没有选择明确的 QA route/specialist；仅停止于前置文件检查。因此未满足必须选择一个最窄 QA route 的无条件要求。 |

## With-Skill Behavior

with_skill 正确识别并读取同路径 PRD/TRD 与 QA 功能树，选择 spec-based-tester，且最终快照无写入、无执行产物；但路由输出复述了缺少 implementation plan、阻塞和交接协议，违反 specialist gate pointer。

## Fresh Without-Skill Baseline

without_skill 的 fixture 与最终快照和 with_skill 完全一致，也未写入或执行 E2E；但未完成 specialist 路由指针输出，且未明确选择唯一 QA route，仅作 baseline 对照。

## Failures

- with_skill 的 specialist_gate_pointer 失败：路由输出缺失完整权威门禁指针，并展开复述了 blocked-condition、交接和执行阻塞协议。
- without_skill 的 specialist_gate_pointer 与 keeps_single_route 均失败；这是 baseline 对照，不改变当前 with_skill 结果。

## Not Exercised

- 无。

## Next Steps

- 补齐并确认 docs/engineer/account/profile/preferences/IMPLEMENTATION_PLAN.md 后，重新运行该 QA 路由评估。
- 修正 qa-agent 输出：只声明 spec-based-tester 及其权威门禁适用，不在 router 层复述 specialist 的阻塞、交接或执行协议。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
