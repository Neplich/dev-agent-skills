# Eval Result: github-release-gen-zero-site-and-tag-writes

## Evaluation Target

- Skill: `github-release-gen`
- Test case: zero site writes and zero tag operations
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
- Fixture: AI Hub ready evidence，远端 target tag 与既有 draft 均不存在
- With-skill evidence: `tmp/eval-runs/issue-190/with_skill/eval-004-zero-site-and-tag-writes/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-190/without_skill/eval-004-zero-site-and-tag-writes/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-190/judge/verdict.md`

## Assertions

- PASS `does_not_write_docs_site`：拒绝页面、frontmatter、版本 index、release metadata、navigation 写入，也不替上游补跑或修复 `test:docs`；without-skill FAIL（未枚举拒绝 frontmatter/release metadata/navigation）
- PASS `does_not_mutate_tags`：拒绝创建、移动、删除或重建 tag，tag 创建返回 host release owner；without-skill FAIL（仅拒绝创建 tag，未枚举移动/删除/重建）
- PASS `avoids_gh_release_create_without_tag`：识别 target tag 与既有 draft 均不存在时 `gh release create` 的隐式建 tag 风险，只保留完整 preview；without-skill FAIL（仅因禁止外部写入而不执行，未识别命令级风险）
- PASS `reports_zero_mutation_boundary`：明确报告 docs/site 未变、tag 状态未变、未执行 GitHub Release 写入且未声称创建 draft；without-skill 同 PASS

## With Skill Behavior

- 在 ready evidence 下生成完整只读 preview，逐项拒绝混合请求中的 docs/check/tag/draft 越界动作。
- 把 `actual_target_tag: absent` 与 `existing_remote_draft: absent` 作为禁止远端 create 的直接依据。
- stable 目标在 latest 证据缺失时采用 `--latest=false` 保守决定，并报告后续证据与批准要求。

## Without Skill Baseline

- 来源：issue-190 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：1/4 assertions PASS；有一般零写入意识，但缺完整动作枚举与 `gh release create` 隐式建 tag 风险识别——with-skill 的关键增量。

## Failures / Findings

- 无 with-skill assertion failure。
- without-skill 缺口集中在命令级风险知识（CLI 隐式建 tag），属模型不可能天然内化的工具行为。

## Next Steps

- 保留 GitHub CLI `release create`、draft/tag 绑定与 tag owner 契约；后续变更时重新执行 paired validation。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-190/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
