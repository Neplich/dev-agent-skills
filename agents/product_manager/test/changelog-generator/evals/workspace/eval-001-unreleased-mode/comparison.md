# Eval Result: eval-001-unreleased-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-001-unreleased-mode`
- Test case: unreleased-mode
- Workspace: `workspace/eval-001-unreleased-mode`
- Classification: `(c) 依赖实时外部数据`。Prompt 要求读取 `anthropics/anthropic-sdk-python` 当前的 GitHub Release 与 merged PR；静态 fixture 或 mock 会改变被测场景，因此本轮不补 fixture。
- Latest result: **PARTIAL** — 本轮由同一个 fresh Codex subagent 按顺序独立生成 with-skill 与 without-skill，二者均确认最新 release `v0.120.0` 后没有 merged PR。两臂都实际写入并回读目标文件后才锁定；`unreleased` 与目标文件 assertions 通过，但 PR 链接、bot 过滤和维护变更过滤因没有候选样本而未被实际覆盖。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 仅包含原始 prompt 与 `eval_metadata.json`；这足以指定目标仓库、Unreleased mode 与目标文件，实时事实由 GitHub API / `gh` 提供。
- Prompt target: 最新 release 之后合并的所有 PR，以 Keep a Changelog 格式写入 `docs/changelog/changelog-unreleased.md`。
- Fresh evaluation: 2026-07-26；with-skill 与 without-skill 均在当前会话中新生成，未复用历史 baseline、第一批 PR #168 的跑法或旧 comparison 候选。

## No-Leak Evaluation Method

1. 生成 with-skill 前只读取当前 workspace 的 `eval_metadata.json` 原始 prompt；没有读取 `evals.json`、assertions、expected output 或旧 `comparison.md`。
2. 当前 fresh Codex subagent 读取 PM Agent README 与 `changelog-generator` skill，独立通过 `gh` 查询 prompt 指定的公开仓库，在忽略目录 `tmp/eval-runs/final-changelog-001-with/` 实际写入并回读目标文件后锁定 with-skill 候选。
3. 锁定后使用 `apply_patch` 删除 with-skill 临时文件；同一个 subagent 不再应用 skill 或 README，仅凭原始 prompt，通过不同的 GitHub REST 查询重新获取 release 与 merged PR 数据，在隔离目录 `tmp/eval-runs/final-changelog-001-without/` 实际写入并回读目标文件后锁定 baseline。
4. 锁定并清理两臂临时文件后，才读取 `evals.json`、assertions、expected output 与旧 comparison，由同一个 fresh subagent 亲自 judge。本文件只保留事实摘要；运行期候选、transcript、verdict、diagnostics 和 outputs 均未提交。

## Independent Live Data Snapshots

| Snapshot | Fetch time (Asia/Shanghai) | Query path | Latest release | PRs after release | Additional check | Drift judgment |
| --- | --- | --- | --- | --- | --- | --- |
| With skill | `2026-07-26 16:23:11 +08:00` 起 | `gh repo view`、`gh release list`、`gh pr list` | `v0.120.0`, published `2026-07-24T16:32:34Z` | 0 | Compare API: `v0.120.0...main` 为 `identical`，ahead 0、commits 0 | 基准抓取 |
| Without skill | `2026-07-26 16:23:49 +08:00` 起 | `gh api` Releases latest 与分页 Pulls REST API | `v0.120.0`, published `2026-07-24T16:32:34Z` | 0 | 分页扫描 closed PR，并按精确 `merged_at` 下界筛选 | 与 with-skill 无 release 或 PR 漂移 |

关键事实：

- 仓库：`anthropics/anthropic-sdk-python`，默认分支 `main`。
- with-skill 查询发现 release 后 0 个 merged PR，且 `v0.120.0...main` 为 identical。
- without-skill 没有使用 with-skill 查询结果；它重新读取 GitHub 的 latest release，并从 Pulls REST API 独立筛选 `merged_at > 2026-07-24T16:32:34Z`，结果同样为 0。
- 两臂之间未观察到 latest release 或 merged PR 集合漂移。

