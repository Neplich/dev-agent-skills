# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421` from `agents/qa/test/exploratory-tester/evals/workspace/eval-3-mapped-doc-exploration`.
- Fixture SHA-256: `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421`
- Prompt SHA-256: `d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- Skill overlay SHA-256: `f90efe8186969e2f5d6c26cc6d2a76589cb8efe0e7f9452cedf25227be4cf8e9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c4de00c65a5c492d58d182077c448786bbd54172790d4519f15e143439929064`
- Metadata SHA-256: `66549bc6a4cd28361d4fb0c300ac0600f32823bbce01dba9736725e4b2d843dd`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出提及变更映射和命中文档，但锁定证据无法证明文档读取顺序或是否遍历了整个 docs/site。 |
| `verifies_against_code` | PASS | 明确指出代码阈值为 10 分钟、文档为 15 分钟，并以代码值作为探索基准，将差异及其影响列为待验证问题。 |
| `treats_unverified_as_low_trust` | PASS | 明确记录 last_verified_version 为 unverified，采用代码事实而非文档值，并声明未进行实际 E2E 验证、执行时需通过测试 harness 或其他运行证据确认关键行为。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=21e80854c9dfe21777e916d294e0386f1ef835c88140240b1b827f9712ee34f3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 以代码阈值为基准，识别文档漂移和 unverified 状态，提出较完整的边界与运行验证章程，未宣称已执行 E2E 验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=47c637614785e6f69d0c32909c92f5604e514f5876a3d139d5e39ce31cb8e01a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 10 分钟代码阈值与 15 分钟文档差异，并提出边界探索；未提及文档未核证状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 执行测试或 E2E harness，以确认 10:00 边界、活动续期及超时后的请求行为。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421` from `agents/qa/test/exploratory-tester/evals/workspace/eval-3-mapped-doc-exploration`.
- Fixture SHA-256: `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421`
- Prompt SHA-256: `d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `afbb19ee49749967688f949ed21bb2386ea86b8301685fafced66b23325118ab`
- Skill overlay SHA-256: `253325aa58a969826ea6853544729e44f6b321de1621777385ced958992f1626`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c4de00c65a5c492d58d182077c448786bbd54172790d4519f15e143439929064`
- Metadata SHA-256: `66549bc6a4cd28361d4fb0c300ac0600f32823bbce01dba9736725e4b2d843dd`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill identifies the change-map requirement, uses the targeted checkout-session API document, and limits scope to necessary checkout-session context without traversing docs/site. |
| `verifies_against_code` | PASS | with_skill explicitly distinguishes code configuration of 10 minutes from the document’s 15 minutes, uses 10 minutes as the validation baseline, and treats the discrepancy as an issue affecting acceptance. |
| `treats_unverified_as_low_trust` | PASS | with_skill notes the relevant documents are unverified, uses code as the provisional implementation basis, and requires confirmation before formal acceptance. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=a92ea9802352333ef0bf5ac59ebb38991d92fccd9cb0786f60016cf46ae9d973; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes the task to exploratory testing, scopes exploration narrowly, verifies the code/document discrepancy, treats unverified documentation cautiously, and proposes prioritized timeout boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=ffd1dff5feb8ec50f3dde4505a540d64d083ab27996bb5b0e539517a94848daa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the 10-minute code threshold, the 15-minute documentation mismatch, and proposes relevant boundary exploration.
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
- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421` from `agents/qa/test/exploratory-tester/evals/workspace/eval-3-mapped-doc-exploration`.
- Fixture SHA-256: `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421`
- Prompt SHA-256: `d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2bfbb6ecc0134ec5f9998274cdf0307f307da434e743767837778ac154a53a86`
- Skill overlay SHA-256: `d11214369d847e3bf37c4f57b3d2f711860c3796c879f82ec5e4e0b0da64ec70`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c4de00c65a5c492d58d182077c448786bbd54172790d4519f15e143439929064`
- Metadata SHA-256: `66549bc6a4cd28361d4fb0c300ac0600f32823bbce01dba9736725e4b2d843dd`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | 输出围绕 change-map 命中的 docs/site/api/checkout-session.md 及必要的结账会话上下文设计探索，未显示遍历整个 docs/site。 |
| `verifies_against_code` | PASS | 明确以 src/checkout/session.rules 中的 10 分钟为真实阈值，指出正式说明仍为 15 分钟，并将 10 分钟前、恰好及超过边界列为重点验证。 |
| `treats_unverified_as_low_trust` | FAIL | 输出未提及文档或变更映射中的 last_verified_version: unverified，也未明确按最低信任处理或要求关键假设由代码或测试再次确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=d7b157c6ca862859bee98bc3ce9b0fe2a5dea969912e20fa57e52f6ec88bd5d6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别代码与文档的 10/15 分钟差异，并提供了较完整的最小探索章程，但遗漏了对 unverified 信任级别的处理。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=c240e72e90c1c3496982a5d380500b175a38681116f2043a282918266a323c97; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 核对了代码、文档和变更映射，并设计了围绕 10 分钟的边界探索；明确提及 unverified。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足 treats_unverified_as_low_trust。
- Next: 明确记录 last_verified_version: unverified 为最低信任，并要求关键探索假设由代码或测试再次确认。

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

