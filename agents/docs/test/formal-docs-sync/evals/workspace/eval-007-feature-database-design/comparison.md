# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Review context: PR #164 stable database-path migration safeguard

## Test Set / Fixture Version

- Fixture: current pristine `workspace/eval-007-feature-database-design` snapshot for PR #164 review repair
- Evidence set: confirmed handoff and candidate scope, Approved PRD, Confirmed TRD/plan, complete closeout, actual diff, passed tests, schema, repository, service, API page, existing stable database page, existing change-map entry, and host standards
- Actual validation date: `2026-07-22`
- Isolation: fresh `codex exec` copied the same fixture into independent lanes; `start-manifest.diff` was zero bytes, historical comparisons were excluded, and the final judge ran as a third fresh read-only subagent

## Latest Result

**PASS (10/10 assertions)** — the with-skill lane preserved the existing verified `docs/site/database/workspace-access.md` page byte-for-byte without a migration plan, retained its change-map coverage, added the complete database/schema/domain/entity subtree, and passed all content, navigation, host-check, and handoff assertions.

## Assertions

- `loads_only_database_design_contracts`: PASS. The lane loaded the host standards/map and only the database/design type modules.
- `passes_design_closeout_gate`: PASS. Approved PRD, Confirmed TRD/plan, complete scope, diff coverage, passed tests, and confirmed candidate scope were verified before writing.
- `creates_database_schema_domain_tree`: PASS. Database root, `primary` schema index, Workspace Access domain index, relationship overview, and three entity/table pages exist and are linked.
- `preserves_unapproved_stable_path`: PASS. The stable page kept its original path and SHA-256 `753cf70472824d61db25fb53e57dbb5e62998171ca7fc88eee30a9c751d30cf0`; the merged map retained that page and appended the confirmed new subtree.
- `documents_current_entity_facts`: PASS. Fields, checks, unique constraints, expiry, indexes, ownership, and lifecycle match current schema and access evidence.
- `links_relationships_bidirectionally`: PASS. The Mermaid overview links all entity pages; every entity links its domain, relationship page, related entities, and API page.
- `distinguishes_physical_and_logical_relations`: PASS. Both `workspace_id` cascade foreign keys are physical, while `user_id` is explicitly a service-validated logical reference without a foreign key.
- `synchronizes_delivered_design`: PASS. The design page documents workspace/user validation before repository upsert and excludes inherited or future roles.
- `updates_atomic_map_and_unverified_pages`: PASS. The stable page plus new subtree are merged in stable path order, the unrelated manual entry is preserved, and all changed pages remain `unverified`.
- `runs_host_checks_and_handoffs_audit`: PASS. Required commands passed; internal navigation contains every nested and stable database page, public navigation excludes internal database/design pages, and the #117 handoff is complete.

## With-Skill Behavior

- Applied the database/schema/data-domain/entity hierarchy, conditional relationship-page contract, stable-path migration safeguard, and physical/logical relation rules.
- Preserved the existing stable page byte-for-byte and merged its existing mapping with the new confirmed subtree without changing the trigger or exclusion.
- Ran `npm ci --ignore-scripts`, `npm run test:docs` (74/74), `npm run build:public`, and `npm run build:internal`; all exited `0`.

## Fresh Without-Skill Baseline

- Source: freshly regenerated from the same prompt and identical pristine fixture; it did not read the target skill, Docs Agent README, internal instructions, old comparison, or with-skill output.
- The baseline preserved the stable page and produced the main subtree, relationships, entity facts, design page, builds, and handoff.
- The fresh judge rated the baseline 8 PASS / 1 PARTIAL / 1 FAIL on behavior-comparable assertions: it did not fully record the seven-item design closeout gate, and its change-map list was not stably sorted and rewrote the existing trigger.
- The target-module loading assertion is intentionally unavailable to a baseline forbidden from reading the target skill and was not treated as baseline behavioral evidence.

## Failures

- With-skill: no assertion, runner, network, credential, dependency-install, or build failure.
- Without-skill: incomplete closeout evidence and non-deterministic/non-minimal change-map maintenance.
- Non-blocking: full command transcripts remain runtime-only; generated navigation, Markdown copies, internal HTML, public exclusions, sync reports, and fresh judge review independently corroborated the recorded command results.

## Next Steps

- Keep the restored stable page/map fixture and `preserves_unapproved_stable_path` assertion as the regression guard for unapproved database-page migration.

## Runtime Artifact Policy

- Source copies, both lanes, installed dependencies, generated sites, candidate outputs, logs, manifests, and judge verdict remain under `tmp/eval-runs/issue-159-review-fix-20260722/`.
- Only this comparison is durable; no transcript, runtime output, verdict, timing, diagnostics, `node_modules`, or generated site is submitted.
