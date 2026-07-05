# Product Manager Internal Routing Map

> Shared routing contract for `idea-to-spec` and the internal instruction
> resources under `_internal/`.
> Load this file first whenever `idea-to-spec` needs to decide lane selection,
> handoff shape, lifecycle routing, or fallback behavior.

## 1. Public Surface and Internal Layout

- `idea-to-spec` is the only public, triggerable design-entry skill in this
  skill group.
- All other capabilities are internal instruction resources and live under:
  - `_internal/analysis/`
  - `_internal/gen/`
  - `_internal/iteration/`
  - `_internal/orchestration/`
  - `_internal/validator/`
- Shared conventions and document schemas live under
  `_internal/_shared/`.
- Default loading rule: keep only `idea-to-spec` in active context, then load
  exactly one internal `INSTRUCTIONS.md` plus the minimum shared references
  needed for the current step.

## 2. Entry Lane Selection

Pick one execution lane during Phase 0. Treat this as the first routing
decision, before deciding which internal instruction resource to load.

| Situation | Lane | Default next action |
| --- | --- | --- |
| Empty workspace, vague concept, early idea validation, or new-repo product request with unsettled scope | `greenfield-discovery` | Stay in `idea-to-spec` |
| Empty workspace and the user wants durable docs now | `greenfield-bootstrap` | Load `project-init` |
| Existing repo, adding a new feature or module | `existing-project-feature` | Stay in `idea-to-spec` until requirements or architecture stabilize |
| Existing repo, changing approved behavior / scope / rollout | `existing-project-update` | Load `change-impactor`, then route to iteration |
| User explicitly wants the full document chain | `pipeline` | Load `flow` |
| User only wants a document diff or comparison | `diff-only` | Load `version-differ` |

## 3. Conversation Protocol Rules

These rules apply before any internal routing:

- Advance one decision point per turn.
- For meaningful product or technical trade-offs, present `2-3` options with
  explicit trade-offs and recommend one default.
- Use section-based progression and do not move to the next section until the
  current one is confirmed or deliberately deferred.
- Record confirmed decisions, open questions, assumptions, and rejected options
  in `docs/pm/{feature_path}/DECISIONS.md` when the conversation is in
  documenting mode.
- Before writing PM feature docs, scan `docs/pm/**/PRD.md` and resolve a
  multi-level `feature_path`. If parent ownership is not clear, block or ask a
  minimal clarification instead of creating a new top-level sibling directory.
- Treat feature docs as durable memory for long-running design threads.
- After a major stage, consolidate process notes into stable declarative prose.

## 4. Progressive Disclosure Rules

- Default to one recommended next skill plus one optional alternative.
- Stay inside `idea-to-spec` while any of these remain unstable:
  - problem statement
  - target users
  - scope and non-goals
  - rollout constraints
  - architecture direction
- For existing-project requests, inspect repo structure and current docs before
  recommending generation or iteration.
- For empty or near-empty workspaces, keep product ideas on the PM path first
  even when the user's verbs sound like "build", "create", or "init".
- For change requests against approved docs, prefer impact analysis and direct
  iteration over regeneration.
- Show the full pipeline only when the user explicitly asks for end-to-end
  coverage or is clearly ready to operationalize multiple formal documents.
- If the user names a downstream capability explicitly, honor the intent but
  still use `idea-to-spec` to frame unresolved assumptions and assemble the
  handoff packet.

## 5. Internal Instruction Resource Registry

Use the narrowest internal instruction resource that matches the lane and
document state.

