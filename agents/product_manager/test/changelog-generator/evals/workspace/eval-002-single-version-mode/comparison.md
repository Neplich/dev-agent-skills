# Eval Result: eval-002-single-version-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-002-single-version-mode`
- Test case: `single-version-mode`
- Workspace: `workspace/eval-002-single-version-mode`
- Classification: `(c) 依赖实时外部数据`。本用例必须读取目标仓库当时的 release、相邻版本窗口、merged PR、author 与 tag compare。
- Latest result: **PASS** — fresh with-skill 正确选中实时最新 release `v0.120.0`，生成 assertion 当前要求的 `## [v0.120.0] - 2026-07-24`，过滤唯一 bot release PR 与 compare 中的 bot commits，并在没有 eligible 内容时省略所有空 section。本轮实际触发的 assertions 全部 PASS；普通 PR 标题清洗和 breaking marker 因实时窗口无相应样本而为 `NOT EXERCISED`，作为覆盖限制记录，不降级已验证行为。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0。
- Fixture: `eval_metadata.json` 中的原始 prompt；未添加静态 GitHub snapshot 或 mock。
- Expected output: 最新 release 的版本块，标题为 `## [v{VERSION}] - YYYY-MM-DD`，目标为 `docs/changelog/changelog-v{version}.md`。
- Fresh pair date: 2026-07-26（Asia/Shanghai）。

## Fresh / No-Leak Method

1. 两个 arm 生成前，只从各自 workspace 的 `eval_metadata.json` 取得原始 prompt；没有读取 `evals.json`、assertions、expected output 或旧 comparison。
2. with-skill arm 完整读取 Product Manager README、`changelog-generator/SKILL.md` 及其 Conventional Commit reference，独立查询 release、PR window 与 tag compare；候选先写入并回读 `tmp/eval-runs/issue173-fresh-eval/with-skill/eval-002/` 后锁定。
3. without-skill arm 不读取、不应用该 README 或 skill，不读取 with-skill scratch，只依据原始 prompt重新查询 live GitHub；全新 baseline 写入并回读 `tmp/eval-runs/issue173-fresh-eval/without-skill/eval-002/` 后锁定。
4. 两臂锁定后才读取本轮 `evals.json` 与旧 comparison，由当前 fresh Codex subagent逐 assertion judge。两臂也都在各自隔离 scratch 的 canonical target path 实际创建并回读目标文件。

## Independent Live Data Snapshots

### With Skill

- Fetch time: `2026-07-26T22:47:36+08:00`。
- Repository: `anthropics/anthropic-sdk-python`；default branch `main`。
- Latest release: `v0.120.0`，published `2026-07-24T16:32:34Z`。
- Previous release: `v0.119.0`，published `2026-07-23T17:34:23Z`。
- Exact window: `2026-07-23T17:34:23Z < mergedAt <= 2026-07-24T16:32:34Z`。
- Merged PRs: only `#1780`, `release: 0.120.0`, merged `2026-07-24T16:31:59Z`; author `app/stainless-app`, GitHub `is_bot: true`。
- Compare fallback `v0.119.0...v0.120.0`: 2 commits；`70c0a64` 与 `60c64fb` 的 author 都是 `stainless-app[bot]`。
- Eligible PRs / commits after skill filtering: 0 / 0。

### Without Skill

- Fetch time: `2026-07-26T22:48:30+08:00`。
- 独立确认 latest `v0.120.0`、previous `v0.119.0` 及相同发布时间。
- 独立查询相同精确窗口，得到唯一 merged PR `#1780`；其 body 列出 3 项 API Features。
- baseline 未应用 skill 的 bot author filtering，因此保留 `#1780` 作为三条 feature 的 PR 引用。
- 两臂均无 external dependency failure，查询期间未观察到 release/window 漂移。

## Assertions

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | FAIL | with-skill 输出 `## [v0.120.0] - 2026-07-24`，满足当前带 `v` assertion；baseline 输出 `## [0.120.0] - 2026-07-24`，缺少 `v`。 |
| `release_tag` | PASS | PASS | 两臂的版本来源均为实时最新 tag `v0.120.0`。 |
| `pr_conventional_commit` | NOT EXERCISED | NOT EXERCISED | 当前窗口没有 eligible 普通 PR title；`#1780` 是 bot release PR，baseline 条目来自其 body features，不能作为 conventional PR title 清洗样本。 |
| `breaking_change_breaking` | NOT EXERCISED | NOT EXERCISED | PR body 与 tag compare 均无 breaking marker；不能虚构 `⚠️ BREAKING` 来制造覆盖。 |
| `section` | PASS | PASS | with-skill 过滤全部 bot 来源后不生成空 section；baseline 只生成有内容的 `Added`。 |

## With Skill Behavior

Fresh source: 原始 prompt、Product Manager README、完整 `changelog-generator` 协议与第一次独立 live 查询。

```markdown
# Changelog - v0.120.0

## [v0.120.0] - 2026-07-24

_No user-facing changes (dependency updates and internal maintenance only)._
```

- 使用 release published times 构建 latest/previous 精确窗口。
- 识别并过滤唯一的 GitHub App bot release PR `#1780`。
- 按少量/无 PR edge case 查询 tag compare，并继续过滤两条 bot-authored commits。
- 没有 eligible 内容时使用 no-user-facing-changes fallback，不生成空 section 或被过滤 PR 的引用。
- 当前带 `v` 的版本标题与修正后的 assertion 一致。

## Fresh Without-Skill Baseline

Fresh source: 仅原始 prompt 与第二次独立 live 查询；未复用旧 baseline、with-skill snapshot 或历史 comparison 的实时事实。

```markdown
# Changelog

## [0.120.0] - 2026-07-24

### Added

- Add Claude Opus 5 model ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
- Add tool addition/removal blocks and tool change events ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
- Expand client-side fallback credit token types and add server-side fallbacks default option ([#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780))
```

- baseline 从自动 release PR body 提取三项 Features 并保留唯一 PR 引用。
- baseline 没有 specialist 的 bot filtering，也没有带 `v` 的版本标题，因此与 with-skill 形成可观察行为差异。

## Failures

- 未发现已触发路径的 with-skill 回归。
- Coverage gap：实时窗口没有 eligible 普通 PR 或 breaking marker，`pr_conventional_commit` 与 `breaking_change_breaking` 为 `NOT EXERCISED`。
- without-skill 未满足带 `v` 的版本标题 assertion，且未过滤 bot release PR；这是 fresh baseline 行为，不是 with-skill failure。
- GitHub API、认证、网络和目标仓库访问均成功，无 external dependency blocker。

## Next Steps

- 无需修改 skill 或 eval assertion；当前带 `v` 标题契约已经一致。
- 后续 latest release 窗口出现 eligible 普通 PR 或 breaking marker 时，重新执行同一 no-leak fresh pair以覆盖剩余两条 assertion。

## Runtime Artifact Policy

- 本轮候选、snapshot 和 canonical target 只写入 git 忽略的 `tmp/eval-runs/issue173-fresh-eval/`，完成评审后全部删除。
- 不提交 candidate、transcript、verdict、timing、outputs 或 diagnostics。
- 仅持久化本 `comparison.md` 的事实摘要与 fresh judge 结论。
