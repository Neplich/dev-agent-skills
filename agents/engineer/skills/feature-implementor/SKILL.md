---
name: feature-implementor
description: "Plan, implement, and verify a scoped change from confirmed PRD/TRD/design inputs after plan approval. Use after engineer-agent routes implementation work."
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

## Mandatory Planning Checkpoint

Before code or test changes, produce one observable checkpoint that:

1. when `docs/site/standards/change-map.yaml` exists, resolves the task's code
   path through that map before reading any mapped formal document or beginning
   broader repository exploration; records the matched code glob and mapped
   documents, then verifies every material planning claim against code or tests
2. resolves the canonical nested `feature_path` and records PRD, decisions,
   TRD, `related_prd`, design, and code-evidence alignment
3. returns a missing or changed PRD to `pm-agent:idea-to-spec`, a missing or
   incomplete TRD to `engineer-agent:trd-gen`, and UI design gaps to
   `designer-agent`; the finder
   names the gap but never performs the receiving role's work
4. scans the fixed active-plan path and archive directory before writing,
   explicitly names both paths, states that the active entry remains fixed and
   archives belong only in that archive directory, and
   records the original active-plan status and `implementation_scope` verbatim
   before any archive or replacement write;
   handles `Implemented`, draft/non-implemented, faithful archive, abandoned,
   and no-active-plan states exactly as the archive gate specifies
5. writes or updates `IMPLEMENTATION_PLAN.md` with current frontmatter version,
   status, alignment, file scope, order, verification, forbidden areas, and an
   explicit implementation/independent-validation split decision; the main
   process retains repository rules, source context, integration, and final
   delivery judgment, while each delegated scope forbids unrelated changes
6. presents the exact plan and waits for user confirmation before coding,
   including for hotfixes and small bug fixes

For a substantive continuation of a draft or other non-`Implemented` active
plan, the checkpoint states the new `version` and `last_updated` together; a
generic statement that the plan will be updated is insufficient. For a
`Superseded` or completed archive, the checkpoint names the exact required
archive metadata: `implementation_scope`, `status`, `archived_at`,
`archive_approved_by`, `source_plan`, the preserved original metadata, and
`superseded_reason` when applicable. Do not substitute similarly named fields.

When `subagent_split` is enabled, state that the main process retains the PRD,
TRD, applicable design documents, repository rules, implementation boundary,
integration, and final delivery judgment. Assign independent validation to a
different sub-agent and require it to check those source documents, changed
scope, deterministic test results, repository rules, unrelated-change safety,
and residual risk.

Render that checkpoint with explicit fields: `feature_path`, `parent_feature`,
`feature_level`, `change_map_path`, `matched_code_glob`, `mapped_docs`,
`prd_alignment`, `prd_path`, `trd_alignment`, `trd_path`,
`active_plan_path`, `active_plan_status`, `active_plan_scope_before`,
`replacement_plan_scope`, `archive_directory`, `active_entry_rule`,
`archive_state`, `decision`, `receiving_owner`, `gap_packet`, `planned_files`,
`verification_commands`, `subagent_split`, `blocked_downstream_actions`, and
`confirmation_required`. Use `N/A` only when the field is genuinely
inapplicable. A gap packet always preserves the feature metadata and expected
document paths. A blocked checkpoint names every prohibited next action that
matters, including implementation, new E2E expectations, QA handoff, delivery,
PR creation, and issue closeout. A planning checkpoint never substitutes a
generic request for more context when the confirmed documents already provide
the field.
For replacement or abandonment, `active_plan_scope_before` must come from the
locked pre-write active plan and remain unchanged in the checkpoint and archive;
`replacement_plan_scope` names the new active plan. Never use the replacement
scope as evidence of what the original plan contained.

For a planning-only request, missing implementation source does not prohibit
creating the plan when confirmed PRD/TRD inputs identify the target file,
behavior, and executable verification command. Record source availability as a
risk, still produce the scoped plan and sub-agent split, and wait for plan
confirmation before implementation.
When the request itself says product and technical owners confirmed the PRD/TRD,
record that exact user-supplied confirmation as the `prd_alignment` and
`trd_alignment` evidence; do not reduce it to a generic aligned label or imply
that an unavailable source tree supplied the confirmation.

After implementation, reconcile the active plan body and frontmatter with the
actual result before any handoff. The final summary must list changed files,
verification, residual risks, runtime-artifact deletion, and—when user-facing
paths may change—the complete QA E2E handoff package based on the confirmed
plan. Runtime outputs never enter Git.

