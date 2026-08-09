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
- Fixture SHA-256: `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `08c04fe57b81475dd890de6778e0567d043b2de7ae5ceb0392b2f8c748e60f69`
- Eval definition SHA-256: `67789de316a1ba3d112d33eabc20baa992cdfc352bddac2855c6bcc9a3f93650`
- Metadata SHA-256: `421f80bf3da30d58b5b544d4c2e96b4cfdc1446ea641a3ffc3d654e2472f3421`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | With-skill output reports zero new files, an empty git status, an empty git diff, and a clean work tree. |
| `reports_skipped_identical` | PASS | With-skill output reports all 42 assets as byte-identical and skipped, with 42 manifest records. |
| `preserves_existing_state` | PASS | With-skill output reports no created files or conflicts, clean Git state, and unchanged existing change-map/site assets. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=ccb22a1e11bfb4c2392115bea571adbf7bb00572b2ab69f33e1be4d061f31576; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Re-initialization is reported as idempotent: all 42 assets were skipped as identical, the manifest remained valid, and Git is clean.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=a65f10cb06c0f7a8c9639b6e892ab9344f3a1b62f6e7f2875c31885add21a672; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Baseline reports successful generation but leaves 38 untracked generated files, so its workspace is not zero-diff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
