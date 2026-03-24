# ADR (Architecture Decision Record) Schema

> Shared schema referenced by `adr-gen`, `adr-validator`, and `adr-iteration`.

## Required Sections

### 1. Document Metadata

```yaml
title: "ADR-<NNN>: <Decision Title>"
version: <SemVer>
status: Proposed | Accepted | Deprecated | Superseded
author: <name>
date: <YYYY-MM-DD>
superseded_by: <ADR number or "N/A">
related_docs: []
```

### 2. Title

Format: `ADR-<NNN>: <Short descriptive title>`

- **Quality**: Must be a concise noun phrase describing the decision.

### 3. Status

One of: `Proposed` | `Accepted` | `Deprecated` | `Superseded by ADR-<NNN>`

- **Quality**: Must be a valid status value.

### 4. Context

- What is the issue or situation that motivates this decision?
- What forces are at play (technical, business, organizational)?
- What constraints exist?
- **Quality**: Must describe at least one technical and one business force.

### 5. Decision

- What is the change being proposed or adopted?
- Written in active voice: "We will..."
- **Quality**: Must be a clear, unambiguous statement of what will be done.

### 6. Consequences

#### Positive
- Benefits of this decision

#### Negative
- Drawbacks, trade-offs, or new constraints introduced

#### Neutral
- Side effects that are neither good nor bad

- **Quality**: Must list at least one positive and one negative consequence.

### 7. Alternatives Considered

| Alternative | Pros | Cons | Why Not Chosen |
|-------------|------|------|----------------|

- **Quality**: At least 2 alternatives; each must have pros, cons, and rejection reason.

### 8. References (Optional)

- Links to research, benchmarks, proof-of-concept results, related ADRs

## Section Completeness Weights

| Section | Weight |
|---------|--------|
| Title | 5% |
| Status | 5% |
| Context | 25% |
| Decision | 25% |
| Consequences | 25% |
| Alternatives Considered | 15% |

## Status Transition Rules

Used by `adr-iteration`:

```
Proposed → Accepted      (requires: reviewer approval)
Proposed → Deprecated    (requires: rationale)
Accepted → Deprecated    (requires: rationale)
Accepted → Superseded    (requires: superseded_by ADR number)
Deprecated → (terminal)
Superseded → (terminal)
```
