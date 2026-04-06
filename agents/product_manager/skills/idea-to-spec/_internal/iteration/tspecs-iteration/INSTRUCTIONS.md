---
name: tspecs-iteration
description: Iteratively update test specifications and test cases based on requirement changes, validator reports, or implementation feedback. Use when users say "update test specs", "revise test cases", "iterate QA plan", "propagate requirement changes to tests", or need to evolve an existing test specification while maintaining version history.
---

# TEST_SPEC Iteration

Apply changes to an existing test specification while preserving coverage
history, traceability, and versioning.

## When to use

- `tspecs-validator` reported issues that need fixing
- PRD / TRD / API changes require test coverage updates
- QA review found missing negative, boundary, regression, or NFR coverage
- **Not for** creating a new test specification from scratch (use `tspecs-gen`)

## Inputs

- **Required**:
  - `test_spec_document`: The existing test specification to update
  - `change_request`: One of:
    - Validator report from `tspecs-validator`
    - Requirement / API / TRD change summary
    - Free-text QA feedback
    - Structured coverage gap list
- **Optional**:
  - `related_prd`: PRD for requirement alignment
  - `related_trd`: TRD for technical / NFR alignment
  - `related_api`: API doc for endpoint and error coverage alignment
  - `preserve_cases`: Test cases that must remain unchanged

## Workflow

1. **Read current document**: Parse metadata, coverage summary, test cases,
   traceability matrix, and changelog.
2. **Classify the requested change**:
   - Coverage gap fix
   - Requirement propagation
   - Execution strategy adjustment
   - Test case retirement or replacement
3. **Update coverage deliberately**:
   - Add or revise test cases for changed requirements
   - Maintain positive, negative, and boundary coverage for P0 items
   - Update NFR, regression, and smoke-pack sections when release criteria
     change
   - Preserve unchanged cases exactly
4. **Repair traceability**:
   - Keep Coverage Summary and Traceability Matrix synchronized
   - Mark retired tests explicitly and note replacement coverage if any
5. **Bump version**: Use
`agents/product_manager/skills/idea-to-spec/_internal/_shared/output-conventions.md`.
6. **Update changelog**: Record coverage added, revised, deferred, or retired.
7. **Run inline validation**: Apply `tspecs-validator` checks, using related
   docs if provided.
8. **Present**: Show a coverage diff summary, validation result, and updated
   TEST_SPEC.

## Output Contract

- **Format**: Updated Markdown TEST_SPEC with bumped version
- **Diff summary**: Coverage-level summary plus test case adds / updates /
  retirements
- **Validation result**: Inline `tspecs-validator` score and remaining issues
- **Traceability notes**: Explicit callout for unresolved coverage gaps

## Failure Handling

- Missing version metadata -> initialize at `1.0.0`
- Requirement IDs changed or are ambiguous -> ask the user to confirm mapping
- Requested removal would leave a P0 item uncovered -> warn before proceeding
- Post-iteration validation still FAIL -> list unresolved gaps and suggest
  another iteration

## Safety Boundaries

- Preserve unchanged test cases exactly
- Never silently drop coverage for a requirement, endpoint, or NFR
- Confirm with the user before MAJOR version bumps or broad test-case
  retirements
- Do not modify files on disk unless explicitly instructed

## Examples

### Example 1

**User**: Update the test spec because password reset links now expire in 15
minutes, and the validator says there is no boundary test for rate limiting.

**Expected Output**:

Changes summary:
- [UPDATED] Coverage Summary: `REQ-07` now references 15-minute expiry behavior
- [ADDED] `TC-014`: Boundary test for reset-request rate limit
- [UPDATED] Regression Pack: Added expiry and lockout smoke checks
- Version: `1.0.0` -> `1.1.0`
