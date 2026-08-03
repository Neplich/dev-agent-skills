---
name: trace-check
description: Check traceability across PRD, TRD, and test specifications. Use when users say "traceability check", "trace matrix", "requirement tracing", "coverage gap", "requirements mapping", or need to verify that every product requirement maps through technical design to test cases.
---

# Traceability Checker

Build and verify a traceability matrix across the full document chain.

## When to use

- Need to verify end-to-end requirement coverage (PRD → TRD → Tests)
- Identify gaps where requirements lack downstream coverage
- Audit before a milestone to ensure nothing was missed
- **Analysis only** — produces a report, does not modify documents

## Inputs

- **Required** (at least 2):
  - `prd`: Product Requirements Document
  - `trd`: Technical Requirements Document
  - `test_specs`: Test specification document
- **Optional**:
  - `trace_depth`: Which levels to check — `prd→trd` / `prd→tests` / `full` (default: full)

## Workflow

1. **Parse documents**: Extract requirement IDs, feature IDs, user story IDs, test case IDs from each document.

2. **Build trace links**: Map relationships:
   - PRD requirements → TRD components/APIs
   - PRD requirements → Test cases
   - TRD APIs → API documentation

3. **Identify gaps**:
   - **Forward gaps**: Upstream requirement with no downstream coverage
   - **Backward gaps**: Downstream item with no upstream justification (orphan)
   - **Partial coverage**: Requirement partially covered (some AC tested, others not)

4. **Generate traceability matrix**:
   ```
   | PRD Requirement | TRD Component | Test Cases | Status |
   ```

5. **Summarize findings**: Coverage percentage, gap list, orphan list.

## Output Contract

- **Format**: Markdown traceability report
- **Structure**:
  ```markdown
  ## Traceability Report

  ### Coverage Summary
  - PRD → TRD: X% (N/M requirements traced)
  - PRD → Tests: X% (N/M requirements tested)

  ### Traceability Matrix
  | PRD ID | TRD ID | Test ID | Status |

  ### Forward Gaps (Missing Coverage)
  | Source ID | Source Doc | Missing In | Severity |

  ### Orphans (No Upstream)
  | Item ID | Document | Description |

  ### Recommendations
  1. ...
  ```

## Failure Handling

- Inconsistent ID formats across docs → use fuzzy matching on names, flag uncertainty
- Missing document → check available levels only, note limited scope
- No IDs in documents → attempt section-level matching by topic

## Safety Boundaries

- Read-only — never modifies documents
- Do not access external URLs

## Examples

### Example 1

**User**: Check traceability across our PRD, TRD, and test specs for the user auth feature.

**Expected Output**: Traceability matrix showing PRD user stories US-01..US-08 mapping to TRD components and test cases TC-001..TC-015. Gap: "US-07 has no test cases". Coverage: PRD→TRD 100%, PRD→Tests 85%.
