# Eval Result: eval-005-feed-mode-completeness

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-005-feed-mode-completeness`
- Test case: Feed mode completeness
- Workspace: `workspace/eval-005-feed-mode-completeness`
- Classification: `(c)` 依赖实时外部数据；验证下游 skill 调用时是否产出机器可读 Feed YAML，并使完整性信号与 Markdown 声明一致。
- Latest result: **PASS** — 当前会话中的 fresh validator 按 no-leak 顺序独立执行两个 live arm。with-skill 满足 3/3 assertions，without-skill 满足 0/3。
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0。
- Fixture: 无静态 fixture；实时查询目标为 `anthropics/anthropic-sdk-python`。
- Prompt: `我是 roadmap-gen，需要 anthropics/anthropic-sdk-python 的当前仓库状态作为结构化输入，请给我完整状态数据`
- Live dependency: GitHub API、网络、已认证 `gh` CLI。
- Validation date: 2026-07-28（Asia/Shanghai）。
- with-skill query: 2026-07-28 18:41:20–18:42:11 CST。
- without-skill query: 2026-07-28 18:44:56–18:45:30 CST。
- 两个 arm 的近 14 天窗口均为 `>2026-07-14`。

## Fresh Validation Method

1. validator 开始时只获得原始 prompt，未读取 `evals.json`、旧 comparison 或 assertions。
2. with-skill arm 完整读取当前 `github-reader/SKILL.md` 与 Product Manager Agent README，使用已认证 `gh` 独立查询，把命令、时间、原始 JSON 和最终报告保存到隔离 runtime 目录并以 SHA-256 锁定。
3. 锁定 with-skill 后，without-skill arm 不读取或应用 skill 与 Agent README，仅凭原始 prompt 重新执行独立 GitHub 查询，没有复用 with-skill 查询结果。
4. 两个 arm 均锁定并复核 checksum 后，validator 才读取 eval-005 的 3 条 assertions 并逐条裁决。
5. canonical workspace 仅保存本 `comparison.md`；transcript、原始查询、checksum 和 verdict 不纳入 git。

## Independent Live Snapshots

| 集合 | With skill total / fetched | Without skill total / fetched | With skill 完整性 |
| --- | ---: | ---: | --- |
| Open issues | 143 / 143 | 143 / 143 | Search `incomplete_results=false`，未截断 |
| Open PRs | 213 / 213 | 213 / 213 | Search `incomplete_results=false`，未截断 |
| 近 14 天 merged PRs | 6 / 6 | 未查 total / 6 | Search `incomplete_results=false`，未截断 |
| 近 14 天 closed issues | 1 / 1 | 未查 total / 1 | Search `incomplete_results=false`，未截断 |
| Open milestones | 0（分页完成） | 0（分页完成） | 完整 |

with-skill Feed 数据中的 `truncated_collections` 与 `incomplete_totals` 均为空数组。

## With-Skill Behavior

- 正确识别下游 skill 调用并进入 Feed mode。
- 在 Markdown 报告后使用 `---` 分隔，输出可解析的 `github_reader_data` YAML。
- Feed 包含 open issues、open PRs、近 14 天 merged PRs 与 closed issues 的 total 和 fetched 字段，以及健康信号。
- 四个总数均来自独立执行的 Search API `total_count`，没有用获取集合长度冒充总数。
- Markdown 完整性表与 YAML 一致：143/143、213/213、6/6、1/1；所有 Search 查询均为 `incomplete_results=false`，milestones 分页完成，因此两个完整性信号数组均为空。

## Without-Skill Baseline

- baseline 仅依据原始 prompt 独立查询，并输出 Markdown 报告和 fenced JSON 结构化块。
- Open issue 与 open PR 总数来自 GraphQL `totalCount`；近 14 天 merged PR 与 closed issue 只报告获取集合长度，没有查询 Search API `total_count`。
- 报告声明 release 明细截断为 20/213，但结构化 JSON 只有局部 `releases.truncated: true`，没有 Feed 契约要求的 `truncated_collections` / `incomplete_totals`。
- baseline 首次因 `gh release list` 使用不支持的 `url` 字段失败；validator 保留错误证据，修正字段后重新独立执行整套 baseline 查询并成功锁定，未复用 with-skill 数据。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge 结论 |
| --- | --- | --- | --- |
| `feed_yaml_present`：Markdown 后包含关键总数字段的 `github_reader_data` YAML | **PASS** | **FAIL** | with-skill 提供并成功解析 YAML；baseline 只有 fenced JSON，没有 Feed YAML。 |
| `completeness_signals_consistent`：结构化完整性信号与报告声明一致 | **PASS** | **FAIL** | with-skill 的 totals、fetched 和两个完整性数组与 Markdown 完全一致；baseline 没有规定的 Feed 完整性字段。 |
| `totals_not_fabricated`：YAML 总数来自 Search API `total_count` | **PASS** | **FAIL** | with-skill 保存了四个 Search API 原始响应；baseline 未使用 Search API totals，近期活动仅使用集合长度。 |

## Failures

- with-skill 无 assertion failure，也没有 GitHub、网络或认证失败。
- without-skill 失败 3 条 assertions，说明原始 prompt 本身不足以稳定触发 Feed YAML、统一完整性字段和 Search API count-first 契约。
- baseline 的首次命令兼容错误已显式记录；完整重跑成功，因此不构成本轮 infrastructure blocker。

## Next Steps

- 保持 **PASS**；eval-005 已覆盖本次新增的 Feed mode `truncated_collections` / `incomplete_totals` 契约。
- 后续 fresh run 必须重新查询 live GitHub，并重新生成 without-skill baseline，不复用本轮快照。
- 若目标仓库未来超过计算集合上限或 GitHub 返回 `incomplete_results=true`，应继续验证非空完整性数组与 Markdown 声明一致。

## Runtime Artifact Policy

- runtime 命令、时间、原始 JSON、两个报告、checksums、查询事件与 verdict 保存在 `tmp/eval-runs/github-reader-eval-005-2026-07-28/`，不纳入 git。
- canonical workspace 不保存 transcripts、raw outputs、timing、diagnostics 或 verdict；durable 结果仅为本 `comparison.md`。
- 本轮 fresh validation 未修改 canonical fixture、specialist `SKILL.md` 或 Agent README。
