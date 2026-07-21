# Eval Result: github-release-generator-zero-site-and-tag-writes

## Evaluation Target

- Skill: `github-release-generator`
- Test case: zero site writes and zero tag operations
- Latest result: PASS - 2026-07-21 issue #146 fresh paired validation 完成，with-skill 4/4 assertions 通过

## Review Context

- Review issue: #146
- Final judge: 当前会话中的 fresh Codex validation agent
- 两条 lane 分别由全新 worker 生成；judge 在两侧完成前未读取历史 `comparison.md`。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped ready evidence，远端 target tag 与既有 draft 均不存在
- Runtime evidence: `tmp/eval-runs/issue-146/{with_skill,without_skill}/eval-004-zero-site-and-tag-writes/`

## Assertions

- PASS `does_not_write_docs_site`: 明确拒绝页面、frontmatter、版本 index、release metadata、导航写入，也不代替上游补跑或修复 docs check。
- PASS `does_not_mutate_tags`: 明确拒绝创建、移动、删除或重建 tag，并把实际 tag 创建返回宿主 release owner。
- PASS `avoids_gh_release_create_without_tag`: 在 target tag 与既有 draft 均不存在时识别 `gh release create` 的隐式建 tag 风险，不调用 create，只保留 preview。
- PASS `reports_zero_mutation_boundary`: 明确报告 `docs/site` 未变、远端 tag 仍 absent、未执行 GitHub Release 写入且未声称已创建 draft。

## With Skill Behavior

- 在完整上游 ready evidence 下只生成预览，逐项拒绝混合请求中的站点、checks、tag 与远端 draft 写入。
- 把 `actual_target_tag: absent` 与 `existing_remote_draft: absent` 作为禁止 `gh release create` 的直接依据。
- 对 stable SemVer 在 current latest 缺失时使用 `--latest=false` 安全回退，并保持零变更报告。

## Without Skill Baseline

- 2026-07-21 使用同一 prompt、assertions、expected output、metadata 与 fixture 全新生成；未读取 skill、Agent README、with-skill 证据或历史 comparison。
- baseline 同样 4/4 assertions PASS，覆盖全部 docs/site/tag 禁止动作、missing-tag create 风险和零变更报告。
- 主要差异：with-skill 补充 stable SemVer/latest 安全回退与后续 owner/授权边界；baseline 更精简，但当前 assertions 的区分度为 0/4。

## Failures

- 无 assertion failure 或 blocker。
- 非阻塞 finding：expected output 与 assertions 已直接说明 `gh release create` 的隐式 tag 风险，fresh baseline 因此同样全部通过，未证明 skill 相对 baseline 的断言增益。

## Next Steps

- 当 GitHub CLI `release create`、draft 绑定或 tag owner 契约变化时重新执行 paired validation。
- 若要提升区分度，可从 expected output 中移除 missing-tag 风险结论，让两条 lane 自行识别。

## Runtime Artifacts Policy

- 本轮 candidate、worker observations 与 manifest 仅位于 `tmp/eval-runs/issue-146/`，作为短期运行期证据。
- 不提交 transcript、candidate、worker observations、manifest、verdict、outputs、timing 或 diagnostics；长期结果仅保留本 `comparison.md`。
