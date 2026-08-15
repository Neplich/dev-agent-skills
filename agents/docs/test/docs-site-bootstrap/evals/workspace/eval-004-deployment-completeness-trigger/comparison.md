# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Identity schema: `2`
- target_skill_sha256: `f325a3bc283b067240ee3d50726f680693f5cd996590e717b72af686853dbf3e`
- eval_definition_sha256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- metadata_sha256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- fixture_sha256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `84cb88cc9e25dde2fbf0d2a0fb5349bfe630e32b333634cfdb918d30e60002a8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8a54b9d8ab53e6a7ef3187af8e3063aff036e0d1740a4b832c4d3a33058de445`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `asks_first_bootstrap_choice` | FAIL | with_skill output blocked on a PM handoff and did not present the required three choices for the unintegrated case. |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | No first-bootstrap durable-commit confirmation or completed integrated classification occurred in the locked with_skill output. |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | No repeated bootstrap or re-read of configuration occurred. |
| `preserves_authorization_boundary` | PASS | The output explicitly limited work to read-only, stated no files would be written, and git evidence shows no changes or commits. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=6dfab3cfcf3d6841987970d809f3c9a2302026e28cfeaa38a3a1f43399e2f465; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Blocked before fixture inspection; preserved the read-only boundary but did not complete the requested classification workflow.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=57b15381e28f83bcb479a8e7dc524463d7a243f0e72fc76b72be446ba4179af3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Inspected all three repository snapshots and provided evidence-based build-to-publish classifications and owners without mutation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane stopped before inspecting the read-only fixture and omitted the required first-bootstrap choice prompt.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
