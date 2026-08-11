# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- Skill overlay SHA-256: `9667198915198da0404e03a7d4c962d38742b19c5de4de5f0cf1473f02db2bf1`
- Judge schema SHA-256: `c9b93b28ac72af6810f4752921bb72d418af8d9162ae5d66c15fe90f929562c8`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | With-skill output explicitly contrasts request/plan `preferences-summary` with PRD/TRD `account-preferences`, identifies the conflict, and blocks before scope confirmation or writes. |
| `design_zero_change` | PASS | With-skill output reports the design document and its change-map mapping were unmodified; locked git evidence shows no status, index, worktree, or commit changes. |
| `routes_to_owner` | FAIL | With-skill output requests PM alignment for PRD/TRD together, but does not route the TRD conflict to Engineer/trd-gen as required. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=3f79feead91c00607adefd6f117afece3cbedd84367fd4ff7fbbc5a8790cf2ba; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly detected the feature-path mismatch and stopped without mutation, but incompletely routed ownership remediation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=b370b2ccd4eb5a2945fc33768fd442ac29affc2980e152ecd692400c2771a1b6; snapshot_sha256=14695aa20f7feaa2b35ff61253ad5e3f55103a5cf00c9f53defbedaffc9960b7
- Behavior: Modified both design and change-map files despite the feature-path mismatch and did not block before writing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- routes_to_owner
- Next: Route the PRD conflict to the PM owner and the TRD path/impact-domain conflict to Engineer/trd-gen; require both to align with the request and plan before retrying.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
