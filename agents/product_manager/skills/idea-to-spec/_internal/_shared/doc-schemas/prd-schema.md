# PRD (Product Requirements Document) Schema

> Shared schema referenced by `prd-gen`, `prd-validator`, and `prd-iteration`.
> Extracted and standardized from `idea-to-spec` template.

## Required Sections

### 1. Document Metadata

```yaml
title: <project name> — Product Requirements Document
version: <SemVer>
status: Draft | In Review | Approved | Superseded
author: <name>
date: <YYYY-MM-DD>
reviewers: []
related_brd: <filename or "N/A">
```

### 2. Background & Motivation

- Problem statement with user/business context
- Link to BRD if available
- **Quality**: Must clearly state the *user pain* being addressed.

### 3. Goals & Non-Goals

#### Goals
- Numbered, measurable product goals

#### Non-Goals
- Explicitly excluded from this version

- **Quality**: At least 1 non-goal to show deliberate scoping.

### 4. User Personas

| Persona | Description | Key Needs | Pain Points |
|---------|-------------|-----------|-------------|

- **Quality**: At least 1 persona; each must have needs and pain points.

### 5. User Stories & Scenarios

Format: `As a <persona>, I want to <action> so that <benefit>.`

| ID | User Story | Priority | Acceptance Criteria |
|----|-----------|----------|---------------------|

- **Quality**: Every P0 story must have acceptance criteria.

### 6. Functional Requirements

| ID | Feature | Description | Priority | Acceptance Criteria |
|----|---------|-------------|----------|---------------------|

- **Quality**: Each requirement has a unique ID; P0 items have testable AC.

### 7. Non-Functional Requirements

| Category | Requirement | Metric | Target |
|----------|-------------|--------|--------|
| Performance | Page load time | p95 latency | < 2s |
| Availability | Uptime | monthly | 99.9% |
| Security | Auth | method | OAuth 2.0 |
| Accessibility | WCAG level | compliance | AA |

### 8. User Flows

- Primary flow: step-by-step or Mermaid diagram
- Alternative / error flows
- **Quality**: At least 1 primary flow documented.

### 9. UI/UX Requirements

- Wireframes or layout descriptions
- Interaction patterns
- Responsive / accessibility notes
- **Quality**: At least a text description of key screens.

### 10. Data Model

- Entity list with key attributes
- Relationships (1:1, 1:N, M:N)
- ER diagram (Mermaid) if applicable
- **Quality**: At least entities mentioned; diagram optional.

### 11. API Touchpoints

| Endpoint | Method | Purpose | Request | Response |
|----------|--------|---------|---------|----------|

- **Quality**: List external and internal API dependencies.

### 12. Assumptions & Constraints

| Type | Description | Impact if Wrong |
|------|-------------|-----------------|

### 13. Dependencies

- External: third-party services, APIs
- Internal: other teams, shared components

### 14. Release Plan & Milestones

| Phase | Scope | Target Date | Owner |
|-------|-------|-------------|-------|

### 15. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|

### 16. Open Questions

| # | Question | Owner | Deadline | Resolution |
|---|----------|-------|----------|------------|

### 17. Appendix (Optional)

- Glossary, mockups, research data, competitor analysis

## Section Completeness Weights

| Section | Weight |
|---------|--------|
| Background & Motivation | 10% |
| Goals & Non-Goals | 10% |
| User Personas | 5% |
| User Stories | 15% |
| Functional Requirements | 15% |
| Non-Functional Requirements | 5% |
| User Flows | 10% |
| UI/UX Requirements | 5% |
| Data Model | 5% |
| API Touchpoints | 5% |
| Release Plan | 5% |
| Risks & Mitigations | 5% |
| Open Questions | 5% |
