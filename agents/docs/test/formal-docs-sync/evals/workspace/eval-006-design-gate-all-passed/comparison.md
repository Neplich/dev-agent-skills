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
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `409f0dff74eed97473da7310514056fa3150a1bcc243e245700365b8124e237d`
- metadata_sha256: `d850062d9ab19e577fb519798bc20c97592f06bfa16acdff382b6c2af72957e7`
- fixture_sha256: `98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `ebe36ab58d09b32dcb1d3a0e60e80a8c30163db5b3f4afa9ec0da402309c3c17`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `passes_completion_gates` | PASS | With-skill output marks all six gates PASS and cites the Approved PRD, Confirmed TRD with impacted code, confirmed plan, completed scope, diff/code coverage, and all required tests passed; fixture evidence supports these claims. |
| `stops_at_scope_confirmation` | PASS | With-skill output identifies docs/site/design/preferences-summary.md, src/preferences_summary.py, supporting evidence, exclusions, unresolved confirmation status, and explicitly asks the maintainer to confirm; locked git evidence shows no modification. |
| `current_state_only` | FAIL | The stated behavior is supported by the fixture code and test results, but the with-skill output also makes the unsupported claim that the change map has an existing code_glob, while the locked change-map evidence contains no code_glob. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=5d8c65ff688e1a220994e2dac0904bb5c6cfe222607c224f7ceaf4776ecf8c5f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly completes the evidence gates and stops for scope confirmation, but includes one unsupported change-map claim.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=a12ead8c4587245652c04ea1c71efe13a34d40abe06f27b2d736396b6096e467; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a fresh baseline with a concise candidate scope and confirmation request, but less complete gate and unresolved-item detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill lane includes an unsupported change-map claim about an existing code_glob, violating the current-state-only assertion.
- Next: Remove or correct the unsupported code_glob claim before presenting the candidate scope.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
