# Eval Result: eval-001-unreleased-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-001-unreleased-mode`
- Test case: unreleased-mode
- Workspace: `workspace/eval-001-unreleased-mode`
- Classification: `(c) 依赖实时外部数据`。Prompt 要求读取 `anthropics/anthropic-sdk-python` 当前的 GitHub Release、merged PR 和 tag-to-main 状态；静态 fixture 或 mock 会改变被测场景，因此本轮不补 fixture。
- Latest result: **PARTIAL** — 本轮 fresh with-skill 与 fresh without-skill 分别独立查询 GitHub，均确认最新 release `v0.120.0` 后没有 merged PR，且 `v0.120.0...main` 为 identical。两者均生成真实的空 Unreleased 结果；`unreleased` 与目标文件 assertions 通过，但 PR 链接、bot 过滤和维护变更过滤因没有候选样本而未被实际覆盖。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 仅包含原始 prompt 与 `eval_metadata.json`；这足以指定目标仓库、Unreleased mode 与目标文件，实时事实由 GitHub API / `gh` 提供。
- Prompt target: 最新 release 之后合并的所有 PR，以 Keep a Changelog 格式写入 `docs/changelog/changelog-unreleased.md`。
- Fresh evaluation: 2026-07-26；with-skill 与 without-skill 均在当前会话中新生成，未复用历史 baseline、第一批 PR #168 的跑法或 parent 预计算 snapshot。

## No-Leak Evaluation Method

1. 生成 with-skill 前只读取当前 workspace 的 `eval_metadata.json` 原始 prompt；没有读取 `evals.json`、assertions、expected output 或旧 `comparison.md`。
2. with-skill 读取 PM Agent README 与 `changelog-generator` skill 后，独立通过 `gh` 查询 prompt 指定的公开仓库，并先锁定候选和事实快照。
3. without-skill 由当前会话中新启动、`fork_turns=none` 的 fresh Codex subagent 生成。子代理只收到原始 prompt，以及“自行实时查询 GitHub并返回候选、抓取时间和关键快照”的要求；没有收到 skill、README、assertions、expected output、旧 comparison、with-skill 候选或 parent 查询结果。
4. 两份候选都锁定后才读取 `evals.json` 与旧 comparison 进行 judge。本文件仅记录 judge 摘要；候选、transcript、verdict、diagnostics 和 outputs 均未落盘。

## Independent Live Data Snapshots

| Snapshot | Fetch time (Asia/Shanghai) | Latest release | PRs after release | Tag-to-main | Drift judgment |
| --- | --- | --- | --- | --- | --- |
| With skill | `2026-07-26 15:36:35 +08:00` 起 | `v0.120.0`, published `2026-07-24T16:32:34Z` | 0 | `identical`, ahead 0, behind 0, commits 0 | 基准抓取 |
| Without skill | `2026-07-26 15:37:13 +08:00` 至 `15:38:36 +08:00` | `v0.120.0`, published `2026-07-24T16:32:34Z` | 0 | `identical`, ahead 0, behind 0, commits 0 | 与 with-skill 无 release、PR 或 branch-tip 漂移 |

关键事实：

- 仓库：`anthropics/anthropic-sdk-python`，默认分支 `main`。
- `v0.120.0` tag target 与当前 `main` 均为 `60c64fba5c2bf340567f627328e57cf0196b868f`。
- 边界 PR `#1780 release: 0.120.0` 合并于 `2026-07-24T16:31:59Z`，比 release 发布时间早 35 秒，不属于 Unreleased。
- with-skill 使用 `gh repo view`、`gh release list`、`gh pr list` 后按精确 `publishedAt` 过滤，并调用 Compare API。
- without-skill 独立使用 Releases、Tags、Search、Pulls、GraphQL 与 Compare API 交叉复核，没有使用 parent 的预计算结果。

