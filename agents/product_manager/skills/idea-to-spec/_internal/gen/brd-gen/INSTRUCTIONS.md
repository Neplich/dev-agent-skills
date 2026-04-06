---
name: brd-gen
description: Generate a Business Requirements Document (BRD) from project context. Use when users say "create BRD", "business requirements", "business case document", "write a BRD", or need to formalize business objectives, stakeholder analysis, and ROI for a project.
---

# BRD Generator

Generate a comprehensive Business Requirements Document following the standardized BRD schema.

## When to use

- Starting a new project and need to articulate business justification
- Translating business goals into a formal requirements document
- Need stakeholder alignment on scope, ROI, and timelines
- **Not** for technical design (use `trd-gen`) or product features (use `prd-gen`)
- **Complements** `idea-to-spec`: BRD focuses on business case; idea-to-spec explores product shape through dialogue

## Inputs

- **Required**:
  - `project_description`: What the project is about (text or existing document)
- **Optional**:
  - `stakeholders`: Known stakeholders and their roles
  - `budget_context`: Budget range or constraints
  - `timeline_context`: Desired timeline or deadlines
  - `existing_docs`: Related documents (market research, competitor analysis)

## Conventions

Follow `agents/product_manager/skills/idea-to-spec/_internal/_shared/gen-conventions.md` for standard workflow, failure handling, and safety boundaries.

- **Schema**: `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/brd-schema.md`
- **Metadata**: `type: BRD`, version `1.0.0`, status `Draft`
- **Naming**: `docs/pm/<feature-name>/BRD.md`

## Workflow Details

Clarifying questions (if input is thin): problem statement, target users, business objectives, known constraints, success criteria.

Generate all required sections per the schema:
- Executive Summary
- Background & Problem Statement (with quantifiable evidence)
- SMART Business Objectives
- Stakeholder Analysis table
- Scope (In/Out)
- High-level Functional Requirements
- Non-Functional Requirements
- ROI & Cost-Benefit Analysis
- Risk Assessment (≥ 3 risks with mitigations)
- Timeline & Milestones (≥ 3 milestones)
- Success Criteria

**BRD-specific failure handling**:
- ROI cannot be estimated → include "ROI: Requires further analysis" with a list of data points needed
- Stakeholders unknown → use generic roles (Product Owner, Engineering Lead, etc.) and mark `[ASSUMED]`

## Examples

### Example 1: E-commerce checkout redesign

**User**: Create a BRD for redesigning our checkout flow. We're losing 40% of users at payment step. Target: reduce cart abandonment by 25% in Q2.

**Expected Output** (abbreviated):

```yaml
---
title: "Checkout Flow Redesign — Business Requirements Document"
type: BRD
version: "1.0.0"
status: Draft
author: "AI Assistant"
date: "2025-01-15"
generated_by: brd-gen
changelog:
  - version: "1.0.0"
    date: "2025-01-15"
    changes: "Initial version"
---
```

**Executive Summary**: The checkout flow redesign project aims to reduce cart abandonment rate from 40% to 15% at the payment step, targeting a 25% overall reduction in Q2 2025...

**Business Objectives**:
1. Reduce payment-step abandonment from 40% to ≤15% by 2025-06-30
2. Increase checkout completion rate by 25% measured via analytics dashboard
...
