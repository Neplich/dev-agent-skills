---
name: tspecs-gen
description: Generate test specifications and test cases from PRD or TRD documents. Use when users say "generate test cases", "test spec", "test plan", "QA spec", "acceptance tests", "create test scenarios", or need structured test cases with preconditions, steps, and expected results.
---

# Test Specifications Generator

Generate structured test case sets from product, technical, or API source
documents.

## When to use

- PRD or TRD is ready and you need test cases before development
- Need to ensure all requirements have corresponding test coverage
- Creating QA handoff documentation
- **Input typically from**: `prd-gen`, `trd-gen`, or `api-gen` output

## Inputs

- **Required**:
  - `source_doc`: PRD, TRD, API documentation, or feature description to derive
    tests from
- **Optional**:
  - `test_level`: Unit / Integration / E2E / All (default: All)
  - `priority_filter`: Only generate tests for P0 / P0+P1 / All (default: All)
  - `format`: Table / Gherkin / Both (default: Table)

## Conventions

Follow `agents/product_manager/skills/idea-to-spec/_internal/_shared/gen-conventions.md` for standard workflow,
failure handling, and safety boundaries.

- **Schema**: `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/test-spec-schema.md`
- **Metadata**: `type: TEST_SPEC`, version `1.0.0`
- **Naming**: `docs/qa/<feature-name>/TEST_SPEC.md`
- **Case files**: every E2E test case must also be written as a separate
  Markdown file under `docs/qa/<feature-name>/test-cases/` using
  `TC-NNN-<short-slug>.md`
- **File exploration memory**: if test cases are derived from project file
  exploration rather than only PRD / TRD / API docs, write
  `docs/qa/<feature-name>/FILE_EXPLORATION.md`

## Workflow Details

1. **Parse source material**: Extract functional requirements, user stories,
   acceptance criteria, endpoints, error cases, and NFRs from the source
   document.
2. **Define the suite**: Generate Test Scope, Strategy Summary, Environment &
   Data assumptions, and release-oriented smoke / regression boundaries.
3. **Map coverage**: Create a requirement-to-test mapping ensuring every P0
   requirement has positive coverage and at least one negative or boundary test.
4. **Generate test cases**: For each requirement or endpoint include Test Case
   ID (`TC-NNN`), Title, Requirement Links, Priority, Level, Category,
   Preconditions, Steps, Expected Result, and Notes.
   - Keep `TEST_SPEC.md` as the index and coverage summary.
   - For every E2E case, create one case file under `test-cases/` and link it
     from the `TEST_SPEC.md` test case table.
   - Non-E2E cases may remain inline unless the user requests per-case files.
5. **Add operational coverage**: Include NFR, reliability, security, or other
   operational checks when the source doc defines measurable targets.
6. **Close traceability**: Produce Coverage Summary plus Traceability Matrix
   showing covered items and explicit gaps.

**Output structure**:
```
## Test Scope & Objectives
## Test Strategy Summary
### Coverage Summary
| Requirement ID | Test Cases | Status |
### Test Environment & Data
### Test Cases
| TC-001 | Title | Case File | Preconditions | Steps | Expected | Priority | Level |
### E2E Case Files
- `test-cases/TC-001-<short-slug>.md`
### Non-Functional & Operational Tests
### Regression & Smoke Pack
### Traceability Matrix
| Requirement | Test Cases |
```

**Quality requirements**:
- Every P0 requirement has at least one mapped test case
- Every P0 requirement has positive coverage plus a negative or boundary test
- Every test case has Preconditions, Steps, and Expected Result
- Every E2E test case has exactly one linked case file under `test-cases/`
- Coverage Summary and Traceability Matrix must stay synchronized

**Tspecs-specific failure handling**:
- Source doc lacks acceptance criteria -> derive testable criteria, mark `[DERIVED]`
- Ambiguous requirement -> generate test for most likely interpretation, flag for review
- Too many requirements (> 50) -> ask user to filter by priority
- Use synthetic data only -> no real user data or credentials

## Related skills

- `tspecs-validator` -> validate suite quality and coverage gaps
- `tspecs-iteration` -> update test specs after requirement changes
- `trace-check` -> verify cross-document coverage

## Examples

### Example 1: From user stories

**User**: Generate test cases from this PRD user story:
> US-01: As a user, I want to reset my password via email so that I can regain access. AC: Reset link sent within 30s, link expires in 24h, new password must meet strength rules.

**Expected Output**:

| ID | Title | Case File | Preconditions | Steps | Expected | Priority | Level |
|----|-------|-----------|---------------|-------|----------|----------|-------|
| TC-001 | Password reset email sent | `test-cases/TC-001-password-reset-email-sent.md` | User exists with verified email | 1. Go to login 2. Click "Forgot password" 3. Enter email 4. Submit | Reset email received within 30s | P0 | E2E |
| TC-002 | Reset link expiration | `test-cases/TC-002-reset-link-expiration.md` | Reset email received > 24h ago | 1. Click reset link after 24h | Error: "Link expired, request a new one" | P0 | E2E |
| TC-003 | Weak password rejected | N/A | Valid reset link clicked | 1. Enter "123" as new password 2. Submit | Error: password strength requirements shown | P0 | Integration |
| TC-004 | Non-existent email | `test-cases/TC-004-non-existent-email.md` | No account with email | 1. Enter unknown email 2. Submit | Same success message (no user enumeration) | P0 | E2E |

Generated E2E case files:

- `docs/qa/password-reset/test-cases/TC-001-password-reset-email-sent.md`
- `docs/qa/password-reset/test-cases/TC-002-reset-link-expiration.md`
- `docs/qa/password-reset/test-cases/TC-004-non-existent-email.md`
