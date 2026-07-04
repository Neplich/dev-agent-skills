# Implementation Planner

> Internal module for feature-implementor. Loaded during Phase 1.

## Purpose

Read confirmed PM, Engineer, and Design documents, then write an implementation
plan document with an ordered list of file-level implementation steps. This
planner runs before implementation for every feature implementation task,
including small, single-file, and spec-backed bug-fix changes routed into
`feature-implementor`.

## Input

- PM documents: PRD, BRD, and DECISIONS or product decision records when present
- Engineer documents: confirmed TRD, API Spec, ADR
- Project Profile (from codebase-analyzer)
- Existing-feature alignment result from the public `feature-implementor`
  PRD alignment gate
- Resolved `feature_path`, `parent_feature`, and `feature_level` from PRD/TRD
  frontmatter or legacy single-level path inference

## Process

### 1. Extract requirements

Before extracting implementation steps, confirm that the public PRD alignment
gate has a clear result:

- `already_approved`: the requested behavior is covered by PRD and confirmed
  TRD, and any present decision records do not conflict; continue planning and
  cite the source docs.
- `needs_pm_update`: the request changes approved behavior; stop and hand off
  to `pm-agent:idea-to-spec` using the `existing-project-update` lane.
- `docs_missing_or_unclear`: PRD or product decision records do not define a
  consistent expected behavior; stop and request PM alignment. Do not classify
  a request this way only because `DECISIONS.md` is absent when PRD and TRD are
  sufficient.
- `trd_gap`: PM scope is stable, but the Engineer TRD is missing, incomplete,
  stale, or conflicts with the codebase; stop and hand back to
  `engineer-agent:trd-gen` with a TRD gap packet.
- A user request to skip PRD alignment is not a valid planning state. Treat it
  as blocked until PRD/TRD alignment is complete.

Before extracting implementation steps, run the feature path gate:

1. Confirm the PRD path is `docs/pm/{feature_path}/PRD.md`.
2. Confirm the TRD path is `docs/engineer/{feature_path}/TRD.md`.
3. Confirm PRD and TRD frontmatter have matching `feature_path`,
   `parent_feature`, and `feature_level`.
4. Confirm TRD `related_prd` points to `docs/pm/{feature_path}/PRD.md`.
5. Confirm the planned output path is
   `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`.

If the PRD is missing or the PM feature path is unclear, stop and hand back to
`pm-agent:idea-to-spec`. If the TRD is missing, stale, or path-mismatched, stop
and hand back to `engineer-agent:trd-gen` with a TRD gap packet. Old single-level
docs without feature path fields remain valid as level-1 features; infer the
fields from the directory name while writing new plans with explicit fields.

Before writing a new or replacement active plan, run the pre-plan archive scan:

1. Check whether `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` already
   exists and read its frontmatter and closeout status.
2. Check `docs/engineer/{feature_path}/implementation-plans/archive/` for prior
   archived plans.
3. If no active plan exists, continue planning and create the new plan.
4. If an active plan exists and no handling decision has been recorded, stop and
   report the existing plan path, status, and scope, then ask the user to choose
   one of: archive the completed plan then create a new plan, continue updating
   the current plan, or archive the old plan as `Superseded` with a reason then
   create a new plan. Do not overwrite the active plan while the decision is
   unresolved.
5. When a new active plan is created after archival, record
   `previous_plan_archive` in its frontmatter pointing to the archive file.

From PRD:
- List all P0 user stories and acceptance criteria
- Note P1 items that affect architecture but may be deferred

From TRD:
- Component breakdown (which modules to create/modify)
- Data model (schemas, types, models)
- Architecture constraints

If the Engineer TRD is missing, incomplete, or conflicts with the codebase, stop
and hand back to `engineer-agent:trd-gen` with a TRD gap packet. Do not silently
create or revise TRD content inside the implementation plan.

The planner is the finder when it detects a TRD gap. It must clearly list the
missing technical decisions; `trd-gen` is responsible for updating the TRD. The
gap packet should cover affected components or modules, data flow / API /
integration impact, validation commands, release or rollout risk, and error
handling, observability, or security strategy when relevant. It must include a
separate boundary line: "Finder only clarifies the TRD gaps;
`engineer-agent:trd-gen` completes the TRD."

From API Spec:
- Endpoint list (method, path, request shape, response shape)
- Auth requirements per endpoint
- Error response codes

From ADR:
- Technology constraints (specific library choices, patterns to follow)

