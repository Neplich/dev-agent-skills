# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-006-design-gate-all-passed`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-006-design-gate-all-passed`.
- Fixture SHA-256: `98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75`
- Prompt SHA-256: `c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `ebe36ab58d09b32dcb1d3a0e60e80a8c30163db5b3f4afa9ec0da402309c3c17`
- Eval definition SHA-256: `409f0dff74eed97473da7310514056fa3150a1bcc243e245700365b8124e237d`
- Metadata SHA-256: `d850062d9ab19e577fb519798bc20c97592f06bfa16acdff382b6c2af72957e7`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `passes_completion_gates` | PASS | With-skill output explicitly marks all six gates PASS, with evidence paths for the Approved PRD, Confirmed TRD, confirmed and completed plan, code/diff coverage, and all required tests passing. |
| `stops_at_scope_confirmation` | PASS | It identifies the candidate design page, code scope, evidence, exclusions, and unresolved confirmation state; locked git evidence shows no changes, and it explicitly asks for confirmation before synchronization. |
| `current_state_only` | PASS | The proposed design behavior matches the fixture code and passing tests: fixed field order, omission of empty values, and compact rendering using the same ordered non-empty values. No unsupported future behavior is proposed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=bf559f22554eaacb0f4e0e9811d69d8b397b7e2449b4ca9bcb35bf70f5944619; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Structured closeout review passed all gates, preserved scope, and stopped for confirmation without mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=0000bb1dda847b0ebe914914df1fdcd437bb85a4cad01478840e9b8c7fc4defa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identified the page and evidence and stopped before mutation, but provided less explicit gate and scope-closeout detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
