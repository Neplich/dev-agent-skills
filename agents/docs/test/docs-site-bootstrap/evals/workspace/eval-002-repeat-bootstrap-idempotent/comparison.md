# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-002-repeat-bootstrap-idempotent`.
- Identity schema: `2`
- target_skill_sha256: `f325a3bc283b067240ee3d50726f680693f5cd996590e717b72af686853dbf3e`
- eval_definition_sha256: `67789de316a1ba3d112d33eabc20baa992cdfc352bddac2855c6bcc9a3f93650`
- metadata_sha256: `421f80bf3da30d58b5b544d4c2e96b4cfdc1446ea641a3ffc3d654e2472f3421`
- fixture_sha256: `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `08c04fe57b81475dd890de6778e0567d043b2de7ae5ceb0392b2f8c748e60f69`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8a54b9d8ab53e6a7ef3187af8e3063aff036e0d1740a4b832c4d3a33058de445`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | With_skill raw Git evidence shows unchanged HEAD, empty status, empty diffs, and no result diffs; the output reports zero-diff. |
| `reports_skipped_identical` | PASS | With_skill raw command evidence reports missing=0, identical=42, conflicts=0, and the manifest read-back contains 42 valid paths all classified skipped-identical. |
| `preserves_existing_state` | PASS | With_skill raw evidence shows unchanged repository state and no result diffs; the candidate explicitly reports no overwrites or conflicts. Existing change-map, release metadata, pages, scripts, and configuration remain unchanged. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=d2b64b8b71cf16c112d9864f0ca43d47e8f1498da5bb3ccae9de9d038af3e737; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Re-initialization was idempotent: all 42 assets were byte-identical, no files changed, and existing state was preserved.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=e6225d6d45cbbca39fdb5d0db59055077f1c8473c1a3b96892914fcc7735ab17; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Fresh baseline ran a generation flow that produced 38 untracked generated files rather than demonstrating the required 42 skipped-identical classifications.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
