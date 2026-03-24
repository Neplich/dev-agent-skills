---
name: version-differ
description: Compare two versions of the same document and produce a structured diff report. Use when users say "compare versions", "diff documents", "what changed", "version diff", "document comparison", or need to understand section-by-section differences between two versions of a BRD, PRD, TRD, or other project document.
---

# Version Differ

Compare two versions of the same document and produce a structured, section-by-section diff report.

## When to use

- Reviewing what changed between two document versions
- Preparing a change summary for stakeholder review
- Auditing document evolution over time
- **Analysis only** — produces a report, does not modify documents

## Inputs

- **Required**:
  - `version_a`: Earlier version of the document (file path or inline)
  - `version_b`: Later version of the document (file path or inline)
- **Optional**:
  - `focus_sections`: Only diff specific sections (default: all)
  - `ignore_formatting`: Skip whitespace/formatting changes (default: true)

## Workflow

1. **Parse both versions**: Extract metadata (version numbers, dates) and section structure.

2. **Align sections**: Match sections between versions by heading name. Detect renamed, added, and removed sections.

3. **Diff each section**: For each matched section pair:
   - Identify added content
   - Identify removed content
   - Identify modified content
   - Classify change significance: Major / Minor / Cosmetic

4. **Summarize changes**:
   - Version transition (e.g., 1.0.0 → 1.2.0)
   - Change statistics (sections added/removed/modified)
   - Per-section change details

5. **Present**: Structured diff report.

## Output Contract

- **Format**: Markdown diff report
- **Structure**:
  ```markdown
  ## Version Diff Report

  ### Document Info
  - Document: <name>
  - Version A: <version> (<date>)
  - Version B: <version> (<date>)

  ### Change Summary
  - Sections added: N
  - Sections removed: N
  - Sections modified: N
  - Overall change magnitude: Major / Minor / Cosmetic

  ### Section-by-Section Diff

  #### <Section Name> — [ADDED | REMOVED | MODIFIED | UNCHANGED]
  **Change type**: Major / Minor / Cosmetic
  **Details**:
  - Added: ...
  - Removed: ...
  - Modified: ...

  ### Changelog Suggestion
  Recommended changelog entry for this version transition.
  ```

## Failure Handling

- Documents appear to be different types → warn but proceed if user confirms
- Cannot match sections (completely restructured) → fall back to full-text diff
- Missing version metadata → use file names or ask user for version labels

## Safety Boundaries

- Read-only — never modifies either document
- Do not access external URLs
- Handle large documents by summarizing rather than showing full inline diffs

## Examples

### Example 1

**User**: Compare PRD v1.0.0 and v1.2.0 for the checkout feature.

**Expected Output**:

```markdown
## Version Diff Report

### Document Info
- Document: prd-checkout-flow
- Version A: 1.0.0 (2025-01-10)
- Version B: 1.2.0 (2025-01-25)

### Change Summary
- Sections added: 1 (Accessibility Requirements)
- Sections removed: 0
- Sections modified: 3
- Overall change magnitude: Minor

### Section-by-Section Diff

#### User Stories — MODIFIED
**Change type**: Minor
- Added: US-08 (Apple Pay support), US-09 (address autocomplete)
- Modified: US-03 acceptance criteria updated with specific timeout value

#### NFR — MODIFIED
**Change type**: Minor
- Modified: Latency target changed from "< 3s" to "< 2s"

#### Accessibility Requirements — ADDED
**Change type**: Major
- New section: WCAG AA compliance requirements added
```
