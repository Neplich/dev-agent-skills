# Eval Result: eval-005-feed-mode-completeness

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-005-feed-mode-completeness`
- Test case: `feed-mode-completeness`
- Prompt:

> 我是 roadmap-gen，需要 anthropics/anthropic-sdk-python 的当前仓库状态作为结构化输入，请给我完整状态数据

- Expected output:

> Markdown 报告后附 `---` 分隔的 `github_reader_data` YAML 块，包含总数类字段；若报告声明了截断或总数不完整，YAML 必须有对应 `truncated_collections` / `incomplete_totals` 字段

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
- With-skill summary: with_skill 实际加载了 github-reader（status.json 的 skill_load_hits=2，transcript 中读取 SKILL.md），随后按技能先尝试仓库查询并检查认证；gh 未认证，未获得实时 GitHub 数据，因此诚实报告阻塞且未伪造 Feed YAML。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载了 github-reader（status.json 的 skill_load_hits=2，transcript 中读取 SKILL.md），随后按技能先尝试仓库查询并检查认证；gh 未认证，未获得实时 GitHub 数据，因此诚实报告阻塞且未伪造 Feed YAML。

## Without-Skill Baseline

without_skill 未加载技能（skill_load_hits=0），输出了另一套 GitHub connector JSON；仅作 baseline 对照，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `feed_yaml_present` | **NOT EXERCISED** | with_skill 的 transcript 显示 gh repo view 因未认证失败，gh auth status 也失败；candidate.md 明确报告无法获取当前状态，因此没有可供判断的实时 Feed 数据或 YAML。 | without_skill 输出了 JSON 快照，没有 Markdown 报告后的 github_reader_data YAML 块。 |
| `completeness_signals_consistent` | **NOT EXERCISED** | 实时仓库集合不可用，且 transcript 没有成功返回查询集合或总数；无法判断 YAML 总数与截断/不完整声明的一致性。 | without_skill 输出 retrieved=100 等集合长度，但未提供 Feed 完整性字段，不能作为 with_skill 结论依据。 |
| `totals_not_fabricated` | **NOT EXERCISED** | 因 GitHub CLI 未认证，with_skill 未获得可用于核验的 search total_count；candidate.md 也未伪造任何总数。 | without_skill 的 JSON 使用 retrieved=100 等字段，未展示 search total_count；仅作对照。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- feed_yaml_present：GitHub 认证不可用，实时 Feed 数据未获取。
- completeness_signals_consistent：没有成功的实时集合/总数可核对。
- totals_not_fabricated：没有成功的 search total_count 可核对。

## Next Steps

- 认证 GitHub CLI 后重跑，以覆盖 Feed YAML、完整性信号和 total_count 三条 assertion。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `35.141s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `150.115s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `51.306s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
