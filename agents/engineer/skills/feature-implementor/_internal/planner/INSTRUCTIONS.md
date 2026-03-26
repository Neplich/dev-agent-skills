# Implementation Planner

> Internal module for feature-implementor. Loaded during Phase 1.

## Purpose

Read PM documents and break the feature into an ordered list of file-level implementation steps.

## Input

- PM documents: PRD, TRD, API Spec, ADR (whichever are relevant)
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

### 3. Order by dependency

Build a dependency graph and produce a linear order:
1. Types / interfaces / schemas first
2. Data layer (models, database schemas)
3. Business logic (services, use cases)
4. API / route layer
5. UI components (if applicable)
6. Configuration / wiring (route registration, middleware, etc.)

### 4. Present plan

Output format:

```text
## 实现计划

### 概述
- 功能: <feature name>
- 来源文档: <list>
- 预估文件数: <N> 个新建, <M> 个修改

### 步骤

1. **创建 `<path>`** — <description> (来自 <doc> §<section>)
   - 依赖: 无
2. **创建 `<path>`** — <description> (来自 <doc> §<section>)
   - 依赖: 步骤 1
3. **修改 `<path>`** — <description> (来自 <doc> §<section>)
   - 依赖: 步骤 1, 2

确认后加载 implementor 开始编码。
```

## Output

An ordered implementation plan with exact file paths, descriptions, and document references. Wait for user confirmation.
