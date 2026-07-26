# Eval Result: eval-002-single-version-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-002-single-version-mode`
- Test case: single-version-mode
- Workspace: `workspace/eval-002-single-version-mode`
- Classification: `(c)` 依赖实时 GitHub 数据。该场景必须读取目标仓库当时的 release、相邻 tag compare、merged PR 和 author；静态 mock 不能替代真实复验。
- Latest result: PARTIAL - 2026-07-26 的 fresh `with_skill` / `without_skill` 已由当前会话中的同一个 fresh Codex subagent 顺序完成两次独立实时查询，并分别在隔离 scratch 中实际写入、回读和清理目标文件。with-skill 正确过滤唯一的 bot release PR 及 compare 中的 bot commits，但其 `## [v0.120.0]` 标题不满足现有 assertion 要求的 `## [x.y.z]`，因此为 2 PASS / 1 FAIL / 2 NOT EXERCISED；without-skill 为 3 PASS / 2 NOT EXERCISED。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0。
- Fixture: 仅包含 eval metadata；不新增静态 GitHub 快照。
- Expected output: 生成最新 release tag 的版本块，格式为 `## [x.y.z] - YYYY-MM-DD`，包含该版本窗口内符合 skill 收录规则的 PR，分组写入，并以 `docs/changelog/changelog-v{version}.md` 为目标路径。
- Fresh pair: 当前 fresh Codex subagent 先生成并锁定 `with_skill`，再由同一个 subagent 不应用 specialist skill 或 Product Manager README，仅凭原始 prompt 重新查询并锁定新的 `without_skill` baseline；没有复用历史 baseline。

## No-Leak Execution

- `with_skill` 生成前只读取本用例 `eval_metadata.json` 的原始 prompt，随后完整读取 Product Manager README 与 `changelog-generator/SKILL.md`；未读取 `evals.json`、assertions、expected output 或旧 comparison。
- `with_skill` 的 live snapshot 和候选先锁定；随后同一个 fresh subagent 进入 baseline arm，不应用先前读取的 specialist skill 或 Product Manager README，仅依据原始 prompt 独立选择查询并生成候选。
- baseline 未读取 `evals.json`、assertions、expected output 或旧 comparison，也未接收预计算 snapshot；它重新调用 `gh` 获取当时的 release 和 PR 数据。
- 两个候选都锁定后，同一个 fresh subagent 才读取 assertions 和旧 comparison 并亲自完成 fresh judge。
- 两个 arm 分别在独立临时目录实际写入并回读 `docs/changelog/changelog-v0.120.0.md`，确认内容后清理临时目录；本轮没有启动第二个 subagent，也没有持久化或提交 transcript、candidate、verdict、timing、outputs 或 diagnostics。

## Independent Live Data Snapshots

### With Skill

