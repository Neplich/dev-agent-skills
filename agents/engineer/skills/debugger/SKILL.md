---
name: debugger
description: "Reproduce, diagnose, and fix bugs with minimal changes. Use this skill when tests fail, builds break, runtime errors occur, or the user reports a bug. Trigger on phrases like '测试失败', '构建报错', '有个 bug', 'fix this error', 'debug', 'why is this failing', 'tests are broken', or when test-writer reports failing tests."
---

# Debugger

Systematically reproduce, diagnose, and fix bugs. Follows a strict process:
align expected behavior first, reproduce the failure, analyze the root cause,
report the bug analysis, plan the repair with user confirmation, then fix
minimally and verify.

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
Align Expected Behavior → Reproduce → Analyze → Report → Repair Plan → Confirm → Fix → Verify
```

Do NOT jump to fixing. Do NOT propose or apply a fix before understanding the
expected behavior, root cause, reporting the analysis, and getting confirmation
on the repair plan.

## Complex Fix Sub-Agent Split

For complex bug fixes, keep the main process responsible for the failure
context, root-cause judgment, repository rules, test evidence, and final risk
summary. When sub-agent capabilities are available, split the work after the
root cause and repair plan are confirmed:

1. implementation sub-agent: applies the smallest scoped fix and related
   regression test updates
2. validation sub-agent: reviews the fix against the failure evidence,
   root-cause analysis, tests, repository rules, and unrelated-change risk
3. main process: integrates the result and produces the final repair report

Do not use this split before reproduction and root-cause analysis. Do not force
it for simple single-file fixes, pure diagnosis, or when the user explicitly
asks not to use sub-agents.

## Repair Plan Gate

After the root cause is confirmed, output the bug analysis report first and ask
whether the user wants a repair implementation plan. Do not write code yet.

If the user confirms, produce a repair plan that includes:

- problem, root cause, location, and impact
- files or modules expected to change
- minimal repair approach
- regression tests or verification commands
- whether implementation/validation sub-agent split is needed
- risks, blockers, and forbidden areas

Present the repair plan and wait for user confirmation. Do not apply the fix,
update tests, or delegate implementation until the user confirms the exact
repair plan.

## Step 0 — Align expected behavior with PRD / TRD

For user-reported bugs in an existing feature, identify the likely feature and
read the durable expected-behavior documents before deciding that code should be
changed:

- `docs/pm/{feature}/PRD.md`
- `docs/pm/{feature}/DECISIONS.md`
- `docs/engineer/{feature}/TRD.md`

Use those docs to classify the report:

- If the code or failing test deviates from PRD / TRD, cite the relevant docs
  as the expected behavior source and continue with reproduction and root-cause
  analysis.
- If the user's requested behavior conflicts with the approved PRD /
  DECISIONS / TRD, stop before repair planning and hand off to
  `pm-agent:idea-to-spec` using the `existing-project-update` lane.
- If PRD / DECISIONS are stable but the Engineer TRD is missing, incomplete,
  stale, or conflicts with the codebase or bug context, stop before repair
  planning and hand off to `engineer-agent:trd-gen` with a TRD gap packet. The
  debugger owns naming the missing or conflicting technical decisions; `trd-gen`
  owns completing the TRD.
- If the relevant docs are missing or ambiguous, stop before fixing and request
  PM alignment unless the user explicitly asked to skip it.
- If the user explicitly skips PRD alignment, state the override in the bug
  analysis and continue with the smallest safe debug path.

A TRD gap packet should list the technical decisions that block debugging or
repair planning, including affected components, data flow / API / integration
impact, verification commands, release or rollback risk, and error handling,
observability, or security strategy when relevant.

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
**预期依据**: <PRD / DECISIONS / TRD paths and sections, or explicit skip>
**根因**: <why it's happening>
**位置**: <file:line>
**影响**: <what else might be affected>
```

## Step 5 — Report and ask for repair planning

After confirming the root cause, report the analysis before planning or fixing:

```text
## Bug 分析汇报

- **问题**: <what's happening>
- **预期依据**: <PRD / DECISIONS / TRD paths and sections, or explicit skip>
- **根因**: <why it's happening>
- **位置**: <file:line>
- **影响**: <what else might be affected>
- **复现证据**: <command/action and observed failure>

是否需要我基于这个根因产出修复实施计划？
```

Wait for the user's answer before producing a repair plan. If the user does not
confirm, stop after the analysis report.

## Step 6 — Produce repair implementation plan

Only after the user confirms repair planning, produce the plan:

```text
## 修复实施计划

### 文件变更清单
- 修改 `<path>` — <minimal fix and why>

### 验证方式
- 重新运行 `<failing command>`
- 运行 `<regression command>`

### Sub-Agent 分工
- 触发判断: <whether complex fix split is needed>
- 实现 sub-agent 范围: <owned files/modules, or none>
- 验收 sub-agent 范围: <failure evidence, tests, repository rules>

确认后开始修复？
```

Wait for user confirmation before fixing.

## Step 7 — Implement minimal fix

Fix the root cause with the smallest possible change:

- Don't refactor surrounding code
- Don't "improve" related code
- Don't add defensive checks elsewhere "just in case"
- Only change what's necessary to fix this specific bug

For complex fixes, delegate this step to an implementation sub-agent only after
the root cause and repair plan are confirmed. The task must include the failing
command, confirmed root cause, confirmed repair plan, owned files or modules,
forbidden areas, and the requirement not to revert unrelated changes.

## Step 8 — Verify fix

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

For complex fixes, assign a separate validation sub-agent after tests are run.
It should check the failure evidence, root-cause fit, regression coverage,
repository rules, unrelated changes, and residual risk. It must not broaden the
fix scope.

## Step 9 — Report

```text
## 修复报告

- **问题**: <brief description>
- **根因**: <root cause>
- **修复**: <what was changed>
- **文件**: <files modified>
- **验证**: 失败测试 ✅ 通过, 回归测试 ✅ 通过
- **验收**: <validation conclusion if sub-agent split was used>
- **遗留风险**: <remaining risks or none>

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
