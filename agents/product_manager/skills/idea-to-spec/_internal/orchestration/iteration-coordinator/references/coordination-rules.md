# Iteration Coordination Rules

## Document Update Order

When multiple documents need updating, follow this dependency order (upstream first):

```
1. ADR (if a new decision is needed)
2. BRD (business objectives / scope)
3. PRD (product requirements)
4. TRD (technical design)
5. API Documentation
6. Test Specifications
```

## Skill Mapping

| Document Type | Iteration Skill | Validator Skill |
|---------------|----------------|-----------------|
| BRD | brd-iteration | brd-validator |
| PRD | prd-iteration | prd-validator |
| TRD | (manual / trd-gen re-run) | trd-validator |
| ADR | adr-iteration | adr-validator |
| API | (manual / api-gen re-run) | api-validator |
| TEST_SPEC | (re-run tspecs-gen) | N/A |

## Cross-Document Consistency Rules

After all iterations, verify:

1. **BRD ↔ PRD**: All BRD objectives have corresponding PRD features
2. **PRD ↔ TRD**: All PRD requirements mapped to TRD components
3. **TRD ↔ API**: All TRD API designs reflected in API docs
4. **PRD ↔ TEST_SPEC**: All P0 requirements have test cases
5. **ADR ↔ TRD**: All accepted ADRs reflected in TRD architecture

## Version Bump Coordination

When a change cascades through documents:
- The source document gets the highest version bump (often MAJOR or MINOR)
- Downstream documents get at least MINOR bumps
- All changelog entries reference the same change description for traceability