## Assertions

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `unreleased` | PASS | PASS | 两个候选都包含 `## [Unreleased]`。 |
| `pr` | NOT EXERCISED | NOT EXERCISED | 窗口内没有条目。本快照无法正向验证非空 PR 的链接格式，不能把空集合当作可用性 PASS。 |
| `bot_pr_dependabot` | NOT EXERCISED | NOT EXERCISED | 精确窗口内没有 bot PR 候选；未引入窗口外 PR 不等于实际执行了 bot 过滤。 |
| `chore_ci_test` | NOT EXERCISED | NOT EXERCISED | 精确窗口内没有 `chore` / `ci` / `test` 候选，无法验证维护变更过滤或当前 skill 的语义审查。 |
| `versioned_changelog_file` | PASS | PASS | 两次运行都把 artifact target 明确设为 `docs/changelog/changelog-unreleased.md`；根据 eval 运行期产物策略未写回 canonical fixture。 |

## With Skill

Fresh source: 只依据原始 prompt、PM Agent README、`changelog-generator` skill 与第一次独立 live 查询生成。

Locked candidate artifact:

```markdown
# Changelog - Unreleased

## [Unreleased]

_No merged PRs since v0.120.0._
```

Observed behavior:

- 正确选择 Unreleased mode 和 canonical target。
- 使用 release `publishedAt` 作为精确窗口下界，没有把早 35 秒合并的 release PR `#1780` 纳入结果。
- release 后无 merged PR，且 tag-to-main identical，因此输出真实空状态而不编造 PR。
- 使用 skill 指定的精确 Unreleased 文件头。

## Without Skill / Baseline

Fresh source: `fork_turns=none` 子代理仅依据原始 prompt 和第二次独立 live 查询生成；没有读取或应用 PM Agent、`changelog-generator`、eval 答案键或 parent snapshot。

Locked candidate artifact:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

_No pull requests have been merged since v0.120.0._

[Unreleased]: https://github.com/anthropics/anthropic-sdk-python/compare/v0.120.0...HEAD
```

Observed behavior:

- Prompt 已直接给出 Unreleased 范围、Keep a Changelog 格式与输出路径，因此 baseline 也选择了正确标题和 artifact target。
- 独立查询确认 release 后 0 个 merged PR，因而没有编造条目。
- 使用通用 Keep a Changelog 头和 compare link，而不是 specialist 指定的 canonical `# Changelog - Unreleased` 文件头；该格式差异不违反现有 assertions。
- 空窗口没有暴露 baseline 对 bot、dependency、internal scope 和低优先级前缀语义审查的处理差异。

## Failures

- 未发现已执行分支的 skill 行为回归。
- Coverage gap：live 窗口为空，因此 `pr`、`bot_pr_dependabot`、`chore_ci_test` 均为 `NOT EXERCISED`，未正向验证非空 PR 的链接、bot 排除和低优先级前缀语义审查。总体结论保持 `PARTIAL`，不能通过伪造 fixture 或条目补足这种实时覆盖。

## External Dependency Failure Policy

- 依赖：GitHub API 可用、DNS / 网络正常、`gh` 已认证且未被限流，以及外部仓库仍公开可访问。
- 外部服务失败：若 `gh` 返回认证、权限、rate-limit、网络、GitHub 5xx 或仓库不可访问错误，且无法取得 release、PR 或 compare snapshot，本 eval 应记为 `BLOCKED (external dependency)`，不能据此判定 skill 回归。
- Skill 回归：live snapshot 成功取得后，若选择错误 release、窗口边界错误、遗漏实际窗口内 PR、纳入窗口外或明确应跳过的 PR、错误地一概排除具有语义影响的 `docs` / `test` / `ci`、缺少 PR 链接、缺少 `## [Unreleased]`，或目标不是 `docs/changelog/changelog-unreleased.md`，才属于 skill / output regression。

## Next Steps

- 无需补 fixture 或修改 skill。
- 外部仓库可能在 comparison 提交后立即产生新 release 或 merged PR；未来出现非空 Unreleased 窗口时，应重新抓取并实际覆盖 PR 链接、bot 过滤和维护变更过滤，不能把本 snapshot 当作固定事实。

## Runtime Artifacts Policy

- 本轮没有把 changelog candidate、transcript、verdict、timing、outputs 或 diagnostics 写入 canonical fixture。
- 只持久化本 `comparison.md` 的事实摘要与 fresh judge 结论；任何临时运行产物都不进入 git。
