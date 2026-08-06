# Eval Result: eval-001-unreleased-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator` → `changelog-gen`（改名后新入口待重跑验证）
- Eval: `eval-001-unreleased-mode`
- Test case: `unreleased-mode`
- Workspace: `workspace/eval-001-unreleased-mode`
- Classification: `(c) 依赖实时外部数据`。原始 prompt 要求读取 `anthropics/anthropic-sdk-python` 当前 GitHub Release 与 merged PR；静态 fixture 会改变本用例。
- Behavior result: **PASS** — fresh with-skill 与 fresh without-skill 都确认 `v0.120.0` 发布后没有 merged PR。with-skill 在实际触发的 `unreleased` 与 `versioned_changelog_file` assertions 上均满足要求，未发现行为回归。
- Coverage result: **PARTIAL** — `pr`、`bot_pr_dependabot`、`chore_ci_test` 均为 **NOT EXERCISED**：实时窗口没有 merged PR，因此没有 PR 链接、bot PR 或维护类 PR 候选可覆盖，不能用空集合伪装成 PASS。
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。
。
- 证据来源：2026-07-26 fresh run（沿用既有记录，本轮仅做结果模型迁移，未重新执行 eval）。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0。
- Fixture: `eval_metadata.json` 中的原始 prompt；未添加静态 GitHub snapshot 或 mock。
- Prompt target: 生成最新 release 之后全部 merged PR 的 Keep a Changelog `Unreleased` 章节，目标为 `docs/changelog/changelog-unreleased.md`。
- Fresh pair date: 2026-07-26（Asia/Shanghai）。

## Fresh / No-Leak Method

1. 两个 arm 生成前，只从各自 workspace 的 `eval_metadata.json` 取得原始 prompt；没有读取 `evals.json`、assertions、expected output 或旧 comparison。
2. with-skill arm 完整读取 Product Manager README、`changelog-gen/SKILL.md` 及其 Conventional Commit reference，独立查询 live GitHub；候选先写入并回读 `tmp/eval-runs/issue173-fresh-eval/with-skill/eval-001/` 后锁定。
3. without-skill arm 不读取、不应用该 README 或 skill，不读取 with-skill scratch，只依据原始 prompt重新查询 live GitHub；全新 baseline 写入并回读 `tmp/eval-runs/issue173-fresh-eval/without-skill/eval-001/` 后锁定。
4. 两臂锁定后才读取本轮 `evals.json` 与旧 comparison，由当前 fresh Codex subagent逐 assertion judge。两臂也都在各自隔离 scratch 的 canonical target path 实际创建并回读目标文件。

## Independent Live Data Snapshots

| Arm | Fetch time | Query | Latest release | Window result | External failure |
| --- | --- | --- | --- | --- | --- |
| with-skill | `2026-07-26T22:47:23+08:00` | `gh repo view`、`gh release list`、`gh pr list` | `v0.120.0`, published `2026-07-24T16:32:34Z` | `mergedAt > 2026-07-24T16:32:34Z`：0 merged PR | 无 |
| without-skill | `2026-07-26T22:48:20+08:00` | 独立执行 `gh repo view`、`gh release list`、`gh pr list` | `v0.120.0`, published `2026-07-24T16:32:34Z` | 同一精确下界：0 merged PR | 无 |

两次查询之间没有观察到 latest release 或 merged PR 集合漂移。仓库默认分支均为 `main`。

## Assertions

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `unreleased` | PASS | PASS | 两个锁定候选均包含 `## [Unreleased]`。 |
| `pr` | NOT EXERCISED | NOT EXERCISED | 窗口内没有 PR 条目，无法正向验证每个条目的 `(#数字)` 链接格式。 |
| `bot_pr_dependabot` | NOT EXERCISED | NOT EXERCISED | 窗口内没有 bot PR；没有误造条目不等于实际执行了 bot 过滤。 |
| `chore_ci_test` | NOT EXERCISED | NOT EXERCISED | 窗口内没有 `chore` / `ci` / `test` 候选，维护类变更过滤未触发。 |
| `versioned_changelog_file` | PASS | PASS | 两臂都在隔离 scratch 中实际创建并回读 `docs/changelog/changelog-unreleased.md`。 |

## With Skill Behavior

Fresh source: 原始 prompt、Product Manager README、完整 `changelog-gen` 协议与第一次独立 live 查询。

```markdown
# Changelog - Unreleased

## [Unreleased]

_No user-facing changes since v0.120.0._
```

- 正确选择 Unreleased mode、release `publishedAt` 下界和 canonical target。
- live 窗口为空时没有编造 PR、链接或分类 section。
- 使用 skill 规定的精确 Unreleased 文件头。

## Fresh Without-Skill Baseline

Fresh source: 仅原始 prompt 与第二次独立 live 查询；未复用旧 baseline、with-skill snapshot 或历史 comparison 的实时事实。

```markdown
# Changelog

## [Unreleased]

_No changes have been merged since v0.120.0._
```

- Prompt 本身明确了范围、格式和路径，因此 baseline 同样选择正确 target 与标题。
- 独立查询得到真实空窗口，没有编造条目。
- 空窗口没有暴露 baseline 对 bot、dependency 或维护类前缀的处理差异。

## Failures

- 未发现已触发路径的 with-skill 回归。
- Coverage gap：`pr`、`bot_pr_dependabot`、`chore_ci_test` 缺少实时候选，Coverage result 保持 `PARTIAL`，Overall result 为 `PASS (partial coverage)`。
- GitHub API、认证、网络和目标仓库访问均成功，无 external dependency blocker。

## Next Steps

- 不补造 fixture 或窗口外 PR。
- 后续 latest release 之后出现非空 PR 窗口时，重新执行同一 no-leak fresh pair，实际覆盖 PR 链接、bot 排除和维护类 PR 过滤。

## Runtime Artifact Policy

- 本轮候选、snapshot 和 canonical target 只写入 git 忽略的 `tmp/eval-runs/issue173-fresh-eval/`，完成评审后全部删除。
- 不提交 candidate、transcript、verdict、timing、outputs 或 diagnostics。
- 仅持久化本 `comparison.md` 的事实摘要与 fresh judge 结论。