| Capability | Skill | Internal path | Use when |
| --- | --- | --- | --- |
| Change impact analysis | `change-impactor` | `_internal/analysis/change-impactor/INSTRUCTIONS.md` | A change request may affect one or more existing docs |
| Traceability review | `trace-check` | `_internal/analysis/trace-check/INSTRUCTIONS.md` | Need coverage or mapping review after generation / iteration |
| Version diff | `version-differ` | `_internal/analysis/version-differ/INSTRUCTIONS.md` | Need comparison only, not editing |
| BRD generation | `brd-gen` | `_internal/gen/brd-gen/INSTRUCTIONS.md` | Business case or stakeholder alignment is stable |
| PRD generation | `prd-gen` | `_internal/gen/prd-gen/INSTRUCTIONS.md` | Requirements and flows are stable |
| TRD generation | `engineer-agent:trd-gen` | `agents/engineer/skills/trd-gen/SKILL.md` | PRD and product decisions are stable; explicit Engineer handoff is needed |
| ADR generation | `engineer-agent:trd-gen` | `agents/engineer/skills/trd-gen/SKILL.md` | A technical decision needs durable Engineer-owned rationale |
| API generation | `engineer-agent:trd-gen` | `agents/engineer/skills/trd-gen/SKILL.md` | Interface contracts are stable and ready for Engineer-owned API documentation |
| Test spec generation | `tspecs-gen` | `_internal/gen/tspecs-gen/INSTRUCTIONS.md` | QA assets should be derived from approved requirements or design |
| Workflow execution | `flow` | `_internal/orchestration/flow/INSTRUCTIONS.md` | User wants an end-to-end pipeline |
| Project bootstrap | `project-init` | `_internal/orchestration/project-init/INSTRUCTIONS.md` | Empty workspace needs durable doc scaffolding |
| Multi-doc update | `iteration-coordinator` | `_internal/orchestration/iteration-coordinator/INSTRUCTIONS.md` | Multiple docs must change together |
| Direct doc update | Matching `*-iteration` | `_internal/iteration/.../INSTRUCTIONS.md` | One approved doc needs revision |
| Quality review | Matching `*-validator` | `_internal/validator/.../INSTRUCTIONS.md` | A generated or updated doc needs a score / gap report |

## 6. Internal PM Handoff Packet Contract

When `idea-to-spec` hands work to any internal instruction resource, pass a
compact packet that preserves settled context and avoids re-asking basics.

- `project_context`: repo path, workspace status, tech stack, key modules
- `docs_context`: doc inventory, maturity, missing artifacts, active feature doc
  paths
- `feature_path`: resolved multi-level PM feature path, or `unresolved`
- `feature`: terminal feature slug or compatible legacy feature value
- `parent_feature`: parent feature path, or `N/A` for level 1
- `feature_level`: positive integer matching `feature_path` depth
- `feature_path_evidence`: list of sources proving why this path is correct
- `request_lane`: one of the lane values above
- `problem_and_goal`: problem, target users, success metrics
- `scope`: MVP, non-goals, priorities, rollout constraints
- `current_state`: integrations, permissions, data flows, dependencies
- `change_request`: delta summary for existing-project updates
- `decisions_locked`: agreed decisions that should not be reopened lightly
- `decision_log_path`: path to `docs/pm/{feature_path}/DECISIONS.md` when it
  exists
- `drafted_sections`: sections already produced in this session or in the
  working docs
- `assumptions_and_open_questions`: unresolved items that need confirmation
- `recommended_next_skill`: selected internal capability and reason

Example packet:

```yaml
project_context:
  path: /repo
  status: existing-project
  tech_stack: [nextjs, postgres]
  key_modules: [comments-service, auth-service, notification-center]
docs_context:
  inventory:
    - docs/pm/notifications/PRD.md
    - docs/engineer/notifications/TRD.md
  maturity: approved-core-docs
  missing_artifacts: [docs/pm/notifications/DECISIONS.md]
  active_feature_docs:
    - docs/pm/notifications/PRD.md
feature_path: notifications
feature: notifications
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/notifications/PRD.md
    reason: Existing level-1 feature PRD matches the requested notification center scope
request_lane: existing-project-feature
problem_and_goal:
  problem: Users miss comment mentions.
  target_users: [workspace members]
  success_metrics: ["notification read rate > 70%"]
scope:
  mvp: [in-app notifications, unread badge]
  non_goals: [email digests]
current_state:
  integrations: [comments service, auth service]
  permissions: [workspace member, admin]
change_request:
  summary: Add in-app notifications for mentions and assignments.
decisions_locked:
  - Start with polling, not websockets
decision_log_path: docs/pm/notifications/DECISIONS.md
drafted_sections:
  - current state
  - user flows
  - acceptance criteria
assumptions_and_open_questions:
  - Notification retention window still unconfirmed
recommended_next_skill:
  name: prd-gen
  reason: Requirements are stable and ready for formalization
```

