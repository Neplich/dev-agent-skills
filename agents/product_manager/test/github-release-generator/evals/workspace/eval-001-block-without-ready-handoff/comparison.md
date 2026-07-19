# Eval Result: github-release-generator-block-without-ready-handoff

## Evaluation Target

- Skill: `github-release-generator`
- Test case: missing and unconfirmed issue #116 handoff
- Latest result: PASS - 2026-07-20 R2 fresh paired validation 与独立 judge 完成，4/4 assertions 通过

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped no-handoff 与 unconfirmed-handoff；R2 已补齐候选页面和 source evidence
- Runtime evidence: `tmp/eval-runs/120-r2/eval-001-block-without-ready-handoff/`

## Assertions

- PASS `blocks_missing_handoff`: 无 #116 handoff 时明确 blocked，不生成可发布正文。
- PASS `blocks_unconfirmed_handoff`: 页面、证据和 docs check 存在仍不能替代 `confirmation_status: confirmed`。
- PASS `returns_to_site_release_notes`: 两个缺口都返回 `docs-agent:release-notes-generator`，不自行修复或假设上游证据。
- PASS `no_publishable_output_or_mutation`: 不生成 preview/draft/publish 内容或命令，不写站点、不动 tag。

## With Skill Behavior

- 对 no-handoff 场景枚举缺失的页面、确认、checks、索引/metadata 和来源证据。
- 对 unconfirmed 场景读取候选页面与 source evidence 后仍以正文未确认为独立充分阻塞条件。
- 只报告 blocker 与下一 owner，未执行 GitHub、tag 或 `docs/site/` 写入。

## Without Skill Baseline

- R2 使用同一 prompt 与补齐后的 fixture 于 2026-07-20 全新生成，未应用或引用 skill、README、R1、旧 baseline 或历史 comparison。
- baseline 也覆盖核心阻塞语义；with-skill 对 #116 完整字段、owner 与禁用动作的说明更完整。Baseline 较强不影响 with-skill PASS。

## Failures

- 无。R1 judge 提出的最小页面/source evidence 健壮性建议已修复；R2 独立 judge 确认 fixture、harness 与语义断言均无剩余问题。

## Next Steps

- 当 #116 ready handoff 字段或 confirmation gate 变化时重新执行 paired validation。

## Runtime Artifacts Policy

- 最终依据为 R2；`with_skill.md`、`without_skill.md` 与 `verdict.md` 仅位于 `tmp/eval-runs/120-r2/`。R1/R2 runtime 均不提交 transcript、verdict、with_skill、without_skill、outputs 或 diagnostics。
