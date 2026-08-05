# Eval Result: eval-003-milestone-focused

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-003-milestone-focused`
- Test case: milestone-focused
- Workspace: `workspace/eval-003-milestone-focused`
- Classification: `(c) 依赖实时外部数据`。该场景验证 specialist 是否通过 `gh` 查询真实 GitHub milestone；静态 fixture 会把时效性场景降级成 mock，因而不补造 fixture。
- Latest result: **PASS**。2026-07-26 的 same-agent fresh paired validation 中，with-skill 在第一次独立实时查询结果上满足 3/3 assertions；fresh without-skill baseline 在第二次独立查询结果上满足 2/3，未采用 skill 规定的 emoji 状态标识。
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: `看一下 facebook/react 最近的 milestone，哪个进度最慢或者已经逾期了？`
- Expected output: Milestone 状态报告，识别出进度最慢或逾期的 milestone，给出具体数据支撑
- Fixture basis: prompt 与 `eval_metadata.json` 已足够定义目标仓库和查询意图；业务证据必须在运行时从 GitHub API 获取。
- Fresh run: 当前会话中的同一个 fresh Codex agent 先读取 PM Agent README 与 `github-reader` skill，完成并锁定 with-skill；随后明确停止应用这些指令，仅凭 metadata 中的原始 prompt 完成并锁定新的 without-skill baseline。两边均为本轮新查询、新生成，未复用历史 baseline。
- No-leak control: 两条 arm 全部锁定之前，执行者只读取 `eval_metadata.json` 中的 prompt，以及 with-skill arm 必需的 PM Agent README 和 specialist skill；没有读取 `evals.json`、assertions、expected output 或旧 `comparison.md`。第二条 arm 没有复用第一次查询的响应或候选文本，而是再次独立调用 `gh`；两条 arm 锁定后才读取答案键并由同一 agent 亲自 judge。

## Live Data Snapshot

- With-skill fetched at: `2026-07-26 16:29:36 CST (+0800)`。
- Without-skill fetched at: `2026-07-26 16:29:52 CST (+0800)`。
- Access path: 两条路径由同一个 fresh agent 分别使用已认证的 `gh` CLI 调用 GitHub REST API；每条 arm 都发起自己的网络请求，没有共享预制 snapshot 或运行期文件。
- Repository resolution: 输入 `facebook/react`，GitHub 返回 canonical repository `react/react`（default branch `main`）。
- With-skill query scope: 仓库身份与全部 open milestones；按 focused-query 规则没有抓取无关 issue/PR 队列。
- Without-skill query scope: 再次独立查询全部 open milestones，并在该次响应上独立计算完成率。
- API fields retained for judgment: with-skill 保留 `number`, `title`, `state`, `open_issues`, `closed_issues`, `due_on`, `created_at`, `updated_at`, `html_url`；without-skill 保留回答 prompt 所需的 `number`, `title`, `state`, `open_issues`, `closed_issues`, `completion_pct`, `due_on`, `html_url`。

Open milestone snapshot:

| Milestone | State | Open | Closed | Completion | Due on | Updated at |
| --- | --- | ---: | ---: | ---: | --- | --- |
| [19.0.0](https://github.com/react/react/milestone/40) | open | 5 | 6 | 54.5% | `null` | `2024-06-29T16:17:34Z` |

The live data does not support an overdue claim: the only open milestone has no `due_on`. It does support identifying `19.0.0` as the slowest active milestone because it is the sole open milestone and is 6/11 complete (54.5%).

## Assertions

| Assertion | With skill | Without skill | Fresh judge evidence |
| --- | --- | --- | --- |
| `assertion_1`：明确指出逾期或进度最慢 | PASS | PASS | 两边都明确说明没有证据判定逾期，并把唯一 active milestone `19.0.0` 判为当前进度最慢；没有把 `due_on: null` 误报成逾期。 |
| `assertion_2`：每个 milestone 有 open/closed 或完成率 | PASS | PASS | 两边都给出 `19.0.0` 的 5 open、6 closed、总数 11 和 54.5%。 |
| `assertion_3`：使用规定 emoji 状态标识 | PASS | FAIL | with-skill 按协议使用 `⚪ 无截止日期`；baseline 只写“无截止日期”，未使用 `✅🟢🟡🔴⚪` 状态标识。 |

## With Skill

Fresh with-skill behavior:

- 读取 PM Agent README 与当前 `github-reader` skill，判定为 milestone-focused query，仅抓取所需 milestone 数据。
- 先通过 `gh repo view facebook/react` 解析目标仓库，再通过独立的 `gh api .../milestones` 请求取得全部 open milestones，并保留抓取时间、查询范围和用于计算的 API 字段。
- 将 `19.0.0` 报告为 `5/11 (54.5%)`、`⚪ 无截止日期`；明确指出“无截止日期”不等于逾期。
- 在只有一个 open milestone 的真实数据边界下，明确说明 `19.0.0` 是当前 active 集合中进度最慢，而不是虚构另一个比较对象。
- 按 focused-query 协议停止在 milestone 数据，没有为满足格式而扩展抓取无关 issue/PR 队列。

## Without Skill / Baseline

Fresh without-skill behavior:

- 同一个 fresh agent 在 with-skill 锁定后停止应用 `github-reader` skill 和 PM Agent README，仅凭原始 prompt 发起第二次独立 `gh api` 请求；此时仍未读取 eval 判分材料、旧 comparison 或答案键。
- 正确识别 canonical repository、唯一 open milestone、54.5% 完成率以及无可证实的逾期 milestone。
- 该 arm 直接在自己的 API 响应上计算完成率并按完成率排序，没有复用 with-skill 的响应或派生值。
- 结论仍有事实依据，因此通过 assertions 1 和 2。
- 采用普通文本“无截止日期”，没有 skill 规定的 emoji 状态标识，因此不满足 assertion 3。

## External Dependency and Failure Attribution

- External dependency: GitHub 可达性、`gh` 认证、REST API 响应、rate limit 和仓库公开状态都会影响本 eval；milestone 数量、issue 计数、截止日期与更新时间在未来运行中可能变化。
- External-service failure: 若 `gh auth status` 失败、DNS/网络不可达、GitHub API 返回 401/403/429/5xx、或无法取得有效 JSON snapshot，本次运行应记为 **BLOCKED (external service)**，不得判为 skill regression，也不得以静态 mock 代替。
- Valid empty result: API 成功但没有 open milestone 属于真实数据结果，不是外部失败；输出应明确“当前无 open milestone”，再按 prompt 与可用的 recent closed 数据解释无法比较 active 进度。此时 assertion 1 的可满足性需由 fresh judge 结合实时数据重新判断，不能虚构最慢或逾期对象。
- Skill regression: API 成功且 snapshot 可用，但 with-skill 未给出 open/closed 或完成率、把 `due_on: null` 误判成逾期、未明确回答“哪个最慢/逾期”，或未使用协议规定的 emoji 状态标识，才属于 skill 行为回归。
- Time-validity risk: 本文件的数值只代表上述抓取时点；未来复验必须重新抓取并记录新 snapshot，不能复用本轮数据冒充 fresh 结果。

## Failures

- With-skill: none.
- Without-skill baseline: 缺少 skill 规定的 emoji milestone 状态标识（`assertion_3`）。

## Next Steps

- 无需修改 fixture、`eval_metadata.json`、`evals.json` 或 specialist `SKILL.md`。
- 后续 fresh eval 继续让同一个 fresh agent 按顺序锁定两条路径，在相邻时间窗内各自实时查询，并分别记录抓取时间与查询范围；两条 arm 锁定前不得读取答案键，也不得把第一条 arm 的 API 响应或候选答案作为第二条 arm 的输入。

## Runtime Artifacts Policy

- 本次只更新 durable `comparison.md`。
- Runtime transcripts、candidate outputs、verdicts、timing、API dumps、diagnostics 与临时 snapshot 不提交到 git。
