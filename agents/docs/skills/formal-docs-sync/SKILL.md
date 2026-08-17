---
name: formal-docs-sync
description: "Synchronize or plan bounded backfill of current API, database, design, ops, and product documentation from confirmed evidence. Use after docs-agent routes formal documentation sync."
visibility: internal
---

# Formal Docs Sync

Synchronizes confirmed current-state facts into a host project's existing
formal documentation site. This file owns only the entry gate and mode
selection. After they pass, load `_internal/INSTRUCTIONS.md`; that entry tells
you which single type module to load for each target page.

## Mandatory Mode Checkpoint

Resolve the active installed `formal-docs-sync` skill directory and load its
`_internal/INSTRUCTIONS.md` after the entry gate; load only the type modules in
scope. Before any write, report the selected mode, accepted evidence, complete
candidate page tree, per-node confirmation state, exact atomic change-map
delta, stable paths and out-of-batch drift, then wait for confirmation whenever
the batch or migration scope is not already confirmed.
For a confirmed multi-type scope, preserve every exact invitation,
repository/schema, service, audit, or other source boundary as its own
`code_glob` row with a complete cross-type `required_docs` closure; a broad
feature glob never substitutes for a missing exact row.

- Feature delivery: enforce PRD/TRD/plan/diff/test and design-closeout evidence;
  update the affected pages and change map together, leave new or unstamped
  pages `unverified`, run host checks, then hand off to `docs-audit`.
- Deployment verification: cross-check the shared environment reference and
  keep Development, Docker, and Kubernetes/Helm evidence and blockers
  separate. Continue confirmed classes, block only the missing class, and never
  invent placeholder commands. Migrate confirmed aggregate paths atomically.
- Release: touch only affected product/ops facts. A Release Notes outcome goes
  to `release-notes-gen`; carry the confirmed host repository, version, scope,
  evidence, and target site surfaces unchanged, and keep the entire site
  zero-diff in that routing step.
- Existing-system backfill: prefer catalog/change-map scope, propose one finite
  API/database/design/ops/product batch, mark every proposed new page
  `visibility: internal`, and remain read-only until confirmed.
Before that confirmation, inspect only the host check definitions needed to
plan verification; do not execute `test:docs`, builds, navigation preparation,
or any other host check. Read-only candidate planning is not authorization to
run the post-write verification phase.

Every completed write batch must run the host's real checks, report their raw
result, hand the affected set to audit, and perform the read-only deployment
completeness recheck. A discovered deployment gap returns to `pm-agent` without
being repaired here.

Make the result auditable with an explicit `Sync decision` block containing:
`mode`, `gate_status`, `confirmed_batch`, `proposed_batch`, `affected_docs`,
`evidence_bindings`, `excluded_paths`, `change_map_delta`,
`change_map_normalization`,
`loaded_type_modules`, `loaded_host_templates`, `hierarchy_drift`,
`host_checks`, and `audit_handoff`. Deployment mode additionally records one status for each of
Development, Docker, and Kubernetes/Helm. The top-level `gate_status` describes
the entry or whole-batch gate; a missing class-specific evidence set marks only
that class `blocked` and must not turn the whole batch into `blocked` while an
independently confirmed class can proceed. Each factual page claim names its implementation, test,
deployment, or maintainer-confirmed evidence. Do not add an ancestor/index,
page, map entry, future version fact, or owner merely because it would make the
site more complete; it must be required by the confirmed batch or existing host
navigation. When a prerequisite fails, set `gate_status: blocked` before scope
confirmation or writes. This applies to entry or whole-batch prerequisites; a
deployment class evidence gap follows the per-class continuation rule above.
Route product/metadata conflicts to `pm-agent` and TRD
path/impact conflicts to `engineer-agent:trd-gen` separately.
Set `change_map_normalization` to the observed result of a pre-return check that
every changed mapping list is deduplicated and stably sorted; a proposed delta
must state this normalization behavior as explicitly as an applied delta.

