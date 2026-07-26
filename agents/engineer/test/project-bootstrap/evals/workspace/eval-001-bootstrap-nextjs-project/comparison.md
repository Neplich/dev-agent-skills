# Eval Result: eval-001-bootstrap-nextjs-project

## Evaluation Target

- Agent: `engineer`
- Skill: `project-bootstrap`
- Eval: `eval-001-bootstrap-nextjs-project`
- Test case: bootstrap-nextjs-project
- Workspace: `workspace/eval-001-bootstrap-nextjs-project`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 3/3 assertions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved `docs/trd.md` defining the Next.js stack, official CLI, tooling, CI, and verification commands
- Expected output: 项目初始化完成 + 配置完成 + 验证通过

## Assertions

- PASS `cli`: 两侧均实际运行 `create-next-app@latest`，使用 App Router、TypeScript、ESLint、src、npm 等非交互参数。
- PASS `assertion_2`: with_skill 配置 ESLint、Prettier 和 GitHub Actions CI。
- PASS `assertion_3`: with_skill 的 build、lint、test、format check 均退出零。

## With Skill

- 使用 Next.js 16.2.12 官方 CLI 完成 scaffold，并补齐 lint、format、CI 与 `node:test`。
- 额外建立约定的顶层目录与 README。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 project-bootstrap skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 3/3 assertions；批准的 TRD 已明确官方 CLI 和基础设施要求，因此没有 assertion-level 增益。

## Failures

- 无 assertion failure。
- `node:test` 出现不影响通过的 `MODULE_TYPELESS_PACKAGE_JSON` warning。

## Next Steps

- 保留官方 CLI 和可运行验证门禁。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, generated projects, outputs, and diagnostics were kept only in an ignored scratch workspace and are not committed.
