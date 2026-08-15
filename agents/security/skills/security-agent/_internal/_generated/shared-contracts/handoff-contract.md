<!-- GENERATED FILE: DO NOT EDIT. Source: agents/product_manager/skills/idea-to-spec/_internal/_shared/handoff-contract.md. -->

# Cross-Role PM Handoff Packet Contract

When `pm-agent` or `idea-to-spec` sends work to Designer, Engineer, QA, DevOps,
Security, Docs, delivery, or another non-PM owner, use this cross-role packet. This
section is the authoritative PM-side field definition for the PM handoff packet.

Required fields:

| Field | Meaning |
| --- | --- |
| `request_type` | Stable request class: `new_feature`, `existing_update`, `bug_report`, `design`, `validation`, `deployment`, `security`, `formal_docs`, `document_structure_governance`, `delivery`, `status`, `feature_catalog`, `competitive_research`, `battlecard`, `changelog`, `release_notes`, `roadmap`, or `repo_status`. |
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

### Diagnosis-Only Optional Extension

For a `bug_report` whose user explicitly requires read-only investigation,
diagnosis only, or no fix, extend the Engineer handoff with these optional,
mode-specific fields:

```yaml
mode: diagnosis_only
allowed_mutations: none
```

These fields are not universal packet requirements and must not be inferred
from ambiguous investigation language such as “查一下” or “为什么挂了”. The
handoff must render the zero-mutation boundary explicitly: no changes to code,
tests, E2E assets, configuration, databases, external state, commits, pushes,
or pull requests. Its `required_output` is an evidence-based diagnosis report.

This narrow route may send objective evidence collection to `Engineer` before
approved PRD/TRD expectations exist. Keep `feature_path` and other unresolved
fields honest, record missing expectations in `blockers_risks`, and require the
downstream diagnosis to use `expected_behavior_alignment: unaligned`; it must
not confirm an `implementation_deviation`, produce a repair plan, or mutate
state. Any later fix request leaves this extension and re-enters the normal PM
and Engineer repair gates.

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
| Confirmed UX, UI, information architecture, wireframes, or visual-system work | `Designer` | PM scope, source PRD, design goal, target users, required design artifact. |
| Explicit read-only `bug_report` with the diagnosis-only optional extension | `Engineer` | Preserve `mode: diagnosis_only`, `allowed_mutations: none`, the explicit zero-mutation boundary, unaligned expectation status when applicable, and the evidence-based report output. |
| Confirmed TRD, implementation, debugging, tests, code review, commit, push, PR, or delivery work | `Engineer` or `delivery` | PRD / TRD / implementation-plan source docs, `change_tier`, verification expectations, delivery state. |
| Confirmed acceptance, exploratory, bug analysis, smoke, retest, or regression work | `QA` | Test basis, expected behavior, environment, affected flows, result format. |
| Confirmed deployment, CI/CD, environment, Docker, Helm, release readiness, rollback, or runbook work | `DevOps` | Environment, release target, rollback expectation, operational risk. |
| Confirmed AppSec, auth/authz, dependency, secret, privacy, upload, webhook, or data-flow review | `Security` | Risk surface, assets, permissions, data categories, remediation expectations. |
| Confirmed formal documentation site bootstrap, post-feature / post-deployment / post-release formal-docs synchronization, existing formal-docs backfill, versioned `docs/site/release-notes/` delivery, or release documentation audit | `Docs` | Source feature / deployment / release evidence, formal-docs scope, target site or pages, synchronization, site Release Notes, or audit output; `docs-agent` routes the request to the matching specialist. |
| Inherited-project feature inventory, competitive research, battlecards, changelogs, GitHub Release bodies/operations, roadmaps, or repository status | Named PM specialist | PM-owned route context only: selected specialist, source repository or release context, optional `N/A` feature scope for non-feature work, and any follow-up handoff condition. GitHub Release work routes to `github-release-gen`; site and user-facing version notes route to Docs. |
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
