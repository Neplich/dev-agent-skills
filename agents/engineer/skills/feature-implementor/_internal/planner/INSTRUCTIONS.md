# Implementation Planner

> Internal module for feature-implementor. Loaded during Phase 1.

## Purpose

Read confirmed PM, Engineer, and Design documents, then write an implementation
plan document with an ordered list of file-level implementation steps.

## Input

- PM documents: PRD, DECISIONS, BRD (whichever are relevant)
- Engineer documents: confirmed TRD, API Spec, ADR
- Project Profile (from codebase-analyzer)

## Process

### 1. Extract requirements

From PRD:
- List all P0 user stories and acceptance criteria
- Note P1 items that affect architecture but may be deferred

From TRD:
- Component breakdown (which modules to create/modify)
- Data model (schemas, types, models)
- Architecture constraints

If the Engineer TRD is missing, incomplete, or conflicts with the codebase, stop
and hand back to `engineer-agent:trd-gen`. Do not silently create or revise TRD
content inside the implementation plan.

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

Do not force the split for single-file small edits, pure explanation, pure code
reading, or explicit user opt-out.

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
- PRD / DECISIONS / design inputs
- exact output path: `docs/engineer/{feature}/IMPLEMENTATION_PLAN.md`
- file change list, sequence, tests, delegation split, forbidden areas, blockers
- instruction not to write code or revise TRD decisions

The main process reviews the document before asking for implementation
confirmation.

### 5. Present plan

Output format:

```text
## 实现计划

### 概述
- 功能: <feature name>
- 来源文档: <list>
- TRD: docs/engineer/<feature>/TRD.md
- 实现计划文档: docs/engineer/<feature>/IMPLEMENTATION_PLAN.md
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
