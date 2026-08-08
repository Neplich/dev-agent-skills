# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Fixture SHA-256: `57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2da7831c1e3b626979a3601984870e16015610b54d1ff8f08ff8c14d15f812ca`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- Metadata SHA-256: `cc603314c84acffcc044d1983ddad5ccbf550b74f01ff0d4a84abd79a152693b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | with_skill 输出识别 docs/site/release-notes/、README.md、.meta/releases.json 缺失，并指出 release-notes 规约与 docs-audit 门禁导致无法进入生成流程；fixture 也确认该目录和元数据不存在。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | with_skill 明确声明工作区无文件变更；其 git_status 与 git_diff 均为空，符合 bootstrap 前保持 pristine 的要求。 |
| `hands_missing_foundation_to_bootstrap` | FAIL | with_skill 指向 docs-site-bootstrap，但未明确交接给 Docs owner，也未携带 release-entry.md 中的 host_repository（current product repository）及完整缺失 foundation；同时未明确排除 docs audit owner 和 GitHub Release owner。 |
| `preserves_release_chain_and_external_zero_writes` | FAIL | with_skill 明确 tag 和 GitHub Release 未创建，但未完整说明不准备、编辑或发布 Release、当前 release execution 未授权，以及 foundation 补齐后需重新进行正文确认和站内检查；只概述了后续生成、审计和创建流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23; output_sha256=c9eae98eadfd7ad48622e76bccb8fcfed586e9b79156b78c04fef7c2c2d994b9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别站点基础缺失并保持零写入、未创建 tag 或 GitHub Release，但交接信息和发布链约束说明不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23; output_sha256=29dede32dac131e64899679166059191876b6422ecbca9ce0ca0c1e82d00006f; snapshot_sha256=5c3bc5968c018cd59ea2b47ebe1c537c392f096f7a75cf47f00e8fb52feb7600
- Behavior: 错误地生成站内页面和 Release 草稿，并创建本地 v1.0.0 tag；仅因无 remote/gh 未创建远程 Release。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整满足 Docs owner blocked handoff 要求。
- with_skill 未完整说明 bootstrap 后的重新确认、站内检查、pre-tag 审计及当前未授权状态。
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口，已按 #238 于 2026-08-06 fresh 隔离重跑）
- Eval: `eval-003-github-release-boundary`
- Scenario: 缺少 Release Notes writing foundation 的混合站内/外部发布请求
- Review context: self-review convergence

## Test Set / Fixture Version

- Fixture version: `foundation cleanup consistency round-4`
- Validation time: `2026-07-29`（历史轮；本轮 #238 重跑来源见 Latest Result 块）
- Runtime: `tmp/eval-runs/issue-177/self-review/`
- 修正原因：round-3 已移除等价 Release Notes 契约与 surfaces，但 `execution_cleanup` 没有覆盖被删除的 Release Notes 目录、release metadata 和可执行测试；复用 scratch 时可能被旧产物重新污染。
- 本轮补齐 cleanup 后，两侧使用同一 prompt 与独立 pristine fixture；without-skill 未读取目标 skill、Docs Agent README、eval metadata、assertions、with-skill 输出、旧 comparison 或历史 round，独立 judge 也未读取旧 comparison。

## Latest Result

- Behavior result: `PASS`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | FAIL | with_skill 明确指出 `docs/site/release-notes/`、编写规范、索引和 `.meta/releases.json` 不存在，并阻止初始化；without_skill 直接报告已完成版本说明。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | FAIL | with_skill 工作区没有版本页、`.meta` 或其他初始化产物；without_skill 实际新增 `docs/site/release-notes/v1.0.0.md`、`.meta/releases.json` 和 `.meta/release-handoff.json`。 |
| `hands_missing_foundation_to_bootstrap` | PASS | FAIL | with_skill 明确说明需交给 `docs-site-bootstrap`；without_skill 未阻塞交接，而是继续生成正文、元数据和交接文件。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | FAIL | with_skill 明确未创建 GitHub Release 或 `v1.0.0` tag，并说明当前未授权发布执行；without_skill 虽未创建 tag/Release，但已提前准备站内发布产物，且未说明 foundation 补齐后需重新确认、检查和审计。 |

