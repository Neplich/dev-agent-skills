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
Security, Docs, delivery, or another non-PM owner, use this cross-role packet. This
section is the authoritative PM-side field definition for issue #52.

Required fields:

| Field | Meaning |
| --- | --- |
| `request_type` | Stable request class: `new_feature`, `existing_update`, `bug_report`, `design`, `validation`, `deployment`, `security`, `formal_docs`, `delivery`, `status`, `feature_catalog`, `competitive_research`, `battlecard`, `changelog`, `release_notes`, `roadmap`, or `repo_status`. |
| `change_tier` | `hotfix`, `standard`, or `major`, using the 变更分级契约 in `AGENTS.md` as the single definition source. |
| `feature_path` | Canonical multi-level feature path, `unresolved` when PM clarification must continue, or `N/A` for confirmed non-feature repo-wide work. |
| `feature` | Terminal feature slug, compatible legacy feature value, or `N/A` for confirmed non-feature repo-wide work. |
| `parent_feature` | Parent feature path, `N/A` for level-1 features, or `N/A` for confirmed non-feature repo-wide work. |
| `feature_level` | Positive integer matching the feature path depth, or `N/A` for confirmed non-feature repo-wide work. |
| `feature_path_evidence` | List of `{source, reason}` entries proving why the path is correct, or an empty list for confirmed non-feature repo-wide work. |
| `source_documents` | PRD, DECISIONS, TRD, design docs, issue, PR, release, repo-status, or other evidence used for routing. |
| `scope_decision` | Confirmed scope, non-goals, and whether approved product expectations changed. |
| `downstream_owner` | Next owner: `Designer`, `Engineer`, `QA`, `DevOps`, `Security`, `Docs`, or `delivery`. |
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

Confirmed non-feature repo-wide downstream handoffs may also use `N/A`
feature-scope fields and `feature_path_evidence: []`. Use this only after PM
classification confirms the work is repository-level rather than feature-tied,
for example repository CI, release automation, deployment assets, or delivery
status. Name the repository or release evidence in `source_documents` and do not
use `N/A` to skip feature-path clarification for product feature work.

PM-only specialist routes such as `feature_catalog`, `competitive_research`,
`battlecard`, `changelog`, GitHub-Release `release_notes`, `roadmap`, and `repo_status` do not
require a cross-role handoff packet when they stay inside PM. For non-feature
repository, release, or market context, set feature-scope fields to `N/A`, keep
`feature_path_evidence: []`, and continue with the selected PM specialist
instead of blocking or inventing a feature path.

### Downstream Owner Map

| Routing condition | downstream_owner | Required packet emphasis |
| --- | --- | --- |
| Confirmed UX, UI, information architecture, wireframes, or visual-system work | `Designer` | PM scope, source PRD / BRD, design goal, target users, required design artifact. |
| Confirmed TRD, implementation, debugging, tests, code review, commit, push, PR, or delivery work | `Engineer` or `delivery` | PRD / TRD / implementation-plan source docs, `change_tier`, verification expectations, delivery state. |
| Confirmed acceptance, exploratory, bug analysis, smoke, retest, or regression work | `QA` | Test basis, expected behavior, environment, affected flows, result format. |
| Confirmed deployment, CI/CD, environment, Docker, Helm, release readiness, rollback, or runbook work | `DevOps` | Environment, release target, rollback expectation, operational risk. |
| Confirmed AppSec, auth/authz, dependency, secret, privacy, upload, webhook, or data-flow review | `Security` | Risk surface, assets, permissions, data categories, remediation expectations. |
| Confirmed formal documentation site bootstrap, post-feature / post-deployment / post-release formal-docs synchronization, existing formal-docs backfill, versioned `docs/site/release-notes/` delivery, or release documentation audit | `Docs` | Source feature / deployment / release evidence, formal-docs scope, target site or pages, synchronization, site Release Notes, or audit output; `docs-agent` routes the request to the matching specialist. |
| Inherited-project feature inventory, competitive research, battlecards, changelogs, GitHub Release bodies/operations, roadmaps, or repository status | Named PM specialist | PM-owned route context only: selected specialist, source repository or release context, optional `N/A` feature scope for non-feature work, and any follow-up handoff condition. GitHub Release work routes to `github-release-generator`; site and user-facing version notes route to Docs. |
| New feature, existing update, unclear scope, or expectation change not yet confirmed | PM specialist | Keep the request in PM; do not send a ready handoff packet. |

PRD, TRD, implementation plans, QA reports, and other role-owned process
documents remain with their owning PM, Engineer, or QA role. Route to `Docs`
only for the formal documentation layer maintained through `docs-agent`.

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

## 8. Safety-Net Closeout and Auto-Continue

This is the cross-role public behavior shared by the seven dispatchers (the PM dispatcher plus the six downstream role routers). It
applies after the current role finishes its scoped task, selected specialist
workflow, or blocked handoff report.