- 抓取时间：2026-07-26 16:38:41 `+08:00`（Asia/Shanghai）。
- 仓库：`anthropics/anthropic-sdk-python`，默认分支 `main`。
- 最新 release：`v0.120.0`，发布时间 `2026-07-24T16:32:34Z`。
- 前一 release：`v0.119.0`，发布时间 `2026-07-23T17:34:23Z`。
- PR 窗口：`2026-07-23T17:34:23Z..2026-07-24T16:32:34Z`。
- 窗口内 merged PR：仅 `#1780`，标题 `release: 0.120.0`，合并于 `2026-07-24T16:31:59Z`；author 为 `app/stainless-app`，GitHub 标记 `is_bot: true`。
- Tag compare：[`v0.119.0...v0.120.0`](https://github.com/anthropics/anthropic-sdk-python/compare/v0.119.0...v0.120.0) 为 `ahead_by: 2`。功能提交 `70c0a64581e7` 与 release 提交 `60c64fba5c2b` 的 author 均为 `stainless-app[bot]`。
- 外部服务失败：无。

### Without Skill

- 抓取时间：2026-07-26 16:39:20 `+08:00`（Asia/Shanghai）。
- baseline 独立确认最新 release `v0.120.0`、前一 release `v0.119.0` 及相同发布时间。
- baseline 独立查询 merged PR，确认最新 release 对应的自动 release PR 为 `#1780`，其正文列出 3 项 Features。
- 外部服务失败：无。

## Assertions

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `x_y_z_yyyy_mm_dd` | FAIL | PASS | assertion 明确要求 `## [x.y.z] - YYYY-MM-DD`。with-skill 按当前 specialist Step 6 模板生成 `## [v0.120.0]`，多出 `v` 前缀；without-skill 生成 `## [0.120.0]`。本轮不放宽 assertion，也不修改 specialist。 |
| `release_tag` | PASS | PASS | 两者均以实时最新 tag `v0.120.0` 为来源。 |
| `pr_conventional_commit` | NOT EXERCISED | NOT EXERCISED | 当前窗口没有普通 PR。`#1780` 是 bot release PR；baseline 的三条内容来自其 body，不是普通 PR title 清洗样本，不能把该断言判为 PASS。 |
| `breaking_change_breaking` | NOT EXERCISED | NOT EXERCISED | 当前 PR body 和 tag compare 均无 breaking marker；未触发时不虚构前缀不能证明两者在出现 breaking change 时会正确添加 `⚠️ BREAKING:`。 |
| `section` | PASS | PASS | with-skill 过滤全部 bot 来源后不生成任何空 section；baseline 只生成有内容的 `Added`。 |

## With Skill

Observed behavior:

- 按 specialist 流程用 `gh` 确认目标仓库、最新和前一 release，并用发布时间建立单版本窗口。
- 查询窗口内 merged PR，识别唯一的 `#1780` 为 bot release PR，并按 author 为 bot 或 login 以 `[bot]` 结尾的规则排除，未把它作为 changelog attribution 或链接。
- 因过滤后没有 PR，按 edge case 查询 tag compare；compare 中的两条 commits 也都是 `stainless-app[bot]` 作者，继续排除。
- 生成 specialist 当前模板规定的 `## [v0.120.0]` header 与 `_No user-facing changes (dependency updates and internal maintenance only)._`，不生成空 section，也不链接被过滤的 `#1780`；该 header 与现有 eval assertion 的无 `v` 格式冲突。
- 在隔离临时目录 `/tmp/issue158-eval002-with-skill.D56BxK/` 中实际写入并回读 `docs/changelog/changelog-v0.120.0.md`，确认内容后清理整个临时目录；未把 runtime candidate 写入 eval fixture。

Candidate behavior summary:

```markdown
# Changelog - v0.120.0

## [v0.120.0] - 2026-07-24

_No user-facing changes (dependency updates and internal maintenance only)._
```

## Without Skill / Baseline

Observed behavior:

- 同一个 fresh subagent 在 baseline arm 中仅按原始 prompt 重新查询 GitHub，没有应用 specialist skill、Product Manager README 或任何 eval answer key。
- 独立选中 `v0.120.0`，并从自动 release PR `#1780` 的正文提取 3 项 Features。
- 将三项功能写入 `Added`，每项都引用 `#1780`；该候选没有 specialist 的 bot author 过滤，因此与 with-skill 形成有效行为差异。
- baseline 的条目不是普通 PR title 清洗样本，所以不满足 `pr_conventional_commit` 的实际覆盖条件。
- 在独立隔离临时目录 `/tmp/issue158-eval002-without-skill.3uD2q4/` 中实际写入并回读 `docs/changelog/changelog-v0.120.0.md`，确认内容后清理整个临时目录；其版本块标题为 `## [0.120.0] - 2026-07-24`。
- 这是本轮新生成的 baseline，不是历史输出或 with-skill 候选的改写。

Candidate behavior summary:

```markdown
# Changelog - v0.120.0

## [0.120.0] - 2026-07-24

### Added

- **api:** Add claude-opus-5 model ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
- **api:** Add tool addition/removal blocks and tool_change events ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
- **api:** Expand client-side fallback credit token types and add server-side fallbacks default option ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
```

## Failures

- 格式契约不一致：现有 eval assertion / expected output 要求 `## [x.y.z] - YYYY-MM-DD`，但 specialist Step 6 的新建版本文件模板要求 `## [v{VERSION}] - YYYY-MM-DD`。with-skill 忠实生成后者，严格 judge 必须把 `x_y_z_yyyy_mm_dd` 判为 `FAIL`；本轮按约束不修改 specialist 或放宽 assertion。
- 覆盖限制：实时窗口唯一 PR `#1780` 是应过滤的 bot release PR，tag compare commits 也均为 bot 作者；`pr_conventional_commit` 没有普通 PR 样本，且窗口没有 breaking marker，`breaking_change_breaking` 的触发分支同样未覆盖，因此总体结论保持 `PARTIAL`。
- baseline 未应用 bot filter，把 `#1780` 当作 changelog PR attribution 和链接；这是 without-skill 行为差异，不是 with-skill failure。
- 两个 arm 均已实际写入、回读并清理隔离 scratch 中的目标文件；文件产出行为不再是未验证覆盖项。
- 没有外部服务失败。

## External Dependency and Failure Triage

- 数据依赖：GitHub API / `gh` CLI、目标仓库 release、PR 搜索、author bot 标记和 compare endpoint；这些数据会随新 release 发布而变化。
- 外部服务失败：认证失败、限流、DNS / TLS / 网络错误、GitHub 5xx、目标仓库暂时不可访问，或抓取过程中 latest release 指针变化。此时应记录命令、时间、退出码和错误，结果标为 `BLOCKED`，不能判为 skill 回归或真实空集合。
- Skill 回归或契约偏差：GitHub 数据可读取且 snapshot 自洽时，选错最新或前一 release、窗口边界错误、未过滤 bot PR/commit、过滤后又把 bot PR 作为条目 attribution 或链接、漏查 tag compare、错误生成空 section、发现 breaking marker 却未加 `⚠️ BREAKING:`，或生成不满足现有 eval assertion 的版本标题。
- 时效风险：release、PR、author 和发布说明均为实时公开数据；后续复验必须重新记录抓取时间、tag/window 和实际样本，不能把本次 `v0.120.0` 快照当作永久 fixture。

## Next Steps

- 由维护者在本 issue 范围外决定统一版本标题契约：修改 specialist 模板或另起经批准的 eval 契约变更；在此之前不得把 `## [v{VERSION}]` 判为满足 `## [x.y.z]`。
- 后续在 latest-release 窗口出现非 bot PR 或 breaking marker 后，按相同 no-leak 流程重新抓取并实际覆盖 `pr_conventional_commit` 与 `breaking_change_breaking`。

## Runtime Artifacts Policy

- Runtime changelog candidates, transcripts, verdicts, timing, outputs, and diagnostics are ephemeral and must not be committed.
- Durable result only: this canonical `comparison.md`; `eval_metadata.json` remains unchanged。