When one batch is confirmed and another is still proposed, report them
separately. The unconfirmed candidate must include its complete ancestor/leaf
tree, code and evidence boundaries, owner, exact change-map delta, exclusions,
and confirmation status even though it remains zero-write. A hierarchy
migration proposal additionally names every drifted path and target node,
old-to-new path mapping, recursive navigation delta, `required_docs` delta, and
out-of-batch drift group, then offers migrate, keep only the confirmed batch,
or defer all changes before any write. In the final result,
name every host command actually run with its cwd and exit status; a generic
test-count or “checks passed” summary is not equivalent evidence.
Use catalog ownership and evidence paths exactly; do not substitute a guessed
team. End every completed write batch with an explicit audit handoff containing
all six fields: `status`, `completed_batch`, `affected_docs_and_map`,
`supporting_evidence`, `exclusions`, and `target_release_version`. When the
release version is not maintainer-confirmed, set `status: blocked` and
`target_release_version: missing`; do not replace either field with prose about
the next owner.
When the host defines `test:docs`, `build:public`, and `build:internal`, a
completed write batch must run and report all three commands with cwd and exit
status. Unit tests, navigation preparation, or a subset of those scripts cannot
substitute for the two visibility builds. Before returning, verify that all six
audit-handoff fields are present and complete rather than only naming
`docs-audit` as the next owner. For a hierarchy proposal, also verify that every
root-level non-index page is classified exactly once, pages that confirmed
catalog or `feature_path` evidence places under the same domain parent remain
in one group, each old-to-new row includes its inbound-link,
recursive-navigation, and `required_docs` deltas, and every out-of-batch group
contains both its page list and proposed target node. Do not return a partial
hierarchy inventory.

After each check, remove its transient work directories, generated previews,
logs, caches, and diagnostics before taking the final workspace snapshot. Keep
only the requested formal documents, change-map updates, and the durable
conclusion/handoff; a passing command does not authorize test process artifacts
to remain in the host tree.

## Entry Gate

Require a PM handoff packet or an equivalent confirmed entry basis for exactly
one mode. The PM packet definition lives in
the plugin-local generated `../docs-agent/_internal/_generated/shared-contracts/handoff-contract.md`.
Direct invocation does not waive this gate.
Security-originated evidence is not an equivalent entry basis for any mode. If
there is no PM handoff packet, stop and guide the request back to `pm-agent` for
classification under `Security Conclusion Escalation to PM` and issue filing.
When a deployment recheck specifically exposes a missing repo-wide deployment
handoff, a PM-authorized bounded read-only recheck remains valid entry basis:
inspect the named site configuration, report the evidence-backed coverage and
gaps, then ask the user whether `pm-agent` should generate that repo-wide
handoff. The missing handoff blocks operational changes, not the scoped review;
do not replace the user-visible question with only a next-owner label.

- **Feature delivery:** require an Approved PRD, a Confirmed TRD with traceable
  impact scope, a confirmed `IMPLEMENTATION_PLAN.md`, the actual diff, and
  required test results. Feature-level design pages additionally require the
  existing design closeout gate described in `_internal/INSTRUCTIONS.md`.
- **Deployment verification:** require confirmed deployment scope classified
  as Development, Docker, and Kubernetes/Helm, the TRD deployment surface,
  deployment configuration, verification commands and results, and known
  environment differences. Missing evidence blocks only the affected class;
  never replace it with placeholder commands.
- **Release:** require confirmed release scope, verified version evidence,
  changelog and release-process evidence, and audit context. This mode does not
  own Release Notes.
- **Existing-system backfill:** require an explicit maintainer request, a
  confirmed host repository, and a feature catalog or permission for bounded
  discovery. An implementation plan is not required, but every finite batch
  requires confirmation.

If the basis is incomplete, stop before writing. Return product ambiguity to
`pm-agent`, technical-impact gaps to `engineer-agent:trd-gen`, and a missing
site foundation to `docs-site-bootstrap`; synchronization must not initialize
the site.

## Mode Selection

| Mode | Confirmed synchronization surface |
| --- | --- |
| Feature delivery | Affected API, database, design, and product pages, with their change-map entries and only necessary indexes or host-required navigation. |
| Deployment verification | Current Development, Docker, and Kubernetes/Helm ops, upgrade, and rollback facts under `ops/deployment/`, with a shared environment reference, per-class change-map entries, and only necessary indexes or host-required navigation. |
| Release | Only affected product and ops pages, reconciled with confirmed version facts. Release Notes body, index, metadata, and navigation belong to `docs-agent:release-notes-gen`. |
| Existing-system backfill | One maintainer-confirmed finite batch of API, database, design, ops, or product current-state pages. Prefer a feature catalog and existing change map; never expand bounded discovery into full-site generation. |

The accepted implementation surface is all five formal document types: API,
database, design, ops, and product. This remains one specialist; do not create
parallel type-specific skills.

## Authoritative Execution Pointer

After the gate and mode are resolved, load `_internal/INSTRUCTIONS.md` and
follow its eight-step host-site contract, mode rules, change-map discipline,
boundaries, and report shape. For each target type, load only the corresponding
`_internal/types/<type>/INSTRUCTIONS.md`; do not read the other four type
modules unless they enter the confirmed write scope or an explicitly requested
read-only candidate-planning scope.

After every completed existing-site content batch, apply the shared read-only
documentation-site deployment completeness recheck in the Safety-Net closeout.
Report evidence and drift and return any user-confirmed gap to `pm-agent`; do
not repair Docker, CI/CD, Compose, Helm, ingress, or runtime configuration. This
does not change the five-type contract above.
