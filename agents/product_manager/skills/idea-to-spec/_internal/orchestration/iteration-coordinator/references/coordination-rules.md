# Iteration Coordination Rules

## Document Update Order

When multiple documents need updating, follow this dependency order (upstream first):

```
1. ADR (if a new decision is needed)
2. PRD (product requirements)
3. TRD (technical design)
4. API Documentation (Engineer-owned)
5. Test Specifications
```

## Skill Mapping

| Document Type | Iteration Skill | Validator Skill |
|---------------|----------------|-----------------|
| PRD | prd-iteration | prd-validator |
| TRD | hand off to engineer-agent:trd-gen | trd-validator |
| ADR | hand off to engineer-agent:trd-gen | adr-validator |
| API | hand off to engineer-agent:trd-gen | api-validator |
| TEST_SPEC | (re-run tspecs-gen) | N/A |

## Cross-Document Consistency Rules

After all iterations, verify:

1. **PRD ↔ TRD**: All PRD requirements mapped to TRD components
2. **TRD ↔ API**: All TRD API designs reflected in API docs
3. **PRD ↔ TEST_SPEC**: All P0 requirements have test cases
4. **ADR ↔ TRD**: All accepted ADRs reflected in TRD architecture

## Version Bump Coordination

When a change cascades through documents:
- The source document gets the highest version bump (often MAJOR or MINOR)
- Downstream documents get at least MINOR bumps
- All changelog entries reference the same change description for traceability
