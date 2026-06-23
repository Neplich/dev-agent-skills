---
name: api-gen
description: Deprecated PM-owned API generator. Do not use for new generation; route API documentation requests to engineer-agent:trd-gen.
---

# API Documentation Generator

Deprecated PM-owned generator retained for historical reference. New API
documentation belongs to Engineer and must be routed to `engineer-agent:trd-gen`
with the confirmed PM scope, feature path, interface goals, constraints, and
available code or OpenAPI evidence.

## When to use

- Need to document an existing API from code or route definitions
- Designing a new API and need structured documentation
- Converting informal API notes into proper documentation
- **Deprecated**: do not trigger this PM generator for new API documents. Use
  `engineer-agent:trd-gen` so API docs are produced with the TRD and feature
  path contract.

## Inputs

- **Required**:
  - `api_source`: One of:
    - Code files (route definitions, controllers)
    - Verbal description of endpoints
    - OpenAPI/Swagger spec to enhance
    - Existing informal API notes
- **Optional**:
  - `base_url`: API base URL
  - `auth_method`: Authentication approach
  - `service_name`: Name of the service
  - `existing_models`: Data model definitions

## Conventions

Follow `agents/product_manager/skills/idea-to-spec/_internal/_shared/gen-conventions.md` for standard workflow, failure handling, and safety boundaries.

- **Schema**: `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/api-schema.md`
- **Metadata**: `type: API`, version `1.0.0`
- **Naming**: `docs/engineer/{feature_path}/API.md`

## Workflow Details

Parse source input to extract endpoints, methods, parameters, request/response schemas, and error codes.

Generate API docs:
- Overview with base URL and versioning
- Authentication section with example headers
- Common headers table
- For each endpoint: method + path, summary, auth requirement, rate limit, path/query parameters, request body schema, response schemas (success + errors)
- Data models with field definitions
- Error code reference table
- Pagination and rate limiting (if applicable)
- At least 1 complete curl example

**Quality requirements**: Every endpoint has method, path, at least one response, and error codes.

**API-specific failure handling**:
- Incomplete code input → document what's found, mark gaps as `[INCOMPLETE]`
- No auth info → include placeholder section with common auth patterns
- Ambiguous parameter types → infer from context, mark `[INFERRED]`
- Do not expose internal implementation details (internal IPs, credentials)
- Do not fabricate endpoints not present in source material
- Sanitize any real data in examples

## Examples

### Example 1: From route definitions

**User**: Document the API for this Express router:
```js
router.get('/users', authMiddleware, listUsers);
router.get('/users/:id', authMiddleware, getUser);
router.post('/users', authMiddleware, createUser);
router.put('/users/:id', authMiddleware, updateUser);
router.delete('/users/:id', authMiddleware, deleteUser);
```

**Expected Output**: Full API documentation with 5 endpoints, Bearer auth, request/response schemas inferred from handler names, standard CRUD error codes, and a curl example for creating a user.
