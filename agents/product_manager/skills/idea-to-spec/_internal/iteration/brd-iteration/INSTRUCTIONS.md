---
name: brd-iteration
description: Iteratively update a BRD document based on change requests or validator reports. Use when users say "update BRD", "revise BRD", "iterate BRD", "fix BRD issues", or need to evolve an existing BRD while maintaining version history.
---

# BRD Iteration

Apply changes to an existing BRD while maintaining version history and quality standards.

## When to use

- BRD validator reported issues to fix
- Business context changed, need to update objectives or scope
- Stakeholder feedback to incorporate
- **Not for** creating a new BRD (use `brd-gen`)

## Inputs

- **Required**:
  - `brd_document`: The existing BRD
  - `change_request`: Validator report, free-text changes, or structured change list
- **Optional**:
  - `preserve_sections`: Sections to not modify

## Workflow

1. **Read current document**: Parse BRD, extract version metadata.
2. **Analyze changes**: Classify as validation fixes, content updates, or scope changes.
3. **Apply changes**: Modify affected sections, preserve unchanged content.
4. **Bump version**: Per output-conventions.md rules.
5. **Update changelog**.
6. **Run inline validation**: Apply brd-validator checks.
7. **Present**: Diff summary + updated document.

## Output Contract

- **Format**: Updated Markdown BRD with bumped version
- **Diff summary**: Section-by-section changes
- **Validation result**: Post-iteration score

## Failure Handling

- Missing version metadata → initialize at 1.0.0
- Conflicting changes → ask user to prioritize
- Changes remove required sections → warn before proceeding

## Safety Boundaries

- Preserve unchanged sections exactly
- Track all deletions in changelog
- Confirm MAJOR version bumps with user

## Examples

### Example 1

**User**: Update the BRD — our target market has shifted from B2C to B2B. Update stakeholders and ROI accordingly.

**Expected Output**: Changes summary showing updated Stakeholder Analysis, ROI section, and Success Criteria. Version 1.0.0 → 2.0.0 (MAJOR: scope change). Changelog entry documenting the market pivot.
