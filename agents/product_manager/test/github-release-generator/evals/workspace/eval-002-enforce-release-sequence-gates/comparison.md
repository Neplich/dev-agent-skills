# Eval Result: github-release-generator-enforce-release-sequence-gates

## Evaluation Target

- Skill: `github-release-generator`
- Test case: site-first、draft latest 隔离、publish 漂移复查与 publication triple gate
- Latest result: **PASS** - 2026-07-22 issue #154 r2 fresh paired validation；with-skill 6/6、without-skill 6/6 assertions 通过

## Review Context

- Review issue: #154
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 在独立 verdict 完成前未读取 durable `comparison.md` 或旧首轮 tmp；裁决基于当前 skill/reference、eval 定义、fixture 与 issue #154 r2 fresh 双侧 candidate。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped `v1.0.0-rc.1` confirmed page、latest `v0.9.0`、`ready_for_tag` 与两个不完整发布场景
- With-skill evidence: `tmp/eval-runs/issue-154/r2-final/with_skill/eval-002-enforce-release-sequence-gates/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-154/r2/without_skill/eval-002-enforce-release-sequence-gates/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-154/r2-final/judge/verdict.md`

## Assertions

- PASS `site_notes_before_github_release`: 双侧都明确站内 Release Notes 确认、docs-audit `ready_for_tag`、PM submit-ready preview 的先后顺序。
- PASS `ready_for_tag_allows_preview_only`: 双侧都只把该状态视为 preview 或另行批准的受限 draft 准备，不替代实际 tag、`release_verified` 或发布批准。
- PASS `draft_omits_latest_and_publish_rechecks`: 双侧都正确识别 prerelease 并展示 `--prerelease --latest=false`；draft 省略两种 latest flag；publish 覆盖含 `isPrerelease` 的 fresh target read、内容写后回读、最终写前 latest/tag OID 复查、最终原子应用 flags 与写后再回读，漂移时停止和路由。
- PASS `blocks_missing_tag_and_post_tag_audit`: 双侧都因场景 A 的实际 tag 与 `release_verified` 缺失而 blocked，分别返回 host release owner 与 `docs-agent:docs-audit`。
- PASS `blocks_missing_independent_approval`: 双侧都在场景 B 拒绝复用页面确认或 preview 请求作为当前独立 publish approval。
- PASS `keeps_preview_or_draft`: 双侧都在缺任一门禁时只保留 preview 或既有 draft，不发布。

## With Skill Behavior

- 完整展示 applicable-site evidence、pre-tag/final compare、单前缀 SemVer 归一化、latest 证据与精确 flags。
- 明确 draft 不得改变 published latest；两阶段 publish 在每个关键写点读取 target/latest/tag OID，并按 latest/tag 漂移分别回 Preview 或 host owner。
- A、B 两个请求在各自门禁处阻塞，本轮零外部写入。

## Without Skill Baseline

- 来源：issue #154 fresh baseline，基于同一 prompt 和 fixture，未读取或应用 skill、Agent README、with-skill 结果或历史 comparison。
- 行为：同样 6/6 assertions PASS，覆盖 release 顺序、draft latest 隔离、publish fresh-read/漂移保护和两组 publication blockers。
- 差异：baseline 对 published latest 必须保持 `v0.9.0` 的 draft readback 表述略弱；with-skill 对站点适用性、compare 双态和 recovery boundary 更完整。当前 assertions 区分度为 0/6。

## Failures / Findings

- 无 with-skill assertion failure 或 blocker。
- 非阻塞 finding：fixture、expected output 与 assertions 对完整写序提示较强，fresh baseline 也全部通过。

## Next Steps

- 当 #116/#117 handoff、draft latest 限制、publish 写序或 tag OID 漂移规则变化时重新执行 paired validation。
- 若需提升区分度，可降低 expected output 对最终写序的直接提示。

## Runtime Artifacts Policy

- 本轮双侧 candidates 与 judge verdict 位于上列精确 r2 scratch 路径，不得提交。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、manifest、verdict、outputs、timing、run status 或 diagnostics。
