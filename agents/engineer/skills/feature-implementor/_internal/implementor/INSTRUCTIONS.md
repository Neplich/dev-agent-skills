# Code Implementor

> Internal module for feature-implementor. Loaded during Phase 2.

## Purpose

Execute the implementation plan step by step, writing code that follows project conventions and traces to PM documents.

## Input

- Confirmed implementation plan (from planner)
- Project Profile
- PM documents for reference

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
