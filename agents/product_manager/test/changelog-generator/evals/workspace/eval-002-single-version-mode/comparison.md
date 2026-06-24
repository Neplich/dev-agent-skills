# Eval Result: eval-002-single-version-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-generator`
- Eval: `eval-002-single-version-mode`
- Test case: single-version-mode
- Workspace: `workspace/eval-002-single-version-mode`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that changelog-generator handles single-version-mode and produces the expected role-specific artifact.
- Expected output: 生成最新 release tag 的版本块，格式为 ## [x.y.z] - YYYY-MM-DD，包含该版本窗口内的 PR，分组写入，每条带 PR 链接，并写入 docs/changelog/changelog-v{version}.md

## Assertions

- `x_y_z_yyyy_mm_dd`: 输出包含版本号和日期，格式 ## [x.y.z] - YYYY-MM-DD
- `release_tag`: 版本号与实际 release tag 匹配
- `pr_conventional_commit`: PR 条目标题经过清洗（去掉 conventional commit 前缀）
- `breaking_change_breaking`: Breaking change 如有则带 ⚠️ BREAKING 前缀
- `section`: 有内容的 section 才出现在输出中

## With Skill

Observed behavior:

- 当前 skill 明确支持最新 release 单版本模式：通过 release/tag 窗口取 PR，版本块带日期，清洗 conventional commit 前缀，处理 breaking change，并省略空 section。

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 真实运行时需确认最新 release tag 与 GitHub 数据。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