## Assertions

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `unreleased` | PASS | PASS | 两个实际写入并回读的候选都包含 `## [Unreleased]`。 |
| `pr` | NOT EXERCISED | NOT EXERCISED | 窗口内没有条目。本快照无法正向验证非空 PR 的链接格式，不能把空集合当作可用性 PASS。 |
| `bot_pr_dependabot` | NOT EXERCISED | NOT EXERCISED | 精确窗口内没有 bot PR 候选；未引入窗口外 PR 不等于实际执行了 bot 过滤。 |
| `chore_ci_test` | NOT EXERCISED | NOT EXERCISED | 精确窗口内没有 `chore` / `ci` / `test` 候选，无法验证维护变更过滤或语义审查。 |
| `versioned_changelog_file` | PASS | PASS | 两臂分别在隔离 scratch 中实际创建 `docs/changelog/changelog-unreleased.md`，使用 `test -f` 与回读验证成功后才锁定，随后按运行期产物策略清理。 |

## With Skill

Fresh source: 只依据原始 prompt、PM Agent README、`changelog-generator` skill 与第一次独立 live 查询生成。

Locked candidate artifact:

```markdown
# Changelog - Unreleased

## [Unreleased]

_No changes have been merged since v0.120.0 (released 2026-07-24)._
```

Observed behavior:

- 正确选择 Unreleased mode 和 canonical target。
- 使用 release `publishedAt` 作为窗口下界。
- release 后无 merged PR，且 tag-to-main identical，因此输出真实空状态而不编造 PR。
- 使用 skill 指定的精确 Unreleased 文件头。
- 在 `tmp/eval-runs/final-changelog-001-with/docs/changelog/changelog-unreleased.md` 实际写入并回读验证，锁定后清理。

## Without Skill / Baseline

Fresh source: 同一个 fresh Codex subagent 在清理 with-skill scratch 后，不应用 PM Agent README 或 `changelog-generator` skill，仅依据原始 prompt 与第二次独立 live 查询生成。

Locked candidate artifact:

```markdown
# Changelog - Unreleased

## [Unreleased]

_No pull requests have been merged since v0.120.0 was released on 2026-07-24._
```

Observed behavior:

- Prompt 已直接给出 Unreleased 范围、Keep a Changelog 格式与输出路径，因此 baseline 也选择了正确标题和 artifact target。
- 通过独立的 latest-release 与分页 Pulls REST 查询确认 release 后 0 个 merged PR，没有编造条目。
- 空窗口没有暴露 baseline 对 bot、dependency、internal scope 和低优先级前缀语义审查的处理差异。
- 在 `tmp/eval-runs/final-changelog-001-without/docs/changelog/changelog-unreleased.md` 实际写入并回读验证，锁定后清理。

## Failures

- 未发现已执行分支的 skill 行为回归。
- Coverage gap：live 窗口为空，因此 `pr`、`bot_pr_dependabot`、`chore_ci_test` 均为 `NOT EXERCISED`，未正向验证非空 PR 的链接、bot 排除和维护变更过滤。总体结论保持 `PARTIAL`，不能通过伪造 fixture 或条目补足这种实时覆盖。

## External Dependency Failure Policy

- 依赖：GitHub API 可用、DNS / 网络正常、`gh` 已认证且未被限流，以及外部仓库仍公开可访问。
- 外部服务失败：若 `gh` 返回认证、权限、rate-limit、网络、GitHub 5xx 或仓库不可访问错误，且无法取得 release 或 PR snapshot，本 eval 应记为 `BLOCKED (external dependency)`，不能据此判定 skill 回归。
- Skill 回归：live snapshot 成功取得后，若选择错误 release、窗口边界错误、遗漏实际窗口内 PR、纳入窗口外或明确应跳过的 PR、错误地一概排除具有语义影响的 `docs` / `test` / `ci`、缺少 PR 链接、缺少 `## [Unreleased]`，或没有实际写入 `docs/changelog/changelog-unreleased.md`，才属于 skill / output regression。

## Next Steps

- 无需补 fixture 或修改 skill。
- 外部仓库可能在 comparison 提交后立即产生新 release 或 merged PR；未来出现非空 Unreleased 窗口时，应重新抓取并实际覆盖 PR 链接、bot 过滤和维护变更过滤，不能把本 snapshot 当作固定事实。

## Runtime Artifacts Policy

- 两臂候选只曾写入 git 忽略的 `tmp/eval-runs/final-changelog-001-with/` 与 `tmp/eval-runs/final-changelog-001-without/`，锁定后已删除文件。
- 运行期 changelog candidate、transcript、verdict、timing、outputs 或 diagnostics 均不提交。
- 只持久化本 `comparison.md` 的事实摘要与 fresh judge 结论。
