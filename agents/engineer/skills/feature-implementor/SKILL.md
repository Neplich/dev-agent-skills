---
name: feature-implementor
description: "Core engineering skill: implement features from confirmed Engineer TRDs and PM/design inputs. Use this skill whenever the user wants to implement a feature, write code for a confirmed requirement, build functionality described in a TRD/spec, or turn a design into code. Trigger on phrases like '实现这个功能', '写代码', '开始编码', 'implement', 'build this feature', 'code this', or any request to turn confirmed technical plans into working code."
---

# Feature Implementor — Public Entry

The core engineering skill. Reads confirmed Engineer TRDs plus PM/design inputs,
confirms existing-feature requests are aligned with approved PRD / decisions,
writes an implementation plan document, then implements code following project
conventions and self-reviews the result.

This is the public entry point. It owns:

- PM / Engineer / Design document reading and requirement extraction
- Implementation plan document writing
  (`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`)
- Implementation planning (which files to create/modify, in what order)
- Delegation to internal modules and, for complex coding tasks, scoped
  implementation/validation sub-agents
- Quality self-check before handoff
- QA E2E documentation handoff after code completion when user-facing flows or
  acceptance paths may be affected

Before implementation plan confirmation, load only the planner internal module.
Do not load implementor or reviewer modules, write code, or run fix steps until
the implementation plan has been presented to the user and explicitly confirmed.

## When to Use

- User wants to implement a feature described in PM documents
- User wants to implement an existing-feature behavior change that is already
  reflected in PRD and Engineer TRD, with no conflict in existing product
  decision records
- User asks to "write code" or "implement" something with a spec available
- After `codebase-analyzer` or `project-bootstrap` has established project context
- After `trd-gen` has produced and the user has confirmed
  `docs/engineer/{feature_path}/TRD.md`

Do NOT use for:
- Bug fixes with no spec (use `debugger` instead)
- Existing-feature behavior changes that require PRD or product decision updates first
  (use `pm-agent:idea-to-spec` with the `existing-project-update` lane)
- Writing tests only (use `test-writer` instead)
- Git/PR operations only (use `delivery` instead)
- Creating or revising the TRD itself (use `trd-gen` instead)

Spec-backed bug fixes may enter `feature-implementor` only after debugger or
Engineer routing confirms the fix is implementation work against approved PRD /
TRD behavior. They still require `IMPLEMENTATION_PLAN.md` and explicit user
confirmation before code changes.

## PRD Alignment Gate

Before creating or updating `IMPLEMENTATION_PLAN.md` for an existing feature
change, resolve `feature_path` and read the relevant PM and Engineer documents:

- `docs/pm/{feature_path}/PRD.md`
- `docs/engineer/{feature_path}/TRD.md`
- `docs/pm/{feature_path}/DECISIONS.md` or other product decision records, when
  present

`feature_path` is the canonical feature key. New documents must use one or more
directory segments and include `feature_path`, `parent_feature`, and
`feature_level` frontmatter. Old single-level documents without those fields
are compatible and should be read as level-1 features. Before planning, verify
that:

- the PRD exists at `docs/pm/{feature_path}/PRD.md`
- the TRD exists at `docs/engineer/{feature_path}/TRD.md`
- PRD and TRD `feature_path`, `parent_feature`, and `feature_level` match
- TRD `related_prd` points to `docs/pm/{feature_path}/PRD.md`
- the target plan path is
  `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`

Classify the request:

- If the requested behavior is already covered by PRD and confirmed TRD, and no
  present decision record conflicts, continue to implementation planning and
  cite those documents in the plan.
- If the request changes approved product behavior, stop before implementation
  planning and hand off to `pm-agent:idea-to-spec` using the
  `existing-project-update` lane.
- If PRD is missing, ambiguous, lacks a resolvable `feature_path`, or an
  existing decision record conflicts with the request, stop and request PM
  alignment before TRD or implementation planning.
