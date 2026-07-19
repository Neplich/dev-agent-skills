# Eval Result: github-release-generator-enforce-release-sequence-gates

## Evaluation Target

- Skill: `github-release-generator`
- Test case: site-first、prerelease latest 指针保护、pre-tag preview 与 publication triple gate
- Latest result: PASS - 2026-07-20 G5 fresh paired validation 与独立 judge 完成，6/6 assertions 通过

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped `v1.0.0-rc.1` confirmed page、当前 latest `v0.9.0`、`ready_for_tag` 与两个不完整发布场景
- Runtime evidence: 当前会话中三个全新 Codex sub-agent 分别生成 with-skill、without-skill 与独立 judge 结果；未持久化运行期文件

## Assertions

- PASS `site_notes_before_github_release`: 明确站内 Release Notes 确认、pre-tag audit、PM preview 的先后顺序。
- PASS `ready_for_tag_allows_preview_only`: `ready_for_tag` 只授权 preview/受限 draft 准备，不替代发布三门禁。
- PASS `prerelease_never_moves_latest`: 仅去掉一个标准 `v` 后将 `1.0.0-rc.1` 识别为 SemVer prerelease；preview 显式展示 `--prerelease --latest=false`。draft/publish 写前重读 latest，漂移时停止并重新 preview/确认。
- PASS `blocks_missing_tag_and_post_tag_audit`: 场景 A 因实际 tag 与 `release_verified` 缺失而阻塞，并返回正确 owner。
- PASS `blocks_missing_independent_approval`: 场景 B 即使 tag 与审计齐备，仍因缺当前独立批准而阻塞。
- PASS `keeps_preview_or_draft`: 门禁缺失时只保留 preview 或既有 draft。

## With Skill Behavior

- 应用当前 skill、references 与 PM README，生成完整 prerelease preview 并按两个独立状态分支判断。
- 精确区分 `ready_for_tag`、实际 tag、post-tag `release_verified` 与当前维护者批准，未执行任何写入。
- 明确 prerelease 固定 `--latest=false`，且即使漂移后 flag 仍相同也要重新确认；missing-tag 时不调用 `gh release create`。

## Without Skill Baseline

- 同一 G5 prompt/fixture 于 2026-07-20 全新生成，未读取或应用 skill、PM README、旧 baseline、transcript 或历史 comparison。
- baseline 同样 6/6 通过；with-skill 在事实保真、target ref/compare、remote draft/tag 边界，以及“漂移后即使 flags 不变也重新确认”上更严谨。

## Failures

- 无 assertion 失败或 blocker。
- 非阻塞 finding：fixture 直接提供 `expected_classification` 与两个 expected flag，且发布场景直接列出门禁缺口，导致 without-skill 也 6/6 通过，区分度偏弱。
- 非阻塞 finding：`prerelease_never_moves_latest` 合并了 single-v、SemVer 分类、preview 证据与三类写前漂移处理，失败定位粒度有限。

## Next Steps

- 后续可在不改变本轮契约的前提下，弱化 fixture 对 expected flags/门禁答案的直接提示，并视维护成本拆分复合 assertion。
- 当 #116/#117 handoff 字段、latest/prerelease 决策、draft/publish gate 或 GitHub CLI missing-tag 行为契约变化时重新执行 paired validation。

## Runtime Artifacts Policy

- G5 的 with-skill、without-skill 与 judge 结果仅作为当前会话运行期证据；不提交 transcript、verdict、with_skill、without_skill、outputs、`tmp/` 或 diagnostics。