The closeout summary explicitly records `changed_files`, `commands_and_results`,
`residual_risks`, and `runtime_artifacts_removed`. The last field confirms that
transcripts, diagnostics, outputs, timing, and run status remain outside Git.

## PM Handoff Entry Gate

Do not execute implementation, write code, or create a plan unless the request
has an explicit PM handoff packet for Engineer / delivery-adjacent Engineer
work, or an equivalent confirmed document chain:
`docs/pm/{feature_path}/PRD.md`,
`docs/engineer/{feature_path}/TRD.md`, and a current implementation-scope
decision.

The PM-side packet field definition lives in
the plugin-local generated `../engineer-agent/_internal/_generated/shared-contracts/handoff-contract.md`.
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
components, data/API/integration impacts, error handling, observability and
security strategy, validation commands, rollout risks, and the boundary: the
finder only clarifies gaps; `trd-gen` completes the TRD.

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
`archive/` directory.

If an active plan exists with `status: "Implemented"` and no handling decision
is recorded, ask the user to choose exactly one of two options: archive the
completed plan then create a new active plan, or archive the old plan as
`Superseded` with a reason then create a new active plan. If the active plan
status is not `Implemented` and no archive on the same feature path faithfully
preserves its current body, continue updating that current plan with a version
bump by default instead of forcing archival or asking for an archive decision.
If such a faithful archive already exists, treat the current round as settled
and ask the user to choose exactly one of three options: archive it then create
a new active plan, continue updating it while redeclaring
`previous_plan_archive` to that faithful archive, or archive it as `Superseded`
with a reason then create a new active plan.
Only when the user or maintainer explicitly abandons that plan may it be
archived as `Superseded` with `superseded_reason` before creating a new active
plan, using the same archive metadata requirements as the `Implemented` branch.
If no active plan exists but the feature path has archive history, the new
active plan must set `previous_plan_archive` to the most recent archive. A
genuinely new feature path with neither an active plan nor archive history does
not need that backlink.

Plan form strength follows `change_tier` from the PM handoff or `AGENTS.md`.
`hotfix` may use the lightweight plan form allowed by the repository contract;
`standard` and `major` keep the full plan confirmation flow. Tiering never
waives PRD/TRD alignment or evidence.

Archival happens only after closeout and user/maintainer approval. Archive
paths must use
`docs/engineer/{feature_path}/archive/IMPLEMENTATION_PLAN-<scope>.md`.
The active plan path remains fixed at
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`.

## Implementation Flow

宿主存在 `docs/site/standards/change-map.yaml` 时，项目探索先按 pm-agent 维护的 `consumption-contract.md`（the plugin-local generated `../engineer-agent/_internal/_generated/shared-contracts/consumption-contract.md`）执行“任务落点 → change-map 反查 → 精准读取 → 关键判断回代码验证”；不存在时静默沿用当前代码探索。

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
Closeout records final status, changed files, commands run or skipped,
residual risks, and next owner.

If frontmatter says `status: "Implemented"`, the body must not keep unresolved
planning wording such as "waiting for confirmation", "not started", or
"pending execution" except as clearly historical context with a resolved result.
Before correcting that closeout, explicitly identify the conflict between the
`Implemented` frontmatter and each unresolved body state found. When an archive
decision is in scope, the user-visible checkpoint also states that
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` remains the fixed active
entry and archives go only under
`docs/engineer/{feature_path}/archive/`.
Runtime eval artifacts must not be committed.

When user-facing flows, acceptance paths, permissions, login, data setup, or
regression coverage may be affected, produce a QA E2E handoff package. Do not
create QA E2E cases unless explicitly routed to QA work.
While `IMPLEMENTATION_PLAN.md` is missing or unconfirmed, creation or update of
QA E2E TCs is explicitly blocked. After confirmation, every QA E2E handoff must
cite that confirmed plan path; source availability does not waive this gate.
Render both facts in the planning checkpoint itself as
`qa_e2e_tc_create_or_update: blocked_until_plan_confirmed` and
`qa_e2e_source_after_confirmation: docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`;
do not defer them to a later QA step.
The same checkpoint renders `qa_e2e_handoff_package_after_implementation` with
explicit fields for PRD path, TRD path, confirmed implementation-plan path,
changed files, verification commands, test results, residual risks, and the
suggested `docs/qa/e2e/{feature_path}/` directory. Values that cannot exist
before implementation are marked pending, but no field or target directory may
be omitted.

## Key Principles

- Read before write.
- Keep changes scoped to the confirmed plan.
- Prefer existing project conventions over new abstractions.
- Every implementation decision traces to PM/TRD/design docs.
- Do not perform missing PM, Designer, QA, DevOps, or Security responsibilities.
