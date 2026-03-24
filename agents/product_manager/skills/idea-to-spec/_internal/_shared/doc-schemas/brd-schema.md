# BRD (Business Requirements Document) Schema

> Shared schema referenced by `brd-gen`, `brd-validator`, and `brd-iteration`.

## Required Sections

### 1. Document Metadata

```yaml
title: <project name> — Business Requirements Document
version: <SemVer>
status: Draft | In Review | Approved | Superseded
author: <name>
date: <YYYY-MM-DD>
reviewers: []
```

### 2. Executive Summary

- One-paragraph project overview (max 200 words)
- **Quality**: Must answer *what*, *why*, and *for whom* in a single read.

### 3. Background & Problem Statement

- Current situation and pain points
- Market context or internal driver
- Data/evidence supporting the problem (metrics, user feedback, competitive analysis)
- **Quality**: At least one quantifiable metric or citation.

### 4. Business Objectives

- Numbered list of SMART objectives (Specific, Measurable, Achievable, Relevant, Time-bound)
- Alignment with company strategy / OKRs
- **Quality**: Each objective must include a success metric and target date.

### 5. Stakeholder Analysis

| Stakeholder | Role | Interest | Influence | Communication Plan |
|-------------|------|----------|-----------|-------------------|

- **Quality**: At least 3 stakeholders identified; product owner must be present.

### 6. Scope

#### 6.1 In Scope

- Feature / capability list (bulleted)

#### 6.2 Out of Scope

- Explicitly excluded items with rationale

- **Quality**: Out-of-scope must list at least 2 items to show deliberate boundary-setting.

### 7. Functional Requirements (High-Level)

| ID | Requirement | Priority (P0/P1/P2) | Rationale |
|----|-------------|----------------------|-----------|

- **Quality**: Every P0 requirement must have a rationale.

### 8. Non-Functional Requirements

| Category | Requirement | Target |
|----------|-------------|--------|
| Performance | ... | ... |
| Security | ... | ... |
| Compliance | ... | ... |

### 9. ROI & Cost-Benefit Analysis

- Estimated cost (development, infrastructure, operations)
- Expected benefits (revenue, efficiency, user satisfaction)
- Break-even timeline
- **Quality**: Must include at least a rough order-of-magnitude estimate.

### 10. Risk Assessment

| Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation |
|------|---------------------|-----------------|------------|

- **Quality**: At least 3 risks; each must have a mitigation strategy.

### 11. Timeline & Milestones

| Milestone | Target Date | Dependencies | Owner |
|-----------|-------------|--------------|-------|

- **Quality**: At least 3 milestones with dates.

### 12. Success Criteria

- Quantifiable acceptance criteria for project sign-off
- **Quality**: Each criterion must be measurable.

### 13. Appendix (Optional)

- Glossary, references, supporting data

## Section Completeness Weights

Used by `brd-validator` for scoring:

| Section | Weight |
|---------|--------|
| Executive Summary | 5% |
| Background & Problem | 15% |
| Business Objectives | 15% |
| Stakeholder Analysis | 10% |
| Scope | 10% |
| Functional Requirements | 10% |
| Non-Functional Requirements | 5% |
| ROI & Cost-Benefit | 10% |
| Risk Assessment | 10% |
| Timeline & Milestones | 5% |
| Success Criteria | 5% |
