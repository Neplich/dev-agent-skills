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
- target_skill_sha256: `2846695e854af26b77f56804bd16db1050e2bacd34407999d119ed4e4a881599`
- eval_definition_sha256: `67789de316a1ba3d112d33eabc20baa992cdfc352bddac2855c6bcc9a3f93650`
- metadata_sha256: `421f80bf3da30d58b5b544d4c2e96b4cfdc1446ea641a3ffc3d654e2472f3421`
- fixture_sha256: `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `08c04fe57b81475dd890de6778e0567d043b2de7ae5ceb0392b2f8c748e60f69`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c4382a755d40b4c37cbb5843089f99a5655b439fd2c6460df6c8b5adeb479967`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | With-skill raw evidence reports 42 assets identical, 0 missing, 0 conflicts; Git status and diff are empty. |
| `reports_skipped_identical` | PASS | The locked manifest contains 42 file entries, all with status skipped-identical; raw evidence confirms the 42/42 byte-identical classification. |
| `preserves_existing_state` | PASS | With-skill Git evidence shows no status or diff changes, and the manifest/pages/configuration remain unchanged. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=5ededabb822eca31e0c0e129b802f74dc366b0080e8aff5e829a5d4d9c9b750f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Repeated initialization produced zero changes; all 42 assets were skipped-identical and existing state was preserved.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=85d33029191e6a4796a9d0528925f5a80cb1f2d002bcd7fdae1a5503b4ae494e; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Reported no tracked-file changes but produced 38 untracked generated artifacts, without the required 42-asset skipped-identical classification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
