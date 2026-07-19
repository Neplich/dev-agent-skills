# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Test Set / Fixture Version

- Fixture: `issue-121-s2c-semantic-assertion`
- Run date: `2026-07-19`

## Latest Result

**PASS** — 本轮全新 with-skill 经独立 fresh judge 判定 4/4 assertions 通过；独立生成的 without-skill baseline 为 1/4。

## With-Skill Behavior

- 正确拒绝 Release Notes 正文、index、metadata 与 navigation 写入。
- 将 v1.5.0 请求与现有证据明确 handoff 给 `docs-agent:release-notes-generator`，而不是 docs-audit、GitHub Release 或泛化 PM 路由。
- `docs/site/` 源文件数保持 41 → 41，全量 pre/post aggregate SHA-256 均为 `c1ee97857b40a5c5670875fdf40958cd38c5a18ed48a00666d6496490fc0bf01`；不创建 tag，也不操作 GitHub Release。

## Without-Skill Baseline

- 本轮独立生成的全新 baseline 仅满足 1/4：直接创建 v1.5.0 页面并修改 release index 与 metadata，`docs/site/` 源文件数由 41 → 42，aggregate hash 由 `c1ee978...` 变为 `81efe826...`；未 handoff 给 `docs-agent:release-notes-generator`，但未操作 GitHub Release。

## Failures

- None。with-skill 四条语义 assertions 均通过。

## Assertion Revision

- 维护者决定从 `handoffs_site_release_notes_specialist` assertion 与 `expected_output` 中移除 `issue #116` 字面要求，以对齐 `AGENTS.md` 的语义断言准则，避免把运行时 skill 绑定到脆弱的 GitHub issue 编号字符串。
- 行为语义未变：仍必须将请求与证据 handoff 给 `docs-agent:release-notes-generator`，而不是 docs-audit、GitHub Release 或泛化 PM 路由。

## Next Steps

- eval-010 门禁已解除；按 S2 交付流程继续确定性验证与 PR 交付。

## Runtime Artifact Policy

- 本轮 transcripts、隔离 workspace 副本、manifest 与 independent judge verdict 仅位于 `tmp/eval-runs/121-s2c-eval010/`，不提交。
