# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-002-focused-pr-query`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/github-reader/evals/workspace/eval-002-focused-pr-query`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `de82acc91104ba7f3d49c7bc1e982de3d7787ab0f48a220e344b248704a9a596`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `254cc92cf58649aa2c5bb2447fe35aa135bdc944368afe7a7cc119c6e2735ba1`
- Skill overlay SHA-256: `86a7dea13dce1a60e9d0c4442e983c46d3a33318b7a112994f13359d56bd6e12`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `48399879c86e4df7cc7f5e646328eb0789d03e0de144e50014e3c4bbd49f4382`
- Metadata SHA-256: `3a8a7f69b9edf1c050358af035fa03246aa31ef41c323e332268181c651cef28`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `pr` | PASS | With_skill 输出仅列出 PR 表格及相关来源说明，没有大量无关 issue 列表。 |
| `assertion_2` | PASS | With_skill 的每一条 PR 都包含作者和等待天数。 |
| `assertion_3` | PASS | With_skill 按等待天数从久到近排列：39、36、33、25、23、16、16、15、10、7、5、5、5 天。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=de82acc91104ba7f3d49c7bc1e982de3d7787ab0f48a220e344b248704a9a596; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=219b8bc80f517abd5dfef7f85ee79bcea867390d08e2a1669141371f484df82f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 聚焦带作者和等待天数的 PR，并按等待时间从久到近排序。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=de82acc91104ba7f3d49c7bc1e982de3d7787ab0f48a220e344b248704a9a596; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e93c280309f5c650c570f0fdfeb94fa75d286b39c43fa7045db3852e1ec05a74; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 列出 PR 并按创建时间排序，但未提供作者信息。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

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

# Eval Result: eval-002-focused-pr-query

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-002-focused-pr-query`
- Test case: `focused-pr-query`
- Prompt:

> 我在 cli/cli 这个仓库里工作，现在有哪些 PR 还在等待 review？按等待时间排序

- Expected output:

> 聚焦 PR 的输出，列出 awaiting review 的 PR 并按等待时间排序，不需要输出 issue 和 milestone 数据

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
- With-skill summary: 目标 skill 已实际加载（status.json 的 skill_load_hits=2，transcript 首先读取 github-reader/SKILL.md）。随后按 focused query 读取仓库、开放 PR 及 PR 总数，但三次 gh 查询均因未认证以 exit_code=4 失败；最终如实报告无法读取并要求 gh auth login。未发生文件写入，前后 snapshot 一致。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

目标 skill 已实际加载（status.json 的 skill_load_hits=2，transcript 首先读取 github-reader/SKILL.md）。随后按 focused query 读取仓库、开放 PR 及 PR 总数，但三次 gh 查询均因未认证以 exit_code=4 失败；最终如实报告无法读取并要求 gh auth login。未发生文件写入，前后 snapshot 一致。

## Without-Skill Baseline

without_skill 成功输出 31 个 PR，包含等待天数并按从长到短排序，但表格未包含作者；其结果仅作为 baseline，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `pr` | **NOT EXERCISED** | with_skill 的 candidate.md 明确报告 GitHub CLI 未登录，未能获得 PR 集合；transcript 中 gh pr list 与 gh api 查询均失败（exit_code=4），因此无法判断实际输出是否聚焦 PR。 | without_skill 输出仅列 PR，没有大量 issue 列表，表现为聚焦 PR。 |
| `assertion_2` | **NOT EXERCISED** | 作者及等待时间/创建时间依赖实时 PR 数据；with_skill 的 gh pr list 查询因认证失败（transcript item_3，exit_code=4），candidate.md 未列出任何 PR，无法判定。 | without_skill 列出等待天数，但未显示作者；仅作为对照。 |
| `assertion_3` | **NOT EXERCISED** | 排序依赖实时 PR 集合；with_skill 的 PR 查询因未认证失败（transcript item_3，exit_code=4），没有可排序的结果，无法判定。 | without_skill 明确声明按等待时间从长到短排序，列表数值呈降序。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- pr：GitHub CLI 未认证，无法获取目标 PR 集合。
- assertion_2：GitHub CLI 未认证，无法获取作者和时间字段。
- assertion_3：GitHub CLI 未认证，无法获取并验证排序所需的 PR 集合。

## Next Steps

- 认证 GitHub CLI 后重新执行 focused PR 查询，以覆盖三条实时数据断言。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `47.453s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `318.365s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `84.155s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
