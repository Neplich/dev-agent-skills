# Code Implementor

> Internal module for feature-implementor. Loaded during Phase 2.

## Purpose

Execute the implementation plan step by step, writing code that follows project conventions and traces to PM documents.

## Input

- User-confirmed implementation plan document (from planner)
- Project Profile
- PM documents for reference
- Confirmed Engineer TRD for reference
- For complex coding tasks: implementation sub-agent scope, forbidden areas,
  expected behavior, and verification commands

## Entry Gate

Do not implement unless the main process has already presented the exact
implementation plan to the user and the user has confirmed it. If the plan is
missing, has only been drafted, or has not been confirmed, stop and ask for plan
confirmation. Do not write code, update tests, or apply fixes while waiting.

For existing-feature behavior changes, the confirmed plan must also include the
PRD alignment result. If the plan says PRD / DECISIONS must be updated, docs are
unclear, or TRD is stale, stop and hand back to the owning PM or TRD step
instead of implementing. When handing back to `trd-gen`, state the TRD gap
packet: affected components, data flow / API / integration impacts, validation
commands, release or rollout risks, and error handling, observability, or
security strategy that the TRD must resolve. The implementor identifies the
gap; `trd-gen` completes the TRD.

## Sub-Agent Execution Contract

When the confirmed plan triggers the complex coding split and sub-agent
capabilities are available, the main process should delegate implementation to
an implementation sub-agent. The delegated task must include:

- owned files, directories, or modules
- source docs and relevant acceptance criteria
- expected behavior and tests to add or run
- forbidden areas and instruction not to revert unrelated user changes
- required output: changed files, implementation summary, verification results,
  and open issues

The implementation sub-agent writes code and tests within scope. The main
process keeps the broader requirements, repository rules, and delivery risks
for final integration.

## Process

For each step in the plan:

### 1. Read context

If modifying an existing file:
- Read the entire file
- Understand its current structure, exports, and patterns
- Identify the exact location for the change

If creating a new file:
- Read 1-2 similar existing files to understand the project's patterns
- Use the same structure, imports, and style

### 2. Write code

Follow these rules strictly:
- Reference `_shared/coding-rules.md` for all coding decisions
- Every function, type, or endpoint should trace to a PM document section
- Every file-level implementation decision should trace to the confirmed TRD or
  implementation plan document
- Use the project's existing patterns, not "best practices" from elsewhere
- Keep the code simple — no abstractions beyond what's needed now

### 3. Verify

After each file:

```bash
# Language-specific build check
# TypeScript: npx tsc --noEmit
# Go: go build ./...
# Rust: cargo check
# Python: python -m py_compile <file>
```

If the build fails, fix it before moving to the next step.

### 4. Progress update

After each step, briefly report:

```text
✅ 步骤 N 完成: <path> — <what was done>
```

## Error Handling

- **Build failure after writing**: Read the error, fix the code, re-verify. Don't move to the next step with a broken build.
- **Ambiguous requirement**: Flag it to the user with the specific PM doc section reference. Ask for clarification before proceeding.
- **Conflicting conventions**: If the project has inconsistent patterns in different areas, follow the pattern in the most similar/nearby file.
- **Missing dependency**: If the code needs a package not yet installed, install it and note it in the progress update.