When the next owner is `engineer-agent:trd-gen`, this packet is mandatory. If
`feature_path` is unresolved, do not hand off as if the path were settled; route
back to PM clarification or document the blocker.

If the target agent's plugin for a cross-agent handoff is not installed or
unavailable, state the missing stage and required plugin, mark that handoff
stage as blocked, and do not perform the missing agent's responsibilities
yourself.

## 7. Cross-Role PM Handoff Packet Contract

When `pm-agent` or `idea-to-spec` sends work to Designer, Engineer, QA, DevOps,
Security, delivery, or another non-PM owner, use this cross-role packet. This
section is the authoritative PM-side field definition for issue #52.

Required fields:

| Field | Meaning |
| --- | --- |
| `request_type` | Stable request class: `new_feature`, `existing_update`, `bug_report`, `design`, `validation`, `deployment`, `security`, `delivery`, `status`, `feature_catalog`, `competitive_research`, `battlecard`, `changelog`, `release_notes`, `roadmap`, or `repo_status`. |
| `change_tier` | `hotfix`, `standard`, or `major`, using the 变更分级契约 in `AGENTS.md` as the single definition source. |
| `feature_path` | Canonical multi-level feature path, or `unresolved` when PM clarification must continue. |
| `feature` | Terminal feature slug or compatible legacy feature value. |
| `parent_feature` | Parent feature path, or `N/A` for level-1 features. |
| `feature_level` | Positive integer matching the feature path depth. |
| `feature_path_evidence` | List of `{source, reason}` entries proving why the path is correct. |
| `source_documents` | PRD, DECISIONS, TRD, design docs, issue, PR, release, repo-status, or other evidence used for routing. |
| `scope_decision` | Confirmed scope, non-goals, and whether approved product expectations changed. |
| `downstream_owner` | Next owner: `Designer`, `Engineer`, `QA`, `DevOps`, `Security`, `delivery`, or a named PM specialist when the request stays PM-owned. |
| `required_output` | Concrete artifact or action expected from the next owner: document, plan, implementation, report, verification evidence, delivery action, or status summary. |
| `blockers_risks` | Missing docs, unresolved decisions, unavailable plugins, platform limits, verification risk, or security / privacy risk. |

`feature_path_evidence` must always use this shape:

```yaml
feature_path_evidence:
  - source: docs/pm/order-management/PRD.md
    reason: Existing parent PRD owns checkout and refund flows, and the requested refund change belongs under that product area.
```

Do not inline route / API / page inventory objects into
`feature_path_evidence`; convert them to concise `{source, reason}` entries.
If the path is unresolved, set `feature_path: unresolved`, explain the blocker
in `blockers_risks`, and do not hand off as if the path were settled.

### Downstream Owner Map

| Routing condition | downstream_owner | Required packet emphasis |
| --- | --- | --- |
| Confirmed UX, UI, information architecture, wireframes, or visual-system work | `Designer` | PM scope, source PRD / BRD, design goal, target users, required design artifact. |
| Confirmed TRD, implementation, debugging, tests, code review, commit, push, PR, or delivery work | `Engineer` or `delivery` | PRD / TRD / implementation-plan source docs, `change_tier`, verification expectations, delivery state. |
| Confirmed acceptance, exploratory, bug analysis, smoke, retest, or regression work | `QA` | Test basis, expected behavior, environment, affected flows, result format. |
| Confirmed deployment, CI/CD, environment, Docker, Helm, release readiness, rollback, or runbook work | `DevOps` | Environment, release target, rollback expectation, operational risk. |
| Confirmed AppSec, auth/authz, dependency, secret, privacy, upload, webhook, or data-flow review | `Security` | Risk surface, assets, permissions, data categories, remediation expectations. |
| Inherited-project feature inventory, competitive research, battlecards, changelogs, release notes, roadmaps, or repository status | Named PM specialist | PM-owned route, selected specialist, source repository or release context, and any follow-up handoff condition. |
| New feature, existing update, unclear scope, or expectation change not yet confirmed | PM specialist | Keep the request in PM; do not send a ready handoff packet. |

