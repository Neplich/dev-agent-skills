# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3dfcf246dc4057e8231ee4e2380b4525eeecf840a484daf60bd4e990283d5e5e`
- Skill overlay SHA-256: `5c214a0a2c2365016d6b3bafaa3e6cd9bb33067b007f4407a0b78fe50c4ba935`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a13934e813a2542c7822dc8e78db937ac0ee61dc52a8ddd247b8b0f1be1069a9`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | PASS | with_skill 输出将 #101 放入 Added，并清洗为“Add OAuth2 login support”。 |
| `fix_fixed` | PASS | with_skill 输出将 #102 放入 Fixed。 |
| `chore_deps` | PASS | with_skill 输出未列出 #103，且明确跳过依赖升级。 |
| `build_deps_skipped` | PASS | with_skill 输出未列出 #114，且明确跳过依赖升级。 |
| `perf_changed` | PASS | with_skill 输出将 #104 放入 Changed。 |
| `feat_added_breaking` | PASS | with_skill 输出将 #105 放入 Added，并以“⚠️ BREAKING”前缀标记。 |
| `docs_release_workflow_changed` | PASS | with_skill 输出将包含 draft releases、changelog preflight、tag retargeting 和 publishing review rules 的 #106 放入 Changed。 |
| `test_release_acceptance_changed` | PASS | with_skill 输出将发布验收覆盖率及发布证据要求变更的 #107 放入 Changed。 |
| `ci_release_gate_changed` | PASS | with_skill 输出将 required repository checks 的 #108 放入 Changed。 |
| `docs_typo_skipped` | PASS | with_skill 输出未列出 #109，并明确跳过 README 拼写修正。 |
| `ci_cache_skipped` | PASS | with_skill 输出未列出 #110，并明确跳过内部缓存维护。 |
| `remove_removed` | PASS | with_skill 输出将 #112 放入 Removed。 |
| `security_security` | PASS | with_skill 输出将 #113 放入 Security。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5237c20d2683883c996eb1df293f661940a25bbc22236142dd7bd332ff5420c0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确整理 Added、Changed、Fixed、Removed、Security 章节，清洗标题并标记破坏性变更，同时跳过无意义内部维护项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cd52450af87a9cb43b9f603492d4d4130297fb14b1a50ca7f03a8a039eec758e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确整理所有用户可见变更、跳过内部维护项，并输出中文 Keep a Changelog；作为 fresh baseline 整体满足断言。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-003-prefix-classification

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`
- Test case: `prefix-classification`
- Prompt:

