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
- **Not** for technical design (use `engineer-agent:trd-gen`) or product features (use `prd-gen`)
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

Follow `_internal/_shared/gen-conventions.md` for standard workflow, failure handling, and safety boundaries.

- **Schema**: `_internal/_shared/doc-schemas/brd-schema.md`
- **Metadata**: `type: BRD`, version `1.0.0`, status `Draft`
- **Naming**: `docs/pm/<feature_path>/BRD.md`
- **Feature path gate**: use the same resolved `feature_path` as the related
  PRD or PM handoff. If no related PRD exists yet, scan `docs/pm/**/PRD.md`
  before choosing the BRD folder. Parent ambiguity blocks generation.

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
- Parent feature ambiguity → ask for confirmation or return blocked; do not
  create a new parallel top-level PM folder for a likely child feature.

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
author: "Neplich Codex"
date: "2025-01-15"
generated_by: brd-gen
feature_path: checkout-flow
feature: checkout-flow
parent_feature: N/A
feature_level: 1
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
