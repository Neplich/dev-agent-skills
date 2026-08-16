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
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- metadata_sha256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- fixture_sha256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d804d7eed6dff47b2c8744abfb057fce66d8fde2359e03e7f21e978c34808373`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | With-skill trace explicitly applies the documentation-only affected-page rule, and reports docs/site/api/catalog.md as affected despite no code or change-map match. |
| `uses_related_code_for_fact_check` | PASS | The page declares related_code src/catalog/routes.txt; the with-skill result cites that file as target code evidence and compares its GET-only content. |
| `classifies_doc_only_conflict_mismatch` | PASS | The with-skill report preserves the DELETE claim, GET-only code fact, routes.txt evidence, blocking impact, and classifies the page as mismatch. |
| `blocks_despite_no_code_diff` | PASS | The with-skill result is pre-tag blocked, says the page cannot be stamped, and does not return ready_for_tag despite the docs-only diff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=a6c94552717ee283d4ebceceef8679694cd0530a44e83828ec5fc6b2fa6a0898; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly included and fact-checked the documentation-only page, detected the DELETE mismatch, and blocked pre-tag release.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=603dc88d5d03441b68fd953e0e4ce5c895208f8d61eb3b3126ff74d0a878a49f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also detected the mismatch and recommended blocking, but did not demonstrate the formal documentation-only impact workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
