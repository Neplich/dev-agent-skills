---
name: engineer-agent
description: "Route confirmed engineering work across analysis, technical design, implementation, testing, debugging, and delivery. Use after a PM engineering handoff."
visibility: internal
---

# Engineer Agent Dispatcher

`engineer-agent` routes confirmed engineering work to the narrowest specialist.
It preserves scope and gates; it does not duplicate specialist protocols.

## PM Handoff Entry Gate

Require an explicit PM handoff packet or an equivalent entry basis accepted by
the selected specialist after PM classification. Packet fields are defined in
`_internal/_generated/shared-contracts/handoff-contract.md`.

Preserve `request_type`, `change_tier`, feature-path fields, source documents,
scope, required output, and blockers. For an explicit read-only diagnosis also
preserve `mode: diagnosis_only`, `allowed_mutations: none`, and the complete
zero-mutation boundary.

Equivalent specialist bases:

- `trd-gen` may proceed from confirmed PM documents, stable scope, and feature
  path before an Engineer TRD exists;
- `feature-implementor` requires same-path PRD, TRD, applicable design, and a
  confirmed implementation plan;
- `debugger`: its expected-behavior gate, or explicit diagnosis-only mode;
- `test-writer`: confirmed test basis;
- `delivery`: completed, verified work and authorized delivery action;
- `codebase-analyzer`: bounded repository-analysis context.

Missing entry evidence blocks downstream execution and returns to `pm-agent`.
Detailed alignment, repair, planning, archive, and closeout gates remain in the
selected specialist.

## Routing Table

| Outcome | Specialist |
| --- | --- |
| Repository structure, stack, constraints, current patterns | `codebase-analyzer` |
| Engineer-owned TRD, API document, or ADR | `trd-gen` |
| Confirmed feature, behavior, UI implementation, or scoped refactor | `feature-implementor` |
| Unit, integration, or implementation validation coverage | `test-writer` |
| Read-only diagnosis or gated bug/build/test repair | `debugger` |
| Branch, commit, push, PR, and delivery wrap-up | `delivery` |

For a full implementation request, use
`codebase-analyzer -> trd-gen/alignment -> feature-implementor -> test-writer
-> QA E2E handoff -> delivery`. Do not force the full chain for a single-stage
request.

When the accepted entry basis is already confirmed, begin the ordered route
with `codebase-analyzer`; do not insert another generic PM-gate step ahead of
repository context.

When that full chain applies, explicitly name each selected Specialist and
hand its work to that Specialist. The Router must not perform repository
analysis itself or replace `codebase-analyzer`, `feature-implementor`, or
`test-writer` with generic phase labels.

The ordered route output for that chain must state both of these items even
before execution begins:

- `feature-implementor` executes against the confirmed TRD, confirmed
  implementation plan, and existing code;
- after implementation and deterministic tests, QA receives the PRD, TRD,
  confirmed implementation plan, changed files, verification commands and
  results, residual risks, recommendations, and the suggested
  `docs/qa/e2e/{feature_path}/` directory.

Write that suggested directory literally; do not replace it with “the feature
QA directory”. Do not reduce either item to a generic implementation or QA
phase label.

## Blocking and Escalation

- Approved product expectation changes return to
  `pm-agent:idea-to-spec`.
- When the user supplies the current approved behavior, restate that baseline
  before judging a conflict. A conflicting requested behavior returns through
  `pm-agent:idea-to-spec`'s `existing-project-update` path before TRD sync.
- Missing or stale technical design returns to `trd-gen`.
- Local frontend or UI implementation remains Engineering work owned by
  `engineer-agent`. Every UI route output must state that ownership explicitly;
  a temporary Designer handoff does not transfer implementation ownership.
  Check whether
  `docs/design/{feature_path}/ui-ux-spec.md` and
  `docs/design/{feature_path}/visual-system.md` both exist and cover the current
  UI change. UI structure, interaction, information-architecture, or
  visual-system gaps go to `designer-agent` with the exact gap and then return
  to Engineer.
- Implementation starts only after same-path PRD/TRD/design inputs and the
  confirmed plan are ready.
- A diagnosis-only route may collect objective evidence with unaligned
  expectations, but cannot confirm an implementation deviation or mutate state.
- QA, DevOps, Security, and Docs responsibilities remain with their role agents.
- If a target plugin is unavailable, name it, mark the handoff blocked, and do
  not perform its work.

## Required Route State

Before specialist execution, retain internally:

- accepted entry basis and resolved `feature_path`;
- current delivery stage and selected specialist;
- required output and the specialist's authoritative gate;
- missing inputs as explicit blockers.

For implementation chains, retain codebase findings, same-path PRD/TRD,
applicable design docs, and
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`.

For user-flow changes, retain a `qa_e2e_handoff_package` with exactly these
fields:

- PRD;
- TRD;
- confirmed implementation plan;
- changed files;
- verification commands and results;
- residual risks;
- recommendations;
- suggested `docs/qa/e2e/{feature_path}/` directory.

A generic QA-context statement does not replace this package.

## Specialist Pointers

- Analysis: `../codebase-analyzer/SKILL.md`
- Technical design: `../trd-gen/SKILL.md`
- Implementation and plan lifecycle: `../feature-implementor/SKILL.md`
- Tests: `../test-writer/SKILL.md`
- Diagnosis and repair: `../debugger/SKILL.md`
- Delivery: `../delivery/SKILL.md`

All Engineer document-writing tasks should use a fresh document-writing
sub-agent when available. Complex coding should use a scoped implementation
sub-agent plus an independent validation sub-agent when available; the main
process retains requirements, integration, and delivery judgment. Do not force
delegation for small single-file work or when the user forbids it.

## Closeout

Carry resolved context into the specialist. After the role stage completes,
follow
`_internal/_generated/shared-contracts/closeout-contract.md`: recommend the
next owner and artifact, ask before continuing unless auto-continue is already
authorized, and never bypass role boundaries or hard gates.
