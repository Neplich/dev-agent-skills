# Code Self-Reviewer

> Internal module for feature-implementor. Loaded during Phase 3.

## Purpose

Review the implemented code against PM documents and project conventions before handoff.

## Input

- List of all files created or modified
- PM documents (PRD, DECISIONS)
- Engineer documents (TRD, IMPLEMENTATION_PLAN, API Spec)
- Project Profile
- Deterministic test results, when available
- For complex coding tasks: implementation sub-agent summary and assigned
  write scope

## Independent Validation Contract

When the implementation used the complex coding split, review should be handled
by a validation sub-agent that is separate from the implementation sub-agent.
The validation task must include:

- PRD/TRD/IMPLEMENTATION_PLAN/design docs and acceptance criteria
- changed files and implementation summary
- deterministic test commands and results
- repository rules, including minimal scope and unrelated-change protection
- requested output: pass/fail conclusion, findings, blockers, missing tests,
  and residual risks

The validation sub-agent reviews only. It must not broaden the implementation
scope or make unrelated edits.

## Review Checklist

### 1. TRD Compliance

For each component described in TRD:
- [ ] Component exists in code
- [ ] Component follows the architecture described in TRD
- [ ] Component boundaries match TRD (not tightly coupled where TRD says loose)
- [ ] Data flow matches TRD description
- [ ] File-level changes match `IMPLEMENTATION_PLAN.md`

### 2. API Compliance (if API Spec exists)

For each endpoint in API Spec:
- [ ] Route path matches spec
- [ ] HTTP method matches spec
- [ ] Request body/params match spec shape
- [ ] Response shape matches spec
- [ ] Error codes match spec
- [ ] Auth requirements implemented per spec

### 3. PRD Coverage

For each P0 acceptance criterion in PRD:
- [ ] There is code that implements this criterion
- [ ] The implementation matches what was specified (not a creative reinterpretation)

### 4. Security Check

- [ ] No hardcoded secrets or credentials
- [ ] User input validated at API boundaries
- [ ] Database queries use parameterized inputs (if applicable)
- [ ] No raw HTML rendering of user content (if applicable)

### 5. Convention Check

- [ ] New files are in the correct directories per project structure
- [ ] Naming follows project conventions
- [ ] Import style matches existing code
- [ ] Error handling follows project patterns

## Output

```text
## 自检结果

| 检查项 | 状态 | 备注 |
|--------|------|------|
| TRD 符合度 | ✅/⚠️/❌ | <details> |
| API 符合度 | ✅/⚠️/❌ | <details> |
| PRD 覆盖 | ✅/⚠️/❌ | <details> |
| 安全检查 | ✅/⚠️/❌ | <details> |
| 规范检查 | ✅/⚠️/❌ | <details> |
| 独立验收 | ✅/⚠️/❌/N/A | <details> |

### 问题 (如有)
1. [严重程度] 描述 — 修复建议

### 遗留风险
- <risk or "无">

### 建议下一步
- <recommendation>
```

## Severity Levels

| Level | Meaning | Action |
|-------|---------|--------|
| ✅ | All checks pass | Proceed |
| ⚠️ | Minor issues | Note and proceed (or fix if trivial) |
| ❌ | Blocking issues | Must fix before handoff |

If any ❌ issues found, go back to Phase 2 to fix them before producing the final review.
