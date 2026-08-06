# Eval Result: eval-003-preserve-facts-and-add-traceability

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`
- Test case: `事实一致与可追溯增强`
- Prompt:

> 请根据 `release-package.md`、`docs/site/release-notes/v1.0.0.md` 和 `github-evidence.md` 准备 GitHub Release 预览。

- Expected output:

> 预览逐项保持已确认的功能、架构、数据库、部署、资产、升级与风险事实，补充可信 compare、代表性 PR/commit 和贡献者链接，不把原始维护列表当成用户说明。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `48f64768ed5b5a87211bb5aee4d2a82f88fd01187214112795689e47210e9e9c`（3 个可见文件；两侧逐字节一致）。
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
- With-skill summary: with_skill 实际加载 github-release-gen（status skill_load_hits=2；transcript item_1 读取 SKILL.md），按技能要求先读取参考规范再读取三份事实材料，未写入工作区，并生成保留事实、精选链接和最终 compare 链接的预览。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-release-gen（status skill_load_hits=2；transcript item_1 读取 SKILL.md），按技能要求先读取参考规范再读取三份事实材料，未写入工作区，并生成保留事实、精选链接和最终 compare 链接的预览。

## Without-Skill Baseline

without_skill 未加载技能（skill_load_hits=0），但也生成了包含主要事实和维护链接的预览文件；仅作对照。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `preserves_confirmed_release_facts` | **PASS** | with_skill candidate 明确保留文件卡片、失败消息原位重试及其独立性、统一附件模型与旧文本兼容、nullable JSONB message_files 与回填/NOT NULL 约束、删除列丢失元数据风险、数据库→Gateway→Web 部署顺序、生产开关、amd64/arm64 资产、升级验证、备份和旧浏览器限制；transcript item_3 读取了三份事实材料，且 before/after 快照显示事实源未被修改。 | without_skill 生成的预览也包含上述主要事实。 |
| `adds_verified_traceability_links` | **PASS** | candidate 使用了 github-evidence.md 中的 PR #116、PR #117、commit 8b6a1f2 及对应贡献者链接，并给出完整 compare https://github.com/example/ai-hub/compare/v0.9.0...v1.0.0；该 endpoint 与目标 tag v1.0.0 一致。transcript item_3 读取 github-evidence.md，item_8 输出了这些链接。 | without_skill 预览文件同样包含 compare、两个 PR、direct commit 和贡献者链接。 |
| `curates_instead_of_dumping` | **PASS** | candidate 将维护链接放在重点更新、其他改进和变更明细中，只列三条代表性变更，并明确说明 18 个格式化、依赖更新和测试 commit 未原样放入正文；与 fixture 中“不得原样堆入正文”一致。 | without_skill 也排除了完整的 18 个维护性 commit feed。 |
| `blocks_on_fact_conflict` | **NOT EXERCISED** | fixture 中 github-evidence.md 仅提供与事实源相容的代表性链接和 release window，没有触发 GitHub 证据冲突或暴露新事实的条件；因此未能从实际行为判定阻塞并返回 docs-agent:release-notes-gen 的分支。 | without_skill 同样未遇到事实冲突，未触发该条件。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- blocks_on_fact_conflict：当前 fixture 没有冲突或新增事实，条件分支未触发。

## Next Steps

- 如需 FULL coverage，补充会与站内事实冲突或 materially extend 的 GitHub 证据 fixture。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `80.97s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `62.622s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `81.651s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
