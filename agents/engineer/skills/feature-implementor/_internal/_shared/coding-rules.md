# Coding Rules

> Shared coding principles referenced by all feature-implementor internal modules.

## Core Rules

### 1. Read Before Write
- ALWAYS read a file before modifying it
- Understand the existing code structure, patterns, and context
- Never assume what a file contains

### 2. Minimal Change
- Only modify what is necessary for the current task
- Do not refactor surrounding code unless explicitly requested
- Do not add comments, docstrings, or type annotations to code you didn't change
- Do not "improve" imports, formatting, or variable names in untouched code

### 3. Convention First
- Follow the project's existing naming conventions (camelCase, snake_case, etc.)
- Place new files where similar files already live
- Use the same import style (relative vs absolute, order)
- Match error handling patterns already in the codebase
- Use the same test patterns for new tests

### 4. Document Traceability
- Every implementation decision should trace to a PM document section
- If a requirement is ambiguous, flag it — don't guess
- If TRD and code conflict, ask which is correct — don't silently pick one

### 5. Security Boundaries
- Validate user input at system boundaries (API routes, form handlers)
- Never hardcode secrets, tokens, or credentials
- Use parameterized queries for database operations
- Sanitize output to prevent XSS in user-facing content
- Don't add security measures for internal code paths that don't need them

### 6. Error Handling
- Follow the project's existing error handling patterns
- Only add error handling at real failure points (I/O, network, user input)
- Don't wrap internal function calls in try-catch unless the project does this
- Propagate errors to where they can be meaningfully handled

### 7. No Over-Engineering
- Don't create abstractions for things used once
- Don't add feature flags unless the TRD specifies them
- Don't design for hypothetical future requirements
- Three similar lines of code is better than a premature abstraction

## File Size Guidance

- Prefer smaller, focused files over large multi-purpose ones
- If a new file exceeds ~200 lines, consider whether it has multiple responsibilities
- When modifying a large existing file, don't refactor it — just make your change
- Only split a file if the TRD or task explicitly calls for restructuring
