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
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `409f0dff74eed97473da7310514056fa3150a1bcc243e245700365b8124e237d`
- metadata_sha256: `d850062d9ab19e577fb519798bc20c97592f06bfa16acdff382b6c2af72957e7`
- fixture_sha256: `98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `ebe36ab58d09b32dcb1d3a0e60e80a8c30163db5b3f4afa9ec0da402309c3c17`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `passes_completion_gates` | PASS | With_skill explicitly marks Approved PRD, Confirmed TRD, confirmed plan, completed scope, code/diff coverage, and all three required tests as PASS; the fixture documents and diff/test evidence support each gate. |
| `stops_at_scope_confirmation` | PASS | With_skill identifies the design page, change-map mapping, code boundary, evidence bindings, exclusions, pending confirmation, and unchanged write state, then asks for confirmation before executing the batch. |
| `current_state_only` | PASS | The proposed behavior is limited to fixture-supported current behavior: fixed field order, omission of empty values, and shared ordered non-empty values for standard and compact output. No unsupported future behavior is proposed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=c88dd02a201b00092f5c6feb5937fb487b6bed67c0058d0aa763ee894ebf7b9b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed evidence-backed candidate planning and correctly stopped for maintainer confirmation without modifying the site.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c76b170dd7794d3734918c7a765e05580924d97e899b93480f8dc75124874544; fixture_sha256=98bf611a541c8fe0137472ae23a2bee304eb1dd895062850790d9e776e872e75; output_sha256=948b56c331a6e92fbf3e56825b6a07c216f07f03a11287089099ab4c1d6ebccd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identified the candidate page, mapping, evidence, current behavior, exclusions, and confirmation gate, but with less structured gate and scope reporting.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
