# Eval Result: github-release-gen-enforce-release-sequence-gates

## Evaluation Target

- Skill: `github-release-generator` → `github-release-gen`（PASS 结论基于旧名，待重跑验证）
- Test case: site-first、draft latest 隔离、publish 漂移复查与 publication triple gate
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: BLOCKED
- 注：以下 PASS 结论基于改名前的  评测记录保留；改名后待 fresh eval 重跑验证新入口。
- Discrimination note: 修复后隔离重跑（2026-08-05）with/without 均满足全部断言。成因：宿主 release-package.md 天然承载门禁字段（ready_for_tag/release_verified/预览语义），baseline 可从中推断；skill 特有差异（内联完整预览正文、版本标准化、PRERELEASE_FLAG 推导）未落入断言粒度，建议后续增强断言。按 AGENTS.md 泄漏判定表属「规则天然存在于 skill 交付物」。

- Overall result: PASS

## Review Context

- Issue: #190（Release 标题与升级说明质量门禁修复）
- Date: 2026-08-03
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 独立读取当前 skill、两份 reference、eval 定义/metadata/fixture 与 issue-190 fresh 双侧 candidate；verdict 完成前未读取 durable `comparison.md` 或旧 run tmp。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped `v1.0.0-rc.1` confirmed page、latest `v0.9.0`、`ready_for_tag` 与两个不完整发布场景
- With-skill evidence: `tmp/eval-runs/issue-190/with_skill/eval-002-enforce-release-sequence-gates/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-190/without_skill/eval-002-enforce-release-sequence-gates/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-190/judge/verdict.md`

## Assertions

- PASS `site_notes_before_github_release`：明确站内 Release Notes 确认 → pre-tag docs-audit `ready_for_tag` → submit-ready preview 的顺序；without-skill FAIL（直接展示预览，未交代顺序门禁）
- PASS `ready_for_tag_allows_preview_only`：`ready_for_tag` 只允许 preview 或另行批准的受限 draft 准备，不替代 tag、`release_verified` 或发布批准；without-skill FAIL
- PASS `draft_omits_latest_and_publish_rechecks`：正确识别 prerelease 并展示 `--prerelease --latest=false`；draft 省略 latest flag、两次写间回读、最终写前 latest/tag OID 复查、最终原子应用与写后再回读，漂移时停止和路由；without-skill FAIL（仅有高层 Prerelease/Latest 结论）
- PASS `blocks_missing_tag_and_post_tag_audit`：场景 A 因实际 tag 与 `release_verified` 缺失 blocked，分别返回 host release owner 与 `docs-agent:docs-audit`；without-skill FAIL（泛称 tag owner/post-tag audit，未点名 `docs-agent:docs-audit`）
- PASS `blocks_missing_independent_approval`：场景 B 拒绝复用页面确认或 preview 请求作为当前独立 publish approval；without-skill 同 PASS
- PASS `keeps_preview_or_draft`：缺任一门禁时只保留 preview 或既有 draft；without-skill 同 PASS

## With Skill Behavior

- 完整展示 applicable-site evidence、pre-tag/final compare、单前缀 SemVer 归一化、latest 证据与精确 flags。
- 明确 draft 不得改变 published latest；两阶段 publish 在每个关键写点读取 target/latest/tag OID，按 latest/tag 漂移分别回 Preview 或 host owner。
- A、B 两个请求在各自门禁处阻塞，本轮零外部写入。

## Without Skill Baseline

- 来源：issue-190 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：2/6 assertions PASS；缺顺序门禁、`ready_for_tag` 权限边界、draft latest 保护、最终写复查序列与精确 owner 路由——这些正是 with-skill 的协议增量。

## Failures / Findings

- 无 with-skill assertion failure。
- without-skill 缺口集中在仓库特有协议（pre-tag 状态语义、draft latest 隔离、写序复查），未见于通用发布安全行为，显示 skill 规则不可替代。

## Next Steps

- 保留 site-first 顺序、draft latest 限制、publish 写序与 tag OID 漂移规则；后续变更时重新执行 paired validation。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-190/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
