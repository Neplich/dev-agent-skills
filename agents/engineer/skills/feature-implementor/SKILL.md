---
name: feature-implementor
description: "Internal engineering specialist—not a direct entry point. Invoked by engineer-agent after pm-agent handoff to implement confirmed TRDs and PM/design inputs through a verified implementation plan."
visibility: internal
---

# Feature Implementor

Implements confirmed Engineer TRDs through a durable
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`, then verifies and closes
out the plan. This entry file owns the gates that must run immediately when the
skill is triggered; execution details live in `_internal/`.

Before plan confirmation, load only `_internal/planner/INSTRUCTIONS.md` plus
`_internal/_shared/coding-rules.md`. After the user confirms the exact plan,
load `_internal/implementor/INSTRUCTIONS.md`. For self-review and closeout,
load `_internal/reviewer/INSTRUCTIONS.md` and
`_internal/_shared/output-conventions.md`.

## PM Handoff Entry Gate

Do not execute implementation, write code, or create a plan unless the request
has an explicit PM handoff packet for Engineer / delivery-adjacent Engineer
work, or an equivalent confirmed document chain:
`docs/pm/{feature_path}/PRD.md`,
`docs/engineer/{feature_path}/TRD.md`, and a current implementation-scope
decision.

The PM-side packet field definition lives in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
If the user directly asks this skill to "implement", "build", "change a
feature", or "do the code" without PM handoff or equivalent confirmed docs,
stop and return the request to `pm-agent` for classification. Direct invocation
does not bypass this gate.

## When To Use

- Implement a feature or behavior change already covered by confirmed PM scope
  and Engineer TRD.
- Turn a confirmed TRD into an implementation plan, code changes, tests, and
  verification evidence.
- Implement spec-backed bug fixes only after Engineer/debugger routing confirms
  the fix is implementation work against approved PRD/TRD behavior.

Do not use this skill for:

- greenfield product ideas or raw feature requests without PM scope
- behavior changes that need PRD or product decision updates first
- missing, stale, or mismatched TRDs
- bug investigation before expected behavior is aligned
- tests-only or delivery-only work

## PRD And TRD Alignment Gate

Before writing or updating `IMPLEMENTATION_PLAN.md`, resolve the canonical
`feature_path` and read `docs/pm/{feature_path}/PRD.md`,
`docs/engineer/{feature_path}/TRD.md`, and
`docs/pm/{feature_path}/DECISIONS.md` or equivalent product decisions when
present.

Proceed only when the PRD exists, the TRD exists, their `feature_path`,
`parent_feature`, and `feature_level` metadata match, and the TRD `related_prd`
points to `docs/pm/{feature_path}/PRD.md`. Legacy single-level PM docs without
feature-path metadata may be read as level-1 features, but new or changed plans
must write explicit feature-path metadata.

Classify before planning: approved scope proceeds; expectation changes return
to `pm-agent:idea-to-spec` using `existing-project-update`; missing PRD or
decisions return to PM; stale, incomplete, path-mismatched, or conflicting TRDs
return to `engineer-agent:trd-gen`; requests to skip alignment are blockers or
risks, not implementation permission.

The TRD gap packet must name the missing technical decisions, affected
components, data/API/integration impacts, validation commands, rollout risks,
and the boundary: the finder only clarifies gaps; `trd-gen` completes the TRD.

## UI Design Handoff Gate

For frontend UI, interaction, visual, component, usability, or information
hierarchy changes, check `docs/design/{feature_path}/ui-ux-spec.md` and
`docs/design/{feature_path}/visual-system.md`.

Cite existing design docs when they cover the change. If the change is narrow
enough not to require Designer updates, state why in the implementation plan.
If design inputs are missing, stale, or conflicting, stop before planning and
hand the gap through `engineer-agent` to `designer-agent`.

## Plan And Archive Gate

`docs/engineer/{feature_path}/TRD.md` is the technical input contract.
`IMPLEMENTATION_PLAN.md` maps that TRD to concrete files, sequence, delegation,
verification, and closeout. It must not rewrite PM scope or TRD decisions.

Before creating or replacing an active plan, scan
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` and its
`implementation-plans/archive/` directory.

If an active plan exists and no handling decision is recorded, ask the user to
choose exactly one: archive completed plan then create new active plan,
continue updating the current plan with a version bump, or archive the old plan
as `Superseded` with a reason then create a new active plan.

Plan form strength follows `change_tier` from the PM handoff or `AGENTS.md`.
`hotfix` may use the lightweight plan form allowed by the repository contract;
`standard` and `major` keep the full plan confirmation flow. Tiering never
waives PRD/TRD alignment or evidence.

Archival happens only after closeout and user/maintainer approval. Archive
paths must use
`docs/engineer/{feature_path}/implementation-plans/archive/IMPLEMENTATION_PLAN-<scope>.md`.
The active plan path remains fixed at
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`.

## Implementation Flow

1. Gather PRD, DECISIONS, TRD, relevant design docs, repo structure, and active
   plan/archive state.
2. Write or update the plan with file list, order, verification, alignment
   result, feature metadata, and sub-agent split decision.
3. Present the exact plan and wait for user confirmation.
4. Implement only the confirmed scope, reading each file before editing.
5. Verify with deterministic commands.
6. Self-review against PRD/TRD/design docs, repo rules, security basics, and
   unrelated-change safety.
7. Update closeout before delivery.

For complex multi-file or spec-heavy work, use separate implementation and
validation sub-agents when available. Do not use that split for small edits or
when the user opts out; the plan gate still applies.

## Closeout And QA Handoff

After implementation and deterministic checks, update or confirm closeout.
Closeout records final status, changed files, commands run or skipped, skill /
fresh subagent eval status when applicable, residual risks, and next owner.

If frontmatter says `status: "Implemented"`, the body must not keep unresolved
planning wording such as "waiting for confirmation", "not started", or
"pending execution" except as clearly historical context with a resolved result.
Runtime eval artifacts must not be committed.

When user-facing flows, acceptance paths, permissions, login, data setup, or
regression coverage may be affected, produce a QA E2E handoff package. Do not
create QA E2E cases unless explicitly routed to QA work.

## Key Principles

- Read before write.
- Keep changes scoped to the confirmed plan.
- Prefer existing project conventions over new abstractions.
- Every implementation decision traces to PM/TRD/design docs.
- Do not perform missing PM, Designer, QA, DevOps, or Security responsibilities.
