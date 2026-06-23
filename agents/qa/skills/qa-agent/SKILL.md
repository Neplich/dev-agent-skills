---
name: qa-agent
description: Route QA work to the right downstream skill. Use when the user needs documented acceptance, exploratory discovery, failure reproduction, or fix verification. Trigger on phrases like "测一下这个功能", "按 spec 验证", "做冒烟测试", "探索一下 UI", "帮我复现这个问题", "分析 bug", "复测这个修复", "回归测试", or any QA-oriented request that should be routed before execution.
---

# QA Agent Dispatcher

`qa-agent` is the QA capability entry point. It routes the request based on the
evidence outcome the user wants, the repository context available, and whether
the work is documented acceptance, exploratory discovery, failure reproduction,
or fix verification.

## Role Boundary

`qa-agent` is responsible for:

- identifying whether the request is about documented acceptance, exploratory
  discovery, failure reproduction, or fix verification
- selecting the narrowest QA skill that owns the expected testing output
- carrying PM and implementation context into the selected QA skill
- stating the expected evidence artifact for the chosen route
- asking at most one route-level clarification question when the testing target
  is truly ambiguous

`qa-agent` is not responsible for:

- implementing product changes or directly fixing bugs
- replacing engineering debugging when code changes are required
- prescribing fixed port, framework, or browser assumptions before repo context
- expanding requested verification into broad discovery by default
- forcing every QA request through a full test battery

## Shared QA Document Contract

When QA work creates, updates, or executes E2E assets, use the function-tree
directory as the durable source of truth:

`docs/qa/e2e/{feature_path}/`

- `TEST_SUITE.md` is the suite index, active TC list, and coverage summary.
- `FLOW_INDEX.md` maps user flows, pages, routes, APIs, and states to TC files.
- `cases/` stores reusable E2E cases, one Markdown file per TC:
  `cases/TC-NNN-<short-slug>.md`.
- `scripts/` stores matching executable or repeatable flow snippets:
  `scripts/TC-NNN-<short-slug>.spec.md`.
- `results/TC-NNN-<short-slug>/{platform-version}/` stores `result.md` and
  `testcase.snapshot.md`; results are appended by platform version, not
  overwritten.
- `_reports/{platform-version}/test-reports-{test-time}.md` stores
  feature-update summary reports. Release-wide reports use
  `docs/qa/e2e/_reports/{platform-version}/test-reports-{test-time}.md`.
- Shared login flows and data live under `docs/qa/e2e/_shared/`.

For E2E routing, carry these fields into the downstream skill:

- Feature path: consume a confirmed `feature_path` from PM/Engineer handoff or
  from `docs/pm/{feature_path}/PRD.md`. Existing-feature changes, bug fixes,
  and code-complete E2E documentation updates must read
  `docs/pm/{feature_path}/PRD.md`,
  `docs/engineer/{feature_path}/TRD.md`, and
  `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` before any acceptance
  TC is created, updated, or executed. If the feature path is ambiguous, hand
  back to `pm-agent:idea-to-spec`; if TRD is missing or mismatched, hand back
  to `engineer-agent:trd-gen`; if the implementation plan is missing or
  mismatched, hand back to `engineer-agent:feature-implementor`.
- Scenario: `feature-update` validates the changed feature and direct impact
  paths in the local development test environment; `release` validates all
  active E2E TC in the release-version test environment. If the scenario cannot
  be inferred, ask one concise scenario question.
- Platform version: confirm before execution. If missing, mark the E2E work
  `blocked` and ask for the version; never archive to `unknown`.
- Scope: confirm the function-tree node or infer it from PRD/TRD, changed
  files, branch context, or existing QA memory. If it cannot be inferred, ask
  one concise scope question.
- Execution entry: repo harness first, Chrome plugin / browser connector
  second, Playwright fallback last. State why the selected entry covers the TC.
- Credentials: committed QA docs may only reference account IDs. If the user
  supplies platform or SSH credentials, follow
  `agents/qa/skills/qa-agent/references/e2e-credential-store.md` and upsert
  `.qa/e2e/accounts.local.json` without echoing sensitive values.
- Report format: summary reports must follow
  `agents/qa/skills/qa-agent/references/e2e-test-report.md`.

For standalone QA or E2E requests where no PM-authored E2E cases are supplied,
route the downstream skill with this required sequence:

