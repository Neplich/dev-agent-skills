# Validator Skill Conventions

> Standard workflow, output format, safety, and failure handling rules shared by all validator skills under `validator/`.
> Each validator skill MUST follow these conventions unless explicitly overridden.

## Standard Workflow

Every validator skill follows this workflow:

1. **Load references**: Read the corresponding schema from
`skills/product-dev/idea-to-spec/_internal/_shared/doc-schemas/`. Use the canonical filenames:
   `brd-schema.md`, `prd-schema.md`, `trd-schema.md`, `adr-schema.md`,
   `api-schema.md`, and `test-spec-schema.md`. Also load
`skills/product-dev/idea-to-spec/_internal/_shared/quality-rules.md`.

2. **Parse document**: Extract all sections and metadata from the input document.

3. **Validate structure**: Check all required sections per the schema are present.

4. **Score dimensions**: Rate Completeness (30%), Consistency (25%), Clarity (25%), Testability (20%) per quality-rules.md (1-5 each).

5. **Run type-specific checks**: Apply the checks defined in each validator's own INSTRUCTIONS.md (CRITICAL / WARNING / SUGGESTION).

6. **Cross-check** (if related documents provided): Verify alignment between documents (e.g., PRD goals map to BRD objectives, TRD covers all PRD endpoints).

7. **Calculate overall score**: Apply weights from quality-rules.md.

8. **Generate validation report**: Output per the Validation Report Template in quality-rules.md.

## Output Contract

All validators produce:

- **Format**: Markdown validation report
- **Verdict**: PASS (≥ 4.0) / NEEDS_WORK (2.5–3.9) / FAIL (< 2.5)
- **Structure**:
  ```markdown
  ## Validation Report
  - Document: <filename>
  - Type: <BRD/PRD/TRD/ADR/API/TEST_SPEC>
  - Overall Score: X.X / 5
  - Status: <PASS/NEEDS_WORK/FAIL>

  ### Dimension Scores
  | Dimension | Score | Weight | Weighted |
  |-----------|-------|--------|----------|

  ### Critical Issues
  1. [CRITICAL] ...

  ### Warnings
  1. [WARNING] ...

  ### Suggestions
  1. [SUGGESTION] ...
  ```
- **No modifications** to the input document — validators are strictly read-only.

## Failure Handling

All validators handle failures gracefully:

- **Cannot parse document** → Report parsing errors with line numbers where possible.
- **Document is wrong type** → Report type mismatch, suggest the correct validator skill.
- **Missing sections** → Score as incomplete, list missing sections in Critical Issues.

## Safety Boundaries

All validators observe these rules:

1. **Read-only** — Never modify the input document.
2. **No external access** — Do not access external URLs or APIs.
3. **No data transmission** — Do not store or transmit document content.
4. **No API execution** — Do not call endpoints to validate API docs.
