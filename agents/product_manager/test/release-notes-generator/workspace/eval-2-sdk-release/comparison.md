# Eval Result: eval-002-sdk-breaking-changes

## Evaluation Target

- Agent: `product_manager`
- Skill: `release-notes-generator`
- Eval: `eval-002-sdk-breaking-changes`
- Test case: sdk-breaking-changes
- Workspace: `workspace/eval-2-sdk-release`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that release-notes-generator handles sdk-breaking-changes and produces the expected role-specific artifact.
- Expected output: 技术受众的 release notes，正确识别并突出 breaking changes（如有），highlights 聚焦 API 变化的用户价值

## Assertions

- `audience_value`: 面向目标用户说明发布价值，而不是只罗列提交或 PR
- `change_grouping`: 按 features、fixes、breaking changes 或等价分组组织变更
- `source_links`: 保留正确版本、仓库和 PR 或 release 相关链接
- `source_audit`: 先审计版本范围内所有 commit 和 PR，再决定 release notes 的分组、摘要或省略
- `requested_output`: 按用户要求写入或明确给出目标 release notes 产物

## With Skill

Observed behavior:

- 当前 skill 仍要求面向技术受众保持用户价值导向，突出 breaking changes 或说明无破坏性变更，并保留升级指引、关键 PR 链接和版本信息。
- 当前 skill 明确要求完整检查版本范围内所有 commit 和 merged PR，不能在审计前过滤 bot、docs、chore 或内部变更。
- `reference/release-outline.md` 保留通用 SDK / library release notes 结构，同时要求按仓库既有大纲输出中文 release notes。
- `reference/github-release-workflow.md` 补充 approved draft 发布前的 changelog、tag 和 draft release 复核流程，不削弱 SDK release notes 的断言。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation on 2026-06-06.

## Next Steps

- 真实运行时需验证 v0.86.0 release 数据。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
