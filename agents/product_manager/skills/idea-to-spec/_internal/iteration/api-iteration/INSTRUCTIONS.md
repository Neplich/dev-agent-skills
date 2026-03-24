---
name: api-iteration
description: Iteratively update API documentation based on change requests, code changes, or validator reports. Use when users say "update API docs", "revise API spec", "iterate API documentation", "apply endpoint changes", or need to evolve an existing API document while maintaining version history.
---

# API Iteration

Apply changes to existing API documentation while preserving contract clarity,
version history, and endpoint-level diffs.

## When to use

- `api-validator` reported issues that need fixing
- Endpoint contracts changed after implementation or review
- New endpoints, fields, auth rules, or error codes need documentation updates
- **Not for** creating a new API document from scratch (use `api-gen`)

## Inputs

- **Required**:
  - `api_document`: The existing API documentation to update
  - `change_request`: One of:
    - Validator report from `api-validator`
    - Code diff or route change summary
    - Free-text change description
    - Structured endpoint change list
- **Optional**:
  - `code_source`: Route definitions or controller snippets for cross-checking
  - `preserve_endpoints`: Endpoints that must remain unchanged

## Workflow

1. **Read current document**: Parse metadata, endpoint inventory, models,
   examples, and changelog.
2. **Classify changes**:
   - Documentation fix
   - Backward-compatible contract update
   - Breaking contract change
   - Endpoint addition / deprecation / removal
3. **Apply updates**:
   - Update affected endpoints, shared headers, auth, models, error codes, and
     examples
   - Preserve unchanged endpoints exactly
   - Mark deprecated endpoints explicitly instead of silently removing them
4. **Assess version impact**:
   - Minor documentation or non-breaking content updates -> MINOR / PATCH
   - Breaking request or response contract changes -> MAJOR
5. **Update changelog**: Record added, changed, deprecated, or removed items.
6. **Run inline validation**: Apply `api-validator` checks, optionally
   cross-checking with `code_source`.
7. **Present**: Show endpoint diff summary, updated changelog, and validation
   result.

## Output Contract

- **Format**: Updated Markdown API document with bumped version
- **Diff summary**: Endpoint-level adds / changes / deprecations / removals
- **Validation result**: Inline `api-validator` score and remaining issues
- **Compatibility notes**: Explicit note when the change is breaking

## Failure Handling

- Missing version metadata -> initialize at `1.0.0`
- Conflicting endpoint changes -> ask the user which source of truth to use
- Change removes required auth or error information -> warn before proceeding
- Post-iteration validation still FAIL -> list unresolved issues and suggest
  another iteration

## Safety Boundaries

- Preserve unchanged endpoints exactly
- Never silently remove fields, error codes, or auth requirements
- Confirm with the user before MAJOR version bumps or destructive deprecations
- Do not modify files on disk unless explicitly instructed

## Examples

### Example 1

**User**: Update the API doc. `POST /sessions` now returns refresh tokens and
the validator says the auth header example is missing.

**Expected Output**:

Changes summary:
- [FIXED] Authentication: Added concrete Bearer header example
- [UPDATED] `POST /sessions`: Response schema now includes `refresh_token`
- [UPDATED] Data Models: Added refresh token field constraints
- Version: `1.0.0` -> `1.1.0`
