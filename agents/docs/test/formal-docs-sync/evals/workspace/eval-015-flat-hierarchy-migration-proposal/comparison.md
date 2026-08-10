# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-015-flat-hierarchy-migration-proposal`.
- Fixture SHA-256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Eval definition SHA-256: `b33925735dcdc1c16e96ba8e543e331eebb29f1fb2575eb75afef7012c2934cd`
- Metadata SHA-256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | PASS | with_skill identifies research-conversations.md and graph-search.md as knowledge-discovery hierarchy drift, tied to catalog/path evidence and not page prose. |
| `proposes_migration_before_write` | PASS | with_skill proposes the ancestor index tree, migration mapping with inbound/navigation/required_docs deltas, change-map updates, exclusions, batch placement, and three confirmation choices before writing. |
| `does_not_deepen_flat_layout` | PASS | Locked git evidence shows no changes; the candidate explicitly waits for confirmation and reports host checks and audit handoff as pending. |
| `reports_out_of_batch_drift_read_only` | PASS | with_skill lists knowledge-building and platform-governance drift pages with proposed target nodes and treats them as out-of-batch read-only observations. |
| `loads_only_api_contract` | PASS | Runner trace directly shows loading the API type instructions and API template, while the report names those loaded resources and provides a hierarchy_drift field; no non-API type modules/templates are loaded. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=4dc2b9c92935fd35f9a7c850304eafaa56bdf49d7a68c4e9ad7e590d2a80e516; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a read-only, evidence-bound feature-delivery scope with hierarchy drift analysis, migration proposal, exclusions, and confirmation gate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=2a78d1cd75466d2500ce9d90785bb887e03d9558f99e309bb34f0cdcede817a8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a basic flat-layout API page proposal without hierarchy drift detection or migration planning.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
