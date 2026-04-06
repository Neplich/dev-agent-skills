---
name: prd-iteration
description: Iteratively update a PRD document based on change requests, feedback, or validator reports. Use when users say "update PRD", "revise PRD", "iterate PRD", "apply changes to PRD", "fix PRD issues", or need to evolve an existing PRD while maintaining version history.
---

# PRD Iteration

Apply changes to an existing PRD while maintaining version history and quality standards.

## When to use

- PRD validator reported issues that need fixing
- Stakeholder feedback requires PRD updates
- Scope changes or new requirements to incorporate
- **Not for** creating a new PRD from scratch (use `prd-gen`)

## Inputs

- **Required**:
  - `prd_document`: The existing PRD to update (file path or inline)
  - `change_request`: One of:
    - Validator report from `prd-validator`
    - Free-text change description
    - Structured change list
- **Optional**:
  - `preserve_sections`: Sections to not modify (default: none)

## Workflow

1. **Read current document**: Parse existing PRD, extract version metadata.

2. **Analyze changes**: Classify the change request:
   - Fix validation issues (CRITICAL first, then WARNING)
   - Apply content changes (additions, modifications, removals)
   - Scope changes (may require MAJOR version bump)

3. **Apply changes**: Modify affected sections while preserving unchanged content.

4. **Bump version**: Per `agents/product_manager/skills/idea-to-spec/_internal/_shared/output-conventions.md`:
   - Typo/formatting → PATCH
   - New/updated content → MINOR
   - Scope change → MAJOR

5. **Update changelog**: Add entry to both frontmatter and inline changelog.

6. **Run inline validation**: Apply `prd-validator` checks to the updated document. Report any remaining issues.

7. **Present**: Show a diff summary of changes + the full updated document.

## Output Contract

- **Format**: Updated Markdown PRD with bumped version
- **Diff summary**: Section-by-section list of changes
- **Validation result**: Inline validation score of the updated document
- **Changelog**: Updated with new entry

## Failure Handling

- Version metadata missing → add it (start at 1.0.0)
- Conflicting changes → ask user to prioritize
- Changes would remove required sections → warn and ask for confirmation
- Post-iteration validation still FAIL → present issues and suggest next iteration

## Safety Boundaries

- Always preserve unchanged sections exactly as-is
- Never silently remove content — track all deletions in changelog
- Confirm with user before MAJOR version bumps
- Do not modify files on disk unless explicitly instructed

## Examples

### Example 1: Fix validator issues

**User**: Update the PRD based on this validator report:
> CRITICAL: US-03 missing acceptance criteria
> WARNING: NFR table missing latency target

**Expected Output**:

Changes summary:
- [FIXED] US-03: Added acceptance criteria "Given... When... Then..."
- [FIXED] NFR table: Added latency target "p95 < 2s"
- Version: 1.0.0 → 1.1.0

Updated PRD with new version header and changelog entry.