- If PRD is stable but TRD is missing, incomplete, stale, uses a different
  `feature_path`, has mismatched `parent_feature` or `feature_level`, or has a
  `related_prd` that does not point to the same PRD path, stop and hand back to
  `engineer-agent:trd-gen` with a TRD gap packet. The finder owns naming the
  missing technical decisions; `trd-gen` owns completing the TRD.
- If the user explicitly asks to skip PRD alignment, record it as a blocker or
  risk, but do not create or update the implementation plan until PRD/TRD
  alignment is complete.

The TRD gap packet must state the unresolved technical decisions that block
implementation planning, including affected components or modules, data flow /
API / integration impacts, verification commands, release or rollout risks, and
error handling, observability, or security strategy when relevant. It must also
include this boundary statement: the finder only clarifies the TRD gaps;
`engineer-agent:trd-gen` completes or updates the TRD.

## TRD and Implementation Plan Boundary

`docs/engineer/{feature_path}/TRD.md` is the technical plan and input contract.
`feature-implementor` consumes the confirmed TRD and writes
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`.

The implementation plan maps TRD decisions to concrete files, sequence,
delegation, verification commands, and rollout checks. It must not change PM
scope or rewrite TRD decisions. If the TRD is missing, incomplete, or conflicts
with the codebase, stop and hand back to `engineer-agent:trd-gen` with the
specific blocker and TRD gap packet. Do not hide TRD gaps inside
`IMPLEMENTATION_PLAN.md`.

If the only missing directory is the target Engineer directory and both PRD and
TRD are confirmed with matching `feature_path`, creating
`docs/engineer/{feature_path}/` for the implementation plan is allowed. Missing
PRD content belongs to `pm-agent:idea-to-spec`; missing, stale, or
path-mismatched TRD content belongs to `engineer-agent:trd-gen`.

Implementation plan frontmatter is part of the confirmed engineering artifact.
New plans should start with `version: "0.1.0"` unless the repository has a
stricter convention. When an existing plan's body, scope, ordered steps,
delegation model, verification commands, status, or diagrams change
substantively, update both `version` and `last_updated` in the same edit. Use a
PATCH bump for clarifications that preserve scope, a MINOR bump for changed
implementation scope or sequencing, and a MAJOR bump only for replacing the
confirmed plan contract. Typo, formatting, or other non-semantic edits may
leave `version` unchanged, but should still refresh `last_updated` when the
file is touched.

All implementation plan document writing must be delegated to a fresh
document-writing sub-agent when sub-agent capabilities are available. The main
process keeps the source docs, repository context, and final approval decision.

The implementation planner is the first step for every implementation task,
including single-file, small, low-risk, and spec-backed bug-fix changes. Small
changes may use a short plan, but they still require
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` and explicit user
confirmation before implementation starts.

## Complex Coding Sub-Agent Split

Decide whether this split is needed inside the implementation plan after the
planner maps the implementation scope.

When the implementation is multi-file, multi-module, spec-backed, or otherwise
context-heavy, keep the main process responsible for PM/design context,
repository constraints, implementation boundaries, final integration, and
delivery risk. When sub-agent capabilities are available, use two separate
delegations:

1. **Implementation sub-agent**: writes code and tests only within the assigned
   file or module scope.
2. **Validation sub-agent**: reviews the result against PRD/TRD/design docs,
   repository rules, test evidence, and role boundaries.

The implementation task must include:

- owned files, directories, or modules
- expected behavior and source document references
- test expectations or verification commands
- forbidden areas and a reminder not to revert unrelated user changes
- required output: changed files, summary, tests, and open issues

The validation task must include:

- source docs and acceptance criteria
- changed files and test evidence
- checks for requirement coverage, test coverage, repository rules, and
  unrelated changes
- required output: pass/fail conclusion, findings, blockers, and residual risks

Do not use the implementation/validation sub-agent split for single-file small
edits, pure explanation, pure code reading, or when the user explicitly opts
out. This exception only skips complex delegation; it never skips implementation
planning or plan confirmation.

