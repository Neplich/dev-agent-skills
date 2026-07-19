# Eval Result: eval-002-sdk-breaking-changes

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-generator`
- Eval: `eval-002-sdk-breaking-changes`
- Test case: sdk-breaking-changes
- Workspace: `workspace/eval-2-sdk-release`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without_skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-06 after tag normalization repair

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Historical pre-rename release-notes fixture; G2 must realign it to github-release-generator gates.
- Expected output: 技术受众的 release notes，正确识别并突出 breaking changes（如有），highlights 聚焦 API 变化的用户价值

## Assertions

- `audience_value`: 面向目标用户说明发布价值，而不是只罗列提交或 PR
- `change_grouping`: 按 features、fixes、breaking changes 或等价分组组织变更
- `source_links`: 保留正确版本、仓库和 PR 或 release 相关链接
- `source_audit`: 先审计版本范围内所有 commit 和 PR，再决定 release notes 的分组、摘要或省略
- `tag_normalization`: 输入带 v 的 tag 时不会在 release、tag 或 changelog 模板中生成双 v
- `target_tag_audit_range`: commit 审计范围使用目标 tag 而不是 HEAD
- `change_detail_prefix`: 变更明细保留来源 PR 标题或 commit subject 中的 conventional commit 前缀
- `requested_output`: 按用户要求写入或明确给出目标 release notes 产物

## With Skill

Observed behavior:

- 当前 skill 仍要求面向技术受众保持用户价值导向，突出 breaking changes 或说明无破坏性变更，并保留升级指引、关键 PR 链接和版本信息。
- 当前 skill 明确要求完整检查版本范围内所有 commit 和 merged PR，不能在审计前过滤 bot、docs、chore 或内部变更。
- 当前 skill 明确区分 `THIS_TAG` 和 `VERSION`，release/tag/compare 命令使用完整 tag，changelog 路径使用去掉前导 `v` 的版本号，避免 `vv0.86.0`。
- 当前 skill 的 commit audit 命令使用 `PREV_TAG..THIS_TAG`，避免已发布旧版本被当前 `HEAD` 后续提交污染。
- `reference/release-outline.md` 保留通用 SDK / library release notes 结构，同时要求按仓库既有大纲输出中文 release notes。
- `变更明细` 保留来源标题中的 conventional commit prefix，例如 `feat:`、`fix:`、`docs:`、`test:` 或 `chore:`。
- `reference/github-release-workflow.md` 补充 approved draft 发布前的 changelog、tag 和 draft release 复核流程，不削弱 SDK release notes 的断言。
- 实际生成 `anthropics/anthropic-sdk-python` v0.86.0 release notes 时，输出包含 breaking changes、What's New、fixes and compatibility、upgrade guide、PR links 和 full changelog。
- 运行记录显示先审计 `v0.85.0...v0.86.0` compare range 的 8 个 commits 和 included merged PR，再进行分组和摘要；`stainless-app[bot]`、internal、generated API 和 release commit 均被纳入审计。`What's Changed` 保留了 `feat:`、`feat(api):`、`fix(client):`、`fix(deps):`、`fix(pydantic):`、`chore(internal):`、`release:` 等前缀。

## Without Skill / Baseline
- BLOCKED: No actual without_skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation on 2026-06-06.

## Next Steps

- G1 仅迁移结构；本历史结果不证明 #116/#117 新门禁，G2 需重写并 fresh validation。

- 保留该 eval 继续覆盖 SDK breaking-change 判断、完整 source audit、升级命令和 conventional prefix 保留行为。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
