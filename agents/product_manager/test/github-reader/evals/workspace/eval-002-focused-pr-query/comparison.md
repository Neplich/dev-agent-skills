# Eval Result: eval-002-focused-pr-query

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-002-focused-pr-query`
- Test case: focused-pr-query
- Workspace: `workspace/eval-002-focused-pr-query`
- Classification: `(c) 依赖实时外部数据`。prompt、expected output、assertions 和 metadata 已足以定义 focused PR 查询；该场景的证据来自 GitHub API 当前状态，不应添加静态 mock fixture。
- Latest result: **PASS** — 本轮 fresh judge 使用同一份实时 `cli/cli` open PR snapshot，分别重新生成 with-skill 与 without-skill 结果；with-skill 满足全部 3 条 assertions，并保留 specialist 的 focused-query、自动化账号剥离、状态分区和等待时间排序规则。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: `我在 cli/cli 这个仓库里工作，现在有哪些 PR 还在等待 review？按等待时间排序`
- Expected output: 聚焦 PR 的输出，列出 awaiting review 的 PR 并按等待时间排序，不需要输出 issue 和 milestone 数据
- Data source: authenticated `gh repo view cli/cli` and `gh pr list --repo cli/cli --state open --limit 200 --json number,title,author,reviewDecision,createdAt,labels,isDraft,url`
- Repository: `cli/cli` (`https://github.com/cli/cli`, default branch `trunk`)
- Fetched at: `2026-07-26T15:22:48+08:00`
- Snapshot size: 55 open PRs。按 github-reader 的强制分区顺序及 GitHub App 作者表示法归一化后，2 个自动化 PR（`app/dependabot`、`app/copilot-swe-agent`）、17 个人工草稿、2 个 `CHANGES_REQUESTED`，其余 34 个进入待 Review 清单。
- Snapshot edge evidence: 待 Review 清单最旧三项为 [#10423](https://github.com/cli/cli/pull/10423)（@iamazeem，528 天）、[#10730](https://github.com/cli/cli/pull/10730)（@cmbrose，477 天）、[#10783](https://github.com/cli/cli/pull/10783)（@franciscoj，467 天）；最新三项为 [#13963](https://github.com/cli/cli/pull/13963)、[#13967](https://github.com/cli/cli/pull/13967)、[#13969](https://github.com/cli/cli/pull/13969)，均为 1 天。
- Protocol note: snapshot 中有 3 个非草稿人工 PR 的 `reviewDecision=APPROVED`。with-skill 遵循 SKILL.md 标记为强制的分类顺序，将非 bot、非草稿且非 `CHANGES_REQUESTED` 的剩余 PR 归入待 Review；此处记录的是当前 skill 协议表现，不改写 skill 或 assertions。

## Assertions

| Assertion | With skill | Without skill | Fresh judge |
| --- | --- | --- | --- |
| `pr`：聚焦 PR 不冗余 | 只输出 PR focused 结果及必要分类摘要，没有抓取或展开 issue、milestone | 只输出 PR 表格，没有 issue、milestone | PASS |
| `assertion_2`：包含等待时间 | 34 条待 Review PR 均带作者和基于 `createdAt` 计算的等待天数 | 32 条字面 review-required 结果均带作者和等待天数 | PASS |
| `assertion_3`：有排序 | 明确按 `createdAt` 升序，最旧在前；首项 #10423，末项 #13969 | 同样按 `createdAt` 升序并明确说明最旧在前 | PASS |

## With Skill

Fresh with-skill run:

- 读取 PM Agent 路由边界和当前 `github-reader` specialist 协议后，将请求识别为 focused query，只调用仓库上下文和 open PR 查询，没有抓取无关 issue 或 milestone。
- 对 55 个 open PR 先识别自动化作者。当前 `gh` 将 GitHub App 作者显示为 `app/dependabot` 和 `app/copilot-swe-agent`，运行时将其规范化为 bot/automation，避免混入人工待 Review 或人工草稿。
- 再依次剥离 17 个人工草稿和 2 个 `CHANGES_REQUESTED` PR；按 skill 的强制分类流程把其余 34 个 PR 放入待 Review。
- 34 条结果均包含链接、标题、作者、等待天数和 labels，并以 `createdAt` 从旧到新排序。focused 模式没有套用 full-status 的 10 行上限。
- 对 snapshot 内 3 个 `APPROVED` PR 按当前强制分区规则保留在“其余 → 待 Review”；没有悄悄用模型常识改写 specialist 协议。

## Without Skill / Baseline

Fresh without-skill baseline:

- 在不读取或应用 github-reader SKILL.md、PM Agent README 的条件下，仅根据相同 prompt 和同一份 `2026-07-26T15:22:48+08:00` snapshot 重新生成。
- baseline 将“等待 review”按字面解释为非草稿且 `reviewDecision=REVIEW_REQUIRED` 或空值，排除 `APPROVED` 和 `CHANGES_REQUESTED`，得到 32 条并按最旧在前排序；每条包含作者和等待天数，且没有输出 issue/milestone。
- baseline 因缺少 specialist 的 bot-first 分类规则，将 `app/dependabot` 的 #13965 留在人工结果中，也没有给出 bot、草稿、changes-requested 的完整分区摘要。
- baseline 仍满足当前三条通用 assertions；对照价值在于确认 with-skill 额外保留了当前 specialist 的分类协议，而不是说明 baseline 必须失败。

## Failures

- Skill regression: none observed.
- External dependency failure: none observed；本轮 `gh` 查询和 GitHub API 均成功返回。

## External Dependency and Failure Interpretation

- 此 eval 必须联网并依赖 GitHub API、`gh` CLI 可用且已认证。PR 数量、review decision、draft 状态、labels 和等待天数都会随时间变化，以上数量只代表抓取时点。
- 若 `gh auth status`、DNS、网络、GitHub API、rate limit 或权限导致查询失败，应记录命令、抓取时间和外部错误，并将本轮结果标为 **BLOCKED / external service failure**；不能把它判成 skill 回归，也不能用静态 mock 冒充本轮 fresh 运行。
- 若 API 成功返回，但 with-skill 抓取了无关 issue/milestone、遗漏作者/等待时间、未按时间排序，或未按当前协议剥离自动化、草稿和 changes-requested，则属于 **skill regression**。
- GitHub 可能改变 App author 的展示形式；`app/dependabot` 等当前表示法具有时效风险。后续运行应根据当次 API 返回重新核对自动化身份，不应复用本轮计数。

## Next Steps

- 当前 fixture 无需增加静态文件；未来复验继续真实查询 prompt 指定仓库，并在 canonical comparison 中更新抓取时间、snapshot 数量与 fresh pair 结论。

## Runtime Artifacts Policy

- 本轮运行期 snapshot、transcripts、完整输出、verdict、timing 和 diagnostics 只用于 fresh judge，不提交到 Git。
- Durable result 仅保留本 canonical `comparison.md`；不得提交 `with_skill/`、`without_skill/`、`outputs/`、`transcript.md`、`subagent-verdict.md` 或 diagnostics 目录。