未满足断言（with/without 任一 FAIL）：``detects_missing_release_notes_foundation``、``keeps_site_zero_diff_before_bootstrap``、``hands_missing_foundation_to_bootstrap``、``preserves_release_chain_and_external_zero_writes``



## Fixture Correction And Discrimination

- 修正后宿主保留正式文档站的其他必要文件，但不存在 `docs/site/release-notes/`、编写规则、index、release metadata、相邻版本页或等价可执行契约。
- 通用脚手架仅拒绝生成 Release Notes 并指向专用 skill，不提供正文、frontmatter、metadata 或 index 写作规则，因此不构成等价 foundation。
- `execution_cleanup` 现在覆盖整个 `docs/site/release-notes`、`docs/site/.meta/releases.json` 与 `docs/site/scripts/__tests__/release-notes.test.mjs`，防止旧 runtime 产物伪造 foundation。
- with-skill 应用 foundation gate 后停止；baseline 自行推断规则并创建 Release Notes surfaces，重新形成明确区分。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | FAIL | with-skill 识别空目录及 writing rules/等价契约缺失；baseline 未识别阻塞并继续生成。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | FAIL | with-skill 的 `docs/site/` 文件 manifest 与源 fixture 完全一致；baseline 新增版本页、index、metadata 与生成物。 |
| `hands_missing_foundation_to_bootstrap` | PASS | FAIL | with-skill blocked 给 `docs-site-bootstrap` 并等待显式初始化授权；baseline 无 bootstrap handoff。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | FAIL | with-skill 保留 bootstrap→Release Notes→checks→pre-tag audit→PM 顺序且不准备外部发布；baseline 跳过 bootstrap 并把自行建立的站内 handoff 宣称为 ready。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 在 site-foundation gate 停止，没有加载内部生成流程。
- 未创建版本页、index、release metadata、导航或 `.generated`；未运行不能证明交付成立的 docs checks。
- 未准备或写入 GitHub Release，未创建或移动 tag；返回携带 host、目标版本、证据边界与缺失 foundation 的 blocked bootstrap handoff。
- Response SHA-256: `2e12af318ce600cda34001d30ac9de7c8a91a65239bd2f693417eff1d8391eec`。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- baseline 自行创建 `v1.0.0.md` 与 Release Notes index，运行 frontmatter 检查和 public/internal builds，并把站内 pre-tag handoff 描述为已完成；它没有修改 `.meta/releases.json`。
- 它未识别 bootstrap gate，也未保留正文重新确认、站内检查与 pre-tag audit 的完整前置链。
- Response SHA-256: `a9ed33574b0b964611a2bb8e88723c0ea1620f79261b4a2f05a80aa67850c0df`。

## Failures And Iterations
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Round 1：with-skill 4/4、baseline 4/4；prompt/fixture 泄漏导致无区分度。
- Round 2：with-skill 4/4、baseline 0/4，但 fixture 保留等价 Release Notes 契约，场景判定失真。
- Round 3：修剪等价契约后 with-skill 4/4、baseline 0/4；Behavior PASS、Coverage FULL，场景与协议一致。
- Round 4：补齐删除 surface 的 cleanup 后重新 fresh 成对验证；with-skill 4/4、baseline 0/4，Behavior PASS、Coverage FULL，独立 judge 确认区分度保持。
- 基础设施失败：none。runtime 未保留 lane transcript、显式读取清单或结构化命令日志，降低读取边界的可审计性，但 workspace diff、响应和 baseline 构建产物足以覆盖本轮 4 条行为 assertion。

## Next Steps

- 保持缺少目录、写作规则和等价站点契约时的 bootstrap stop 为回归门禁。

## Runtime Artifact Policy

- `tmp/eval-runs/issue-177/self-review/` 下的 workspace、依赖、页面副本、构建产物、response、handoff 和 judge verdict 不提交。
- 本 `comparison.md` 是本轮唯一 durable eval 结果。
