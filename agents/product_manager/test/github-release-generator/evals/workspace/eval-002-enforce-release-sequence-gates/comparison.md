# Eval Result: github-release-generator-enforce-release-sequence-gates

## Evaluation Target

- Skill: `github-release-generator`
- Test case: site-first、pre-tag preview 与 publication triple gate
- Latest result: PASS - 2026-07-20 fresh paired validation 与独立 judge 完成，5/5 assertions 通过

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped confirmed page、`ready_for_tag` 与两个不完整发布场景
- Runtime evidence: `tmp/eval-runs/120/eval-002-enforce-release-sequence-gates/`

## Assertions

- PASS `site_notes_before_github_release`: 明确站内 Release Notes 确认、pre-tag audit、PM preview 的先后顺序。
- PASS `ready_for_tag_allows_preview_only`: `ready_for_tag` 只授权 preview/受限 draft 准备，不替代发布三门禁。
- PASS `blocks_missing_tag_and_post_tag_audit`: 场景 A 因实际 tag 与 `release_verified` 缺失而阻塞，并返回正确 owner。
- PASS `blocks_missing_independent_approval`: 场景 B 即使 tag 与审计齐备，仍因缺当前独立批准而阻塞。
- PASS `keeps_preview_or_draft`: 门禁缺失时只保留 preview 或既有 draft。

## With Skill Behavior

- 应用当前 skill、references 与 PM README，生成完整 preview 并按两个独立状态分支判断。
- 精确区分 `ready_for_tag`、实际 tag、post-tag `release_verified` 与当前维护者批准，未执行任何写入。
- 明确 missing-tag 时不调用 `gh release create`，tag 与审计分别返回宿主 release owner 和 Docs audit。

## Without Skill Baseline

- 同一 prompt/fixture 于 2026-07-20 全新生成，未应用或引用 skill、README、旧 baseline 或历史 comparison。
- baseline 也覆盖主要门禁；with-skill 额外给出准确 owner、missing-tag 命令边界和完整可执行时序。Baseline 较强不影响 with-skill PASS。

## Failures

- 无。独立 judge 未发现 skill、fixture、harness 或脆弱断言问题。

## Next Steps

- 当 #116/#117 handoff 字段、draft/publish gate 或 GitHub CLI missing-tag 行为契约变化时重新执行 paired validation。

## Runtime Artifacts Policy

- 本轮 `with_skill.md`、`without_skill.md` 与 `verdict.md` 仅位于 `tmp/eval-runs/120/`，不提交 transcript、verdict、with_skill、without_skill、outputs 或 diagnostics。
