# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-005-feed-mode-completeness`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56` from `agents/product_manager/test/github-reader/evals/workspace/eval-005-feed-mode-completeness`.
- Fixture SHA-256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- Prompt SHA-256: `733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `cbc27cddf5543ee4c60ccd8f54bf10c1ec8b7799d5c9eb603008973679be6d9f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c049e8ab5f946f319bc21927957f6fda02a148471bd8950bd306a941a14167f6`
- Metadata SHA-256: `07ab98c6d1c3adcc9277e1cfe784f8d017e9650890973540f2c3871622f64ed2`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feed_yaml_present` | PASS | with_skill 输出在 Markdown 报告后包含 github_reader_data YAML 块，并提供 open_issues_total 等关键字段。 |
| `completeness_signals_consistent` | FAIL | YAML 声明 snapshot_complete=true、truncated_collections和incomplete_totals为空，报告也声称未发现截断；但原始快照显示里程碑开放 issue 总数为5而全局总数为4，且 v0.81 声称3个开放 issue却仅有1条明细，未反映该完整性矛盾。 |
| `totals_not_fabricated` | NOT_EXERCISED | 输出总数与原始 search.total_count 一致，但锁定证据无法证明这些总数实际取自 search.total_count 而非集合长度。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=1bd97ecf45fdb5c06b5541beaa5ddc8012ff6c3006ba66f3a6b5c201d95b86ad; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了 Markdown 报告和 github_reader_data YAML，但错误地将快照标为完整且未反映里程碑计数与明细的不一致。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=464a9f48b0a89f088d6f5c8c98edb4df177a6ef0ecba371fad65138b2e12e9d8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未提供 Feed mode YAML；提供了 JSON 状态输入，并明确指出里程碑与全局开放 issue 数量存在完整性矛盾。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出的完整性信号与原始快照中的跨区段不一致相矛盾。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-005-feed-mode-completeness`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56` from `agents/product_manager/test/github-reader/evals/workspace/eval-005-feed-mode-completeness`.
- Fixture SHA-256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- Prompt SHA-256: `733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6e29f2b22f72bb9078ec886f3bf0d4599e102bac697619f52f799318f68df6c7`
- Skill overlay SHA-256: `08b4455eaa3f2baaf8b11c20e163fe95beeff153e05846e54d69f650a80acb16`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c049e8ab5f946f319bc21927957f6fda02a148471bd8950bd306a941a14167f6`
- Metadata SHA-256: `07ab98c6d1c3adcc9277e1cfe784f8d017e9650890973540f2c3871622f64ed2`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feed_yaml_present` | PASS | with_skill 输出在 Markdown 报告后包含 github_reader_data YAML 块，并提供 open_issues_total 等关键字段。 |
| `completeness_signals_consistent` | PASS | 报告声明搜索结果完整且未截断；YAML 的 incomplete_results、fetched、truncated_collections 和 incomplete_totals 与该声明一致，并注明 closed issue 仅有 numbers-only 详情。 |
| `totals_not_fabricated` | PASS | YAML 的总数与原始快照 search.total_count 一致，且 query_evidence 明确记录了各查询的 total_count 与 fetched 数量。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=99e822525c67031b2a9f924e76633df0bf3220b5939ba286b55d858157603867; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 输出了带完整性声明、查询证据和总数来源的 Markdown 报告及 github_reader_data YAML 块。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=733e42077f632553b5cf8048118a1b14f8ea055ecbaf96d2e6e26af0ff51b1b5; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=370267ca74ece9ac92664fcd9253c8c0687846fcc23fb452f73ce08c47a73be6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 输出了结构化 JSON，但没有 Markdown 报告后的 github_reader_data YAML feed 数据块。
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
- Eval: `eval-005-feed-mode-completeness`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/github-reader/evals/workspace/eval-005-feed-mode-completeness`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `029745af57e009404f9c7ceebcc74f54e570d04bee88bfaccd1c5fa34abc8793`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `254cc92cf58649aa2c5bb2447fe35aa135bdc944368afe7a7cc119c6e2735ba1`
- Skill overlay SHA-256: `86a7dea13dce1a60e9d0c4442e983c46d3a33318b7a112994f13359d56bd6e12`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e28759533157a8d0a4167f2385fb8f224c61db6a311a631c34e3ba38a30119a`
- Metadata SHA-256: `e37defd1d9cdbecb372a4632260b266e4fd3099ba90c3045a70d2c0415f1fb58`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feed_yaml_present` | FAIL | With_skill 输出包含 YAML 代码块，但块顶层键为 `repository_status`，未提供要求的 `github_reader_data` YAML 块。 |
| `completeness_signals_consistent` | PASS | 报告中的 Open Issues、Open Pull Requests、Closed Pull Requests 和 Milestones 数值分别与 YAML 中的 53、143、1085 和 0 一致；未声明截断或不完整，因此无需 `truncated_collections` 或 `incomplete_totals`。 |
| `totals_not_fabricated` | FAIL | With_skill 输出未提供实际搜索查询的 `total_count` 原始证据，也未将总数明确追溯到 search `total_count`；仅声称数据来自 GitHub 页面/API 元数据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=029745af57e009404f9c7ceebcc74f54e570d04bee88bfaccd1c5fa34abc8793; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=55be29e3b76302c3dea62187770c6c4ac83e61b24f8a94faa4b4b9d5389b25f9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了 Markdown 报告及 YAML 状态块，报告与 YAML 的主要总数一致，但块名称不符合要求，且缺少 search `total_count` 原始证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=029745af57e009404f9c7ceebcc74f54e570d04bee88bfaccd1c5fa34abc8793; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=861c3a83294f9a6efeec34a9d47c129112d28b72ed65fbd25936f3dba0ea02b2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了 JSON 状态数据，但没有要求的 Feed mode YAML 块，且未提供 search `total_count` 证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 缺少顶层 `github_reader_data` YAML 块。
- 总数缺少实际查询 search `total_count` 原始证据。
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

# Eval Result: eval-005-feed-mode-completeness

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-005-feed-mode-completeness`
- Test case: `feed-mode-completeness`
- Prompt:

