---
name: debugger
description: "Diagnose failures in read-only mode or repair confirmed implementation defects. Use after engineer-agent provides the diagnosis or repair basis required by the selected mode."
visibility: internal
---

# Debugger

Use one specialist for two modes: `diagnosis_only` gathers and reports
read-only evidence without mutation, while `repair` aligns expected behavior,
reproduces the failure, analyzes the root cause, obtains repair-plan
confirmation, then fixes minimally and verifies.

## Reader-Facing Writing Composition

For substantial reader-facing prose, co-load `human-writing` even on direct
invocation; use the same context, not a later pass. This Skill retains evidence,
facts, structure, paths, gates, and verification. Skip code-, config-, schema-,
lockfile-, and data-only output.

## Mode Selection

Select the mode before applying the repair checkpoint:

- Use `diagnosis_only` only when the user explicitly requires a read-only
  investigation, diagnosis only, or no fix. Preserve handoff fields
  `mode: diagnosis_only` and `allowed_mutations: none` when present.
- Use `repair` for a requested fix and for ambiguous investigation language
  such as “查一下”, “为什么挂了”, or “帮我调查” that does not explicitly impose a
  no-mutation boundary.
- A request to fix after a diagnosis-only report always starts a new `repair`
  entry. Previous evidence may be reused, but the diagnosis-only authorization
  cannot authorize a plan, mutation, or delivery action.

## Mandatory Repair Checkpoint

In `repair` mode, before any repair or E2E edit, make the following sequence
observable in one checkpoint response:

1. when `docs/site/standards/change-map.yaml` exists, resolve the task's code
   path through the change map before reading any mapped formal document; read
   only the matched `required_docs`, then verify every material claim against
   code or tests
2. resolve the nested `feature_path`; read same-path PRD, decisions, TRD, and
   validate `related_prd`
3. classify the report as `implementation_deviation`, `requirement_change`,
   `missing_docs`, or `trd_gap`
4. only for `implementation_deviation`, reproduce the exact failure and report
   the evidence-backed root cause
5. present the analysis and tier-appropriate repair plan together, including
   changed scope, verification, split decision, risks, and QA handoff condition
6. wait for explicit plan confirmation before changing code, tests, or E2E
   assets

The checkpoint must cite the exact resolved `prd_path` and `trd_path`, plus any
decision-record paths that were checked; do not replace those paths with only
document-type labels or the `feature_path`. Record the TRD's actual
`related_prd` target beside the expected same-path PRD so the alignment evidence
is reviewable from the response.

`requirement_change` returns to `pm-agent:idea-to-spec`; a TRD gap returns to
`engineer-agent:trd-gen` with the affected components, data/API/integration,
verification, rollout/rollback, observability, error-handling, and security
decisions still needed. A request to skip alignment or confirmation remains
blocked and never becomes permission to write a repair plan or code.
For a requirement change, state the order explicitly: PM updates the PRD or
product decision record first, `engineer-agent:trd-gen` synchronizes the TRD
second, a confirmed implementation plan follows, and only then may the new E2E
expectation be written. A request to skip PRD alignment does not waive any step.
When raw code evidence proves an observable value mismatch against an
`unverified` document, report the code-grounded discrepancy and its runtime
effect as a low-trust documentation conflict even while repair remains blocked
on expected-behavior alignment; do not turn the document gap into a refusal to
provide the requested evidence-based diagnosis.
The checkpoint prints the resolved `feature_path` value, not only PRD/TRD
paths. For requirement changes, explicitly prohibit writing the new expectation
into `docs/qa/e2e/` before PRD, TRD, and plan alignment, even when the user asks
to skip alignment. Any future QA E2E handoff names the confirmed
`IMPLEMENTATION_PLAN.md` it will consume.

## When to Use

- User explicitly requests read-only diagnosis without a fix
- Tests are failing
- Build is broken
- Runtime error reported
- `test-writer` flagged a code bug
- User reports unexpected behavior
- GitHub Issue describes a bug

## Repair Core Principle

**Never guess.** Follow this order strictly:

```
Align Expected Behavior → Reproduce → Analyze → Report + Repair Plan → Confirm → Fix → Verify
```

Do NOT jump to fixing. Do NOT propose or apply a fix before understanding the
expected behavior, root cause, reporting the analysis, and getting confirmation
on the repair plan. Do NOT create or update E2E test cases before the plan is confirmed.

## PM Handoff Entry Gate

