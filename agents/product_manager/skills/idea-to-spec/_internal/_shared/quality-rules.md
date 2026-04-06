# Quality Rules & Scoring System

> Shared quality framework referenced by all validator and gen skills.

## Scoring Dimensions

### 1. Completeness (权重: 30%)

All required sections present with substantive content.

| Score | Criteria |
|-------|----------|
| 5 | All required sections present and fully populated |
| 4 | All required sections present; 1-2 have minor gaps |
| 3 | 1-2 required sections missing or mostly empty |
| 2 | 3+ required sections missing |
| 1 | Document is a skeleton with minimal content |

### 2. Consistency (权重: 25%)

Terminology, formatting, and cross-references are internally consistent.

| Score | Criteria |
|-------|----------|
| 5 | Uniform terminology; all IDs/refs resolve; no contradictions |
| 4 | Minor terminology inconsistency (1-2 instances) |
| 3 | Noticeable inconsistencies; some broken cross-references |
| 2 | Frequent contradictions or unresolved references |
| 1 | Document sections appear disconnected |

### 3. Clarity (权重: 25%)

Content is unambiguous and understandable by the target audience.

| Score | Criteria |
|-------|----------|
| 5 | Clear, concise; no jargon without definition; actionable |
| 4 | Mostly clear; 1-2 ambiguous statements |
| 3 | Several vague or overly abstract sections |
| 2 | Significant portions unclear or full of undefined jargon |
| 1 | Largely incomprehensible or purely aspirational |

### 4. Testability (权重: 20%)

Requirements and criteria can be objectively verified.

| Score | Criteria |
|-------|----------|
| 5 | All P0 items have measurable acceptance criteria |
| 4 | Most P0 items testable; 1-2 lack clear metrics |
| 3 | Mixed — some testable, some vague ("should be fast") |
| 2 | Most requirements lack measurable criteria |
| 1 | No testable criteria anywhere |

## Overall Score Calculation

```
Overall = Completeness × 0.30 + Consistency × 0.25 + Clarity × 0.25 + Testability × 0.20
```

## Verdict Thresholds

| Overall Score | Status | Meaning |
|---------------|--------|---------|
| ≥ 4.0 | **PASS** | Ready for review/approval |
| 2.5 – 3.9 | **NEEDS_WORK** | Requires revisions before proceeding |
| < 2.5 | **FAIL** | Major rework needed |

## Validation Report Template

```markdown
## Validation Report

- **Document**: <filename>
- **Type**: BRD / PRD / TRD / ADR / API / TEST_SPEC
- **Schema Version**: <version of schema used>
- **Overall Score**: X.X / 5
- **Status**: PASS / NEEDS_WORK / FAIL

### Dimension Scores

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Completeness | X/5 | 30% | X.X |
| Consistency | X/5 | 25% | X.X |
| Clarity | X/5 | 25% | X.X |
| Testability | X/5 | 20% | X.X |

### Section Results

| Section | Status | Score | Issues | Suggestions |
|---------|--------|-------|--------|-------------|
| ... | PASS/WARN/FAIL | X/5 | ... | ... |

### Issue Summary

- **Critical**: N (must fix before approval)
- **Warnings**: N (should fix)
- **Suggestions**: N (nice to have)

### Critical Issues

1. [CRITICAL] ...
2. [CRITICAL] ...

### Warnings

1. [WARNING] ...

### Suggestions

1. [SUGGESTION] ...
```

## Document Length Checks

Validators MUST check document length and flag violations:

| Check | Threshold | Severity | Action |
|-------|-----------|----------|--------|
| Total document lines | > 500 lines | CRITICAL | Must split into multiple documents (L2) or compress sections (L1) |
| Single section without sub-headings | > 80 lines | WARNING | Should split into sub-sections or move details to Appendix |
| Table rows in a single table | > 20 rows | WARNING | Should summarize + move full table to Appendix |
| Supporting docs missing from `related_docs` | When sibling docs exist | CRITICAL | Main document must reference supporting docs via stable paths |

## Issue Severity Definitions

| Severity | Definition | Blocks Approval? |
|----------|-----------|-----------------|
| CRITICAL | Missing required section, broken reference, contradiction, document exceeds 500 lines | Yes |
| WARNING | Incomplete section, vague requirement, missing metric, section exceeds 80 lines | No (but should fix) |
| SUGGESTION | Formatting improvement, additional detail, best practice | No |
