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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `b193497852920517172f09f5d68ba6d13d4646f7f71948ca300566e66c51cb59`
- Judge schema SHA-256: `08c04fe57b81475dd890de6778e0567d043b2de7ae5ceb0392b2f8c748e60f69`
- Eval definition SHA-256: `67789de316a1ba3d112d33eabc20baa992cdfc352bddac2855c6bcc9a3f93650`
- Metadata SHA-256: `421f80bf3da30d58b5b544d4c2e96b4cfdc1446ea641a3ffc3d654e2472f3421`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | With-skill raw evidence reports inventory 42, identical 42, no missing/issues, zeroDiff true; Git evidence shows unchanged HEAD and clean status/diff. |
| `reports_skipped_identical` | PASS | Locked manifest output shows all 42 entries as skipped-identical; raw verification reports 42 identical and 42 manifest entries. |
| `preserves_existing_state` | PASS | Git evidence shows no changes, and manifest evidence preserves createdAt with no kept-as-is or created entries. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=589e54c72306e55cb6bffef6b87f2d258dda834bce8b7ef1b41e175ca29eaa18; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly completed an idempotent reinitialization with all 42 assets skipped-identical, zero diff, and preserved manifest state.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=c2ceb0fa333699ef0346b0f1879a28bac89fffd59b526a9e0a6d37964bf0bb7e; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Reported success but generated 38 new untracked files and did not satisfy the 42-asset skipped-identical requirement.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
