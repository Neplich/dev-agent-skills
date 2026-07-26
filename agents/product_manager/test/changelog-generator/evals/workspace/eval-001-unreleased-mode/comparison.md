# Eval Result: eval-001-unreleased-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-001-unreleased-mode`
- Test case: unreleased-mode
- Workspace: `workspace/eval-001-unreleased-mode`
- Classification: `(c) 依赖实时外部数据`。Prompt 要求读取 `anthropics/anthropic-sdk-python` 的当前 GitHub Release 与 merged PR；静态 fixture 或 mock 会改变被测场景，因此本轮不补 fixture。
- Latest result: **PASS** — 2026-07-26 的 fresh with-skill 与 fresh without-skill 使用同一份 live GitHub snapshot；两者都忠实生成空的 Unreleased 结果，没有为满足 PR-link assertion 编造条目。链接与过滤 assertions 在空集合上成立，但本次快照没有形成非空候选的正向覆盖。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 仅包含 prompt 与 `eval_metadata.json`；这足以指定目标仓库、模式与目标文件，实时事实由 GitHub API / `gh` 提供。
- Prompt target: 最新 release 之后合并的所有 PR，以 Keep a Changelog 格式写入 `docs/changelog/changelog-unreleased.md`。
- Fresh evaluation: 2026-07-26（同一当前会话中新生成 with-skill 与 without-skill；未复用历史 baseline）。

## Live Data Snapshot

- 抓取时间：`2026-07-26T15:18:44+08:00` 至 `2026-07-26T15:19:34+08:00`（Asia/Shanghai；对应截止时间 `2026-07-26T07:19:34Z`）。
- 仓库：`anthropics/anthropic-sdk-python`，默认分支 `main`。
- 最新非 draft GitHub Release：`v0.120.0`，published at `2026-07-24T16:32:34Z`，tag target `60c64fba5c2bf340567f627328e57cf0196b868f`。
- 实际 PR 窗口：`mergedAt > 2026-07-24T16:32:34Z` 且 `mergedAt <= 2026-07-26T07:19:34Z`。
- 查询结果：0 个 merged PR。日期预筛选唯一返回的 PR 是 `#1780 release: 0.120.0`，其 `mergedAt` 为 `2026-07-24T16:31:59Z`，早于 release 发布时间 35 秒，按精确窗口正确排除。
- 关键 live 命令：
  - `gh repo view anthropics/anthropic-sdk-python --json nameWithOwner,url,defaultBranchRef`
  - `gh release list -R anthropics/anthropic-sdk-python --json tagName,publishedAt,name,isDraft,isPrerelease --order desc --limit 10`
  - `gh api repos/anthropics/anthropic-sdk-python/releases/latest`
  - `gh pr list -R anthropics/anthropic-sdk-python --state merged --search 'merged:>=2026-07-24' --limit 200 --json number,title,body,mergedAt,author,url`，再以精确 UTC release 时间过滤。

## Assertions

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `unreleased` | PASS | PASS | 两个候选都包含 `## [Unreleased]`。 |
| `pr` | PASS（空集合） | PASS（空集合） | 窗口内无条目；没有缺失链接的条目，也没有伪造 PR。该快照未正向覆盖非空 PR 的链接格式。 |
| `bot_pr_dependabot` | PASS（空集合） | PASS（空集合） | 精确窗口内没有 bot PR 可纳入；候选均未错误引入窗口外的 release bot PR。 |
| `chore_ci_test` | PASS（空集合） | PASS（空集合） | 精确窗口内没有 `chore` / `ci` / `test` 候选。当前 skill 规则是语义审查 `docs` / `test` / `ci`，不是一概跳过；本窗口没有候选可进一步区分。 |
| `versioned_changelog_file` | PASS | PASS | 两个候选都将 artifact target 明确设为 `docs/changelog/changelog-unreleased.md`；运行期候选未写回 canonical fixture。 |

## With Skill

Fresh source: 当前会话先读取 PM Agent README 与 `changelog-generator` skill，再执行其 repo detection、release discovery、精确 PR-window 与分类协议。

Candidate artifact:

```markdown
# Changelog - Unreleased

## [Unreleased]

_No merged PRs since v0.120.0._
```

Observed behavior:

- 选择 Unreleased mode 和正确的 canonical target。
- 以 release `publishedAt` 而不是仅按日期作为窗口下界，并对 `gh pr list` 的日期预筛选结果再次按精确时间过滤。
- 结果为空时明确输出空状态；未把 release PR `#1780`、bot、维护项或不存在的 PR 填入 changelog。
- 保留当前 skill 的语义规则：`docs` / `test` / `ci` 只有在正文或文件上下文表明影响 skill 行为、eval 契约、release workflow、installation 或协作边界时才进入 changelog。本次窗口没有这类候选。

## Without Skill / Baseline

Fresh source: 在同一当前会话中，使用相同 prompt 和上面的同一 live snapshot 重新生成；不读取或应用 changelog-generator / PM Agent 协议作为 baseline 的生成依据，也未复用历史 baseline。

Candidate artifact:

```markdown
# Changelog - Unreleased

## [Unreleased]

_No merged PRs since v0.120.0._
```

Observed behavior:

- Prompt 已直接给出 Unreleased 范围、Keep a Changelog 格式与输出路径，因此 baseline 也选对标题和 artifact target。
- 在共享 snapshot 中看到 release 后 0 个 merged PR，因而同样没有编造条目。
- 空窗口没有暴露 baseline 对 bot、dependency、internal scope 以及 `docs` / `test` / `ci` 语义审查的处理差异；这属于本轮 live 数据覆盖限制，不是把历史 baseline 当作 fresh 结果。

## Failures

- 无 assertion failure。
- Coverage caveat：live 窗口为空，因此 `pr`、`bot_pr_dependabot`、`chore_ci_test` 只得到空集合证据，未正向验证非空 PR 的链接、bot 排除和低优先级前缀语义审查。后续某次 live 窗口出现候选时应重新观察这些分支，但不应为制造覆盖而伪造 fixture。

## External Dependency Failure Policy

- 依赖：GitHub API 可用、DNS / 网络正常、`gh` 已认证且未被限流，以及外部仓库仍公开可访问。
- 外部服务失败：若 `gh` 返回认证、权限、rate-limit、网络、GitHub 5xx 或仓库不可访问错误，且无法取得 release / PR snapshot，本 eval 应记为 `BLOCKED (external dependency)`，不能据此判定 skill 回归。
- Skill 回归：live snapshot 成功取得后，若选择错误 release、窗口边界错误、遗漏实际窗口内 PR、纳入窗口外或明确应跳过的 PR、错误地一概排除具有语义影响的 `docs` / `test` / `ci`、缺少 PR 链接、缺少 `## [Unreleased]`，或目标不是 `docs/changelog/changelog-unreleased.md`，才属于 skill / output regression。

## Next Steps

- 无需补 fixture 或修改 skill。
- 竞品仓库可能在 comparison 提交后立即产生新 release 或 merged PR；本结论只对应上面的精确抓取窗口，未来复验必须重新抓取并记录新的时间点，不能把此 snapshot 当作固定事实。

## Runtime Artifacts Policy

- 本轮没有把 changelog candidate、transcript、verdict、timing、outputs 或 diagnostics 写入 canonical fixture。
- 只持久化本 `comparison.md` 的事实摘要与 fresh judge 结论；任何临时运行产物都不进入 git。
