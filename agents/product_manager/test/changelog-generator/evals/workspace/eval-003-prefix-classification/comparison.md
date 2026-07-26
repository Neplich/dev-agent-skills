# Eval Result: eval-003-prefix-classification

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-003-prefix-classification`
- Test case: prefix-classification
- Workspace: `workspace/eval-003-prefix-classification`
- Evaluation time: 2026-07-26 15:32:35 CST (+0800)
- Latest result: PASS - fresh `with_skill` 满足 13/13 assertions；独立生成的 fresh `without_skill` baseline 满足 12/13，暴露出 breaking `feat!` 章节归属差异。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Classification: (a) fixture 已足够，只缺合规的 fresh baseline。
- Reason: 14 条 PR 的标题、正文、编号以及 docs/test/ci 语义判断要求均完整内嵌在原始 prompt；assertions 验证的分类、标题清洗、跳过规则和 breaking 标记都不依赖仓库 fixture 或实时外部数据，因此无需添加 fixture 文件。
- Fixture change: 无。

## No-Answer-Key Fresh Method

本轮 fresh Codex evaluator 按以下隔离顺序执行，候选锁定前不读取答案键：

1. 生成阶段首先只读取 workspace 的 `eval_metadata.json`，从中取得完整原始 prompt；未读取 `evals.json`、`expected_output`、assertions 或旧 `comparison.md`。
2. `with_skill` 阶段读取当前 `agents/product_manager/README.md` 与 `agents/product_manager/skills/changelog-generator/SKILL.md`，仅依据原始 prompt 和 skill 契约独立生成并锁定候选。
3. `without_skill` 阶段仅依据同一份原始 prompt 独立生成并锁定 baseline；未读取或应用 Agent README、skill、`evals.json`、assertions、`expected_output` 或旧 comparison。
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

- Added：`#101 Add OAuth2 login support`
- Changed：`#104 Reduce API response time by caching`、`#105 ⚠️ BREAKING: Redesign plugin configuration API`、`#106 Update release notes generator publishing workflow`、`#107 Tighten changelog-generator eval contract`、`#108 Require repository and eval contract checks before release`
- Fixed：`#102 Resolve crash when token expires`、`#111 Correct button alignment on mobile`
- Removed：`#112 Drop Python 3.7 support`
- Security：`#113 Patch XSS vulnerability in template renderer`
- 跳过：`#103`、`#114`、`#109`、`#110`

结论：12/13 assertions 通过。baseline 单凭 prompt 也能完成 docs/test/ci 的语义筛选和多数 conventional prefix 分类，但把描述“重设计既有 API”的 breaking `feat! #105` 按语义放入 Changed；当前 skill 契约要求 `feat!` 仍归 Added，并以 `⚠️ BREAKING` 标记，因此 `feat_added_breaking` 未通过。

## Assertion Review

| Assertion | With skill | Without skill | Result |
| --- | --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | #101 进入 Added，清洗为 `Add OAuth2 login support` | 相同 | Both PASS |
| `fix_fixed` | #102、#111 进入 Fixed | 相同 | Both PASS |
| `chore_deps` | 跳过 #103 | 相同 | Both PASS |
| `build_deps_skipped` | 跳过 #114 | 相同 | Both PASS |
| `perf_changed` | #104 进入 Changed | 相同 | Both PASS |
| `feat_added_breaking` | #105 进入 Added，带 `⚠️ BREAKING` 且置顶 | #105 带 breaking 标记但进入 Changed | With skill PASS / Baseline FAIL |
| `docs_release_workflow_changed` | 根据正文将 #106 纳入 Changed | 相同 | Both PASS |
| `test_eval_contract_changed` | 根据正文将 #107 纳入 Changed | 相同 | Both PASS |
| `ci_release_gate_changed` | 根据正文将 #108 纳入 Changed | 相同 | Both PASS |
| `docs_typo_skipped` | 跳过仅 copyediting 的 #109 | 相同 | Both PASS |
| `ci_cache_skipped` | 跳过仅 cache maintenance 的 #110 | 相同 | Both PASS |
| `remove_removed` | #112 进入 Removed | 相同 | Both PASS |
| `security_security` | #113 进入 Security | 相同 | Both PASS |

## Failures

- `with_skill` 无 assertion failure。
- `without_skill` baseline 未满足 `feat_added_breaking`：breaking 标记正确，但章节错误地归入 Changed，而不是 Added。
- 旧 comparison 的 baseline 描述受答案键污染：它声称生成时使用了 assertions，并把 baseline 记录成与 expected output 完全一致。本轮已用严格的 no-answer-key 顺序重新生成候选并纠正该记录；未复用旧 baseline。

## Risks / Next Steps

- 本用例使用 prompt 内嵌的确定性 PR 数据，不验证 GitHub API、`gh` CLI、分页或日期窗口行为；这些能力由 changelog-generator 的实时数据 eval 覆盖。
- prompt 已直接给出 docs/test/ci 需要按正文语义判断的要求，因此 baseline 在这部分同样通过并不削弱用例有效性；本轮差异表明 skill 对 breaking conventional prefix 的明确映射提供了可观察增益。
- 保留此用例作为 conventional prefix、breaking change 和低优先级前缀语义审查的回归覆盖。

## Runtime Artifact Policy

- 本轮只持久化 canonical `comparison.md`。
- Fresh candidates、transcripts、judge verdict、timing、diagnostics 与其他运行期产物不提交到 git。
