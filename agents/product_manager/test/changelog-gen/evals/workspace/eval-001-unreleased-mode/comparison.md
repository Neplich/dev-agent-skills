# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-001-unreleased-mode`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `816b4de603f11081701f38913293ff8bf45f51d9500e3f42bbaccf19e6d1cd7c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3dfcf246dc4057e8231ee4e2380b4525eeecf840a484daf60bd4e990283d5e5e`
- Skill overlay SHA-256: `5c214a0a2c2365016d6b3bafaa3e6cd9bb33067b007f4407a0b78fe50c4ba935`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d79133c1bbb156df00e2bf94905fa052c00f56ec190d786d942617fe98a1c3a2`
- Metadata SHA-256: `2e8886660979e8d508feb617ffafcb0337fa9f27576f749f4ff86dbac479ac74`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill delivery snapshot contains the exact heading ## [Unreleased]. |
| `pr` | NOT_EXERCISED | The with_skill output contains no entries, and the fixture directory provides no raw PR evidence to evaluate this criterion. |
| `bot_pr_dependabot` | NOT_EXERCISED | No raw PR list is present in the fixture, so skipping bot PRs cannot be independently verified. |
| `chore_ci_test` | NOT_EXERCISED | No raw PR list is present in the fixture, so exclusion of internal chore/ci/test changes cannot be independently verified. |
| `versioned_changelog_file` | PASS | with_skill workspace_manifest and delivery_snapshot both identify docs/changelog/changelog-unreleased.md. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=816b4de603f11081701f38913293ff8bf45f51d9500e3f42bbaccf19e6d1cd7c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=90ecdbd4c1816b3377901ec9dc4c9d7a0253020fb3552f238e6d96491d81abdf; snapshot_sha256=72c252991da4d355b40317539f88c89a1dd688b867b6bf0c3d380a79fae226ff
- Behavior: Created the requested file with an Unreleased heading and claimed no user-facing changes after v0.120.2; no PR-level content was provided.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=816b4de603f11081701f38913293ff8bf45f51d9500e3f42bbaccf19e6d1cd7c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f776d312c769cd3872fdba8394161ace8c6d8d9acb29b5fac9bb2510d590a6a5; snapshot_sha256=cabb63678d1342a76b66cc21488c626cbd56aefa8ed4e9080c9770e4ea43a080
- Behavior: Created the requested file with an Unreleased heading and claimed no changes after v0.121.0.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the raw release and merged-PR fixture to evaluate the PR-content assertions.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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

# Eval Result: eval-001-unreleased-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`
- Test case: `unreleased-mode`
- Prompt:

> 我在 https://github.com/anthropics/anthropic-sdk-python 这个仓库里工作。帮我生成 Unreleased 章节 —— 也就是最新 release tag 之后合并的所有 PR，写成 Keep a Changelog 格式，输出到 docs/changelog/changelog-unreleased.md。

- Expected output:

> 生成 ## [Unreleased] 章节，包含最新 release 之后的 PR 列表，按 Added/Changed/Fixed 分组，每条带 PR 链接，写入 docs/changelog/changelog-unreleased.md

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
- Coverage result: **PARTIAL**
- Overall result: PASS (partial coverage)
- With-skill summary: with_skill 实际加载了 changelog-gen（status.json skill_load_hits=2；transcript item_1 读取 SKILL.md），按要求创建并写入目标文件。trace 显示 Git/gh 查询分别因非 Git 工作区和未认证失败，网络查询也无可验证结果；因此 PR 相关断言无法覆盖。未发现读取评测脚手架泄漏。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载了 changelog-gen（status.json skill_load_hits=2；transcript item_1 读取 SKILL.md），按要求创建并写入目标文件。trace 显示 Git/gh 查询分别因非 Git 工作区和未认证失败，网络查询也无可验证结果；因此 PR 相关断言无法覆盖。未发现读取评测脚手架泄漏。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），但其 trace 也创建了目标文件并包含 Unreleased 标题；该结果仅作为对照，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `unreleased` | **PASS** | with_skill trace item_16 读取到写入内容，其中包含 `## [Unreleased]`；after-snapshot.json 也确认目标文件已生成。 | without_skill trace item_17 的文件内容同样包含 `## [Unreleased]`。 |
| `pr` | **NOT EXERCISED** | PR 范围属于实时 GitHub 数据；with_skill 的 git 查询因 `not a git repository` 失败，gh 查询因未认证失败，网络查询无可验证返回，不能确认实际 PR 集合或据此判定链接格式。 | without_skill 也没有 PR 条目，trace item_17 仅写入 `No changes yet.`，因此 PR 链接格式未被实际练习。 |
| `bot_pr_dependabot` | **NOT EXERCISED** | 没有可验证的实时 PR 实体可供判断是否跳过 dependabot 等 bot PR；不能把无法取得数据等同于 PASS。 | without_skill 没有 PR 条目，bot PR 过滤未被实际练习。 |
| `chore_ci_test` | **NOT EXERCISED** | 没有可验证的实时 PR 实体及其标题/内容可供判断 chore/ci/test 过滤；相关查询基础设施不可用。 | without_skill 没有 PR 条目，内部变更过滤未被实际练习。 |
| `versioned_changelog_file` | **PASS** | with_skill trace item_14 创建目录，item_15 明确新增 `docs/changelog/changelog-unreleased.md`；after-snapshot.json 确认该路径存在，candidate.md 也提供了该文件链接。 | without_skill trace item_16 的 file_change 同样明确写入 `docs/changelog/changelog-unreleased.md`。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- pr
- bot_pr_dependabot
- chore_ci_test

## Next Steps

- 提供可用的 GitHub/Git 数据或预置 PR fixture 后重跑，以覆盖 PR 链接与过滤断言。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `85.978s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `115.481s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `90.851s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
