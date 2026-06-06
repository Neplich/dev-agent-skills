# Eval Result: eval-003-library-release-notes

## Evaluation Target

- Agent: `product_manager`
- Skill: `release-notes-generator`
- Eval: `eval-003-library-release-notes`
- Test case: library-release-notes
- Workspace: `workspace/eval-3-library-release`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that release-notes-generator handles library-release-notes and produces the expected role-specific artifact.
- Expected output: 库发版说明，features 和 fixes 正确区分，升级指引清晰

## Assertions

- `audience_value`: 面向目标用户说明发布价值，而不是只罗列提交或 PR
- `change_grouping`: 按 features、fixes、breaking changes 或等价分组组织变更
- `source_links`: 保留正确版本、仓库和 PR 或 release 相关链接
- `source_audit`: 先审计版本范围内所有 commit 和 PR，再决定 release notes 的分组、摘要或省略
- `requested_output`: 按用户要求写入或明确给出目标 release notes 产物

## With Skill

Observed behavior:

- 当前 skill 继续支持库版本 release notes：feature/fix/upgrade 分组、升级命令、PR 链接、用户视角语气和可选无 breaking 说明均被协议覆盖。
- 当前 skill 明确要求用完整 commit/PR 审计作为 release notes 依据，再进行用户可读的归并和取舍。
- `reference/release-outline.md` 拆出 release 大纲与格式规则，确保 `变更明细`、贡献者 mention 和完整变更链接位置稳定。
- `reference/github-release-workflow.md` 拆出 tag、draft release、changelog preflight 和发布复核流程，不影响库 release notes 的请求产物输出要求。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation on 2026-06-06.

## Next Steps

- 真实运行时需验证 fastapi 0.135.0 release 数据。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
