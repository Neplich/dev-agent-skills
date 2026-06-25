# Eval Result: eval-001-analyze-nodejs-project

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`
- Test case: analyze-nodejs-project
- Workspace: `workspace/eval-001-analyze-nodejs-project`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without_skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that codebase-analyzer handles analyze-nodejs-project and produces the expected role-specific artifact.
- Expected output: 结构化的 Project Profile，包含技术栈识别、目录结构、编码规范、依赖分析、架构模式

## Assertions

- `assertion_1`: 识别技术栈
- `assertion_2`: 目录结构分析
- `assertion_3`: 编码规范检测
- `yaml`: 输出 YAML 格式

## With Skill

Observed behavior:

- 当前 SKILL.md 明确要求扫描项目结构、识别 package manager/framework/language、提取 lint/format 规范，并以 YAML Project Profile 输出 source_dirs、test_dirs 等字段，满足断言。

## Without Skill / Baseline
- BLOCKED: No actual without_skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 保留无运行期产物策略。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
