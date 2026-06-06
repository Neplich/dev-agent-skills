# Eval Result: eval-003-library-release-notes

## Evaluation Target

- Agent: `product_manager`
- Skill: `release-notes-generator`
- Eval: `eval-003-library-release-notes`
- Test case: library-release-notes
- Workspace: `workspace/eval-3-library-release`
- Latest result: PASS - Codex CLI eval generation completed on 2026-06-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that release-notes-generator handles library-release-notes and produces the expected role-specific artifact.
- Expected output: 库发版说明，features 和 fixes 正确区分，升级指引清晰

## Assertions

- `audience_value`: 面向目标用户说明发布价值，而不是只罗列提交或 PR
- `change_grouping`: 按 features、fixes、breaking changes 或等价分组组织变更
- `source_links`: 保留正确版本、仓库和 PR 或 release 相关链接
- `source_audit`: 先审计版本范围内所有 commit 和 PR，再决定 release notes 的分组、摘要或省略
- `change_detail_prefix`: 变更明细保留来源 PR 标题或 commit subject 中的 conventional commit 前缀
- `requested_output`: 按用户要求写入或明确给出目标 release notes 产物

## With Skill

Observed behavior:

- 当前 skill 继续支持库版本 release notes：feature/fix/upgrade 分组、升级命令、PR 链接、用户视角语气和可选无 breaking 说明均被协议覆盖。
- 当前 skill 明确要求用完整 commit/PR 审计作为 release notes 依据，再进行用户可读的归并和取舍。
- `reference/release-outline.md` 拆出 release 大纲与格式规则，确保 `变更明细`、贡献者 mention 和完整变更链接位置稳定。
- `变更明细` 保留来源标题中的 conventional commit prefix，例如 `feat:`、`fix:`、`docs:`、`test:` 或 `chore:`。
- `reference/github-release-workflow.md` 拆出 tag、draft release、changelog preflight 和发布复核流程，不影响库 release notes 的请求产物输出要求。
- 实际生成 `fastapi/fastapi` 0.135.0 release notes 时，输出包含 SSE feature highlight、bug-fix absence statement、documentation notes、upgrade guide、PR link 和 full changelog。
- 运行记录显示先审计 `0.134.0...0.135.0` compare range 的 3 个 commits 和 merged PR [#15030](https://github.com/fastapi/fastapi/pull/15030)，再进行分组和摘要；release metadata commit 与 bot-authored release note commit 均被纳入审计。该 release 来源标题未使用 conventional prefix，因此输出按来源保留 emoji/title 格式。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in Codex CLI eval generation on 2026-06-06.

## Next Steps

- 保留该 eval 继续覆盖 library release notes、完整 source audit、升级命令和来源标题保留行为。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
