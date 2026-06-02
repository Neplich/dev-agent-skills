# Eval Result: eval-001-npm-audit

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-001-npm-audit`
- Test case: NPM Dependency Audit
- Workspace: `workspace/eval-001-npm-audit`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Test audit of Node.js project with vulnerable dependencies
- Expected output: Structured dependency risk audit that identifies vulnerable, outdated, or abandoned packages with severity, evidence, and upgrade or mitigation guidance.

## Assertions

- `dependency_inventory`: 识别依赖生态、关键包和风险来源
- `risk_classification`: 区分漏洞、废弃、过期或供应链风险并说明严重度
- `evidence`: 引用依赖文件、版本或已知风险作为证据
- `upgrade_plan`: 给出升级、替换或缓解建议

## With Skill

Observed behavior:

- 当前 skill 要求识别 package.json/package-lock.json，运行或模拟 npm audit，按 CVE/版本/严重度分析并给出升级或缓解建议。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
