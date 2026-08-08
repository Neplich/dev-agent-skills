---
name: formal-docs-sync
description: "Synchronize or plan bounded backfill of current-state API, database, design, ops, and product docs from confirmed feature, deployment, or release evidence. Use after docs-agent routes a complete sync basis."
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

- Feature delivery: enforce PRD/TRD/plan/diff/test and design-closeout evidence;
  update the affected pages and change map together, leave new or unstamped
  pages `unverified`, run host checks, then hand off to `docs-audit`.
- Deployment verification: cross-check the shared environment reference and
  keep Development, Docker, and Kubernetes/Helm evidence and blockers
  separate. Continue confirmed classes, block only the missing class, and never
  invent placeholder commands. Migrate confirmed aggregate paths atomically.
- Release: touch only affected product/ops facts. A Release Notes outcome goes
  to `release-notes-gen`; keep the entire site zero-diff in that routing step.
- Existing-system backfill: prefer catalog/change-map scope, propose one finite
  API/database/design/ops/product batch, and remain read-only until confirmed.

Every completed write batch must run the host's real checks, report their raw
result, hand the affected set to audit, and perform the read-only deployment
completeness recheck. A discovered deployment gap returns to `pm-agent` without
being repaired here.

When one batch is confirmed and another is still proposed, report them
separately. The unconfirmed candidate must include its complete ancestor/leaf
tree, code and evidence boundaries, owner, exact change-map delta, exclusions,
and confirmation status even though it remains zero-write. In the final result,
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
`docs-audit` as the next owner.

After each check, remove its transient work directories, generated previews,
logs, caches, and diagnostics before taking the final workspace snapshot. Keep
only the requested formal documents, change-map updates, and the durable
conclusion/handoff; a passing command does not authorize test process artifacts
to remain in the host tree.

## Entry Gate

Require a PM handoff packet or an equivalent confirmed entry basis for exactly
one mode. The PM packet definition lives in
the active installed `idea-to-spec` skill's `_internal/_shared/skill-map.md`.
Direct invocation does not waive this gate.
Security-originated evidence is not an equivalent entry basis for any mode. If
there is no PM handoff packet, stop and guide the request back to `pm-agent` for
classification under `Security Conclusion Escalation to PM` and issue filing.

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
