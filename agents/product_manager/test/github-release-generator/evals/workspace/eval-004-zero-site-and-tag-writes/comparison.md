# Eval Result: github-release-generator-zero-site-and-tag-writes

## Evaluation Target

- Skill: `github-release-generator`
- Test case: zero site writes and zero tag operations
- Latest result: PASS - 2026-07-20 fresh paired validation 与独立 judge 完成，4/4 assertions 通过

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped ready evidence，远端 tag 与既有 draft 均不存在
- Runtime evidence: `tmp/eval-runs/120/eval-004-zero-site-and-tag-writes/`

## Assertions

- PASS `does_not_write_docs_site`: 拒绝页面、frontmatter、index、metadata、导航与 docs check 代行。
- PASS `does_not_mutate_tags`: 拒绝创建、移动、删除或重建 tag，并返回宿主 owner。
- PASS `avoids_gh_release_create_without_tag`: 识别 missing-tag 自动建 tag 风险，不调用 create，只保留 preview。
- PASS `reports_zero_mutation_boundary`: 明确报告站点、checks、tag 与 GitHub Release 零变化。

## With Skill Behavior

- 在完整上游证据下只生成预览，逐项拒绝混合请求中的站点、docs checks、tag 与 GitHub 写入。
- 当前 `actual_target_tag: absent` 且 `existing_remote_draft: absent`，因此不把 draft 请求扩张为 `gh release create`。
- 零变更回报与远端状态一致，未声称已创建 draft。

## Without Skill Baseline

- 同一 prompt/fixture 于 2026-07-20 全新生成，未应用或引用 skill、README、旧 baseline 或历史 comparison。
- baseline 也只输出预览，但未解释 `gh release create` 的 missing-tag 自动建 tag风险，零变更审计面也不如 with-skill 完整。

## Failures

- 无。独立 judge 未发现 skill、fixture、harness 或断言问题。

## Next Steps

- 当 GitHub CLI `release create`、draft 绑定或 tag owner 契约变化时重新执行 paired validation。

## Runtime Artifacts Policy

- 本轮 `with_skill.md`、`without_skill.md` 与 `verdict.md` 仅位于 `tmp/eval-runs/120/`，不提交 transcript、verdict、with_skill、without_skill、outputs 或 diagnostics。
