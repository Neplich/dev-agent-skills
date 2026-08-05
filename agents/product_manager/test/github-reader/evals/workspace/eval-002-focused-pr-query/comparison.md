# Eval Result: eval-002-focused-pr-query

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-002-focused-pr-query`
- Test case: focused-pr-query
- Workspace: `workspace/eval-002-focused-pr-query`
- Classification: `(c) 依赖实时外部数据`。prompt、expected output、assertions 和 metadata 已足以定义 focused PR 查询；场景证据必须来自 GitHub 当前状态，不应添加静态 mock fixture。
- Latest result: **PASS** — 本轮由同一个 fresh Codex agent 完成 no-leak 双臂复验和最终 judge；with-skill 与 without-skill 均真实查询 `cli/cli`，且都满足 3 条 assertions。
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: `我在 cli/cli 这个仓库里工作，现在有哪些 PR 还在等待 review？按等待时间排序`
- Expected output: 聚焦 PR 的输出，列出 awaiting review 的 PR 并按等待时间排序，不需要输出 issue 和 milestone 数据
- Repository: `cli/cli` (`https://github.com/cli/cli`，default branch `trunk`)
- With-skill source: authenticated `gh repo view cli/cli` and `gh pr list -R cli/cli --state open --limit 100 --json number,title,state,author,reviewDecision,createdAt,labels,isDraft,url`
- With-skill fetched at: `2026-07-26 16:30:01 CST (+08:00)`
- Without-skill source: authenticated `gh pr list --repo cli/cli --state open --limit 100 --json number,title,author,isDraft,reviewDecision,createdAt,url`
- Without-skill fetched at: `2026-07-26 16:30:14 CST (+08:00)`

## Snapshot