Example cross-role handoff:

```yaml
request_type: existing_update
change_tier: standard
feature_path: order-management/refunds
feature: refunds
parent_feature: order-management
feature_level: 2
feature_path_evidence:
  - source: docs/pm/order-management/PRD.md
    reason: The existing order-management PRD owns post-purchase refund behavior.
source_documents:
  - docs/pm/order-management/PRD.md
  - docs/pm/order-management/DECISIONS.md
scope_decision:
  summary: Update refund approval copy without changing approval workflow.
  expectation_changed: true
  non_goals: [payment-provider integration changes]
downstream_owner: Engineer
required_output:
  - Update Engineer TRD for the approved copy behavior.
  - Prepare implementation plan after TRD alignment.
blockers_risks:
  - Current TRD does not yet mention refund approval copy.
```

If the target agent or skill is unavailable, state the missing stage, name the
plugin or capability needed, mark the handoff blocked in `blockers_risks`, and
do not perform that downstream role's responsibilities yourself.

## 8. Phase and Situation Routing

| Phase / Situation | Primary internal skill | Alternative / follow-up |
| --- | --- | --- |
| Empty workspace, durable docs needed | `project-init` | Stay in `idea-to-spec` for lightweight validation only |
| Business case, ROI, or stakeholder alignment needed | `brd-gen` | Stay in `idea-to-spec` for a brief validation memo |
| Existing repo, new feature requirements stable | `prd-gen` | `prd-validator` after generation |
| Existing repo, technical design needed after PRD confirmation | `engineer-agent:trd-gen` | Engineer-owned API / ADR docs through `trd-gen`, then matching validators after Engineer TRD confirmation |
| Existing repo, one approved PM doc needs revision | Matching PM `*-iteration` | Matching validator; Engineer-owned TRD/API/ADR revisions hand off to `engineer-agent:trd-gen` |
| Existing repo, multiple docs need coordinated revision | `change-impactor` -> `iteration-coordinator` | `trace-check` and `version-differ` after updates |
| QA assets or regression mapping needed | `tspecs-gen` | `tspecs-validator` or `trace-check` |
| Full end-to-end pipeline requested | `flow` | Narrower gen / validator steps if the user backs off |
| Diff only | `version-differ` | `trace-check` if the issue is coverage rather than versioning |

## 9. Existing-Project Update Rules

- Run `change-impactor` first when the user asks to update an existing feature,
  requirement, rollout policy, or integration and the blast radius is unclear.
- If exactly one core doc is affected, use the matching `*-iteration` skill
  directly instead of `iteration-coordinator`.
- If multiple docs are affected, use this order by default:
  - BRD -> PRD -> TRD -> API -> TEST_SPEC
  - ADR handoffs to `engineer-agent:trd-gen` run in parallel when a decision record is affected
- After multi-doc updates, prefer `trace-check` before closing the loop.
- Regenerate from scratch only when:
  - the target artifact is missing
  - the current artifact is too incomplete to safely iterate
  - the user explicitly prefers regeneration

## 10. Lifecycle Coverage Matrix

| Document Type | Generator | Validator | Iteration |
| --- | --- | --- | --- |
| BRD | `brd-gen` | `brd-validator` | `brd-iteration` |
| PRD | `prd-gen` | `prd-validator` | `prd-iteration` |
| TRD | `engineer-agent:trd-gen` | `trd-validator` | hand off to `engineer-agent:trd-gen` for revisions |
| API | `engineer-agent:trd-gen` | `api-validator` | hand off to `engineer-agent:trd-gen` for revisions |
| ADR | `engineer-agent:trd-gen` | `adr-validator` | hand off to `engineer-agent:trd-gen` for revisions |
| TEST_SPEC | `tspecs-gen` | `tspecs-validator` | `tspecs-iteration` |

## 11. Shared References

- Schema source root:
  `_internal/_shared/doc-schemas/`
- Generator conventions:
  `_internal/_shared/gen-conventions.md`
- Validator conventions:
  `_internal/_shared/validator-conventions.md`
- Quality scoring:
  `_internal/_shared/quality-rules.md`
- Versioning and output rules:
  `_internal/_shared/output-conventions.md`
