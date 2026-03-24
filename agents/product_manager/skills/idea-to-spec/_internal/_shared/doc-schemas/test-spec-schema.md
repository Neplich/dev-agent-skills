# TEST_SPEC (Test Specification) Schema

> Shared schema referenced by `tspecs-gen`, `tspecs-validator`, and
> `tspecs-iteration`.

## Required Sections

### 1. Document Metadata

```yaml
title: <project or feature name> - Test Specification
version: <SemVer>
status: Draft | In Review | Approved | Superseded
author: <name>
date: <YYYY-MM-DD>
related_prd: <filename or "N/A">
related_trd: <filename or "N/A">
related_api: <filename or "N/A">
```

### 2. Test Scope & Objectives

- Feature / release under test
- What this suite is intended to prove
- Explicit out-of-scope items
- **Quality**: Must state both scope and out-of-scope boundaries.

### 3. Test Strategy Summary

| Test Level | Goal | In Scope | Out of Scope |
| --- | --- | --- | --- |
| Unit | ... | ... | ... |
| Integration | ... | ... | ... |
| E2E | ... | ... | ... |

- **Quality**: At least one test level must be defined.

### 4. Coverage Summary

| Requirement ID | Requirement Summary | Priority | Covered By | Coverage Status |
| --- | --- | --- | --- | --- |

- **Quality**: Every P0 requirement must map to at least one planned test case.

### 5. Test Environment & Data

- Environments used (local / staging / prod-like)
- Required accounts, roles, fixtures, or seed data
- Reset / cleanup expectations
- **Quality**: Must describe where the suite runs and what data it depends on.

### 6. Test Cases

Each test case must capture:

| Field | Description |
| --- | --- |
| ID | Stable test case ID such as `TC-001` |
| Title | Short scenario title |
| Requirement Links | Requirement IDs or endpoint references |
| Priority | P0 / P1 / P2 |
| Level | Unit / Integration / E2E / Regression / Performance |
| Category | Positive / Negative / Boundary / Security / Reliability |
| Preconditions | Required starting state |
| Steps | Ordered execution steps |
| Expected Result | Observable pass condition |
| Notes | Test data, automation hint, or dependency |

- **Quality**: Each test case must have Preconditions, Steps, and Expected
  Result.

### 7. Non-Functional & Operational Tests

| Category | Scenario | Target / Threshold | Method |
| --- | --- | --- | --- |
| Performance | ... | ... | ... |
| Security | ... | ... | ... |
| Reliability | ... | ... | ... |

- **Quality**: If PRD/TRD includes quantified NFRs, this section must cover how
  they will be tested.

### 8. Regression & Smoke Pack

- Smoke tests required for release
- Regression buckets by feature area
- Deferred tests and why they are deferred

### 9. Traceability Matrix

| Source Item | Test Cases | Gaps / Notes |
| --- | --- | --- |

- **Quality**: Must reconcile coverage gaps explicitly instead of leaving them
  implicit.

### 10. Risks, Gaps & Assumptions

| Type | Description | Impact | Mitigation / Follow-up |
| --- | --- | --- | --- |

### 11. Exit Criteria & Reporting

- Pass/fail bar for the suite
- Required reports or dashboards
- Defect severity thresholds for sign-off

### 12. Appendix (Optional)

- Example payloads, seed data, reusable fixtures, links to automation assets

## Section Completeness Weights

| Section | Weight |
| --- | --- |
| Test Scope & Objectives | 10% |
| Test Strategy Summary | 10% |
| Coverage Summary | 20% |
| Test Environment & Data | 10% |
| Test Cases | 25% |
| Non-Functional & Operational Tests | 10% |
| Regression & Smoke Pack | 5% |
| Traceability Matrix | 5% |
| Risks, Gaps & Assumptions | 3% |
| Exit Criteria & Reporting | 2% |
