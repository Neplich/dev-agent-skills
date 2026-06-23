---
name: adr-gen
description: Deprecated PM-owned ADR generator. Do not generate ADRs from PM; route ADR requests to engineer-agent:trd-gen.
---

# ADR Handoff

This internal PM resource is retained only as a migration stub for older
references. Architecture Decision Records are Engineer-owned and must be
handled by `engineer-agent:trd-gen`.

## When to use

- Only when a legacy PM flow or stale reference points at `adr-gen`
- Only to stop PM-side ADR generation and prepare an Engineer handoff packet
- Do not create, update, renumber, accept, deprecate, or supersede ADR files
  from this PM resource

## Required handoff

Route ADR requests to `engineer-agent:trd-gen` with:

- confirmed `feature_path`, `feature`, `parent_feature`, and `feature_level`
- source PRD and decision context
- the technical decision to record or revise
- known alternatives, constraints, and trade-offs
- business forces PM has confirmed
- open questions or blockers that Engineer must resolve

## Output contract

Return a handoff packet only. The target Engineer output path is
`docs/engineer/{feature_path}/ADR-<NNN>-<decision-title>.md`, but this PM
resource must not write it.

If `feature_path` is unresolved or PM scope is not confirmed, return to
`idea-to-spec` path and scope clarification before handing off to Engineer.
