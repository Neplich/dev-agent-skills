---
name: project-init
description: Initialize a project documentation structure with document stubs. Use when users say "init project", "project setup", "create project docs", "bootstrap project", "scaffold docs", or need to set up the standard directory and document skeleton for a new project.
---

# Project Initializer

Generate a project documentation directory structure with stub documents for
each document type.

This is an internal secondary skill. Expect `idea-to-spec` to load it when an
empty workspace needs durable documentation scaffolding.

## When to use

- Starting a brand new project and need the documentation skeleton
- Setting up standardized doc structure for an existing project
- Onboarding a project to the document management workflow
- Often triggered from `idea-to-spec` Phase 0 when the workspace is empty or
  the user wants a durable docs foundation before detailed generation
- **First step** in a typical project lifecycle, before running gen skills

## Inputs

- **Required**:
  - `project_name`: Name of the project (used in file naming)
- **Optional**:
  - `project_type`: webapp / mobile / api / library / data-pipeline (affects
    which doc types to include)
  - `doc_types`: Override which documents to create -> BRD / PRD / TRD / ADR /
    API / TEST_SPEC (default: all applicable)
  - `description`: Brief project description (pre-populates Background sections)
  - `team`: Team members and roles (pre-populates Stakeholder sections)
  - `handoff_packet`: Phase 0 context from `idea-to-spec` to preserve settled
    scope and naming

## Shared Routing Contract

Read `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` before
finalizing doc types,
schema sources, or recommended next steps.

Use it to:

- stay aligned with the durable-docs branch of `idea-to-spec` Phase 0
- generate stubs from the canonical shared schemas, including
  `test-spec-schema.md`
- keep README workflow guidance aligned with `flow` and the lifecycle matrix

## Workflow

1. **Determine doc set**: Based on `project_type`, select applicable document
   types:
   - webapp / mobile: BRD + PRD + TRD + ADR + API + TEST_SPEC
   - api: PRD + TRD + ADR + API + TEST_SPEC
   - library: TRD + ADR + TEST_SPEC
   - data-pipeline: BRD + TRD + ADR
2. **Create directory structure**:
   ```text
   docs/
   ├─ brd/
   ├─ prd/
   ├─ trd/
   ├─ adr/
   ├─ api/
   ├─ test-specs/
   └─ reports/
   ```
3. **Generate stub documents**:
   - For BRD / PRD / TRD / API / TEST_SPEC, create a stub document with:
     - Complete YAML frontmatter (version `0.1.0`, status `Draft`)
     - All required section headings from the corresponding schema
     - `[TODO]` placeholders for content
     - Pre-populated fields from inputs (project name, description, team)
   - For ADR, create the directory plus an ADR template note or index rather
     than inventing a concrete decision record up front

   Use these canonical schema sources:

   | Doc Type | Shared Schema |
   | --- | --- |
   | BRD | `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/brd-schema.md` |
   | PRD | `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/prd-schema.md` |
   | TRD | `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/trd-schema.md` |
   | ADR | `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/adr-schema.md` |
   | API | `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/api-schema.md` |
   | TEST_SPEC | `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/test-spec-schema.md` |
4. **Create index file**: Generate `docs/README.md` with:
   - Project overview
   - Document inventory table
   - Workflow guide aligned to
     `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`
5. **Present**: Summary of created files and suggested next steps.

## Output Contract

- **Format**: Directory structure with Markdown files
- **Stub quality**: Each stub has valid frontmatter and all required headings
- **Index**: `docs/README.md` with document inventory
- **Next steps**: Recommended skill execution order

## Failure Handling

- Directory already exists -> warn, ask whether to merge or skip existing files
- Invalid project type -> list valid types and ask the user to choose
- No description provided -> create minimal stubs with `[TODO]` throughout

## Safety Boundaries

- Ask before overwriting existing files
- Do not delete any existing content
- Create only in the specified directory (default: `docs/`)

## Examples

### Example 1: Web app project

**User**: Initialize docs for project "smart-checkout", a web app for
e-commerce checkout optimization.

**Expected Output**:

```text
Created project documentation structure:

docs/
├─ README.md                              (Project index)
├─ pm/
│  └─ smart-checkout/
│     ├─ DECISIONS.md                     (decision log stub)
│     ├─ BRD.md                           (BRD stub)
│     └─ PRD.md                           (PRD stub)
├─ engineer/
│  └─ smart-checkout/
│     ├─ TRD.md                           (TRD stub)
│     ├─ API.md                           (API doc stub)
│     └─ ADR-001-initial-architecture.md  (ADR stub)
├─ qa/
│  └─ smart-checkout/
│     └─ TEST_SPEC.md                     (TEST_SPEC stub)
├─ design/
│  └─ smart-checkout/
│     └─ ui-ux-spec.md                    (UI/UX spec stub)
├─ devops/
│  └─ smart-checkout/
│     └─ RELEASE_PLAN.md                  (release plan stub)
└─ security/
   └─ smart-checkout/
      └─ SECURITY_REVIEW.md               (security review stub)

Suggested next steps:
1. Run `brd-gen` to flesh out `docs/pm/smart-checkout/BRD.md`
2. Run `prd-gen` to define `docs/pm/smart-checkout/PRD.md`
3. Update `docs/pm/smart-checkout/DECISIONS.md` as decisions are confirmed
4. Run `trd-gen` and `tspecs-gen` to populate downstream docs
```