# Eval Result: eval-003-mapped-doc-exploration

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`
- Test case: mapped-doc-exploration
- Workspace: `workspace/eval-3-mapped-doc-exploration`
- Natural user prompt:

> 围绕 src/checkout/session.rules 的结账会话超时行为制定最小探索章程，并指出应重点验证的边界。

- Expected artifact: 以映射文档定位、代码事实核证的探索章程和风险记录。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/exploratory-tester--eval-003-mapped-doc-exploration/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `df8fd85df6e085de7b81dd75f9024f74dbb28600bd3bdebc72a765cb13a763a9`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 3 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>先消费命中的结账会话文档 | PASS | transcript 显示先定位规则，随后读取 change-map，并在同一命令中读取其命中的 docs/site/api/checkout-session.md；最终仅有三份 fixture 文件，没有遍历整个 docs/site。 | FAIL | transcript 顺序为先读规则、再做全局 rg，最后在同一命令中先读取 checkout-session.md、后读取 change-map，未体现命中 change-map 后优先消费文档。 |
| `verifies_against_code`<br>探索边界以代码事实为准 | PASS | tool trace 两次读取 src/checkout/session.rules，最终内容为 session_timeout_minutes = 10；candidate 明确指出文档写 15 分钟，并将差异及其对时间边界、配置一致性的影响列为风险，而非直接采用文档值。 | PASS | transcript 读取并核对规则文件和文档；candidate 明确区分代码 10 分钟与文档 15 分钟，并要求将该差异作为待验证风险。 |
| `treats_unverified_as_low_trust`<br>未核证文档不作为确认事实 | PASS | 最终快照和 transcript 均显示 change-map 与 API 文档的 last_verified_version 为 unverified；candidate 不把文档值当作事实，采用代码的 10 分钟作为当前配置事实，并明确尚未执行、需用时间控制/测试再次验证行为。 | PASS | transcript 读取到两处 last_verified_version: unverified；candidate 将文档声明列为需验证的不一致项，并把实际行为、规则文件和文档一致性作为验证标准，没有据未核证文档直接下结论。 |

## With-Skill Behavior

with_skill 三项断言均有 transcript、tool trace、candidate 与最终快照支持；未发生实际探索执行，因此没有把候选的计划误判为执行结果。两条 lane 的 fixture 快照一致。

## Fresh Without-Skill Baseline

without_skill 作为 baseline：也核证了代码与文档差异，但未遵循 change-map 命中后的优先文档读取顺序。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 执行章程中的 9:59、10:00、10:01、活动续期、过期提交及并发边界测试。
- 修正文档中的 15 分钟声明，或确认代码配置应改为产品契约值，并更新验证版本。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
