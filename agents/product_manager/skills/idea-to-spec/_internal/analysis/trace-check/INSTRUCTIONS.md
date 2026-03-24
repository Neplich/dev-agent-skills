---
name: trace-check
description: Check traceability across BRD, PRD, TRD, and test specifications. Use when users say "traceability check", "trace matrix", "requirement tracing", "coverage gap", "requirements mapping", or need to verify that every business requirement maps through product requirements to technical design and test cases.
---

# Traceability Checker

Build and verify a traceability matrix across the full document chain.

## When to use

- Need to verify end-to-end requirement coverage (BRD → PRD → TRD → Tests)
- Identify gaps where requirements lack downstream coverage
- Audit before a milestone to ensure nothing was missed
- **Analysis only** — produces a report, does not modify documents

## Inputs

- **Required** (at least 2):
  - `brd`: Business Requirements Document
  - `prd`: Product Requirements Document
  - `trd`: Technical Requirements Document
  - `test_specs`: Test specification document
- **Optional**:
  - `trace_depth`: Which levels to check — `brd→prd` / `prd→trd` / `prd→tests` / `full` (default: full)

## Workflow

1. **Parse documents**: Extract requirement IDs, feature IDs, user story IDs, test case IDs from each document.

2. **Build trace links**: Map relationships:
   - BRD objectives → PRD features/user stories
   - PRD requirements → TRD components/APIs
   - PRD requirements → Test cases
   - TRD APIs → API documentation

3. **Identify gaps**:
   - **Forward gaps**: Upstream requirement with no downstream coverage
   - **Backward gaps**: Downstream item with no upstream justification (orphan)
   - **Partial coverage**: Requirement partially covered (some AC tested, others not)

4. **Generate traceability matrix**:
   ```
   | BRD Objective | PRD Requirement | TRD Component | Test Cases | Status |
   ```

5. **Summarize findings**: Coverage percentage, gap list, orphan list.

## Output Contract

- **Format**: Markdown traceability report
- **Structure**:
  ```markdown
  ## Traceability Report

  ### Coverage Summary
  - BRD → PRD: X% (N/M objectives traced)
  - PRD → TRD: X% (N/M requirements traced)
  - PRD → Tests: X% (N/M requirements tested)

  ### Traceability Matrix
  | BRD ID | PRD ID | TRD ID | Test ID | Status |

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

**User**: Check traceability across our BRD, PRD, and test specs for the user auth feature.

**Expected Output**: Traceability matrix showing BRD objectives BO-01..BO-03 mapping to PRD user stories US-01..US-08, with test cases TC-001..TC-015. Gaps: "BO-03 (compliance) has no PRD coverage", "US-07 has no test cases". Coverage: BRD→PRD 67%, PRD→Tests 85%.
