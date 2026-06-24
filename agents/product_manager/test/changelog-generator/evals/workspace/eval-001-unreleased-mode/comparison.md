# Eval Result: eval-001-unreleased-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-001-unreleased-mode`
- Test case: unreleased-mode
- Workspace: `workspace/eval-001-unreleased-mode`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without_skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that changelog-generator handles unreleased-mode and produces the expected role-specific artifact.
- Expected output: 生成 ## [Unreleased] 章节，包含最新 release 之后的 PR 列表，按 Added/Changed/Fixed 分组，每条带 PR 链接，写入 docs/changelog/changelog-unreleased.md

## Assertions

- `unreleased`: 输出包含 ## [Unreleased] 标题
- `pr`: 每个条目包含 PR 链接，格式为 (#数字)
- `bot_pr_dependabot`: 跳过了 bot PR（dependabot 等）
- `chore_ci_test`: 不包含 chore/ci/test 等内部变更
- `versioned_changelog_file`: 输出写入了 docs/changelog/changelog-unreleased.md 文件

## With Skill

Observed behavior:

- 当前 skill 明确支持 Unreleased mode：定位最新 release 后的 merged PR，跳过 bot 和 chore/ci/test 等内部变更，按 Keep a Changelog 输出 ## [Unreleased] 并写入 docs/changelog/changelog-unreleased.md。

## Without Skill / Baseline
- BLOCKED: No actual without_skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 真实运行时仍需 gh 数据验证具体 PR 窗口。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
