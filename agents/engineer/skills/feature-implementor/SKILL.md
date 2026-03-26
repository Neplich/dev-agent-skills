---
name: feature-implementor
description: "Core engineering skill: implement features based on PM documents (PRD, TRD, ADR, API Spec). Use this skill whenever the user wants to implement a feature, write code for a requirement, build functionality described in a spec, or turn a design into code. Trigger on phrases like '实现这个功能', '写代码', '开始编码', 'implement', 'build this feature', 'code this', or any request to turn PM documents into working code."
---

# Feature Implementor — Public Entry

The core engineering skill. Reads PM documents (PRD, TRD, ADR, API Spec), breaks the work into ordered implementation steps, writes code following project conventions, and self-reviews the result.

This is the public entry point. It owns:

- PM document reading and requirement extraction
- Implementation planning (which files to create/modify, in what order)
- Delegation to internal modules for step execution
- Quality self-check before handoff

Do not load internal modules until the implementation plan is confirmed.

## When to Use

- User wants to implement a feature described in PM documents
- User asks to "write code" or "implement" something with a spec available
- After `codebase-analyzer` or `project-bootstrap` has established project context

Do NOT use for:
- Bug fixes with no spec (use `debugger` instead)
- Writing tests only (use `test-writer` instead)
- Git/PR operations only (use `delivery` instead)

## Phase 0: Gather Context

### Read PM documents

Scan `docs/` for relevant specs:

```bash
ls docs/*.md docs/**/*.md 2>/dev/null
```

Read the documents relevant to the current task:
- **PRD**: functional requirements, user stories, acceptance criteria
- **TRD**: technical approach, component breakdown, architecture decisions
- **ADR**: specific technology choices and constraints
- **API Spec**: endpoint contracts, request/response shapes

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
- Existing modules affected: <list>
- New modules needed: <list>
```

## Phase 1: Plan the Implementation

Read the internal routing contract before planning:

`agents/engineer/skills/feature-implementor/_internal/_shared/coding-rules.md`

Break the feature into ordered implementation steps:

1. List every file that needs to be **created** or **modified**
2. Determine the dependency order (e.g., data model before API route before UI)
3. For each file, note:
   - What it does
   - Which PM doc section drives it
   - Dependencies on other files in this plan

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

确认后开始实现？
```

Wait for user confirmation before coding.

## Phase 2: Implement

Load the implementor internal module:

`agents/engineer/skills/feature-implementor/_internal/implementor/INSTRUCTIONS.md`

For each step in the plan:

1. **Read before write**: If modifying an existing file, read it first. Understand the current code.
2. **Write code**: Follow project conventions (naming, style, patterns). Reference the specific PM doc section.
3. **Verify compilation**: After each file, ensure the project still compiles/builds.
4. **Minimal scope**: Only write what the plan calls for. No "bonus" improvements.

## Phase 3: Self-Review

Load the reviewer internal module:

`agents/engineer/skills/feature-implementor/_internal/reviewer/INSTRUCTIONS.md`

Check the implementation against:

1. **TRD compliance**: Does the code match the architecture described in TRD?
2. **API compliance**: Do endpoints match the API Spec (routes, methods, request/response shapes)?
3. **PRD coverage**: Does the code fulfill all P0 acceptance criteria from PRD?
4. **Security basics**: No hardcoded secrets, no SQL injection, no XSS, proper input validation at boundaries.
5. **Convention compliance**: Naming, file placement, import style match the project.

Output a brief review summary:

```text
## 自检结果
- TRD 符合度: ✅ 所有组件按 TRD §3 实现
- API 符合度: ✅ 3/3 端点匹配 API Spec
- PRD 覆盖: ✅ 4/4 P0 验收标准覆盖
- 安全检查: ✅ 无明显安全问题
- 规范检查: ✅ 命名和结构符合项目规范
```

## Handoff

After implementation and self-review:

```text
## 建议下一步

- **写测试**: 使用 `test-writer` 基于 Test Spec 编写测试
- **直接交付**: 使用 `delivery` 创建 PR（如果测试已有或不需要）
```

## Key Principles

- **先读后写** — Never modify a file you haven't read
- **最小变更** — Only change what's needed for this feature
- **规范优先** — Follow existing project conventions, don't invent new ones
- **文档驱动** — Every code decision should trace back to a PM document
- **渐进加载** — Only load the internal module needed for the current phase
