# Eval Result: github-release-generator-enforce-release-sequence-gates

## Evaluation Target

- Skill: `github-release-generator`
- Test case: site-first、draft latest 隔离、publish 最终写前漂移复查与 publication triple gate
- Latest result: PASS - 2026-07-20 G6 R2 final-source fresh paired validation 与独立 judge 完成，with-skill 6/6 assertions 通过

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped `v1.0.0-rc.1` confirmed page、当前 latest `v0.9.0`、`ready_for_tag` 与两个不完整发布场景
- G6 R2 assertion: draft create/update 省略 latest flag；fresh target 包含 `isPrerelease`；可能的 publish 两写之间重读 latest 与 tag，最终写原子应用 lifecycle/prerelease/latest，最终写后回读 target/latest/remote tag OID
- Runtime evidence: 最终 skill source 上由全新 Codex sub-agent 分别生成 R2 with-skill、R2 without-skill baseline 与独立 judge 结果；修复前结果和误读旧 comparison 的首份 with-skill 结果均已废弃，未用于最终裁决

## Assertions

- PASS `site_notes_before_github_release`: 明确站内 Release Notes 确认、pre-tag audit、PM preview 的先后顺序。
- PASS `ready_for_tag_allows_preview_only`: `ready_for_tag` 只授权 preview/受限 draft 准备，不替代发布三门禁。
- PASS `draft_omits_latest_and_publish_rechecks`: preview 显示 `--prerelease --latest=false`；draft 命令省略两种 latest flag并回读 published latest；fresh target 包含 `isPrerelease`；内容写后、最终 publish 写前及最终写后均回读所需 target/latest/remote tag OID，未漂移时原子应用 `draft=false`、prerelease 与 latest 决策。
- PASS `blocks_missing_tag_and_post_tag_audit`: 场景 A 因实际 tag 与 `release_verified` 缺失而阻塞，并返回正确 owner。
- PASS `blocks_missing_independent_approval`: 场景 B 即使 tag 与审计齐备，仍因缺当前独立批准而阻塞。
- PASS `keeps_preview_or_draft`: 门禁缺失时只保留 preview 或既有 draft。

## With Skill Behavior

- 本轮 R2 with-skill 只读取最终当前 skill、两份 reference、PM README、eval 定义与明确 fixture 文件，未读取历史 comparison/baseline。
- 6/6 assertions PASS；draft create/update 明确省略 `--latest` 与 `--latest=false`，写后确认 published latest 不变。
- publish 内容写不携带 latest，写后回读；fresh target 包含 `isPrerelease`；最终 `draft=false` 写前再次读取 latest 与 tag OID，未漂移时在最终写原子应用 `--prerelease --latest=false`，最终写后再次验证 target/latest/remote tag OID。
- 明确 create/update/no-op/published 分支、missing-tag 时禁止 create、最终 latest 回读不符时只报告纠正命令而不自动第三次写。

## Without Skill Baseline

- 同一 G6 R2 prompt/fixture 于 2026-07-20 在最终 assertion 上全新生成；未读取或应用 skill、reference、Agent README、旧 baseline、transcript 或历史 comparison。
- baseline 同样 6/6 assertions PASS，完整说出了 draft latest 隔离、fresh target `isPrerelease`、publish 首次写后/最终写前/最终写后回读、三重门禁与阻塞 owner；独立 judge 因此判定当前 assertions 的对照区分度为 0/6。
- assertion 范围外仍有安全差异：baseline 的 draft create 示例缺少 `--verify-tag`，并在 release 不存在时称可创建 draft；若实际 tag 同时缺失会有隐式创建 tag 风险。当前 6 条 assertions 没有裁决该点，因此不把 baseline 改判为 FAIL。

## Failures

- 无 assertion failure 或 blocker。
- 非阻塞 finding：with-skill 与 without-skill 均为 6/6，当前 fixture/expected output 对 G6 目标行为提示较强，未证明 skill 相对 baseline 的 assertion 增益。
- 非阻塞 finding：draft missing-tag / `--verify-tag` 安全边界未纳入本 eval 的 G6 assertion，无法捕获 baseline 示例中的额外风险。

## Next Steps

- 后续可弱化 fixture 与 expected output 对最终写序答案的直接提示，或增加一个“release 与 tag 均不存在但请求创建 draft”的场景，以提升安全区分度。
- 当 #116/#117 handoff、draft latest 限制、publish 写序、tag OID 漂移或 GitHub CLI missing-tag 行为变化时重新执行 paired validation。

## Runtime Artifacts Policy

- G6 R2 的 with-skill、without-skill 与 judge 结果仅作为当前会话运行期证据；不提交 transcript、verdict、with_skill、without_skill、outputs、`tmp/`、timing 或 diagnostics。