Before `repair`, require an explicit PM/Engineer handoff packet or an equivalent
confirmed document chain that defines expected behavior. If the user directly
invokes `debugger` with a raw repair request and no approved PRD/TRD expectation
source, do not reproduce or fix yet; return the request to `pm-agent` for
classification. Direct invocation does not bypass the repair gate.

An explicit diagnosis-only handoff is the narrow exception for investigation,
not repair: it may proceed without approved PRD/TRD only when it carries or
unambiguously establishes `mode: diagnosis_only` and
`allowed_mutations: none`. It must mark expected behavior as unaligned where
the documents are missing or conflicting and cannot confirm an
`implementation_deviation`.

Use the PM-side packet definition in
the plugin-local generated `../engineer-agent/_internal/_generated/shared-contracts/handoff-contract.md`.
When equivalent docs are present, Step 0 below remains the authoritative
expected-behavior gate.

## Diagnosis-Only Protocol

Lock `allowed_mutations: none` before collecting evidence. Allowed actions are
limited to reading code, documents, configuration, logs, read-only database
query results, and runtime state, plus reproduction commands that are proven
not to persist files, caches, database changes, or external state. If an action
cannot be proven side-effect free, do not execute it; record the evidence gap.

Never modify source, tests, E2E assets, configuration, databases, or external
systems in this mode. Do not commit, push, open a PR, generate a repair plan,
or delegate implementation. The repository and external state must remain
unchanged.

Read available PRD, TRD, DECISIONS, and applicable API contracts when they
exist, but do not make them prerequisites to objective investigation:

- use `expected_behavior_alignment: aligned` only when the available sources
  establish a consistent approved expectation;
- use `expected_behavior_alignment: unaligned` when those sources are missing,
  conflicting, or insufficient;
- with unaligned expectations, separate observed facts from inference and do
  not describe a suspected cause as a confirmed `implementation_deviation`.

Return an evidence-based report with these semantics (equivalent readable
Markdown is acceptable):

```yaml
mode: diagnosis_only
allowed_mutations: none
expected_behavior_alignment: aligned | unaligned
observed_facts: []
direct_evidence: []
root_cause_assessment:
  conclusion: "..."
  confidence: high | medium | low
impact_scope: []
unknowns: []
minimum_next_step: "..."
```

Stop after the report. Do not append a repair plan or ask whether to fix it
now. If the user later requests a fix, re-enter through PM/Engineer, perform
Step 0 and the full repair classification, reproduce and confirm the root
cause, present the tier-appropriate plan, wait for confirmation, then apply
the minimal fix and verify it.

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

After confirming the root cause, output the bug analysis and repair plan
together without asking whether to produce the plan. Do not write code yet.

Consume `change_tier` from the PM handoff packet. When an equivalent confirmed
document chain satisfies the entry gate without a handoff packet, default to
`standard` per the contract in `AGENTS.md` (变更分级契约). For `hotfix`, the
plan may be one sentence covering root cause and repair approach plus the
verification command. For `standard` and `major`, include:

- problem, root cause, location, and impact
- PRD/TRD alignment conclusion and source document paths
- files or modules expected to change
- minimal repair approach
- regression tests or verification commands
- suggested QA E2E function directory:
  `docs/qa/e2e/{feature_path}/`, when the fix may affect E2E
  acceptance coverage
- whether implementation/validation sub-agent split is needed
- risks, blockers, and forbidden areas

Present the combined analysis and tier-appropriate plan, then wait for one user
confirmation. Until then, do not apply the fix, update tests or E2E artifacts,
or delegate implementation.

## Step 0 — Align expected behavior with PRD / TRD

宿主存在 `docs/site/standards/change-map.yaml` 时，项目探索先按 pm-agent 维护的 `consumption-contract.md`（the plugin-local generated `../engineer-agent/_internal/_generated/shared-contracts/consumption-contract.md`）执行“任务落点 → change-map 反查 → 精准读取 → 关键判断回代码验证”；不存在时静默沿用当前代码探索。

For user-reported bugs in an existing feature, identify the likely
`feature_path` and read the durable expected-behavior documents before deciding
that code should be changed:

- `docs/pm/{feature_path}/PRD.md`
- `docs/engineer/{feature_path}/TRD.md`
- `docs/pm/{feature_path}/DECISIONS.md` or other product decision records, when
  present

命中的 API contract 文档可作为预期依据来源之一，但只有与 Approved PRD/TRD、测试及代码证据不冲突时才可采信。