- with-skill 查询观测到 55 个 open PR；按人工作者、非 draft、`reviewDecision=REVIEW_REQUIRED` 口径得到 31 个待 Review PR。
- without-skill 独立查询同样得到 31 个待 Review PR；两次查询相隔 13 秒，31 个 PR 的编号、顺序和最旧/最新边界完全一致，没有观察到状态漂移。
- 两臂锁定的 PR 编号依次为：`#10423`、`#10730`、`#10783`、`#12942`、`#13013`、`#13155`、`#13247`、`#13282`、`#13318`、`#13340`、`#13348`、`#13364`、`#13400`、`#13505`、`#13556`、`#13602`、`#13673`、`#13697`、`#13758`、`#13760`、`#13788`、`#13798`、`#13875`、`#13894`、`#13946`、`#13952`、`#13953`、`#13955`、`#13963`、`#13967`、`#13969`。
- 最旧三项均为 [#10423](https://github.com/cli/cli/pull/10423)（@iamazeem，528 天）、[#10730](https://github.com/cli/cli/pull/10730)（@cmbrose，477 天）、[#10783](https://github.com/cli/cli/pull/10783)（@franciscoj，467 天）；最新三项均为 #13963、#13967、#13969。
- with-skill 还观测到 18 个 draft、2 个非 bot `CHANGES_REQUESTED` PR 和 3 个非 bot `APPROVED` PR；Dependabot #13965 的 author login 在本轮 API 中表现为 `app/dependabot`，作为自动化 PR 从人工待 Review 清单剥离。

## Same-Agent No-Leak Fresh Pair

1. 当前 fresh agent 首先只读取 `eval_metadata.json` 的原 prompt；没有读取 `evals.json`、assertions、expected output 或历史 `comparison.md`。
2. with-skill 臂随后读取 PM Agent README 与当前 `github-reader/SKILL.md`，独立调用 `gh` 查询并锁定候选结果。
3. 同一个 agent 在第二臂不应用 PM Agent README 或 `github-reader` 指令，仅依据原 prompt 重新设计并执行独立 `gh` 查询；没有读取或使用答案键、父臂结果、assertions、expected output 或旧 comparison，随后锁定 without-skill 结果。
4. 两臂均锁定后，该 agent 才读取 `evals.json` 中本 eval 的 expected output、assertions 与历史 comparison，并亲自完成 judge；本轮没有 spawn child/subagent，也没有复用历史 baseline。

## Assertions

| Assertion | With skill | Without skill | Fresh judge |
| --- | --- | --- | --- |
| `pr`：聚焦 PR 不冗余 | 只查询 repo context 与 open PR，没有抓取 issue 或 milestone | 只查询并输出 open PR 的 focused 结果 | PASS |
| `assertion_2`：包含等待时间 | 31 条人工待 Review PR 均包含作者、等待天数和 labels | 31 条结果均包含作者和 `createdAt` | PASS |
| `assertion_3`：有排序 | 明确按 `createdAt` 升序，即等待最久在前 | 独立按 `createdAt` 升序；首项 #10423，末项 #13969 | PASS |

## With Skill

- 将请求识别为 focused PR query，只调用仓库上下文和 open PR 查询；未抓取无关 issue、milestone 或近期合并数据。
- 按自动化作者、draft 和 review decision 分类，排除 Dependabot #13965、draft、`CHANGES_REQUESTED` 与 `APPROVED` PR。
- 输出 31 个人工、非 draft、`REVIEW_REQUIRED` PR，包含链接、标题、作者、等待天数与 labels，并按创建时间从旧到新排列。
- focused 模式未套用 full-status 的 10 行上限。

## Without Skill / Baseline

- 同一个 fresh agent 在不应用 skill 或 PM README 的条件下，仅凭原 prompt 重新执行独立 `gh pr list` 查询。
- baseline 以 `reviewDecision=REVIEW_REQUIRED`、非 draft、非 GitHub App author 为口径，同样得到 31 条，并按 `createdAt` 从旧到新排列；每条包含链接、标题、作者和创建时间，没有输出 issue 或 milestone。
- baseline 没有输出等待天数和 labels，但 `createdAt` 已满足 assertion 对“等待天数或创建时间”的要求，因此 baseline 同样为 PASS。
- 对照价值在于确认当前通用 assertions 不强制 specialist 的 labels 增量，而不是要求 baseline 必须失败。

## Drift and Protocol Notes

- GitHub PR 状态、review decision、draft、labels 和等待时间持续变化；本 comparison 的数量只代表上述两个抓取时点。后续 fresh run 必须重新查询，不能把本轮 31 条当成固定答案。
- SKILL.md 的“强制分类流程”把非 bot、非 draft、非 `CHANGES_REQUESTED` 的“其余”归入待 Review，而 health signal 又把待 Review 明确定义为 `REVIEW_REQUIRED` 或空值；对 `APPROVED` 存在内部口径歧义。本轮按用户问题与 health signal 排除 3 个 `APPROVED` PR。当前 assertions 不要求裁决该分区冲突，且任务禁止修改 specialist 行为，因此只记录风险。
- GitHub App author 的 login 表示可能随 API 层变化；本轮 Dependabot 表示为 `app/dependabot`。后续复验应依据当次 API 的 bot/app 身份重新判断，不应把本轮 login 当成固定 fixture。

## Failures

- Skill regression: none observed against the three eval assertions.
- External dependency failure: none observed；本轮 `gh` CLI、GitHub API 和认证均正常。
- Remaining risk: specialist 对 `APPROVED` PR 的分区口径存在上述文档内歧义，但不影响本 eval 对 focused、作者/时间字段和排序的验证结论。

## External Dependency and Failure Interpretation

- 此 eval 必须联网并依赖 GitHub API、`gh` CLI 可用且已认证；后续复验必须重新抓取，不能复用本轮数量或伪造静态 snapshot。
- 若 `gh auth status`、DNS、网络、GitHub API、rate limit 或权限导致查询失败，应记录命令、抓取时间和外部错误，并将本轮标为 **BLOCKED / external service failure**；不能判为 skill regression，也不能用 mock 冒充 fresh 运行。
- 若 API 成功返回，但 with-skill 抓取无关 issue/milestone、遗漏作者或时间信息、未按等待时间排序，则属于 **skill regression**。

## Next Steps

- fixture 无需增加静态文件；未来复验继续真实查询 prompt 指定仓库，并在 canonical comparison 中更新抓取时间、snapshot 数量、same-agent no-leak fresh pair 和 drift 结论。
- 若后续要把 bot 分区或 `APPROVED` 处理纳入 pass/fail，应另行对齐 SKILL.md 口径并新增/收紧 assertion；本轮不修改 skill 或 eval 定义。

## Runtime Artifacts Policy

- 本轮运行期 snapshot、完整输出、verdict、timing 和 diagnostics 只用于 fresh judge，不提交到 Git。
- Durable result 仅保留本 canonical `comparison.md`；不得提交 `with_skill/`、`without_skill/`、`outputs/`、`transcript.md`、`subagent-verdict.md` 或 diagnostics 目录。
