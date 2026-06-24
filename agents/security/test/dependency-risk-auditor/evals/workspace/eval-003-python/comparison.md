# Eval Result: eval-003-python

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`
- Test case: Python Dependency Audit
- Workspace: `workspace/eval-003-python`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without_skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-02

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Test audit of Python project dependencies
- Expected output: Structured dependency risk audit that identifies vulnerable, outdated, or abandoned packages with severity, evidence, and upgrade or mitigation guidance.

## Assertions

- `dependency_inventory`: 识别依赖生态、关键包和风险来源
- `risk_classification`: 区分漏洞、废弃、过期或供应链风险并说明严重度
- `evidence`: 引用依赖文件、版本或已知风险作为证据
- `upgrade_plan`: 给出升级、替换或缓解建议

## With Skill

Observed behavior:

- 当前 skill 覆盖 requirements.txt/Pipfile、pip-audit、Python CVE/版本证据、严重度分类和升级/缓解建议，满足 eval 断言。

## Without Skill / Baseline
- BLOCKED: No actual without_skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- 无需修改当前 skill 指令。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
