# Eval Result: eval-006-site-less-degraded-gate

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-006-site-less-degraded-gate`
- Test case: `无文档站宿主降级双态审计门禁`
- Prompt:

> 请读取 `release-package.md`、`docs/changelog/changelog-v1.4.0.md`、`evidence/version-bump.md` 与 `scenarios/no-confirmed-fact-source.md`，处理其中两种 GitHub Release 场景。

- Expected output:

> 可信事实源场景因宿主无 docs/site 且无 release-notes-gen 站内 Release Notes 能力链，将 release-notes-gen / docs-audit 双态审计 handoff 门禁判为不适用并生成完整 preview，显式记录降级依据、已确认 changelog 与版本 bump 证据；预览交维护者批准且不执行任何写入。无可信版本事实源场景保持 blocked，不臆造版本事实。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `cf75cbbf67a65894298fe934a83d0c3f2f3701462abb01c13f26fe10b3f8ba45`（4 个可见文件；两侧逐字节一致）。
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
- With-skill summary: with_skill 实际加载 github-release-gen（status.json skill_load_hits=2；transcript item_1、item_3 读取技能及其 references），按场景生成预览或阻塞，且未产生写入。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-release-gen（status.json skill_load_hits=2；transcript item_1、item_3 读取技能及其 references），按场景生成预览或阻塞，且未产生写入。

## Without-Skill Baseline

without_skill 未加载目标 skill（skill_load_hits=0），但作为对照同样处理了两个场景；其标题为裸 v1.4.0 且预览结构较不完整。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `proceeds_without_handoff_when_site_absent` | **PASS** | with_skill/candidate.md 场景 A 明确说明 docs/site、站内 Release Notes 能力链及 handoff 缺失，但仍生成了 v1.4.0 的完整标题、正文、compare 链接和预览决策；transcript item_4 记录当前模式为仅 Preview。 | without_skill 也生成预览，但标题仅为 v1.4.0，且正文较简略。 |
| `records_downgrade_basis` | **PASS** | candidate 明确记录文档站未初始化、docs/site/ 与站内 Release Notes 能力链缺失，并说明双态审计 handoff 的降级适用性；同时列出 docs/changelog/changelog-v1.4.0.md 和 evidence/version-bump.md。fixture-manifest.json 与快照确认这些证据文件存在且未被修改。 | without_skill 记录了无正式文档站及相关 handoff，并引用确认 changelog，但降级依据表述较简略。 |
| `still_requires_maintainer_approval` | **PASS** | candidate 顶部明确未执行任何 GitHub 写入、创建或移动 tag；场景 A 标注仅 Preview、无维护者写入批准，并明确 Draft/Publish 前须分别取得当前、明确的维护者批准。before-snapshot.json 与 after-snapshot.json 完全一致，transcript 无写入命令。 | without_skill 也明确未执行 Tag、Draft 或 Publish 写入，但未达到 with_skill 的详细审批与后续复核表述。 |
| `blocks_without_confirmed_fact_source` | **PASS** | candidate 场景 B 明确 blocked：版本化 changelog 不存在、version_bump_status 为 proposed、无维护者确认事实源，并声明 commit subjects 与未确认摘要不能作为 Release 事实；未生成可提交 Preview 或执行 Draft/Publish。 | without_skill 同样将场景 B 标记 blocked，并拒绝使用未确认材料。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `98.93s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `80.206s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `85.912s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