Resolve `feature_path` by scanning `docs/pm/**/PRD.md` and reading
`feature_path`, `parent_feature`, and `feature_level` frontmatter where
present. Old single-level docs without those fields are compatible and count as
level-1 features. If the likely feature is ambiguous, the PRD is missing, the
path is invalid, or the report appears to target a child feature that was
generated as a wrong top-level directory, classify the report as `missing_docs`
and request PM alignment instead of guessing.

Use those docs to classify the report:

- If the code or failing test deviates from PRD / TRD, and no present decision
  record conflicts, cite the relevant docs as the expected behavior source and
  continue with reproduction and root-cause analysis.
- If the user's requested behavior conflicts with the approved PRD, TRD, or an
  existing decision record, stop before repair planning and hand off to
  `pm-agent:idea-to-spec` using the `existing-project-update` lane.
- If PRD is stable but the Engineer TRD is missing, incomplete, stale, conflicts
  with the codebase or bug context, uses a different `feature_path`, has
  mismatched `parent_feature` or `feature_level`, or has a `related_prd` that
  does not point to `docs/pm/{feature_path}/PRD.md`, stop before repair
  planning and hand off to `engineer-agent:trd-gen` with a TRD gap packet. The
  debugger owns naming the missing or conflicting technical decisions;
  `trd-gen` owns completing the TRD.
- If PRD is missing or ambiguous, or an existing decision record conflicts with
  the report, stop before fixing and request PM alignment. A user request to
  skip PRD alignment is a blocker or risk note, not permission to continue into
  repair planning, implementation, or E2E updates.

If the target agent's plugin for a cross-agent handoff is not installed or
unavailable, state the missing stage and required plugin, mark that handoff
stage as blocked, and do not perform the missing agent's responsibilities
yourself.

Record the classification explicitly as one of:

- `implementation_deviation`: approved PRD / TRD already defines the expected
  behavior and the implementation or test deviates from it.
- `requirement_change`: the user is asking to change approved expected
  behavior, so PM alignment is required before repair planning.
- `missing_docs`: PRD, product decision records, or expected behavior
  are missing or ambiguous.
- `trd_gap`: PM scope is stable, but the TRD is missing, stale, incomplete, or
  conflicts with the codebase or bug context.

A TRD gap packet should list the technical decisions that block debugging or
repair planning, including affected components, data flow / API / integration
impact, verification commands, release or rollback risk, and error handling,
observability, or security strategy when relevant.

Do not update E2E TC, scripts, assertions, or QA result files while the
classification is `requirement_change`, `missing_docs`, or `trd_gap`.
For `requirement_change`, do not write the new expectation into
`docs/qa/e2e/**` until PM updates the PRD or product decision record, TRD is
synchronized, and a confirmed
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` exists. If a confirmed
repair later affects E2E coverage, pass a QA E2E handoff package after the fix
and verification rather than editing TC during diagnosis or repair planning.
That handoff must cite the confirmed
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`, PRD/TRD alignment
conclusion, changed files, verification commands, and suggested QA E2E function
directory.

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

## Step 4 — Identify and confirm root cause

Before fixing, state the root cause clearly:

```text
## 根因分析

**问题**: <what's happening>
**预期依据**: <PRD / TRD paths and sections, optional decisions, or blocked alignment gap>
**根因**: <why it's happening>
**位置**: <file:line>
**影响**: <what else might be affected>
```

## Step 5 — Report analysis and repair plan

Report the analysis and tier-appropriate repair plan together before fixing:

```text
## Bug 分析与修复计划

- **问题**: <what's happening>
- **预期依据**: <PRD / TRD paths and sections, optional decisions, or blocked alignment gap>
- **根因**: <why it's happening>
- **位置**: <file:line>
- **影响**: <what else might be affected>
- **复现证据**: <command/action and observed failure>

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

For `hotfix`, compress the template as described in the gate above. For
`standard` and `major`, keep it in full. Wait for one confirmation before fixing.

## Step 6 — Implement minimal fix

Fix the root cause with the smallest possible change:

- Don't refactor surrounding code
- Don't "improve" related code
- Don't add defensive checks elsewhere "just in case"
- Only change what's necessary to fix this specific bug

For complex fixes, delegate this step to an implementation sub-agent only after
the root cause and repair plan are confirmed. The task must include the failing
command, confirmed root cause, confirmed repair plan, owned files or modules,
forbidden areas, and the requirement not to revert unrelated changes.

## Step 7 — Verify fix

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

## Step 8 — Report

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
