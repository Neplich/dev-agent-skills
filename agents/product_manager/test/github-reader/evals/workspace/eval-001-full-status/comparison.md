# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56` from `agents/product_manager/test/github-reader/evals/workspace/eval-001-full-status`.
- Fixture SHA-256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- Prompt SHA-256: `01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `cbc27cddf5543ee4c60ccd8f54bf10c1ec8b7799d5c9eb603008973679be6d9f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a688cc91089931e5821e56e4470a0bc8844e7a9c13d1b4c5bcc8d2e3929da0ce`
- Metadata SHA-256: `94b279ac62424134e6355f46df23e4185fa4034dd04349372cf9178ca3c8c29f`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `milestone` | PASS | With-skill 输出包含带标题和百分比的 Milestone 进度表。 |
| `pr` | PASS | With-skill 输出区分待 Review、需作者跟进、草稿，并单列近 14 天已合并 PR。 |
| `assertion_3` | PASS | 输出末尾包含数字化健康摘要，涵盖 open issue、open PR、里程碑进度及近期活动。 |
| `pr_2` | PASS | PR 条目使用了 [#NUMBER](GitHub URL) 格式。 |
| `data_completeness` | PASS | 输出声明数字来自快照中的 GitHub Search total_count、查询结果完整且非实时；该声明与 raw evidence 中 incomplete_results=false、milestones_complete=true 一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=3daa2b9f7470bd0cc0972ffbfd2a915833e7693b6a1dc4e53c2de7abedc952e7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整呈现里程碑进度、issue 分类、PR 队列与合并情况、数据时点、链接和数字化健康摘要。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=7faa567ce0e1a072b5e9c8f86ca251ef2bcbaa82b2a6d81feea873f3844ee30b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 包含里程碑、open issue 和 PR 信息，但缺少 GitHub PR 链接、健康摘要及明确的数据完整性声明。
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

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56` from `agents/product_manager/test/github-reader/evals/workspace/eval-001-full-status`.
- Fixture SHA-256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- Prompt SHA-256: `01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6e29f2b22f72bb9078ec886f3bf0d4599e102bac697619f52f799318f68df6c7`
- Skill overlay SHA-256: `08b4455eaa3f2baaf8b11c20e163fe95beeff153e05846e54d69f650a80acb16`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a688cc91089931e5821e56e4470a0bc8844e7a9c13d1b4c5bcc8d2e3929da0ce`
- Metadata SHA-256: `94b279ac62424134e6355f46df23e4185fa4034dd04349372cf9178ca3c8c29f`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `milestone` | PASS | With-skill 输出包含带标题和进度百分比的 Milestone 表格。 |
| `pr` | PASS | With-skill 输出区分待 Review、需作者跟进、草稿及近 14 天已合并的 PR。 |
| `assertion_3` | PASS | 末尾“总结”包含数字化健康摘要：4 个 open issue、3 个 open PR、1 个待 review、1 个需修改等。 |
| `pr_2` | PASS | PR 条目均使用 [#NUMBER](GitHub URL) 格式。 |
| `data_completeness` | PASS | 输出声明快照搜索结果完整且未标记 incomplete_results，给出各集合总数，并显式说明 milestone 汇总与全局 issue 总数的 1 个差异及采用的原始 total_count。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=1b7513c3723717aa9db4892171d0fcc4874094bacd336bcd7b2683561c73c3b9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整整理数据时点、Milestone 进度、open issue、PR 队列、合并情况、健康摘要和数据完整性说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=04051d8b3982cefb874341ff534a854908c841ec159f1f9b8fdac71387d395fb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 包含 Milestone、open issue 和 PR 信息，但未提供 PR GitHub 链接、末尾数字化健康摘要或明确的完整性声明。
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

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/github-reader/evals/workspace/eval-001-full-status`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `1493e8ad45559bbc5b4bea241fbc6897a1fd400094ebebd9e530360f72c03906`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `254cc92cf58649aa2c5bb2447fe35aa135bdc944368afe7a7cc119c6e2735ba1`
- Skill overlay SHA-256: `86a7dea13dce1a60e9d0c4442e983c46d3a33318b7a112994f13359d56bd6e12`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5118c2b783b26288410de500b4b1953d713b7a3bd8b126ea94bcd4d729f93e60`
- Metadata SHA-256: `c0371765feed3291a029ddfa0b1a8e14c63074210c329b26ba8af6b5faba5b6c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `milestone` | FAIL | With-skill output has Milestone headings and counts, but no progress table or percentage. |
| `pr` | FAIL | It has a PR queue section and open/closed totals, but does not distinguish pending review from merged PRs. |
| `assertion_3` | PASS | The ending summary includes numeric figures: 143 open PRs and 53 open issues. |
| `pr_2` | FAIL | No individual PR entries use the required [#NUMBER](URL) format; only a general Pull requests link is provided. |
| `data_completeness` | PASS | The output attributes counts to the current pages and explicitly states that review-status categories cannot be reliably split, avoiding unsupported complete category counts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1493e8ad45559bbc5b4bea241fbc6897a1fd400094ebebd9e530360f72c03906; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=05717a1ed7d5718e98f6313149e1ae8a32bce73fbbbb98d82875ffc4a961dffd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Adds structured headings, source links, numeric summary, and a caveat about unavailable PR review decisions, but still lacks the required milestone table, review/merged distinction, and individual PR links.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1493e8ad45559bbc5b4bea241fbc6897a1fd400094ebebd9e530360f72c03906; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=bb150efc4f1378ae0520682529202f7feee1aa37d28fc6293fd79d8cde7a27b9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reports milestone, issue, and PR counts, but lacks the required milestone table, review/merged PR distinction, individual PR links, numeric ending summary, and explicit completeness caveat.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- milestone
- pr
- pr_2
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

# Eval Result: eval-001-full-status

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`
- Test case: `full-status`
- Prompt:

> 帮我看一下 anthropics/anthropic-sdk-python 现在的项目状态，包括 milestone 进度、open issue 数量和 PR 队列情况

- Expected output:

> 结构化的项目状态报告，包含 Milestone 进度表、Open Issues 分组、PR 队列（待 review / 草稿 / 近期合并），以及健康摘要

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`（0 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- Overall result: PASS (partial coverage)
- With-skill summary: with_skill 实际加载 github-reader（status.json 的 skill_load_hits=2，transcript 中完整读取 SKILL.md），按要求先执行仓库上下文查询；GitHub CLI 因未认证失败，随后如实报告无法读取并未伪造项目数据。快照前后仅有 fixture-manifest.json 且哈希不变，无写入。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-reader（status.json 的 skill_load_hits=2，transcript 中完整读取 SKILL.md），按要求先执行仓库上下文查询；GitHub CLI 因未认证失败，随后如实报告无法读取并未伪造项目数据。快照前后仅有 fixture-manifest.json 且哈希不变，无写入。

## Without-Skill Baseline

without_skill 仅作对照：尝试网页/API 查询后输出了项目数字，但未提供完整的 milestone 表、PR 分类队列或数字化健康摘要。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `milestone` | **NOT EXERCISED** | 所需实时 milestone 数据不可用：with_skill transcript 中 gh repo view 因未认证以 exit_code=4 失败，candidate 明确说明无法读取仓库状态，因此不能判定 milestone 表格要求。 | without_skill 声称无 milestone，但未输出带进度百分比的 Milestone 表格。 |
| `pr` | **NOT EXERCISED** | 所需实时 PR 队列数据不可用：with_skill 在仓库上下文认证失败后未能继续获取 PR 数据，candidate 明确要求先 gh auth login，因此不能判定 PR 分类要求。 | without_skill 仅给出 open/closed PR 数字和概述，未区分待 review、草稿及已合并队列。 |
| `assertion_3` | **NOT EXERCISED** | 健康摘要依赖实时 issue、PR、milestone 及近期活动数据；with_skill 因 GitHub CLI 未认证无法获取这些集合，candidate 未伪造摘要。 | without_skill 有文字性整体判断，但没有输出末尾数字化健康摘要。 |
| `pr_2` | **NOT EXERCISED** | with_skill 未获得任何 PR 条目，故无法验证 PR 条目的 [#NUMBER](URL) 格式；这是认证导致的实时数据不可用。 | without_skill 的 PR 相关内容没有 PR 条目链接可供核验。 |
| `data_completeness` | **NOT EXERCISED** | 各集合总数与分类统计所需的实时 GitHub 查询不可用；with_skill 如实报告无法读取，没有声称部分数据完整，因此该数据完整性断言不具备可执行覆盖。 | without_skill 仅对 open_issues_count 的 issue+PR 混合口径作了说明，但未提供各集合总数与分类统计的数据基础声明。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- milestone
- pr
- assertion_3
- pr_2
- data_completeness

## Next Steps

- 在 GitHub CLI 认证可用后重新运行 with_skill，以覆盖实时数据相关断言。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `32.257s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `71.423s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `62.277s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
