---
name: trd-gen
description: Generate a Technical Requirements Document (TRD) from a PRD or technical context. Use when users say "create TRD", "technical design", "tech spec", "architecture document", "system design doc", or need to define architecture, data models, API contracts, and deployment plans.
---

# TRD Generator

Generate a comprehensive Technical Requirements Document following the standardized TRD schema.

## When to use

- Translating product requirements (PRD) into a technical design
- Documenting architecture decisions, data models, and API contracts
- Need a technical blueprint before implementation
- **Differs from** `idea-to-spec`: idea-to-spec produces PRD+TRD combined through dialogue; trd-gen focuses solely on the technical layer
- **Complements** `prd-gen`: Use prd-gen first for requirements, then trd-gen for technical design

## Inputs

- **Required**:
  - `technical_context`: What to design (PRD, feature description, or system description)
- **Optional**:
  - `related_prd`: PRD document to derive requirements from
  - `tech_stack`: Preferred or existing technology stack
  - `constraints`: Performance targets, infrastructure constraints
  - `existing_architecture`: Current system architecture description

## Conventions

Follow `skills/product-dev/idea-to-spec/_internal/_shared/gen-conventions.md` for standard workflow, failure handling, and safety boundaries.

- **Schema**: `skills/product-dev/idea-to-spec/_internal/_shared/doc-schemas/trd-schema.md`
- **Metadata**: `type: TRD`, version `1.0.0`, status `Draft`
- **Naming**: `trd-<system-name>-v1.0.0.md`

## Workflow Details

Clarifying questions (if no PRD provided): system purpose, scale requirements, integration points, tech preferences, deployment environment.

Generate all sections:
- Overview (linked to PRD)
- Architecture Overview with Mermaid C4/flowchart diagram
- Technology Stack table with rationale
- Data Model with ER diagram (Mermaid)
- API Design (all endpoints from PRD)
- System Interactions with sequence diagrams
- NFR table with quantified targets
- Security Design (auth, encryption, threats)
- Deployment Architecture
- Monitoring & Observability
- Testing Strategy table
- Risks & Technical Debt
- Open Technical Questions

**Quality requirements**: At least 1 architecture diagram + 1 sequence diagram (Mermaid). All NFRs must have numeric targets.

**TRD-specific failure handling**:
- Unknown tech stack → propose standard stack with rationale, mark `[PROPOSED]`
- Cannot estimate NFR targets → use industry defaults marked `[DEFAULT]`
- Architecture too complex → split recommendation + skeleton for each component
- Do not recommend specific commercial products without stating alternatives

## Examples

### Example 1: Payment microservice

**User**: Create a TRD for a payment processing microservice. We use Node.js, PostgreSQL, deployed on AWS. Must handle 500 TPS with p99 < 500ms.

**Expected Output** (abbreviated):

Architecture Overview with C4 diagram showing Payment Service, Database, Payment Gateway, and Event Bus. Technology stack: Node.js 20 + Fastify, PostgreSQL 16, Redis for caching, SQS for events. Data model with ER diagram for transactions, payment_methods, and audit_log tables. API endpoints for POST /payments, GET /payments/:id, POST /payments/:id/refund. NFR table with 500 TPS throughput, p99 < 500ms latency, 99.95% availability targets.
