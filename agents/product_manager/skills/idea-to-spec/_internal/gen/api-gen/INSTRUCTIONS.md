---
name: api-gen
description: Deprecated PM-owned API generator. Do not generate API docs from PM; route API documentation requests to engineer-agent:trd-gen.
---

# API Documentation Handoff

This internal PM resource is retained only as a migration stub for older
references. API documentation is Engineer-owned and must be handled by
`engineer-agent:trd-gen`.

## When to use

- Only when a legacy PM flow or stale reference points at `api-gen`
- Only to stop PM-side API generation and prepare an Engineer handoff packet
- Do not create, update, or scaffold `API.md` from this PM resource

## Required handoff

Route API documentation requests to `engineer-agent:trd-gen` with:

- confirmed `feature_path`, `feature`, `parent_feature`, and `feature_level`
- source PRD and decision context
- interface goals, constraints, and non-goals
- available code, route definitions, or OpenAPI evidence
- known auth, data model, error handling, and versioning requirements
- open questions or blockers that Engineer must resolve

## Output contract

Return a handoff packet only. The target Engineer output path is
`docs/engineer/{feature_path}/API.md`, but this PM resource must not write it.

If `feature_path` is unresolved or PM scope is not confirmed, return to
`idea-to-spec` path and scope clarification before handing off to Engineer.