> 我是 roadmap-gen，需要 anthropics/anthropic-sdk-python 的当前仓库状态作为结构化输入，请给我完整状态数据

- Expected output:

> Markdown 报告后附 `---` 分隔的 `github_reader_data` YAML 块，包含总数类字段；若报告声明了截断或总数不完整，YAML 必须有对应 `truncated_collections` / `incomplete_totals` 字段

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
- With-skill summary: with_skill 实际加载了 github-reader（status.json 的 skill_load_hits=2，transcript 中读取 SKILL.md），随后按技能先尝试仓库查询并检查认证；gh 未认证，未获得实时 GitHub 数据，因此诚实报告阻塞且未伪造 Feed YAML。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载了 github-reader（status.json 的 skill_load_hits=2，transcript 中读取 SKILL.md），随后按技能先尝试仓库查询并检查认证；gh 未认证，未获得实时 GitHub 数据，因此诚实报告阻塞且未伪造 Feed YAML。

## Without-Skill Baseline

without_skill 未加载技能（skill_load_hits=0），输出了另一套 GitHub connector JSON；仅作 baseline 对照，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `feed_yaml_present` | **NOT EXERCISED** | with_skill 的 transcript 显示 gh repo view 因未认证失败，gh auth status 也失败；candidate.md 明确报告无法获取当前状态，因此没有可供判断的实时 Feed 数据或 YAML。 | without_skill 输出了 JSON 快照，没有 Markdown 报告后的 github_reader_data YAML 块。 |
| `completeness_signals_consistent` | **NOT EXERCISED** | 实时仓库集合不可用，且 transcript 没有成功返回查询集合或总数；无法判断 YAML 总数与截断/不完整声明的一致性。 | without_skill 输出 retrieved=100 等集合长度，但未提供 Feed 完整性字段，不能作为 with_skill 结论依据。 |
| `totals_not_fabricated` | **NOT EXERCISED** | 因 GitHub CLI 未认证，with_skill 未获得可用于核验的 search total_count；candidate.md 也未伪造任何总数。 | without_skill 的 JSON 使用 retrieved=100 等字段，未展示 search total_count；仅作对照。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- feed_yaml_present：GitHub 认证不可用，实时 Feed 数据未获取。
- completeness_signals_consistent：没有成功的实时集合/总数可核对。
- totals_not_fabricated：没有成功的 search total_count 可核对。

## Next Steps

- 认证 GitHub CLI 后重跑，以覆盖 Feed YAML、完整性信号和 total_count 三条 assertion。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `35.141s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `150.115s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `51.306s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
