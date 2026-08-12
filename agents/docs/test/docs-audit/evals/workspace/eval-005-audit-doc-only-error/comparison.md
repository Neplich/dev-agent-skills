# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Identity schema: `2`
- target_skill_sha256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- eval_definition_sha256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- metadata_sha256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- fixture_sha256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d804d7eed6dff47b2c8744abfb057fce66d8fde2359e03e7f21e978c34808373`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | With-skill output identifies docs/site/api/catalog.md as both the changed file and affected formal page; raw diff confirms the only change is documentation. |
| `uses_related_code_for_fact_check` | PASS | With-skill output explicitly uses related_code src/catalog/routes.txt and reports the target contract contains only GET /catalog/items; fixture content confirms this. |
| `classifies_doc_only_conflict_mismatch` | PASS | With-skill output preserves the DELETE declaration, GET-only code fact, evidence path, impact, and classifies the page as mismatch. |
| `blocks_despite_no_code_diff` | PASS | With-skill output reports pre-tag blocked, says the conflict prevents stamping, and does not return ready_for_tag; trace records no writes or release commit. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=4b090973ec4f5a2d58ce596af267630abf54855f5cbea01a40a9e9998ac58d6a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly audits the documentation-only change, fact-checks related code, classifies the conflict as mismatch, and blocks pre-tag release.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=1caeabce4118d7cc581a0c4ceed3e24f0e40f2bc8c613097cb7c89aade3e7ec8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also detects the DELETE mismatch and recommends blocking release, but provides less explicit audit-layer coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
