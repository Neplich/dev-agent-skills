---
name: adr-iteration
description: Deprecated PM-owned ADR iteration resource. Do not update ADR files from PM; route ADR revision requests to engineer-agent:trd-gen.
---

# ADR Iteration Handoff

ADRs are Engineer-owned. This internal PM instruction only analyzes why an ADR
must change and hands the request to `engineer-agent:trd-gen`.

## When to use

- A legacy PM route points at `adr-iteration`
- `adr-validator` or review feedback indicates an ADR should change
- An ADR status, supersession, or content update needs Engineer ownership
- Do not edit, accept, deprecate, supersede, or renumber ADR files from PM

## Inputs

- `adr_document`: existing ADR path or summary, when available
- `change_request`: validator report, review comments, architecture decision,
  status transition request, or supersession context
- `related_prd`: source PRD or PM decision context
- `feature_path` metadata and evidence

## Workflow

1. Read the current ADR context and requested transition or content change.
2. Check whether PM scope or product decisions are impacted.
3. Prepare a handoff packet for `engineer-agent:trd-gen` with the requested
   status or content change and supporting evidence.
4. Do not modify ADR files; Engineer owns the revision, numbering, status, and
   changelog.

## Output contract

Return an Engineer handoff packet with decision context, requested transition,
alternatives or constraints, related PM evidence, and unresolved questions.