- Use the existing Downstream Owner Map and the collaboration chain
  `PM -> Designer -> Engineer -> QA -> DevOps -> Security` to identify the
  most likely next owner. Insert `Docs` when formal documentation work is due:
  after feature implementation, recommend `formal-docs-sync`; before release,
  recommend `docs-audit`. Do not create a
  parallel owner map or new chain.
- At closeout, proactively tell the user what the recommended next step is,
  why that owner is next, and what artifact or action that owner should
  produce.
- Unless the user has already authorized automatic continuation, ask for user
  confirmation before continuing into the next role or skill. One role
  completion normally produces one next-step proposal.
- If the user authorizes auto-continue with wording such as "后面自动继续",
  "auto", or an equivalent instruction, continue through the collaboration
  chain without step-by-step confirmation until the chain ends, a blocker is
  reached, a required target is unavailable, or the user tells the agent to
  stop.
- Role boundaries and role-only gates take precedence over auto-continue.
  Auto-continue never authorizes the current role to execute another role's
  workflow, call that role's specialists, or bypass a hard stop. Across roles,
  auto-continue only automates the next-owner proposal and handoff; the next
  owner agent performs the actual work under its own gates. Roles with hard
  stopping points, such as Designer stopping at design deliverables and handing
  implementation to `engineer-agent`, may auto-continue only up to that handoff
  point.
- If a user directly invokes a downstream role, dispatcher, or specialist but
  the required upstream PM handoff packet, confirmed document chain, or
  specialist entry basis is missing, softly guide the request back through
  `pm-agent` to fill the prerequisite context. This is a safety-net guidance
  path, not a silent refusal and not permission to execute downstream work
  without the missing basis.

### Security Conclusion Escalation to PM

This subsection is the authoritative cross-role rule for when a confirmed
Security conclusion returns to `pm-agent` for entry classification and issue
filing. The escalation is conditional: not every security review returns to
PM.

**Trigger conditions.** Escalate only when a confirmed Security conclusion — a
review finding, or a Security re-review confirming that a remediation has
landed — establishes that at least one of the following has changed:

- formal-documentation facts under `docs/site/`: documented current-state API,
  database, design, ops, or product behavior, for example authentication
  requirements, permission rules, data handling, or endpoint behavior
- externally visible behavior of the system
- operational or deployment facts, for example hardening steps, required
  environment configuration, or rollback behavior
- release readiness

**Non-trigger conditions.** Do not escalate when the security review finds no
issues, when findings and fixes stay internal without changing any of the
trigger categories above (formal-documentation facts, externally visible
behavior, operational or deployment facts, or release readiness), or when the
only outputs are Security-owned process reports under
`docs/security/{feature_path}/`. Those reports remain process documents owned
by Security.

**Escalation action.** Security returns the confirmed conclusion and evidence
to `pm-agent`, which classifies the entry and files the issue. The trigger is
Security's own conclusion; Security does not wait for a separate Engineer or
DevOps return handoff. Security must not hand evidence directly to `docs-agent`,
file the issue itself, or modify formal documentation (`docs/site/` or
documentation owned by other roles). Security-owned process reports under
`docs/security/{feature_path}/` remain required escalation evidence and are not
restricted by this prohibition.

**Evidence payload.** Include the Security report under
`docs/security/{feature_path}/` for feature-scoped work, or repo-wide audit
evidence for repo-wide scope. Also include the affected scope (`feature_path`
values or a repo-wide marker), affected formal document types across api /
database / design / ops / product, a short summary of which fact changed, and
the affected release version when release readiness is impacted. When the
conclusion confirms remediation for an existing tracking issue, the evidence
payload must include the original issue number or link.

**Downstream action.** `pm-agent` classifies the issue with request type
`bug_report`, `formal_docs`, `security`, or `deployment`; release-readiness
impacts map to `deployment`. After the user confirms the entry classification,
`pm-agent` uses `gh issue create` to create the tracking issue and owns its
lifecycle. Remediation is dispatched through the normal cross-role handoff
packet. After remediation lands, route the work back to Security for re-review.
When Security returns the re-review conclusion to PM, PM updates and
closes the original issue rather than creating a duplicate; only a conclusion
without an existing tracking issue creates a new issue. Any Docs work reaches a
documentation specialist only through a PM handoff packet and follows that
specialist's existing gates.

## 9. Phase and Situation Routing

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

## 10. Existing-Project Update Rules

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

## 11. Lifecycle Coverage Matrix

| Document Type | Generator | Validator | Iteration |
| --- | --- | --- | --- |
| BRD | `brd-gen` | `brd-validator` | `brd-iteration` |
| PRD | `prd-gen` | `prd-validator` | `prd-iteration` |
| TRD | `engineer-agent:trd-gen` | `trd-validator` | hand off to `engineer-agent:trd-gen` for revisions |
| API | `engineer-agent:trd-gen` | `api-validator` | hand off to `engineer-agent:trd-gen` for revisions |
| ADR | `engineer-agent:trd-gen` | `adr-validator` | hand off to `engineer-agent:trd-gen` for revisions |
| TEST_SPEC | `tspecs-gen` | `tspecs-validator` | `tspecs-iteration` |

## 12. Shared References

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
