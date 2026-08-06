# Eval Result: eval-001-block-without-ready-handoff

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-001-block-without-ready-handoff`
- Test case: `缺少 release-notes-gen ready handoff 时阻塞`
- Prompt:

> 请分别审查 `scenarios/no-handoff.md` 与 `scenarios/unconfirmed-handoff.md` 中的 GitHub Release 请求，并说明每个场景当前能否继续。

- Expected output:

> 两个场景均明确 blocked：缺少 ready handoff 或 confirmation_status 非 confirmed 时返回 docs-agent:release-notes-gen，不生成可发布 GitHub Release、draft 或发布命令。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `c605709dc3c9ab798d99c0f946697d42aa5ba95fdbc48355a536b076cbbcbd1a`（4 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- Overall result: FAIL
- With-skill summary: with_skill 实际加载了 github-release-gen（status skill_load_hits=2，transcript item_1 读取 SKILL.md），正确阻塞两个场景且未写入；但仅场景 A 明确返回 docs-agent:release-notes-gen，场景 B 未明确返回该 owner。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载了 github-release-gen（status skill_load_hits=2，transcript item_1 读取 SKILL.md），正确阻塞两个场景且未写入；但仅场景 A 明确返回 docs-agent:release-notes-gen，场景 B 未明确返回该 owner。

## Without-Skill Baseline

without_skill 两个场景均阻塞且未写入，但未加载 skill；仅作基线对照。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `blocks_missing_handoff` | **PASS** | with_skill transcript item_1 读取 no-handoff.md，记录 site_release_notes_handoff: missing；最终 candidate.md 明确场景 A“阻塞”、缺少完整 release-notes-gen handoff，不能绕过门禁。 | without_skill 也识别 site_release_notes_handoff 为 missing，并阻止生成或发布。 |
| `blocks_unconfirmed_handoff` | **PASS** | with_skill transcript item_1 读取 confirmation_status: unconfirmed、docs check passed 与 handoff blocked；candidate.md 明确指出页面仍为 unconfirmed，且未获得维护者确认前不能生成或写入 draft。 | without_skill 也识别 unconfirmed、draft 与 blocked 状态，并阻止 draft 生成。 |
| `returns_to_site_release_notes` | **FAIL** | candidate.md 对场景 A 明确写出返回 docs-agent:release-notes-gen；但对场景 B 只写“应由维护者确认完整页面正文后重新提交 handoff”，未明确返回 docs-agent:release-notes-gen，未满足两个入口都按要求路由。 | without_skill 两个场景都要求补齐或完成 handoff，但未明确使用 docs-agent:release-notes-gen 路由。 |
| `no_publishable_output_or_mutation` | **PASS** | candidate.md 未输出完整可发布 Release 正文，并明确不能生成或写入 draft；with_skill before-snapshot.json 与 after-snapshot.json 的全部文件 size/hash 相同，transcript 中仅有 sed/rg 只读命令，没有 GitHub、docs/site、tag 或 draft 写入。 | without_skill 同样未产生完整 Release 正文或外部写入；其快照前后也未变化。 |

## Failures

- returns_to_site_release_notes：场景 B 未明确返回 docs-agent:release-notes-gen，仅要求维护者确认后重新提交 handoff。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 将场景 B 的阻塞后续明确表述为返回 docs-agent:release-notes-gen，补齐 confirmation_status: confirmed 的 site-ready handoff。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `82.575s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `73.531s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `95.911s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
