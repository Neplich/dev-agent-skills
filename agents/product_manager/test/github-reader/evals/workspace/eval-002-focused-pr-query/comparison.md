# Eval Result: eval-002-focused-pr-query

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-002-focused-pr-query`
- Test case: focused-pr-query
- Workspace: `workspace/eval-002-focused-pr-query`
- Classification: `(c) 依赖实时外部数据`。prompt、expected output、assertions 和 metadata 已足以定义 focused PR 查询；场景证据必须来自 GitHub 当前状态，不应添加静态 mock fixture。
- Latest result: **PASS** — 本轮 no-leak fresh pair 均真实查询 `cli/cli`；with-skill 与 without-skill 都满足 3 条 assertions。with-skill 额外按 specialist 规则把 Dependabot 从人工待 Review 表格剥离，并保留 labels。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: `我在 cli/cli 这个仓库里工作，现在有哪些 PR 还在等待 review？按等待时间排序`
- Expected output: 聚焦 PR 的输出，列出 awaiting review 的 PR 并按等待时间排序，不需要输出 issue 和 milestone 数据
- Repository: `cli/cli` (`https://github.com/cli/cli`，default branch `trunk`)
- With-skill source: authenticated `gh repo view cli/cli` and `gh pr list --repo cli/cli --state open --limit 100 --json number,title,state,author,reviewDecision,createdAt,labels,isDraft,url`
- With-skill fetched at: `2026-07-26 15:47:39 CST (+08:00)`
- Without-skill source: authenticated `gh api graphql`，完整分页查询 `cli/cli` open PR，`hasNextPage=false`
- Without-skill fetched at: `2026-07-26 15:49:40 CST (+08:00)`

## Snapshot

