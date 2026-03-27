---
name: debugger
description: "Reproduce, diagnose, and fix bugs with minimal changes. Use this skill when tests fail, builds break, runtime errors occur, or the user reports a bug. Trigger on phrases like '测试失败', '构建报错', '有个 bug', 'fix this error', 'debug', 'why is this failing', 'tests are broken', or when test-writer reports failing tests."
---

# Debugger

Systematically reproduce, diagnose, and fix bugs. Follows a strict process: reproduce first, then analyze, then fix minimally, then verify.

## When to Use

- Tests are failing
- Build is broken
- Runtime error reported
- `test-writer` flagged a code bug
- User reports unexpected behavior
- GitHub Issue describes a bug

## Core Principle

**Never guess.** Follow this order strictly:

```
Reproduce → Analyze → Hypothesize → Fix → Verify
```

Do NOT jump to fixing. Do NOT propose a fix before understanding the root cause.

## Step 1 — Gather error context

Collect all available information:

- **Error message**: Full text including stack trace
- **Where it happens**: Which test, command, or user action
- **When it started**: Recent changes that might have caused it
- **Frequency**: Always, sometimes, or only under certain conditions

If the error came from `test-writer`:
```bash
# Re-run the specific failing test with verbose output
npm test -- --verbose <test-file>
pytest -v <test-file>::<test-name>
go test -v -run <TestName> ./...
cargo test <test_name> -- --nocapture
```

If the error came from a GitHub Issue:
```bash
gh issue view <number> --json body,title,comments
```

## Step 2 — Reproduce

Run the exact command that produces the error:

```bash
<the failing command>
```

If it succeeds (intermittent failure):
- Run it 3 more times
- Check for timing dependencies, shared state, or environment issues
- If still can't reproduce, report this and ask for more context

Capture the exact error output for analysis.

## Step 3 — Analyze root cause

Read the relevant source code. Start from the error location and trace upward:

1. **Read the failing line/function**: What is it trying to do?
2. **Read the caller**: What input does it receive?
3. **Read related code**: What state could cause this failure?
4. **Check recent changes**: `git log --oneline -10 -- <file>` and `git diff HEAD~5 -- <file>`

Common root cause patterns:

| Error Type | Likely Cause | Where to Look |
|-----------|-------------|---------------|
| TypeError / nil pointer | Missing null check or wrong type | Input validation, API response handling |
| Import/module not found | Wrong path, missing export | Import statements, package.json exports |
| Test assertion failure | Logic error or wrong expected value | Both test and implementation |
| Build failure | Type mismatch, missing dependency | Type definitions, package manifest |
| Timeout | Async issue, infinite loop | Promises, goroutines, event handlers |

## Step 4 — Identify and confirm root cause

Before fixing, state the root cause clearly:

```text
## 根因分析

**问题**: <what's happening>
**根因**: <why it's happening>
**位置**: <file:line>
**影响**: <what else might be affected>
```

## Step 5 — Implement minimal fix

Fix the root cause with the smallest possible change:

- Don't refactor surrounding code
- Don't "improve" related code
- Don't add defensive checks elsewhere "just in case"
- Only change what's necessary to fix this specific bug

## Step 6 — Verify fix

Run the previously failing command:

```bash
<the same command from Step 2>
```

Then run the full test suite to check for regressions:

```bash
<project test command>
```

### Verification outcomes

- **Fix works, no regressions**: Report success
- **Fix works, but other tests break**: The fix exposed another issue, or the fix is wrong. Investigate.
- **Fix doesn't work**: Back to Step 3 — the root cause analysis was wrong

## Step 7 — Report

```text
## 修复报告

- **问题**: <brief description>
- **根因**: <root cause>
- **修复**: <what was changed>
- **文件**: <files modified>
- **验证**: 失败测试 ✅ 通过, 回归测试 ✅ 通过

### 建议下一步
- <recommendation>
```

## Edge Cases

- **Multiple test failures**: Triage first. Look for a common root cause. If failures are independent, fix them one at a time starting with the simplest.
- **Flaky test**: If the test passes sometimes, focus on state management, timing, and test isolation rather than the implementation.
- **Environment-specific**: If the bug only happens in CI or on specific OS, check environment differences (Node version, OS paths, env vars).
- **Can't reproduce locally**: Ask for CI logs, environment details, or specific reproduction steps.
- **Fix requires changing PM docs**: If the bug reveals that the spec is wrong (not the code), flag this and recommend going back to PM Agent for a spec update.
```
