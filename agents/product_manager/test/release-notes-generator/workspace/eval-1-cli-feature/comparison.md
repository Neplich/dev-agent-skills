# Eval Result: eval-001-cli-feature-release

## Evaluation Target

- Agent: `product_manager`
- Skill: `release-notes-generator`
- Eval: `eval-001-cli-feature-release`
- Test case: cli-feature-release
- Workspace: `workspace/eval-1-cli-feature`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-06 after tag normalization repair

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that release-notes-generator handles cli-feature-release and produces the expected role-specific artifact.
- Expected output: 用户友好的 release notes，包含高亮功能、bug fixes 摘要、正确的 PR 链接，语气面向终端用户

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

- 当前 skill 通过 `reference/release-outline.md` 保持用户价值导向、分组组织、PR/compare 链接和请求产物输出要求。
- 当前 skill 明确要求先审计 compare 范围内全部 commit 和 merged PR，再决定哪些内容进入高亮、分组、摘要或省略。
- 当前 skill 明确区分 `THIS_TAG` 和 `VERSION`，release/tag/compare 命令使用完整 tag，changelog 路径使用去掉前导 `v` 的版本号，避免 `vv2.88.0`。
- 当前 skill 的 commit audit 命令使用 `PREV_TAG..THIS_TAG`，避免已发布旧版本被当前 `HEAD` 后续提交污染。
- 新增 release 大纲规范要求沿用仓库既有结构，`变更明细` 使用 `by @user in [#N](PR_URL)`，并把完整变更链接放在变更明细之后。
- `变更明细` 保留来源标题中的 conventional commit prefix，例如 `feat:`、`fix:`、`docs:`、`test:` 或 `chore:`。
- 新增 GitHub release workflow 覆盖 approved draft 发布前的 changelog archive、根 `CHANGELOG.md` 索引、tag 指向、draft 更新、发布和最终状态复核。
- 实际生成 `cli/cli` v2.88.0 release notes 时，输出包含 `What's New`、bug fixes、other improvements、upgrading、PR links 和 full changelog。`What's Changed` 中保留了 `feat(pr diff):`、`feat(repo):`、`fix:`、`docs:`、`build:`、`refactor:`、`chore(deps):` 等来源前缀。
- 运行记录显示先审计 `v2.87.3...v2.88.0` compare range 的 135 个 commits 和 release 范围内 39 个 merged PR，再进行分组和摘要；bot、dependency 和 internal-looking 条目被纳入审计。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation on 2026-06-06.

## Next Steps

- 保留该 eval 继续覆盖完整 source audit、PR 链接、升级说明和 conventional prefix 保留行为。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
