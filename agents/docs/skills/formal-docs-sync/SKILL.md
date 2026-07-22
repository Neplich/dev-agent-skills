---
name: formal-docs-sync
description: "Internal documentation specialist—not a direct entry point. Invoked by docs-agent to synchronize current-state API, database, design, ops, and product docs from confirmed feature, deployment, release, or bounded backfill evidence."
visibility: internal
---

# Formal Docs Sync

Synchronizes confirmed current-state facts into a host project's existing
formal documentation site. This file owns only the entry gate and mode
selection. After they pass, load `_internal/INSTRUCTIONS.md`; that entry tells
you which single type module to load for each target page.

## Entry Gate

Require a PM handoff packet or an equivalent confirmed entry basis for exactly
one mode. The PM packet definition lives in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
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
| Release | Only affected product and ops pages, reconciled with confirmed version facts. Release Notes body, index, metadata, and navigation belong to `docs-agent:release-notes-generator`. |
| Existing-system backfill | One maintainer-confirmed finite batch of API, database, design, ops, or product current-state pages. Prefer a feature catalog and existing change map; never expand bounded discovery into full-site generation. |

The accepted implementation surface is all five formal document types: API,
database, design, ops, and product. This remains one specialist; do not create
parallel type-specific skills.

## Authoritative Execution Pointer

After the gate and mode are resolved, load `_internal/INSTRUCTIONS.md` and
follow its eight-step host-site contract, mode rules, change-map discipline,
boundaries, and report shape. For each target type, load only the corresponding
`_internal/types/<type>/INSTRUCTIONS.md`; do not read the other four type
modules unless they enter the confirmed scope.
