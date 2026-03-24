---
name: change-impactor
description: Analyze the impact of a proposed change across project documents. Use when users say "impact analysis", "change impact", "what does this change affect", "dependency analysis", "ripple effect", or need to understand which BRDs, PRDs, TRDs, and test specs are affected by a proposed change.
---

# Change Impact Analyzer

Scan project documents to identify all artifacts affected by a proposed change.

## When to use

- Proposing a scope change and need to know what documents to update
- Evaluating the effort of a change request
- Before running `iteration-coordinator` to understand the blast radius
- **Analysis only** — produces a report, does not modify documents

## Inputs

- **Required**:
  - `change_proposal`: Description of the proposed change
- **Optional**:
  - `docs_directory`: Path to scan for project documents (default: current directory)
  - `doc_types`: Which document types to scan — BRD / PRD / TRD / ADR / API / TEST_SPEC (default: all)

## Workflow

1. **Parse change**: Extract the nature, scope, and affected domains of the proposed change.

2. **Scan documents**: Find all project documents in the directory (by YAML frontmatter `type` field or filename patterns).

3. **Build dependency graph**: Map relationships between documents:
   - BRD → PRD (business objectives → product requirements)
   - PRD → TRD (product requirements → technical design)
   - PRD → TEST_SPEC (requirements → test cases)
   - TRD → API (technical design → API contracts)
   - ADR ↔ TRD (decisions ↔ technical design)

4. **Analyze impact**: For each document, determine:
   - **Direct impact**: Document explicitly covers the changed area
   - **Indirect impact**: Document depends on a directly impacted document
   - **Affected sections**: Which specific sections need updating
   - **Impact severity**: High / Medium / Low

5. **Generate report**: Output an impact analysis with recommended update order.

## Output Contract

- **Format**: Markdown impact report
- **Structure**:
  ```markdown
  ## Change Impact Analysis

  ### Change Summary
  <description>

  ### Impact Overview
  | Document | Type | Impact | Severity | Affected Sections |

  ### Dependency Graph
  ```mermaid
  graph TD
  ```

  ### Recommended Update Order
  1. ...

  ### Estimated Effort
  - Documents to update: N
  - Sections affected: N
  - Suggested approach: ...
  ```

## Failure Handling

- No documents found → report empty scan, suggest directory
- Cannot determine document type → skip with warning
- Circular dependencies detected → flag in report

## Safety Boundaries

- Read-only — never modifies documents
- Do not access external URLs
- Report only, no automatic changes

## Examples

### Example 1

**User**: We're changing the auth system from session-based to JWT. What's the impact?

**Expected Output**: Impact report showing PRD (auth requirements), TRD (auth architecture, API design, security section), API docs (auth headers), test specs (auth test cases) are all directly impacted. ADRs may need a new decision record. Recommended order: ADR → PRD → TRD → API → TEST_SPEC.