### 2. Map to file changes

For each component in TRD, determine:
- Is this a new file or a modification?
- If modification, which existing file?
- What does this file depend on? (Other files in this plan)
- Whether the task is complex enough to use the implementation/validation
  sub-agent split:
  - multi-file or multi-module change
  - spec-backed implementation with PM/design docs
  - tests must be added or updated
  - the main process must retain substantial requirement, code, test, and
    delivery context

Do not force the implementation/validation sub-agent split for single-file small
edits, pure explanation, pure code reading, or explicit user opt-out. This only
controls delegation. It does not remove the requirement to write
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` and wait for explicit
user confirmation.

### 3. Order by dependency

Build a dependency graph and produce a linear order:
1. Types / interfaces / schemas first
2. Data layer (models, database schemas)
3. Business logic (services, use cases)
4. API / route layer
5. UI components (if applicable)
6. Configuration / wiring (route registration, middleware, etc.)

### 4. Write implementation plan document

When sub-agent capabilities are available, delegate the plan document writing to
a fresh document-writing sub-agent. The delegated task must include:

- confirmed TRD path
- PRD / optional DECISIONS / design inputs
- PRD alignment result and source-document evidence
- exact output path: `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`
- file change list, sequence, tests, delegation split, forbidden areas, blockers
- frontmatter maintenance for `version`, `last_updated`, `feature_path`,
  `parent_feature`, `feature_level`, `related_prd`, and `related_trd`
- traceable frontmatter author using
  `<generation requester display name> <agent platform name>`, for example
  `Neplich Codex`; the platform name may be custom, so ask the user when either
  part is unknown and do not use empty values or placeholders
- instruction not to write code or revise TRD decisions

For small changes, write a short plan that still names the target file, planned
edit, source requirement, verification command, and why complex sub-agent
delegation is not needed. Small changes still need a PRD alignment result; do
not convert "single file" or "small bug fix" into implicit PM approval or
permission to skip `IMPLEMENTATION_PLAN.md`.

#### Frontmatter version rules

`IMPLEMENTATION_PLAN.md` frontmatter must stay in sync with the plan body:

- New plans should start at `version: "0.1.0"` unless the repository has a
  stricter convention, and must include `feature`, `feature_path`,
  `parent_feature`, `feature_level`, `date`, `last_updated`, `related_prd`, and
  `related_trd`.
- Substantive plan changes must update both `version` and `last_updated` in the
  same edit. Substantive changes include changed implementation scope, ordered
  steps, file list, delegation model, verification commands, status, rollout
  checks, or architecture / flow diagrams.
- Use PATCH for clarifications that preserve the confirmed scope, MINOR for
  changed implementation scope or sequencing, and MAJOR only when replacing the
  confirmed plan contract.
- Typo, formatting, or non-semantic copy edits may keep the existing `version`,
  but should refresh `last_updated` when the file is touched.
- Preserve existing optional frontmatter fields such as `related_issue`,
  `related_pr`, `author`, and `generated_by` unless the current edit directly
  invalidates them.

The main process reviews the document before asking for implementation
confirmation.

### 5. Present plan

Output format:

```text
## 实现计划

### 概述
- 功能: <feature name>
- 来源文档: <list>
- Feature path: <feature_path>
- TRD: docs/engineer/<feature_path>/TRD.md
- 实现计划文档: docs/engineer/<feature_path>/IMPLEMENTATION_PLAN.md
- PRD 对齐: <已覆盖 / 需要 PM 更新 / 文档缺失或不清 / TRD gap>
- 预估文件数: <N> 个新建, <M> 个修改

### 步骤

1. **创建 `<path>`** — <description> (来自 <doc> §<section>)
   - 依赖: 无
2. **创建 `<path>`** — <description> (来自 <doc> §<section>)
   - 依赖: 步骤 1
3. **修改 `<path>`** — <description> (来自 <doc> §<section>)
   - 依赖: 步骤 1, 2

### Sub-Agent 分工
- 触发判断: <是否触发复杂编码分工及原因>
- 实现 sub-agent 范围: <owned files/modules, expected behavior, tests, forbidden areas>
- 验收 sub-agent 范围: <source docs, changed files, tests, repository rules, residual risks>

确认后加载 implementor 开始编码。
```

## Output

An implementation plan document plus a short summary with exact file paths,
descriptions, and document references. Wait for user confirmation before coding.
Do not start implementation in the same turn after writing the plan unless the
user has already confirmed this exact plan.
