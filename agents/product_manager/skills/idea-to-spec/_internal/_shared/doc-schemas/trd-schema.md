# TRD (Technical Requirements Document) Schema

> Shared schema referenced by `trd-gen`, `trd-validator`.

## Required Sections

### 1. Document Metadata

```yaml
title: <project name> — Technical Requirements Document
version: <SemVer>
status: Draft | In Review | Approved | Superseded
author: <name>
date: <YYYY-MM-DD>
related_prd: <filename or "N/A">
```

### 2. Overview

- Technical summary of the solution (max 300 words)
- Link to PRD for business context
- **Quality**: Must reference the PRD or business requirement driving this design.

### 3. Architecture Overview

- High-level architecture diagram (Mermaid C4 or flowchart)
- Component list with responsibilities
- **Quality**: Must include at least one diagram and a component table.

### 4. Technology Stack

| Layer | Technology | Version | Rationale |
|-------|-----------|---------|-----------|
| Frontend | ... | ... | ... |
| Backend | ... | ... | ... |
| Database | ... | ... | ... |
| Infrastructure | ... | ... | ... |

- **Quality**: Each choice must have a rationale.

### 5. Data Model

- Entity-Relationship diagram (Mermaid ER)
- Table/collection definitions with field types
- Index strategy
- Data migration plan (if applicable)
- **Quality**: At least ER diagram + key entity definitions.

### 6. API Design

| Endpoint | Method | Auth | Request Schema | Response Schema | Error Codes |
|----------|--------|------|---------------|-----------------|-------------|

- Versioning strategy
- Rate limiting policy
- **Quality**: All endpoints from PRD must be covered.

### 7. System Interactions

- Sequence diagrams for key flows (Mermaid)
- External service integration details
- Event/message contracts (if event-driven)
- **Quality**: At least 1 sequence diagram for the primary flow.

### 8. Non-Functional Requirements (Quantified)

| Category | Metric | Target | Measurement Method |
|----------|--------|--------|--------------------|
| Latency | p95 response time | < 200ms | APM dashboard |
| Throughput | RPS | 1000 | Load test |
| Availability | Uptime | 99.9% | Monitoring |
| Storage | Growth rate | 10GB/month | DB metrics |

- **Quality**: Targets must be numeric and measurable.

### 9. Security Design

- Authentication & authorization model
- Data encryption (at rest / in transit)
- Input validation strategy
- Threat model (STRIDE or equivalent)
- **Quality**: Must address auth, encryption, and at least one threat.

### 10. Deployment Architecture

- Environment topology (dev/staging/prod)
- CI/CD pipeline overview
- Rollback strategy
- Infrastructure as Code references
- **Quality**: Must describe at least prod deployment and rollback.

### 11. Monitoring & Observability

- Logging strategy (structured logs, log levels)
- Metrics & dashboards
- Alerting rules
- Distributed tracing

### 12. Testing Strategy

| Level | Scope | Tool | Coverage Target |
|-------|-------|------|-----------------|
| Unit | Business logic | Jest/pytest | > 80% |
| Integration | API contracts | Supertest | All endpoints |
| E2E | Critical paths | Playwright | Top 5 flows |
| Performance | Load/stress | k6 | NFR targets |

### 13. Risks & Technical Debt

| Risk/Debt | Impact | Mitigation | Timeline |
|-----------|--------|------------|----------|

### 14. Open Technical Questions

| # | Question | Owner | Deadline |
|---|----------|-------|----------|

### 15. Appendix (Optional)

- Glossary, ADR references, spike findings

## Section Completeness Weights

| Section | Weight |
|---------|--------|
| Overview | 5% |
| Architecture Overview | 15% |
| Technology Stack | 10% |
| Data Model | 10% |
| API Design | 15% |
| System Interactions | 10% |
| NFR (Quantified) | 10% |
| Security Design | 10% |
| Deployment Architecture | 5% |
| Testing Strategy | 5% |
| Risks & Technical Debt | 5% |