## Phase 0: Gather Context

### Read source documents

Scan `docs/` for relevant specs:

```bash
ls docs/*.md docs/**/*.md 2>/dev/null
```

Read the documents relevant to the current task:
- **PRD**: functional requirements, user stories, acceptance criteria
- **DECISIONS**: when present, approved product decisions, rejected options,
  assumptions, and open questions
- **Engineer TRD**: technical approach, component breakdown, architecture decisions
- **ADR**: specific technology choices and constraints
- **API Spec**: endpoint contracts, request/response shapes

For existing feature changes, complete the PRD alignment gate before loading
the planner. Do not treat a small change as already approved just because it is
low-risk or single-file.

If `docs/engineer/{feature_path}/TRD.md` is missing, not confirmed, or does not
mirror `docs/pm/{feature_path}/PRD.md`, do not create the implementation plan.
Hand off to `engineer-agent:trd-gen` with the TRD gap packet and boundary
statement: finder only clarifies gaps, `engineer-agent:trd-gen` completes the
TRD.

### Check for Project Profile

If a Project Profile was produced by `codebase-analyzer`, use it. If not, run a quick scan:
- What language and framework?
- What are the existing coding conventions?
- What's the directory structure?

### Output context summary

```text
Implementation context:
- Project: <name> (<framework>)
- Feature: <feature name from PRD>
- Relevant docs: <list of PM docs read>
- PRD alignment: <already approved / needs PM update / docs missing / trd gap>
- Existing modules affected: <list>
- New modules needed: <list>
```

## Phase 1: Plan the Implementation

Load only the planner internal module for this phase:

`agents/engineer/skills/feature-implementor/_internal/planner/INSTRUCTIONS.md`

Read the internal routing contract before planning:

`agents/engineer/skills/feature-implementor/_internal/_shared/coding-rules.md`

Every implementation task must go through this phase before code changes,
regardless of size. The plan may be brief for small changes, but it must still
be written to `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`, include
the PRD alignment result, feature path gate result, implementation/validation
sub-agent split decision, and wait for user confirmation.

Delegate implementation plan document writing to a fresh document-writing
sub-agent when available. The delegated task must write or update:

```text
docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md
```

Break the feature into ordered implementation steps:

1. List every file that needs to be **created** or **modified**
2. Determine the dependency order (e.g., data model before API route before UI)
3. For each file, note:
   - What it does
   - Which PM doc section drives it
   - Dependencies on other files in this plan
4. Decide whether the complex coding sub-agent split applies. If it does,
   include the implementation sub-agent write scope and validation sub-agent
   review scope in the plan.
5. Include the PRD / optional DECISIONS / TRD paths, implementation plan path,
   resolved `feature_path`, `parent_feature`, `feature_level`, and any blockers
   that require returning to PM or `trd-gen`.

Present the plan to the user:

```text
## 实现计划

### 文件变更清单
1. 创建 `src/models/notification.ts` — 数据模型（来自 TRD §3.2）
2. 创建 `src/services/notification-service.ts` — 业务逻辑（来自 TRD §3.3）
3. 创建 `src/api/notifications.ts` — API 路由（来自 API Spec）
4. 修改 `src/api/index.ts` — 注册新路由

### 实现顺序
按上述编号顺序，每完成一步验证编译通过。

### PRD 对齐
- 状态: <已覆盖 / 需要 PM 更新 / 文档缺失或不清 / TRD gap>
- 依据: <PRD / TRD paths and sections, plus DECISIONS when present>

### Sub-Agent 分工
- 触发判断: <是否触发复杂编码分工及原因>
- 实现 sub-agent 范围: <files/modules and forbidden areas>
- 验收 sub-agent 范围: <source docs, tests, and review criteria>

确认后开始实现？
```

Wait for user confirmation before coding.

Stop after presenting the plan. Do not start implementation in the same turn
unless the user has already confirmed this exact implementation plan.

