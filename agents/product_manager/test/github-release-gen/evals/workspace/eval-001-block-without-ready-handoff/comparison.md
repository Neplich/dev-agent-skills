# Eval Result: github-release-gen-block-without-ready-handoff

## Evaluation Target

- Skill: `github-release-gen`
- Test case: missing and unconfirmed `docs-agent:release-notes-gen` handoff
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- Overall result: PASS

## Review Context

- Issue: #190（Release 标题与升级说明质量门禁修复）
- Date: 2026-08-03
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 独立读取当前 skill、两份 reference、eval 定义/metadata/fixture 与 issue-190 fresh 双侧 candidate；verdict 完成前未读取 durable `comparison.md` 或旧 run tmp。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped no-handoff 与 unconfirmed-handoff，包含候选页面和 source evidence
- With-skill evidence: `tmp/eval-runs/issue-190/with_skill/eval-001-block-without-ready-handoff/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-190/without_skill/eval-001-block-without-ready-handoff/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-190/judge/verdict.md`

## Assertions

- PASS `blocks_missing_handoff`：无 handoff 场景明确 blocked，指出缺少已就绪的站内 Release Notes handoff，不能生成可发布正文；without-skill FAIL（泛称 handoff/文档 owner，未点名 `docs-agent:release-notes-gen`）
- PASS `blocks_unconfirmed_handoff`：识别 `confirmation_status: unconfirmed`，docs check 与页面存在不替代正文确认；without-skill 同 PASS
- PASS `returns_to_site_release_notes`：两个场景返回 `docs-agent:release-notes-gen` 补齐确认或 handoff，不自行补证；without-skill FAIL（仅用「文档 owner」泛称，未点名具体 owner）
- PASS `no_publishable_output_or_mutation`：未生成可发布正文或发布命令，未创建 draft/tag、未执行写入；without-skill 同 PASS

## With Skill Behavior

- 两个入口缺口均判 blocked 并交回 `docs-agent:release-notes-gen`，完整列举缺失 handoff 字段（release_version、site_release_note_path、confirmation_status、docs checks、release surfaces、来源证据）与零写入边界。

## Without Skill Baseline

- 来源：issue-190 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：2/4 assertions PASS；能识别阻塞语义与零写入边界，但两次入口缺口均未点名 `docs-agent:release-notes-gen` 这一仓库特有 owner——精确 owner 路由是 with-skill 的有效增量。未见规则泄漏迹象。

## Failures / Findings

- 无 with-skill assertion failure。
- 非阻塞 finding：baseline 已内化通用阻塞与零写入语义（2/4 PASS），但两次入口缺口均未点名 `docs-agent:release-notes-gen` 这一仓库特有 owner——精确 owner 路由是 with-skill 的增量。

## Next Steps

- 保留当前 handoff 阻塞规则；后续修改 entry gate 或 handoff 契约时重新运行。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-190/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
