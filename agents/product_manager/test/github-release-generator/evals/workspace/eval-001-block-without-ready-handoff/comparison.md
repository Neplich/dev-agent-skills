# Eval Result: github-release-generator-block-without-ready-handoff

## Evaluation Target

- Skill: `github-release-generator`
- Test case: missing and unconfirmed issue #116 handoff
- Latest result: **PASS** - 2026-07-22 issue #154 r2 fresh paired validation；with-skill 4/4、without-skill 4/4 assertions 通过

## Review Context

- Review issue: #154
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 先完整读取当前 skill、两份 reference、eval 定义、metadata、fixtures 与本轮双侧 candidate；独立 verdict 写入后才读取 durable `comparison.md`，且未读取旧首轮 tmp。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped no-handoff 与 unconfirmed-handoff，包含候选页面和 source evidence
- With-skill evidence: `tmp/eval-runs/issue-154/r2-final/with_skill/eval-001-block-without-ready-handoff/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-154/r2/without_skill/eval-001-block-without-ready-handoff/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-154/r2-final/judge/verdict.md`

## Assertions

- PASS `blocks_missing_handoff`: with-skill 与 without-skill 都对场景 A 明确 blocked，列出缺失的 #116 site-ready handoff，并拒绝由候选证据生成可发布正文。
- PASS `blocks_unconfirmed_handoff`: 双侧都识别 `confirmation_status: unconfirmed`，未把页面存在或 docs check 通过视为 ready。
- PASS `returns_to_site_release_notes`: 双侧都把两个入口缺口返回 `docs-agent:release-notes-generator`，没有修复、补写或假设上游证据。
- PASS `no_publishable_output_or_mutation`: 双侧都未输出完整可发布正文或 mutation 命令，未写 docs/site、draft、Release 或 tag。

## With Skill Behavior

- 先确认宿主存在 `docs/site/`，因此 #116/#117 门禁适用且不得因 handoff 缺失降级。
- 分别识别 missing 与 unconfirmed 状态，完整说明页面路径、确认、checks、release surfaces 和来源证据门禁。
- 仅报告 blocker、下一 owner 与零写入边界。

## Without Skill Baseline

- 来源：issue #154 fresh baseline，使用同一 prompt、assertions、expected output、metadata 与 fixture；未读取或应用 skill、Agent README、with-skill 输出或历史 comparison。
- 行为：同样 4/4 assertions PASS，能区分两类 blocker、返回正确 owner 并保持零写入。
- 差异：with-skill 额外记录站点门禁适用性并枚举更完整的 ready-handoff 证据面；当前 assertions 区分度为 0/4。

## Failures / Findings

- 无 with-skill assertion failure 或 blocker。
- 非阻塞 finding：prompt 与 assertions 已直接给出主要阻塞语义，fresh baseline 也全部通过。

## Next Steps

- 当 #116 handoff 字段、站点适用性或 confirmation gate 变化时重新执行 paired validation。
- 若需评估 skill 增益，可减少 expected output 对 owner 与禁用动作的直接提示。

## Runtime Artifacts Policy

- 本轮双侧 candidates 与 judge verdict 位于上列精确 `tmp/eval-runs/issue-154/r2-final/`、`tmp/eval-runs/issue-154/r2/` 路径，属于短期运行期诊断证据。
- 不提交 transcript、candidate、manifest、verdict、outputs、timing、run status 或 diagnostics；长期结果仅保留本 `comparison.md`。
