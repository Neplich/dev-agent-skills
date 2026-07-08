---
name: idea-to-spec
description: "Internal PM specialist—not a direct entry point. Invoked by pm-agent after entry classification to turn confirmed product discovery, empty-workspace app, existing-feature update, or spec-update scope into structured PM/design outputs."
visibility: internal
---

# Idea To Spec

Turns product ideas, empty-workspace app requests, existing-feature changes, or
spec updates into structured PM outputs before downstream work. This entry file
keeps the public protocol and loading rules; detailed lane maps, generators,
validators, iteration flows, schemas, and handoff packet fields live under
`_internal/`.

Always read `_internal/_shared/skill-map.md` before loading any other internal
resource or assembling a handoff packet. Load only the narrowest internal
`INSTRUCTIONS.md` needed for the current next step.

## Non-Negotiable Protocol

1. Read workspace and document context before proposing formal design.
2. Advance one decision point at a time; present `2-3` options with a default
   when trade-offs matter.
3. Record confirmed decisions and write durable PM docs after stable stages.
4. Keep written docs declarative and consolidate them after major stages.
5. Do not recommend downstream generation until scope, users, constraints, and
   current-state understanding are confirmed or explicitly assumed.
6. Prefer delta-oriented iteration over regenerating existing documents.
7. Empty or near-empty product requests stay in PM lanes unless the user
   explicitly says to skip PM and start coding now.
8. Use a fresh document-writing sub-agent for durable docs when available; the
   main process preserves context and reviews quality.

## Operating Modes And Lanes

Choose the conversation mode first: `explore` for vague or unstable scope, or
`fast` when goals, users, scope, constraints, and likely boundaries are already
provided. Fast mode compresses turns but does not skip protocol.

Choose one lane during Phase 0:

| Lane | Use when | Next action |
| --- | --- | --- |
| `greenfield-discovery` | empty workspace, vague idea, or concept validation | stay in `idea-to-spec` |
| `greenfield-bootstrap` | empty workspace and durable docs are needed now | load `_internal/orchestration/project-init/INSTRUCTIONS.md` |
| `existing-project-feature` | existing repo adds a new capability | stay here until requirements or architecture stabilize |
| `existing-project-update` | approved behavior, docs, rollout, or scope must change | load `_internal/analysis/change-impactor/INSTRUCTIONS.md` first when impact is unclear |
| `pipeline` | user explicitly wants the full document workflow | load `_internal/orchestration/flow/INSTRUCTIONS.md` |
| `diff-only` | user only needs revision comparison | load `_internal/analysis/version-differ/INSTRUCTIONS.md` |

If uncertain between new feature and existing update, ask whether this is a
net-new capability or a revision to current docs or implementation.

## When To Use

- User has an idea and wants a concrete PM plan or spec.
- Workspace is empty or near-empty and the user is describing product behavior
  before stack or scope is settled.
- Existing repo needs a new feature anchored in current architecture.
- Existing approved docs or decisions need targeted revision.
- User needs the next best PM step without manually choosing generators,
  validators, or iteration skills.

Do not use this for pure implementation, debugging, code review, tests-only
work, or stack-only bootstrap when the user explicitly wants to skip PM.

## Feature Document Memory

Use `feature_path` as the durable feature key. Before choosing or writing a
feature folder, scan `docs/pm/**/PRD.md`:

- If an existing parent PRD owns the request, attach the new child under that
  parent feature path.
- If parent ownership is unclear, block or ask the smallest clarifying question.
  Do not create a parallel top-level folder for a possible child feature.
- Treat legacy single-level feature folders without `feature_path` frontmatter
  as level-1 features for read compatibility.

Feature-scoped PM docs use `docs/pm/{feature_path}/DECISIONS.md`, `PRD.md`,
`BRD.md`, and temporary `design.md` drafts before formal design docs split out.

New formal PM documents must include `feature_path`, `feature`,
`parent_feature`, and `feature_level` frontmatter.

## Phase 0: Context Detection

Inspect repo markers, stack markers, architecture directories, existing docs,
and `docs/pm/**/PRD.md` metadata. Output a compact context summary covering
directory, project status, detected stack, existing docs, feature path, chosen
lane, and likely next step.

Only perform local read-only inspection in Phase 0 unless the user asked for
file output or document authoring is already underway.

## Requirement Shaping Flow

Use these phases as the public contract; detailed generation instructions live
in `_internal/`: clarify problem, users, success metrics, MVP, non-goals,
constraints, current state, change type, and risks; optionally validate the
bet; shape testable P0/P1 requirements and acceptance criteria; shape just
enough technical trade-off context for `engineer-agent:trd-gen`; then plan
delivery with test, release, rollback, compatibility, and verification notes.

For existing projects, always describe the delta from current behavior,
impacted modules, compatibility/migration constraints, and rollback risk.

## Internal Routing Contract

Use `_internal/_shared/skill-map.md` as the authority for lane selection,
progressive disclosure, PM internal packet fields, cross-role handoff packet
fields, generator/validator/iteration routing, document memory, update policy,
and fallback behavior.

When the next owner is Designer, Engineer, QA, DevOps, Security, delivery, or
another non-PM owner, assemble the cross-role PM handoff packet defined in that
file. If `feature_path` is unresolved, do not hand off as if it were settled;
keep the request in PM clarification or report the blocker.

## Deliverable Shapes

Default durable PM outputs live under `docs/pm/{feature_path}/`. Downstream
docs mirror the same feature path under `docs/design/`, `docs/engineer/`,
`docs/qa/e2e/`, `docs/devops/`, and `docs/security/`.

Before delivery, validate with `_internal/_shared/quality-rules.md` and confirm
that P0 requirements are testable, assumptions are explicit, confirmed
decisions are reflected in `DECISIONS.md`, and existing-project changes include
compatibility, migration, and rollback implications.

## Handoff Behavior

After each phase or when the request is stable enough, recommend the next best
step with the best next skill, why it is next, input to pass forward, expected
output, and one optional alternative when useful.

Always prefer the narrowest useful next skill. Recommend direct iteration before
`flow` for existing-doc updates. If a target agent or skill is unavailable,
name the missing capability, mark the handoff blocked, and do not perform that
downstream role's responsibilities yourself.

## Safety Boundaries

- Do not access external URLs or APIs from this skill unless another explicit
  PM task requires it and repo/user context allows it.
- Do not fabricate business constraints, technical facts, metrics, or policy.
- Do not silently reopen confirmed decisions.
- Do not write code, tests, deployment config, or security fixes.
