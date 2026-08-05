# Eval Result: eval-003-prefix-classification

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-003-prefix-classification`
- Test case: prefix-classification
- Workspace: `workspace/eval-003-prefix-classification`
- Evaluation time: 2026-07-26 16:21:37 CST (+0800)
- Latest result: PASS - same-agent fresh `with_skill` 与 fresh `without_skill` baseline 均满足 13/13 assertions；本轮未观察到两 arm 的行为差异。
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Classification: (a) fixture 已足够，只缺合规的 fresh baseline。
- Reason: 14 条 PR 的标题、正文、编号以及 docs/test/ci 语义判断要求均完整内嵌在原始 prompt；assertions 验证的分类、标题清洗、跳过规则和 breaking 标记都不依赖仓库 fixture 或实时外部数据，因此无需添加 fixture 文件。
- Fixture change: 无。

## No-Answer-Key Fresh Method

本轮由同一个 fresh Codex evaluator 按以下隔离顺序执行；未委派其他 agent，候选锁定前不读取答案键：

1. 生成阶段首先只读取 workspace 的 `eval_metadata.json`，从中取得完整原始 prompt；未读取 `evals.json`、`expected_output`、assertions 或旧 `comparison.md`。
2. `with_skill` 阶段读取完整的当前 `agents/product_manager/README.md` 与 `agents/product_manager/skills/changelog-generator/SKILL.md`，仅依据原始 prompt 和 skill 契约独立生成并锁定候选。
3. 同一 evaluator 随后进入 `without_skill` 阶段，仅依据同一份原始 prompt 与通用 Keep a Changelog 语义独立生成并锁定 baseline；该阶段未读取或应用 Agent README、skill、`evals.json`、assertions、`expected_output` 或旧 comparison。
4. 两份候选都锁定后，才读取 `evals.json` 中本用例的 assertions、expected output 与旧 comparison，并逐项 judge；judge 阶段没有反向修改候选。

候选、transcript 与 judge diagnostics 均未写入仓库。

## Fresh Paired Results

### With Skill

锁定候选的行为摘要：

- Added：`#105 ⚠️ BREAKING: Redesign plugin configuration API`（置顶）、`#101 Add OAuth2 login support`
- Changed：`#104 Reduce API response time by caching`、`#106 Update release notes generator publishing workflow`、`#107 Tighten changelog-generator eval contract`、`#108 Require repository and eval contract checks before release`
- Fixed：`#102 Resolve crash when token expires`、`#111 Correct button alignment on mobile`
- Removed：`#112 Drop Python 3.7 support`
- Security：`#113 Patch XSS vulnerability in template renderer`
- 跳过：`#103 chore(deps)`、`#114 build(deps)`、`#109` 仅 typo/copyediting、`#110` 仅 cache maintenance

结论：13/13 assertions 通过。skill 正确保留 `feat!` 的 Added 映射并添加 breaking 标记，同时根据正文语义区分应纳入 Changed 的 docs/test/ci 与应跳过的低价值维护项。

### Without Skill / Baseline

锁定 baseline 的行为摘要：

- Added：`#105 ⚠️ BREAKING: Redesign plugin configuration API`（置顶）、`#101 Add OAuth2 login support`
- Changed：`#104 Reduce API response time by caching`、`#106 Update release notes generator publishing workflow`、`#107 Tighten changelog-generator eval contract`、`#108 Require repository and eval contract checks before release`
- Fixed：`#102 Resolve crash when token expires`、`#111 Correct button alignment on mobile`
- Removed：`#112 Drop Python 3.7 support`
- Security：`#113 Patch XSS vulnerability in template renderer`
- 跳过：`#103`、`#114`、`#109`、`#110`

结论：13/13 assertions 通过。baseline 单凭 prompt 与通用 Keep a Changelog 语义，也将 conventional `feat! #105` 保留在 Added 并添加 breaking 标记，同时完成 docs/test/ci 的语义筛选；本轮没有观察到 skill 相对 baseline 的行为增益。

## Assertion Review

| Assertion | With skill | Without skill | Result |
| --- | --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | #101 进入 Added，清洗为 `Add OAuth2 login support` | 相同 | Both PASS |
| `fix_fixed` | #102、#111 进入 Fixed | 相同 | Both PASS |
| `chore_deps` | 跳过 #103 | 相同 | Both PASS |
| `build_deps_skipped` | 跳过 #114 | 相同 | Both PASS |
| `perf_changed` | #104 进入 Changed | 相同 | Both PASS |
| `feat_added_breaking` | #105 进入 Added，带 `⚠️ BREAKING` 且置顶 | 相同 | Both PASS |
| `docs_release_workflow_changed` | 根据正文将 #106 纳入 Changed | 相同 | Both PASS |
| `test_eval_contract_changed` | 根据正文将 #107 纳入 Changed | 相同 | Both PASS |
| `ci_release_gate_changed` | 根据正文将 #108 纳入 Changed | 相同 | Both PASS |
| `docs_typo_skipped` | 跳过仅 copyediting 的 #109 | 相同 | Both PASS |
| `ci_cache_skipped` | 跳过仅 cache maintenance 的 #110 | 相同 | Both PASS |
| `remove_removed` | #112 进入 Removed | 相同 | Both PASS |
| `security_security` | #113 进入 Security | 相同 | Both PASS |

## Failures

- `with_skill` 与 `without_skill` baseline 均无 assertion failure。
- 本轮 same-agent fresh baseline 与历史记录不同：本轮在读取答案键前已将 `feat! #105` 锁定为 Added，而不是 Changed。canonical comparison 已按本轮真实结果纠正，未复用或迁就历史 baseline。

## Risks / Next Steps

- 本用例使用 prompt 内嵌的确定性 PR 数据，不验证 GitHub API、`gh` CLI、分页或日期窗口行为；这些能力由 changelog-generator 的实时数据 eval 覆盖。
- prompt 已直接给出 docs/test/ci 需要按正文语义判断的要求，并且 conventional `feat!` 的 Added 归类可由通用知识正确推导，因此 baseline 全部通过是合理结果；该用例本轮证明 skill 行为满足契约，但未证明相对无 skill baseline 的可观察增益。
- 保留此用例作为 conventional prefix、breaking change 和低优先级前缀语义审查的回归覆盖。

## Runtime Artifact Policy

- 本轮只持久化 canonical `comparison.md`。
- Fresh candidates、transcripts、judge verdict、timing、diagnostics 与其他运行期产物不提交到 git。