1. Read the target function-tree `TEST_SUITE.md`, `FLOW_INDEX.md`,
   `cases/*.md`, `scripts/*.spec.md`, prior `results/`, and `_reports/`.
2. If the request comes from an existing-feature change, bug fix, or
   code-complete E2E documentation update, require PRD/TRD expectation
   alignment on the same `feature_path` and a confirmed
   `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` before creating,
   updating, or executing acceptance TC.
3. For `feature-update`, select the changed feature, direct impact paths, and
   related regression TC. For `release`, select all active E2E TC.
4. If reusable TC already cover the target, execute from those TC instead of
   rediscovering the project.
5. If coverage is missing and the user authorizes exploration or PRD/TRD case
   generation, add or update `cases/`, `scripts/`, and `FLOW_INDEX.md` in the
   function-tree directory. Do not create duplicate synonym TC.
6. Execute every E2E TC through a subagent by default, even when there is only
   one TC. The main agent owns scope confirmation, task splitting, result
   confirmation, and the final summary report.

## Available Skills

- `qa-agent:exploratory-tester` - Exploratory, smoke, and edge-case UI testing
- `qa-agent:spec-based-tester` - Structured validation against specs, PRD, TRD, or test docs
- `qa-agent:bug-analyzer` - Failure triage, reproduction notes, and detailed bug reports
- `qa-agent:regression-suite` - Regression verification after fixes or before release

## Routing Signals

Route by the evidence outcome the user wants.

- 文档化验收、规范验证、"按需求验收", "按 spec 测", "这个实现符合 PRD 吗"
  -> `spec-based-tester`
- 探索式发现、冒烟、边界发现、"探索一下", "随便走一遍", "找潜在问题"
  -> `exploratory-tester`
- 失败复现、缺陷写作、归因整理、"帮我复现", "分析这个 bug", "写 bug 报告"
  -> `bug-analyzer`
- 修复验证、回归扫测、已知问题复核、"复测", "回归验证", "确认修复没反弹"
  -> `regression-suite`

## Default Routes

| QA Outcome | Primary Skill |
| --- | --- |
| 文档化验收、规范验证 | `spec-based-tester` |
| 探索式发现、冒烟、边界发现 | `exploratory-tester` |
| 失败复现、缺陷写作、归因整理 | `bug-analyzer` |
| 修复验证、回归扫测、已知问题复核 | `regression-suite` |

If the request is QA-shaped but underspecified, use these defaults:

- if there is a clear documented acceptance target -> `spec-based-tester`
- if the user wants exploratory discovery -> `exploratory-tester`
- if the user starts from a failure symptom or defect report -> `bug-analyzer`
- if the user starts from a known fix or bug ID -> `regression-suite`

## Escalation Rules

- Ask one route-level clarification question only when the evidence target truly
  changes and the repo context does not already answer it.
- If the environment or docs are incomplete, still choose the narrowest QA
  route first rather than bouncing the user back immediately.
- If code changes are clearly required, keep the QA route focused on evidence
  and hand the fix back to `engineer-agent`.

## Output Behavior

When routing is complete:

- state which QA skill should handle the request
- state the expected evidence artifact for the route
- for E2E, list the complete QA memory read set before any execution:
  `TEST_SUITE.md`, `FLOW_INDEX.md`, `cases/*.md`, `scripts/*.spec.md`, prior
  `results/`, and `_reports/`
- for E2E, state scenario, function-tree scope, platform version status,
  subagent execution plan, selected execution entry, and why the selected entry
  follows repo harness > Chrome plugin / browser connector > Playwright fallback
- for E2E, state the credential handling reference
  `agents/qa/skills/qa-agent/references/e2e-credential-store.md`, the local
  store `.qa/e2e/accounts.local.json`, and the summary report reference
  `agents/qa/skills/qa-agent/references/e2e-test-report.md`
- for existing-feature changes, bug fixes, or code-complete E2E documentation
  updates, state the same-path PRD, TRD, and confirmed
  `IMPLEMENTATION_PLAN.md` gate explicitly; expectation changes return to PM,
  TRD gaps return to `engineer-agent:trd-gen`, and missing implementation plans
  return to `engineer-agent:feature-implementor`
- if E2E is blocked by missing platform version, credentials, environment,
  unclear `feature_path`, PRD/TRD alignment, or confirmed
  `IMPLEMENTATION_PLAN.md`, report the blocker and next owner instead of
  creating or executing TC
