# Eval Result: eval-002-single-version-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-002-single-version-mode`
- Test case: single-version-mode
- Workspace: `workspace/eval-002-single-version-mode`
- Classification: `(c)` 依赖实时 GitHub 数据。该场景必须读取目标仓库当时的 release、tag compare、merged PR 和 PR body；静态 mock 不能替代真实复验。
- Latest result: PARTIAL - 2026-07-26 的 fresh `with_skill` / `without_skill` 已用两次独立实时查询成对完成；4 条 assertions 通过，`pr_conventional_commit` 因版本窗口内只有应过滤的 bot release PR 而没有可执行的普通 PR 标题样本。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0。
- Fixture: 仅包含 eval metadata；不新增静态 GitHub 快照。
- Expected output: 生成最新 release tag 的版本块，格式为 `## [x.y.z] - YYYY-MM-DD`，包含该版本窗口内的 PR，分组写入，每条带 PR 链接，并写入 `docs/changelog/changelog-v{version}.md`。
- Fresh pair: `with_skill` 与 `without_skill` 分别实时查询 GitHub，没有复用历史 baseline，也没有把父进程候选或预计算 snapshot 传给 baseline。

## No-Leak Execution

- `with_skill` 生成前只读取本用例 `eval_metadata.json` 的原始 prompt，随后读取 Product Manager README 与 `changelog-generator/SKILL.md`，未读取 `evals.json`、assertions、expected output 或旧 comparison。
- `with_skill` 候选和 live snapshot 锁定后，才启动 `fork_turns=none` 的 fresh baseline。
- baseline 只收到原始 prompt；未获得 specialist skill、Agent README、assertions、expected output、旧 comparison、父进程候选或父进程 snapshot。
- baseline 自行调用 `gh` 重新查询 release、PR 时间窗、tag compare 和 commit-to-PR 关联；其候选锁定后才读取 assertions 与旧 comparison 进行 fresh judge。
- 两次查询结果独立一致，不代表把同一预计算答案作为两条运行路径的输入。

## Independent Live Data Snapshots

### With Skill

