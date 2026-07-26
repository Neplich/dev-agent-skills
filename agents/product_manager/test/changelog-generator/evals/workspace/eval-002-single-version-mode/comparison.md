# Eval Result: eval-002-single-version-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-002-single-version-mode`
- Test case: single-version-mode
- Workspace: `workspace/eval-002-single-version-mode`
- Classification: `(c)` 依赖实时 GitHub 数据。该场景必须读取目标仓库当时的 release、tag compare 和 merged PR，静态 mock 不能替代真实复验。
- Latest result: PARTIAL - 2026-07-26 的 fresh `with_skill` / `without_skill` 已成对完成；当前版本窗口只有一个应被过滤的发布机器人 PR，因此普通 PR 标题清洗断言没有可执行样本，其余断言通过。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 仅包含 eval metadata；不新增静态 GitHub 快照。
- Expected output: 生成最新 release tag 的版本块，格式为 `## [x.y.z] - YYYY-MM-DD`，包含该版本窗口内的 PR，分组写入，每条带 PR 链接，并写入 `docs/changelog/changelog-v{version}.md`。
- Fresh pair: 本轮使用同一份 live snapshot，先应用 `changelog-generator` 生成 `with_skill`，再仅按原始 prompt 生成新的 `without_skill`；未复用历史 baseline。

## Live Data Snapshot

- 抓取时间：2026-07-26 15:18:54-15:20:17 `+08:00`（Asia/Shanghai）。
- 仓库：`anthropics/anthropic-sdk-python`，默认分支 `main`。
- 最新 release：`v0.120.0`，发布时间 `2026-07-24T16:32:34Z`。
- 前一 release：`v0.119.0`，发布时间 `2026-07-23T17:34:23Z`。
- PR 窗口：`(2026-07-23T17:34:23Z, 2026-07-24T16:32:34Z]`。
- 窗口内 merged PR：仅 [#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780)，`release: 0.120.0`，合并于 `2026-07-24T16:31:59Z`，作者为 `stainless-app[bot]`。
- Tag compare：[`v0.119.0...v0.120.0`](https://github.com/anthropics/anthropic-sdk-python/compare/v0.119.0...v0.120.0) 有 2 个提交；功能提交包含 3 条 `feat(api):` 变化，另一个为 `release: 0.120.0`。未发现 `!` 或 `BREAKING CHANGE:` 标记。

## Assertions

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `x_y_z_yyyy_mm_dd` | PASS | PASS | 两者均生成 `## [0.120.0] - 2026-07-24`。 |
| `release_tag` | PASS | PASS | 两者均以实时最新 tag `v0.120.0` 为来源，并按 changelog 标题格式去掉 tag 的 `v` 前缀。 |
| `pr_conventional_commit` | NOT EXERCISED | NOT EXERCISED | 窗口内唯一 PR 是应过滤的 release bot PR；tag compare 的 `feat(api):` 提交标题已被清洗，但这不能冒充普通 PR 标题清洗证据。 |
| `breaking_change_breaking` | PASS | PASS | 当前窗口没有 breaking marker；“如有则加前缀”的条件未触发，两个输出均未虚构 `⚠️ BREAKING:`。 |
| `section` | PASS | PASS | 两者只输出有内容的 `Added`，没有生成空 section。 |

## With Skill

Observed behavior:

- 通过 `gh release list` / release API 确认最新和前一 release，并使用精确发布时间建立单版本窗口。
- 识别 #1780 为机器人发布 PR，按 skill 的 bot 过滤规则不把它当作用户变化条目。
- 在没有可纳入 PR 后，按 edge-case 规则回退到 tag compare；将一个 `feat(api):` 提交中的 3 条功能变化清洗为 `Added` 条目，并保留提交来源链接。
- 生成候选版本块 `## [0.120.0] - 2026-07-24`，只包含 `### Added`，解析目标路径为 `docs/changelog/changelog-v0.120.0.md`。
- 未把候选 changelog 写入 eval fixture；本轮只持久化 fresh judge 摘要。

## Without Skill / Baseline

Observed behavior:

- 未读取或应用 specialist skill / Agent README，仅按原始 prompt 和同一 live snapshot 独立查询最新 release、前一 release、窗口 PR 与 release 内容。
- 同样生成 `## [0.120.0] - 2026-07-24` 和单一 `Added` section，并从 release 内容整理 3 条 API 功能变化。
- baseline 能保留 #1780 作为发布来源引用，但没有 specialist 的明确 bot-filter + tag-compare fallback 判定链；它不能为“普通 PR conventional prefix 清洗”提供额外证据。
- 这是本轮重新生成的 baseline，不是 2026-06-02 的历史输出。

## Failures

- 没有发现 skill 行为回归。
- 覆盖限制：实时窗口缺少非 bot PR，`pr_conventional_commit` 无法在本次 snapshot 中被实际触发，因此总体结论保持 `PARTIAL`，不能将 tag compare 的提交标题清洗虚报成 PR 标题清洗 PASS。

## External Dependency and Failure Triage

- 数据依赖：GitHub API / `gh` CLI、目标仓库 release、PR 搜索、commit-to-PR 关联和 compare endpoint；这些数据会随新 release 发布而变化。
- 外部服务失败：认证失败、限流、DNS / 网络错误、GitHub 5xx、目标仓库暂时不可访问，或同一抓取窗口内 release 指针发生变化。此时应记录命令、时间和错误，结果标为 `BLOCKED`，不能判为 skill 回归。
- Skill 回归：在 GitHub 数据可读取且 snapshot 一致时，选错最新或前一 release、窗口边界错误、未过滤明确 bot PR、该回退 tag compare 时未回退、标题未清洗、错误生成空 section，或发现 breaking marker 却未加 `⚠️ BREAKING:`。
- 时效风险：release、PR、标题和发布说明均为实时公开数据；后续复验必须重新记录抓取时间、tag/window 和实际样本，不能把本次 `v0.120.0` 快照当作永久 fixture。

## Next Steps

- 下次 live snapshot 出现非 bot PR 时，重新运行此 eval 以实际覆盖 `pr_conventional_commit`；在此之前保留当前 `PARTIAL`，不添加 mock PR。

## Runtime Artifacts Policy

- Runtime changelog candidates, transcripts, verdicts, timing, outputs, and diagnostics are ephemeral and must not be committed.
- Durable result only: this canonical `comparison.md`; `eval_metadata.json` remains unchanged.