## Phase 2: Implement

Only after the user confirms the implementation plan, load the implementor
internal module:

`agents/engineer/skills/feature-implementor/_internal/implementor/INSTRUCTIONS.md`

For each step in the plan:

1. **Read before write**: If modifying an existing file, read it first. Understand the current code.
2. **Write code**: Follow project conventions (naming, style, patterns). Reference the specific PM doc section.
3. **Verify compilation**: After each file, ensure the project still compiles/builds.
4. **Minimal scope**: Only write what the plan calls for. No "bonus" improvements.

For complex coding tasks, delegate implementation to a scoped implementation
sub-agent instead of letting the main process absorb all implementation detail.
The main process must keep the source docs, boundaries, tests, and delivery
risks available for final integration.

## Phase 3: Self-Review

Load the reviewer internal module:

`agents/engineer/skills/feature-implementor/_internal/reviewer/INSTRUCTIONS.md`

Check the implementation against:

1. **TRD compliance**: Does the code match the architecture described in TRD?
2. **API compliance**: Do endpoints match the API Spec (routes, methods, request/response shapes)?
3. **PRD coverage**: Does the code fulfill all P0 acceptance criteria from PRD?
4. **Security basics**: No hardcoded secrets, no SQL injection, no XSS, proper input validation at boundaries.
5. **Convention compliance**: Naming, file placement, import style match the project.

For complex coding tasks, assign a separate validation sub-agent after the
implementation result and deterministic test evidence are available. The
validation sub-agent reviews the implementation against PRD/TRD/design docs,
repository rules, test coverage, and residual risk; it does not expand the
implementation scope.

Output a brief review summary:

```text
## 自检结果
- TRD 符合度: ✅ 所有组件按 TRD §3 实现
- API 符合度: ✅ 3/3 端点匹配 API Spec
- PRD 覆盖: ✅ 4/4 P0 验收标准覆盖
- 安全检查: ✅ 无明显安全问题
- 规范检查: ✅ 命名和结构符合项目规范
```

## QA E2E Documentation Handoff

After implementation and self-review, output a QA E2E documentation handoff
package when the change can affect user-facing behavior, acceptance flows,
routes, permissions, login, data setup, or regression coverage.

The package must include:

- PRD path and relevant sections
- TRD path and relevant sections
- confirmed `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`
- PRD alignment result, including DECISIONS or TRD gap resolution when applicable
- changed files and affected modules
- verification commands run, results, and commands not run with reasons
- known risks, environment assumptions, and QA scope questions
- suggested QA E2E function directory:
  `docs/qa/e2e/{feature_path}/`
- likely E2E impact: create TC, update existing TC, update script/assertions,
  or no E2E update needed with rationale

If the confirmed implementation plan is missing, stop and return to Phase 1
instead of producing a QA E2E handoff. Small, single-file, low-risk, and
spec-backed bug-fix changes still require the confirmed implementation plan
before this handoff.

Do not create or update QA E2E TC directly from this skill unless the user
explicitly routes that QA documentation work. The default responsibility here is
to hand off complete evidence to the QA E2E documentation flow.

## Handoff

After implementation and self-review:

```text
## 建议下一步

- **补充 QA E2E 文档**: 将 QA E2E documentation handoff package 交给 `qa-agent`
  判断是否新增或更新 E2E TC
- **写测试**: 使用 `test-writer` 基于 Test Spec 编写测试
- **直接交付**: 使用 `delivery` 创建 PR（如果测试已有或不需要）
```

When the complex coding split was used, include implementation result,
validation conclusion, tests run, and residual risks before recommending the
next step.

## Key Principles

- **先读后写** — Never modify a file you haven't read
- **最小变更** — Only change what's needed for this feature
- **规范优先** — Follow existing project conventions, don't invent new ones
- **文档驱动** — Every code decision should trace back to a PM document
- **渐进加载** — Only load the internal module needed for the current phase