- 两次查询均观测到 55 个 open PR；两分钟窗口内关键计数和排序边界一致，没有观察到 PR 状态漂移。
- 快照包含 49 个 `REVIEW_REQUIRED` PR，其中 17 个是 draft；另有 1 个 `reviewDecision` 为空的 draft、3 个 `APPROVED`、2 个 `CHANGES_REQUESTED`。
- 当前有 2 个自动化作者：非 draft 的 Dependabot PR #13965，以及 draft 的 Copilot agent PR #13017。
- 本轮将“等待 review”按 SKILL.md 的 health signal 定义解释为非 draft 且 `reviewDecision` 为 `REVIEW_REQUIRED` 或空值。with-skill 剥离 bot 后得到 31 个人工待 Review PR；without-skill 得到 32 个，但其中包含 Dependabot #13965。
- 两路结果最旧三项均为 [#10423](https://github.com/cli/cli/pull/10423)（@iamazeem，528 天）、[#10730](https://github.com/cli/cli/pull/10730)（@cmbrose，477 天）、[#10783](https://github.com/cli/cli/pull/10783)（@franciscoj，467 天）；人工结果最新三项均为 #13963、#13967、#13969。

## No-Leak Fresh Pair

1. 主 judge 首先只读取 `eval_metadata.json` 的原 prompt；没有读取 `evals.json`、assertions、expected output 或历史 `comparison.md`。
2. with-skill 路径随后读取 PM Agent README 与当前 `github-reader/SKILL.md`，独立调用 `gh` 查询并锁定候选结果。
3. 候选锁定后，启动 `fork_turns=none` 的 fresh Codex subagent。它只收到原 prompt，以及“自行实时查询并报告时间、数据源和关键数量”的要求；没有收到 skill、Agent README、答案键、父进程 snapshot、assertions 或旧 comparison。
4. baseline 返回并锁定后，主 judge 才读取 assertions、expected output 和历史 comparison，逐项裁决。

## Assertions

| Assertion | With skill | Without skill | Fresh judge |
| --- | --- | --- | --- |
| `pr`：聚焦 PR 不冗余 | 只查询并输出 repo context 与 open PR，没有抓取 issue 或 milestone | 只输出 open PR 的 focused 结果 | PASS |
| `assertion_2`：包含等待时间 | 31 条人工待 Review PR 均包含作者、等待天数或 `createdAt`，并包含 labels | 32 条结果均包含作者、精确到小时的等待时间和创建日期 | PASS |
| `assertion_3`：有排序 | 明确按 `createdAt` 升序，即等待最久在前 | 明确按等待时间从长到短；首项 #10423，末项 #13969 | PASS |

## With Skill

- 将请求识别为 focused PR query，只调用仓库上下文和 open PR 查询；未抓取无关 issue、milestone 或近期合并数据。
- 先按 `author.is_bot` / GitHub App 身份剥离自动化作者，再排除 draft、`CHANGES_REQUESTED` 与已 `APPROVED` PR。
- 输出 31 个人工、非 draft、`REVIEW_REQUIRED` PR，包含链接、标题、作者、等待天数与 labels，并按创建时间从旧到新排列。
- focused 模式未套用 full-status 的 10 行上限。

## Without Skill / Baseline

- fresh child 不读取或应用本地 skill、Agent README、eval 定义或历史结果，自行通过 GitHub GraphQL 查询全部 55 个 open PR。
- baseline 以 `reviewDecision=REVIEW_REQUIRED` 且非 draft 为口径，得到 32 条并按等待时间从长到短排列；每条包含链接、作者、等待时间和创建日期，没有输出 issue 或 milestone。
- baseline 没有执行 specialist 的 bot-first 分区，把 Dependabot #13965 混入人工清单；它也没有输出 labels。
- 这些差异不违反当前 3 条通用 assertions，因此 baseline 同样为 PASS；对照价值在于验证 specialist 的 bot 分类与 labels 增量，而不是要求 baseline 必须失败。

## Drift and Protocol Notes

- GitHub PR 状态、review decision、draft、labels 和等待时间持续变化；本 comparison 的数量只代表上述两个抓取时点。两次 fresh 查询相隔约 2 分钟，关键集合没有漂移，但等待时长显示精度不同。
- 历史 comparison 在 `2026-07-26 15:22:48 +08:00` 把 3 个 `APPROVED` PR 也归入待 Review，记录为 34 条。当前 fresh run 依据 SKILL.md 的 health signal 定义排除 `APPROVED`，得到 31 条人工待 Review；这是口径修正，不是 GitHub 状态变化。
- SKILL.md 的“强制分类流程”把非 bot、非 draft、非 `CHANGES_REQUESTED` 的“其余”归入待 Review，而 health signal 又把待 Review 明确定义为 `REVIEW_REQUIRED` 或空值；对 `APPROVED` 存在内部口径歧义。本轮 assertions 不要求裁决该分区冲突，且任务禁止修改 specialist 行为，因此仅如实记录风险。

## Failures

- Skill regression: none observed against the three eval assertions.
- External dependency failure: none observed；本轮 `gh` CLI、GitHub REST/GraphQL API 和认证均正常。
- Remaining risk: specialist 对 `APPROVED` PR 的分区口径存在上述文档内歧义，但不影响本 eval 对 focused、作者/时间字段和排序的验证结论。

## External Dependency and Failure Interpretation

- 此 eval 必须联网并依赖 GitHub API、`gh` CLI 可用且已认证；后续复验必须重新抓取，不能复用本轮数量或伪造静态 snapshot。
- 若 `gh auth status`、DNS、网络、GitHub API、rate limit 或权限导致查询失败，应记录命令、抓取时间和外部错误，并将本轮标为 **BLOCKED / external service failure**；不能判为 skill regression，也不能用 mock 冒充 fresh 运行。
- 若 API 成功返回，但 with-skill 抓取无关 issue/milestone、遗漏作者或时间信息、未按等待时间排序，则属于 **skill regression**。
- GitHub App author 表示法可能变化；后续运行应基于当次 API 的 `author.is_bot` 与登录名重新识别，不能硬套本轮 `app/dependabot` 文本。

## Next Steps

- fixture 无需增加静态文件；未来复验继续真实查询 prompt 指定仓库，并在 canonical comparison 中更新抓取时间、snapshot 数量、no-leak fresh pair 和 drift 结论。
- 若后续要把 bot 分区或 `APPROVED` 处理纳入 pass/fail，应另行对齐 SKILL.md 口径并新增/收紧 assertion；本轮不修改 skill 或 eval 定义。

## Runtime Artifacts Policy

- 本轮运行期 snapshot、transcripts、完整输出、verdict、timing 和 diagnostics 只用于 fresh judge，不提交到 Git。
- Durable result 仅保留本 canonical `comparison.md`；不得提交 `with_skill/`、`without_skill/`、`outputs/`、`transcript.md`、`subagent-verdict.md` 或 diagnostics 目录。