> 以下是一批 PR 标题和正文，帮我把它们分类到 Keep a Changelog 的各个章节（Added/Changed/Fixed/Deprecated/Removed/Security），并按格式输出，跳过不需要出现在 changelog 的条目。注意：docs/test/ci 不能只按前缀跳过，需要根据正文判断是否影响用户可见能力、skill 行为、eval 契约、release workflow、installation 或协作边界。
>
> - feat(auth): add OAuth2 login support (#101)
>   Body: Adds a new OAuth2 login flow for users.
> - fix: resolve crash when token expires (#102)
>   Body: Fixes a user-visible crash.
> - chore(deps): bump requests from 2.28 to 2.31 (#103)
>   Body: Dependency maintenance only.
> - build(deps): bump vite from 5.0.0 to 5.0.1 (#114)
>   Body: Dependency maintenance only.
> - perf: reduce API response time by caching (#104)
>   Body: Improves response time.
> - feat!: redesign plugin configuration API (#105)
>   Body: BREAKING CHANGE: plugin configuration fields changed.
> - docs: update release notes generator publishing workflow (#106)
>   Body: Adds GitHub draft release, changelog preflight, tag retargeting, and publishing review rules used by release owners.
> - test: tighten changelog-gen eval contract (#107)
>   Body: Updates eval assertions and durable comparison requirements so docs/test/ci PRs are judged by semantic impact.
> - ci: require repository and eval contract checks before release (#108)
>   Body: Changes required release gates for this skill marketplace.
> - docs: fix typo in README heading (#109)
>   Body: Copyediting only; no behavior or workflow change.
> - ci: tune cache restore key (#110)
>   Body: Internal cache maintenance only; no release gate change.
> - fix(ui): correct button alignment on mobile (#111)
>   Body: Fixes visible UI layout.
> - remove: drop Python 3.7 support (#112)
>   Body: Removes unsupported runtime.
> - security: patch XSS vulnerability in template renderer (#113)
>   Body: Fixes a security vulnerability.

- Expected output:

> Added: feat items. Changed: perf items plus docs/test/ci items with semantic impact. Fixed: fix items. Removed: remove items. Security: security items. 跳过 chore(deps)、build(deps)、formatting-only docs 和 cache-only ci。Breaking change (#105) 带 ⚠️ BREAKING 前缀。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`（0 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS
- With-skill summary: with_skill 加载了 changelog-gen（status.json skill_load_hits=2；transcript 先读取 SKILL.md），输出完整且正确分类所有条目，并准确跳过三类维护项；fixture-manifest 未被写入。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 加载了 changelog-gen（status.json skill_load_hits=2；transcript 先读取 SKILL.md），输出完整且正确分类所有条目，并准确跳过三类维护项；fixture-manifest 未被写入。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），作为对照其输出遗漏了若干标题清洗/格式细节，但不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | **PASS** | with_skill candidate.md 将 #101 放入 Added，并输出“**auth:** Add OAuth2 login support”。 | without_skill 也将 #101 放入 Added，但使用中文标题。 |
| `fix_fixed` | **PASS** | with_skill candidate.md 将 #102 放入 Fixed，输出“Resolve crash when token expires”。 | without_skill 也将 #102 放入 Fixed。 |
| `chore_deps` | **PASS** | with_skill 明确写入“已跳过：依赖维护（#103、#114）”，且正文无 #103 条目。 | without_skill 未输出 #103。 |
| `build_deps_skipped` | **PASS** | with_skill 明确写入“已跳过：依赖维护（#103、#114）”，且正文无 #114 条目。 | without_skill 未输出 #114。 |
| `perf_changed` | **PASS** | with_skill 将 #104 放入 Changed，输出“Reduce API response time by caching”。 | without_skill 也将 #104 放入 Changed。 |
| `feat_added_breaking` | **PASS** | with_skill 将 #105 放入 Added，并以“⚠️ **BREAKING:**”前缀标记。 | without_skill 将 #105 错放入 Changed，且未使用要求的 BREAKING 前缀。 |
| `docs_release_workflow_changed` | **PASS** | with_skill 将 #106 放入 Changed；其 SKILL.md 明确要求依据 release workflow、changelog preflight 等正文语义纳入。 | without_skill 也将 #106 放入 Changed。 |
| `test_eval_contract_changed` | **PASS** | with_skill 将 #107 放入 Changed；transcript 中加载的 SKILL.md 明确覆盖 eval contract/durable comparison 语义。 | without_skill 也将 #107 放入 Changed。 |
| `ci_release_gate_changed` | **PASS** | with_skill 将 #108 放入 Changed；其 SKILL.md 明确要求 release gates、required checks 等语义纳入。 | without_skill 也将 #108 放入 Changed。 |
| `docs_typo_skipped` | **PASS** | with_skill 明确写入“README 拼写修正（#109）”已跳过，且无 #109 条目。 | without_skill 未输出 #109。 |
| `ci_cache_skipped` | **PASS** | with_skill 明确写入“CI 缓存维护（#110）”已跳过，且无 #110 条目。 | without_skill 未输出 #110。 |
| `remove_removed` | **PASS** | with_skill 将 #112 放入 Removed，输出“Drop Python 3.7 support”。 | without_skill 也将 #112 放入 Removed。 |
| `security_security` | **PASS** | with_skill 将 #113 放入 Security，输出“Patch XSS vulnerability in template renderer”。 | without_skill 也将 #113 放入 Security。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `30.96s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `23.374s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `79.221s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
