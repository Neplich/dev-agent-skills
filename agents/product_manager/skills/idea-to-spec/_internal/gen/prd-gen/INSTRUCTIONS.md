---
name: prd-gen
description: Generate a standardized Product Requirements Document (PRD) from product context. Use when users say "create PRD", "product requirements", "write a PRD", "product spec", or need to define user stories, functional requirements, and acceptance criteria for a feature or product.
---

# PRD Generator

Generate a comprehensive Product Requirements Document following the standardized PRD schema.

## When to use

- Defining product requirements for a new feature or product
- Standardizing an informal spec into a proper PRD
- Converting BRD business objectives into actionable product requirements
- **Differs from** `idea-to-spec`: idea-to-spec is a dialogue-driven flow that shapes requirements and handoff context; prd-gen focuses solely on standardized product requirements
- **Tip**: Use `idea-to-spec` (explore mode) first to shape ideas, then `prd-gen` to formalize into a standalone PRD

## Inputs

- **Required**:
  - `product_description`: What to build (text, BRD, or design doc)
- **Optional**:
  - `target_users`: User personas or audience description
  - `related_brd`: BRD document to extract objectives from
  - `existing_prd`: Previous PRD version to build upon
  - `constraints`: Technical or business constraints

## Conventions

Follow `agents/product_manager/skills/idea-to-spec/_internal/_shared/gen-conventions.md` for standard workflow, failure handling, and safety boundaries.

- **Schema**: `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/prd-schema.md`
- **Metadata**: `type: PRD`, version `1.0.0`, status `Draft`
- **Naming**: `docs/pm/<feature_path>/PRD.md`
- **Feature path gate**: before writing, scan `docs/pm/**/PRD.md`, resolve a
  multi-level `feature_path`, and include `feature_path`, `feature`,
  `parent_feature`, and `feature_level` in frontmatter. If the request may be a
  child feature but parent ownership is unclear, blocked/clarify instead of
  creating a new top-level PRD.

## Workflow Details

Clarifying questions (if input is thin): target users, core problem, must-have features, constraints, timeline.

Generate all sections per schema:
- Background & Motivation
- Goals & Non-Goals
- User Personas (≥ 1)
- User Stories with Acceptance Criteria (P0 stories must have AC)
- Functional Requirements table
- Non-Functional Requirements
- User Flows (≥ 1 primary flow, Mermaid if applicable)
- UI/UX Requirements
- Data Model
- API Touchpoints
- Assumptions & Constraints
- Dependencies
- Release Plan & Milestones
- Risks & Mitigations
- Open Questions

**PRD-specific failure handling**:
- No user persona info → generate reasonable default persona, mark `[ASSUMED]`
- Missing technical context for NFRs → include standard defaults (p95 < 2s, 99.9% uptime) marked `[DEFAULT]`
- Parent feature ambiguity → do not write `docs/pm/<child>/PRD.md`; ask for
  parent confirmation or return a blocked PM path result.

## Examples

### Example 1: User authentication feature

**User**: Generate a PRD for adding social login (Google, GitHub) to our SaaS app. Currently only email/password. Target: increase signup conversion by 30%.

**Expected Output** (abbreviated):

```yaml
---
title: "Social Login — Product Requirements Document"
type: PRD
version: "1.0.0"
status: Draft
author: "Neplich Codex"
date: "2025-01-15"
generated_by: prd-gen
feature_path: social-login
feature: social-login
parent_feature: N/A
feature_level: 1
related_brd: "N/A"
changelog:
  - version: "1.0.0"
    date: "2025-01-15"
    changes: "Initial version"
---
```

**User Personas**:

| Persona | Description | Key Needs | Pain Points |
|---------|-------------|-----------|-------------|
| Busy Developer | Uses GitHub daily, dislikes form-filling | Quick signup | Abandons long registration forms |

**User Stories**:

| ID | User Story | Priority | Acceptance Criteria |
|----|-----------|----------|---------------------|
| US-01 | As a new user, I want to sign up with Google so that I can start in one click | P0 | Given I'm on signup page, When I click "Sign in with Google", Then I'm authenticated and redirected to dashboard within 3s |
