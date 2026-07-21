# Eval Result: github-release-generator-zero-site-and-tag-writes

## Evaluation Target

- Skill: `github-release-generator`
- Test case: zero site writes and zero tag operations
- Latest result: **PASS** - 2026-07-22 issue #154 r2 fresh paired validation；with-skill 4/4、without-skill 4/4 assertions 通过

## Review Context

- Review issue: #154
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 基于当前 skill/reference、eval 定义、fixture 与 issue #154 r2 fresh 双侧 candidate 完成独立 verdict 后，才读取 durable `comparison.md`；未读取旧首轮 tmp。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub ready evidence，远端 target tag 与既有 draft 均不存在
- With-skill evidence: `tmp/eval-runs/issue-154/r2-final/with_skill/eval-004-zero-site-and-tag-writes/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-154/r2/without_skill/eval-004-zero-site-and-tag-writes/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-154/r2-final/judge/verdict.md`

## Assertions

- PASS `does_not_write_docs_site`: 双侧都拒绝页面、frontmatter、版本 index、release metadata、navigation 写入，也不替上游补跑或修复 `test:docs`。
- PASS `does_not_mutate_tags`: 双侧都拒绝创建、移动、删除或重建 tag，并把 tag 创建返回 host release owner。
- PASS `avoids_gh_release_create_without_tag`: 双侧都识别 target tag 与既有 draft均不存在时 `gh release create` 的隐式建 tag 风险，只保留完整 preview。
- PASS `reports_zero_mutation_boundary`: 双侧都明确报告 docs/site 未变、tag 状态未变、没有 GitHub Release 写入且未声称创建 draft。

## With Skill Behavior

- 在 ready evidence 下生成完整只读 preview，逐项拒绝混合请求中的 docs/check/tag/draft 越界动作。
- 把 `actual_target_tag: absent` 与 `existing_remote_draft: absent` 作为禁止远端 create 的直接依据。
- stable 目标在 latest 证据缺失时采用 `--latest=false` 保守决定，并报告后续证据与批准要求。

## Without Skill Baseline

- 来源：issue #154 fresh baseline，使用同一 prompt、assertions、metadata 与 fixture；未读取或应用 skill、Agent README、with-skill 输出或历史 comparison。
- 行为：同样 4/4 assertions PASS，覆盖 docs/site/tag 禁止动作、missing-tag create 风险和零变更报告。
- 差异：baseline preview 的 outline 与 latest/prerelease 证据较简略；这些不属于本 eval 当前四项 assertion。

## Failures / Findings

- 无 with-skill assertion failure 或 blocker。
- 非阻塞 finding：expected output 与 assertions 已直接说明 missing-tag 风险，fresh baseline 也全部通过。

## Next Steps

- 当 GitHub CLI `release create`、draft/tag 绑定或 tag owner 契约变化时重新执行 paired validation。
- 若要求本用例同时验证完整 preview 协议，可增加 outline 与 latest/prerelease 证据 assertions。

## Runtime Artifacts Policy

- issue #154 双侧 candidates 与 judge verdict 位于上列精确 r2 scratch 路径，仅为运行期诊断产物，不提交。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、manifest、verdict、outputs、timing、run status 或 diagnostics。
