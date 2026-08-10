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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
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
| `blocks_on_evidence_mismatch` | PASS | With-skill output explicitly compares the request/plan path `preferences-summary` with PRD/TRD `feature_path: account-preferences`, identifies the conflict, blocks the gate before candidate confirmation, and reports zero writes. |
| `design_zero_change` | PASS | With-skill git evidence shows unchanged HEAD, empty worktree/index diffs, and no status changes; the output reports `confirmed_batch: none; zero writes` and `none written` for the affected design/map scope. |
| `routes_to_owner` | FAIL | The output routes the conflict to `pm-agent`, but does not route the TRD path/impact alignment to Engineer or `trd-gen` as required. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=08d36d2af5ad24ad194a8cb82578cdf5032fdfc60e85b181851162b6b259c15a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked on the feature-path mismatch and made no writes, but incompletely routed ownership.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=7aaa2dc2004e21a58f435aad7766c6ad817d3a09ebb8321474089b2d0e95a118; snapshot_sha256=bdbebd71a49f2a3ea19e6fc13305703c801ff11beb1adcb8953eb53ef5f78afb
- Behavior: Performed the requested document changes despite acknowledging the PRD/TRD metadata mismatch.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Missing the required Engineer / trd-gen route for TRD path and impact-domain alignment.
- Next: Route TRD path and impact-domain alignment to Engineer / trd-gen, alongside the PM owner route, and require unified evidence before retry.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
