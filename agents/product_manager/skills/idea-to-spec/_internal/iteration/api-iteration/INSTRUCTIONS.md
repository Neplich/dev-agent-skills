---
name: api-iteration
description: Deprecated PM-owned API iteration resource. Do not update API docs from PM; route API revision requests to engineer-agent:trd-gen.
---

# API Iteration Handoff

API documentation is Engineer-owned. This internal PM instruction only analyzes
why an API document must change and hands the request to
`engineer-agent:trd-gen`.

## When to use

- A legacy PM route points at `api-iteration`
- `api-validator` or review feedback indicates an API document should change
- Endpoint contracts, auth, errors, or data models changed and need Engineer
  documentation work
- Do not edit `API.md` directly from PM

## Inputs

- `api_document`: existing API document path or summary, when available
- `change_request`: validator report, review comments, code diff, route change,
  or endpoint change list
- `related_prd`: source PRD or PM decision context
- `feature_path` metadata and evidence

## Workflow

1. Read the current API context and the requested change.
2. Classify the change: validation fix, non-breaking contract update, breaking
   contract update, endpoint addition, deprecation, or removal.
3. Identify PM-side requirement or decision impacts.
4. Prepare a handoff packet for `engineer-agent:trd-gen`.
5. Do not modify `API.md`; Engineer owns the revision and versioning.

## Output contract

Return an Engineer handoff packet with affected endpoints, source evidence,
compatibility risks, related PRD / DECISIONS impact, and unresolved questions.
