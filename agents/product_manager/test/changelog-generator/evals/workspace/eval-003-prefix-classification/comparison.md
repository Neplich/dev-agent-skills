# Eval Result: eval-003-prefix-classification

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-003-prefix-classification`
- Test case: prefix-classification
- Workspace: `workspace/eval-003-prefix-classification`
- Evaluation date: 2026-07-26 (Asia/Shanghai)
- Latest result: PASS - 本轮 fresh `with_skill` 与 fresh `without_skill` baseline 均满足全部 13 条 assertions。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Classification: (a) fixture 已足够，只缺 fresh baseline。
- Reason: 14 条 PR 的标题、正文、编号以及 docs/test/ci 语义判断要求均完整内嵌在 prompt；13 条 assertions 只验证这些输入的分类、标题清洗、跳过规则和 breaking 标记，不依赖仓库文件或实时外部数据，因此无需添加 fixture 文件。
- Expected output: Added 包含 feat；Changed 包含 perf 及具有 release workflow、eval contract、required gate 语义影响的 docs/test/ci；Fixed 包含 fix；Removed 包含 remove；Security 包含 security；跳过 dependency bump、仅 copyediting 的 docs 和仅 cache maintenance 的 ci；#105 带 `⚠️ BREAKING` 标记。

## Fresh Paired Results

### With Skill

本轮 fresh judge 读取当前 `agents/product_manager/README.md`、`changelog-generator/SKILL.md`、prefix reference、eval prompt 与 assertions 后，按 skill 协议独立生成结果：

- Added：`#105 ⚠️ BREAKING: Redesign plugin configuration API`（置顶）、`#101 Add OAuth2 login support`
- Changed：`#104 Reduce API response time by caching`、`#106 Update release notes generator publishing workflow`、`#107 Tighten changelog-generator eval contract`、`#108 Require repository and eval contract checks before release`
- Fixed：`#102 Resolve crash when token expires`、`#111 Correct button alignment on mobile`
- Removed：`#112 Drop Python 3.7 support`
- Security：`#113 Patch XSS vulnerability in template renderer`
- 跳过：`#103 chore(deps)`、`#114 build(deps)`、`#109` 仅 typo/copyediting、`#110` 仅 cache maintenance

结论：skill 不仅按 conventional prefix 分类，也读取正文区分具有契约或发布影响的 docs/test/ci 与低价值维护项；全部 assertions 通过。

### Without Skill / Baseline

本轮 fresh judge 在不读取或应用 skill、Agent README 与 prefix reference 的 baseline 条件下，仅使用相同 prompt 和 assertions 重新生成结果：

- Added：`#105 ⚠️ BREAKING: Redesign plugin configuration API`、`#101 Add OAuth2 login support`
- Changed：`#104 Reduce API response time by caching`、`#106 Update release notes generator publishing workflow`、`#107 Tighten changelog-generator eval contract`、`#108 Require repository and eval contract checks before release`
- Fixed：`#102 Resolve crash when token expires`、`#111 Correct button alignment on mobile`
- Removed：`#112 Drop Python 3.7 support`
- Security：`#113 Patch XSS vulnerability in template renderer`
- 跳过：`#103`、`#114`、`#109`、`#110`

结论：baseline 也满足全部 assertions。原因是 prompt 本身已显式要求按正文语义审查 docs/test/ci，并提供足够明确的 PR 正文；这说明该用例可验证 skill 行为未回归，但不是证明这些基础分类只能依赖 skill 才能完成。

## Assertion Review

| Assertion | With skill | Without skill | Result |
| --- | --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | #101 进入 Added，清洗为 `Add OAuth2 login support` | 相同 | PASS |
| `fix_fixed` | #102、#111 进入 Fixed | 相同 | PASS |
| `chore_deps` | 跳过 #103 | 相同 | PASS |
| `build_deps_skipped` | 跳过 #114 | 相同 | PASS |
| `perf_changed` | #104 进入 Changed | 相同 | PASS |
| `feat_added_breaking` | #105 进入 Added，带 `⚠️ BREAKING` 且置顶 | 带 `⚠️ BREAKING` | PASS |
| `docs_release_workflow_changed` | 根据正文将 #106 纳入 Changed | 相同 | PASS |
| `test_eval_contract_changed` | 根据正文将 #107 纳入 Changed | 相同 | PASS |
| `ci_release_gate_changed` | 根据正文将 #108 纳入 Changed | 相同 | PASS |
| `docs_typo_skipped` | 跳过仅 copyediting 的 #109 | 相同 | PASS |
| `ci_cache_skipped` | 跳过仅 cache maintenance 的 #110 | 相同 | PASS |
| `remove_removed` | #112 进入 Removed | 相同 | PASS |
| `security_security` | #113 进入 Security | 相同 | PASS |

## Failures

- 无 assertion failure。
- 历史 PARTIAL 的原因是缺少 `without_skill` baseline；本轮已用同一 prompt 和 assertions 重新生成成对结果，不复用历史 baseline。

## Risks / Next Steps

- 本用例使用 prompt 内嵌的确定性 PR 数据，不验证 GitHub API、`gh` CLI、分页或日期窗口行为；这些能力由 changelog-generator 的实时数据 eval 覆盖。
- baseline 同样 PASS 是预期且可解释的：prompt 已直接提供关键语义规则。回归价值在于确认 skill 没有把 docs/test/ci 机械跳过，也没有错误纳入低价值维护项。
- 保留此用例作为 conventional prefix、breaking change 和低优先级前缀语义审查的回归覆盖。

## Runtime Artifacts Policy

- 本轮只持久化 canonical `comparison.md`。
- Fresh outputs、transcripts、judge verdict、timing、diagnostics 与其他运行期产物不提交到 git；本仓库没有该 specialist 的 deterministic transcript runner 时，不以虚构 transcript 代替 fresh judge 证据。
