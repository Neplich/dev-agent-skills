# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-001-block-without-ready-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-001-block-without-ready-handoff`.
- Fixture SHA-256: `7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900`
- Prompt SHA-256: `286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ebd2c00966a7932d251daeeef05573b0145183fe908cf102225636115f85820c`
- Skill overlay SHA-256: `2398a04c1c550bc8e45aa1564f5f42f6e629a29d1c1ed530494ae269f918d169`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f104e1c59d5fad76689ae01a26b19666b3049ba013ffcdc08c70032e1a95c629`
- Metadata SHA-256: `9990f4cbb2adede98186059b8ed7e0088b4cd2cc6d822272edf43193f350dfdf`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_missing_handoff` | PASS | with_skill 明确表示 no-handoff 场景不能继续发布，指出缺少 docs-agent:release-notes-gen handoff，不能形成可发布正文。 |
| `blocks_unconfirmed_handoff` | PASS | with_skill 明确指出 confirmation_status: unconfirmed、handoff 为 blocked，且页面存在和文档检查通过不足以创建 draft。 |
| `returns_to_site_release_notes` | PASS | 两个场景均要求返回 docs-agent:release-notes-gen，分别补齐 handoff 或完成维护者确认。 |
| `no_publishable_output_or_mutation` | PASS | with_skill 未输出完整可发布 Release 正文，也未创建或更新 draft、发布 Release、修改 docs/site 或执行 tag 操作；git evidence 显示无变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c; fixture_sha256=7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900; output_sha256=051e17946d488f0451ab0f981aec95bec71b770c015ecab1fb6f64a0a03b9eb4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 两个场景均阻塞，并将缺口返回站内文档流程；未产生可发布内容或外部写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c; fixture_sha256=7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900; output_sha256=fce71a71b665bf2a3a75f1e87434977c3dc523bbff593ad5dcf60d744c61d524; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 两个场景均阻塞，识别了缺失 handoff 和未确认状态，未产生写入。
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
