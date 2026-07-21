# Eval Result: github-release-generator-block-without-ready-handoff

## Evaluation Target

- Skill: `github-release-generator`
- Test case: missing and unconfirmed issue #116 handoff
- Latest result: PASS - 2026-07-21 issue #146 fresh paired validation 完成，with-skill 4/4 assertions 通过

## Review Context

- Review issue: #146
- Final judge: 当前会话中的 fresh Codex validation agent
- 两条 lane 分别由全新 worker 生成；judge 在两侧完成前未读取历史 `comparison.md`。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped no-handoff 与 unconfirmed-handoff，包含候选页面和 source evidence
- Runtime evidence: `tmp/eval-runs/issue-146/{with_skill,without_skill}/eval-001-block-without-ready-handoff/`

## Assertions

- PASS `blocks_missing_handoff`: 无 #116 site-ready handoff 时明确 blocked，候选范围证据不能生成可发布正文。
- PASS `blocks_unconfirmed_handoff`: `confirmation_status: unconfirmed` 时，即使页面、索引与 docs check 已存在也不能视为 ready。
- PASS `returns_to_site_release_notes`: 两个缺口均返回 `docs-agent:release-notes-generator`，未自行修复、补写或假设上游证据。
- PASS `no_publishable_output_or_mutation`: 未输出完整可发布正文或发布命令，未创建或更新 draft，站点、GitHub 与 tag 均零写入。

## With Skill Behavior

- 分别识别 missing handoff 与 unconfirmed handoff，并把正文确认作为不可替代的独立门禁。
- 对 no-handoff 场景列出页面路径、确认、checks、release surfaces 与来源证据缺口；对 unconfirmed 场景未把候选页面升级为事实源。
- 只报告 blocker、下一 owner 和零写入边界。

## Without Skill Baseline

- 2026-07-21 使用同一 prompt、assertions、expected output、metadata 与 fixture 全新生成；未读取 skill、Agent README、with-skill 证据或历史 comparison。
- baseline 同样 4/4 assertions PASS，能区分两类 blocker、返回正确 owner 并保持零写入。
- 主要差异：with-skill 对完整 handoff 字段、后续 `ready_for_tag` 顺序和禁用动作说明更完整；当前 assertions 的区分度为 0/4。

## Failures

- 无 assertion failure 或 blocker。
- 非阻塞 finding：expected output 与 assertions 已直接给出主要阻塞语义，fresh baseline 同样全部通过，未证明 skill 相对 baseline 的断言增益。

## Next Steps

- 当 #116 handoff 字段或 confirmation gate 变化时重新执行 paired validation。
- 若要评估 skill 增益，可减少 prompt/expected output 对 owner 与禁用动作的直接提示。

## Runtime Artifacts Policy

- 本轮 candidate、worker observations 与 manifest 仅位于 `tmp/eval-runs/issue-146/`，作为短期运行期证据。
- 不提交 transcript、candidate、worker observations、manifest、verdict、outputs、timing 或 diagnostics；长期结果仅保留本 `comparison.md`。
