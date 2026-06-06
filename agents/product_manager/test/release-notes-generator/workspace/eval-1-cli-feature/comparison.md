# Eval Result: eval-001-cli-feature-release

## Evaluation Target

- Agent: `product_manager`
- Skill: `release-notes-generator`
- Eval: `eval-001-cli-feature-release`
- Test case: cli-feature-release
- Workspace: `workspace/eval-1-cli-feature`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that release-notes-generator handles cli-feature-release and produces the expected role-specific artifact.
- Expected output: 用户友好的 release notes，包含高亮功能、bug fixes 摘要、正确的 PR 链接，语气面向终端用户

## Assertions

- `audience_value`: 面向目标用户说明发布价值，而不是只罗列提交或 PR
- `change_grouping`: 按 features、fixes、breaking changes 或等价分组组织变更
- `source_links`: 保留正确版本、仓库和 PR 或 release 相关链接
- `source_audit`: 先审计版本范围内所有 commit 和 PR，再决定 release notes 的分组、摘要或省略
- `change_detail_prefix`: 变更明细保留来源 PR 标题或 commit subject 中的 conventional commit 前缀
- `requested_output`: 按用户要求写入或明确给出目标 release notes 产物

## With Skill

Observed behavior:

- 当前 skill 通过 `reference/release-outline.md` 保持用户价值导向、分组组织、PR/compare 链接和请求产物输出要求。
- 当前 skill 明确要求先审计 compare 范围内全部 commit 和 merged PR，再决定哪些内容进入高亮、分组、摘要或省略。
- 新增 release 大纲规范要求沿用仓库既有结构，`变更明细` 使用 `by @user in [#N](PR_URL)`，并把完整变更链接放在变更明细之后。
- `变更明细` 保留来源标题中的 conventional commit prefix，例如 `feat:`、`fix:`、`docs:`、`test:` 或 `chore:`。
- 新增 GitHub release workflow 覆盖 approved draft 发布前的 changelog archive、根 `CHANGELOG.md` 索引、tag 指向、draft 更新、发布和最终状态复核。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation on 2026-06-06.

## Next Steps

- 真实运行时需 gh release/PR 数据验证。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