- 抓取时间：2026-07-26 15:37:52-15:38:30 `+08:00`（Asia/Shanghai）。
- 仓库：`anthropics/anthropic-sdk-python`，默认分支 `main`。
- 最新 release：`v0.120.0`，发布时间 `2026-07-24T16:32:34Z`。
- 前一 release：`v0.119.0`，发布时间 `2026-07-23T17:34:23Z`。
- PR 窗口：`(2026-07-23T17:34:23Z, 2026-07-24T16:32:34Z]`。
- 窗口内 merged PR：仅 [#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780)，`release: 0.120.0`，合并于 `2026-07-24T16:31:59Z`。
- Tag compare：[`v0.119.0...v0.120.0`](https://github.com/anthropics/anthropic-sdk-python/compare/v0.119.0...v0.120.0) 为 `ahead_by: 2`；功能提交包含 3 条 `feat(api):` 变化，另一个为 release commit。
- PR body 与 GitHub Release body 都列出同样 3 条 API 功能，没有 `!` 或 `BREAKING CHANGE:` 标记。

### Without Skill

- 抓取时间：2026-07-26 15:39:44 `+08:00`（Asia/Shanghai）。
- baseline 独立确认最新 release `v0.120.0`、前一 release `v0.119.0` 及相同精确发布时间。
- baseline 独立查询相同窗口，确认唯一 merged PR 为 #1780。
- baseline 独立查询 tag compare，确认 `ahead_by: 2`、功能提交 `70c0a64581e7` 与发布提交 `60c64fba5c2b`。
- baseline 额外通过 commit-to-PR 关联确认两个 tag 间提交都只关联 #1780，因此完整 PR 引用集合没有遗漏。

## Assertions

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `x_y_z_yyyy_mm_dd` | PASS | PASS | 两者均生成 `## [0.120.0] - 2026-07-24`。 |
| `release_tag` | PASS | PASS | 两者均以实时最新 tag `v0.120.0` 为来源，并在版本块中使用 `0.120.0`。 |
| `pr_conventional_commit` | NOT EXERCISED | NOT EXERCISED | #1780 是 `stainless-app[bot]` 的 release PR，按 skill 规则应过滤。PR body / release body 中的 3 条 `feat(api):` 内容和 tag compare commit 可用于理解版本变化，但不能冒充普通 PR 标题清洗证据。 |
| `breaking_change_breaking` | PASS | PASS | 当前 PR body、release body 和 tag compare 均无 breaking marker；条件未触发，两者都未虚构 `⚠️ BREAKING:`。 |
| `section` | PASS | PASS | 两者只输出有内容的 `Added`，没有生成空 section。 |

## With Skill

Observed behavior:

- 按 specialist 流程用 `gh` 确认目标仓库、最新和前一 release，并用精确发布时间建立单版本窗口。
- 查询窗口内 merged PR，识别 #1780 为 bot release PR 并按规则从普通 PR 条目候选中排除；再用 tag compare、PR body 和 release body核对 SDK generator 仓库的真实变化。
- 可从 tag compare / release 内容整理 3 条 API 功能变化，但这些不是普通 PR title 样本，不能据此把 `pr_conventional_commit` 判为 PASS。
- 生成 `## [0.120.0] - 2026-07-24`，只包含非空 `### Added`，目标路径为 `docs/changelog/changelog-v0.120.0.md`。
- 未把候选 changelog 写入 eval fixture；本轮只持久化 fresh judge 摘要。

Candidate behavior summary:

```markdown
# Changelog - v0.120.0

## [0.120.0] - 2026-07-24

### Added

- **api:** Add claude-opus-5 model ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
- **api:** Add tool addition/removal blocks and tool_change events ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
- **api:** Expand client-side fallback credit token types and add server-side fallbacks default option ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
```

## Without Skill / Baseline

Observed behavior:

- 在 `fork_turns=none` 子进程中仅按原始 prompt 独立查询 GitHub，没有读取或应用 specialist skill、Agent README 或任何 eval answer key。
- 独立选中 `v0.120.0`，建立正确 release 窗口，并用 PR、tag compare 与 commit-to-PR 关联交叉验证 #1780 是完整 PR 集合。
- 同样可从 release 内容整理 `Added` section，但把 body / commit 文本清洗后链接到 #1780 仍不构成普通 PR title 清洗覆盖。
- 这是本轮全新 baseline，不是历史输出，也不是父进程 snapshot 的改写。

## Failures

- 没有发现 skill 行为回归。
- 覆盖限制：实时窗口唯一 PR #1780 是应过滤的 `stainless-app[bot]` release PR；`pr_conventional_commit` 没有普通 PR 样本，因此总体结论保持 `PARTIAL`。不能用该 PR body、release body 或 tag compare commit 的清洗结果替代 PR title 断言。
- 没有外部服务失败；baseline 首次 API 命令因未给 zsh 中的 `?` 加引号而失败，修正命令后实时查询成功。这是 baseline 的本地命令构造错误，不是 GitHub 服务失败，也未影响最终证据完整性。

## External Dependency and Failure Triage

- 数据依赖：GitHub API / `gh` CLI、目标仓库 release、PR 搜索、PR body、commit-to-PR 关联和 compare endpoint；这些数据会随新 release 发布而变化。
- 外部服务失败：认证失败、限流、DNS / TLS / 网络错误、GitHub 5xx、目标仓库暂时不可访问，或抓取过程中 release 指针变化。此时应记录命令、时间、退出码和错误，结果标为 `BLOCKED`，不能判为 skill 回归或真实空集合。
- Skill 回归：GitHub 数据可读取且 snapshot 自洽时，选错最新或前一 release、窗口边界错误、漏查 tag compare 或关联 PR、标题未清洗、漏掉 PR 引用、错误生成空 section，或发现 breaking marker 却未加 `⚠️ BREAKING:`。
- 时效风险：release、PR、标题和发布说明均为实时公开数据；后续复验必须重新记录各自独立的抓取时间、tag/window 和实际样本，不能把本次 `v0.120.0` 快照当作永久 fixture。

## Next Steps

- 当前无需修改 fixture 或 assertions；后续在 latest-release 窗口出现非 bot PR 后，按相同 no-leak 流程重新抓取并实际覆盖 `pr_conventional_commit`。

## Runtime Artifacts Policy

- Runtime changelog candidates, transcripts, verdicts, timing, outputs, and diagnostics are ephemeral and must not be committed.
- Durable result only: this canonical `comparison.md`; `eval_metadata.json` remains unchanged。
