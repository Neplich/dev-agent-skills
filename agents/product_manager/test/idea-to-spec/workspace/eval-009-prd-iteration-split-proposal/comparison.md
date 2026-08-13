# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-009-prd-iteration-split-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997` from `agents/product_manager/test/idea-to-spec/workspace/eval-009-prd-iteration-split-proposal`.
- Identity schema: `2`
- target_skill_sha256: `34042e851466ff927567e09fc5777d952f1546cabc96fbe4de98617d27f5b1fb`
- eval_definition_sha256: `8ef466ccd13d937453c02f105817ced47839fb573011ea1ee300be62facb6b71`
- metadata_sha256: `ae189abbce9ec160b22d49ab4f79a0a7a8f521d1a6e2046930669caf75d7dab0`
- fixture_sha256: `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `9c9a733fc3c46fd3cb1cdea794218e66a7a987137063c1a3c970e8e9386d1a58`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98`
- Repository HEAD: `c13c53a9b6e4cf18215450050bc9e7d0a810b73c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `55d032569bbd4014a60103aafb1c0773a93ff9dbe0ea681c46297ebeef4a35b3`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `applies_requested_change` | NOT_EXERCISED | With_skill produced no updated PRD or file snapshot; it stopped at the confirmation checkpoint before the update. |
| `detects_l2b_signals` | PASS | It explicitly identified 3 independent domains and 18 US/FR rows, satisfying two L2b signals. |
| `presents_split_proposal` | PASS | It provided a three-branch feature_path tree, section migration mapping, and impacts for Engineer, Design, QA, DevOps, and Security. |
| `waits_for_confirmation` | PASS | It explicitly requested confirmation and showed options to retain the current path or accept the split; no split files or moves were made. |
| `rejection_keeps_current_flow` | NOT_EXERCISED | No rejection occurred, so the post-rejection continuation behavior was not exercised. |
| `body_consolidation` | NOT_EXERCISED | The PRD was not updated because the workflow paused for confirmation; current-body consolidation therefore was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=11292067d2c39b92a665147bac9044273f98ee9a4652aa9bf97488b436e98923; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Detected the L2b checkpoint, presented a complete confirmation-gated split proposal, and made no filesystem mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=dfa3b057c7f8952ad67a49966e9d2293899868474d507eb85cc86ea9ab209136; snapshot_sha256=b3a6a548162a143cf1a9b8153a77dca6038be23317a95cbfd06d692a8f538d7e
- Behavior: Updated the PRD directly from polling to event-driven delivery, but did not present the L2b split proposal or confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the user's choice to retain the current feature path or accept the proposed split, then continue the corresponding workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
