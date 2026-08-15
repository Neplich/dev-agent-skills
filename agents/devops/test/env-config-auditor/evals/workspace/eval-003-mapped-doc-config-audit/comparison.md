# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Identity schema: `2`
- target_skill_sha256: `a8f87afda76c64d983a7b5f9d6a3f49bd751951e01d3714fb0439b6add7757ba`
- eval_definition_sha256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- metadata_sha256: `a409117cbc37644389cd1b3fee7ddaa2ea9110d0eb3d552191443a51d68ee791`
- fixture_sha256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `79bb3dd33873d6df8baf21e6b0c5f2908c29f5d530191b5eb998f51613f0fe2f`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | Raw trace shows the candidate read runtime-config.md before reading change-map.yaml, so it did not establish the required map-guided order. |
| `verifies_against_code` | FAIL | The with_skill output explicitly says it had not read src/config/required.env and made no API_TOKEN conclusion. |
| `treats_unverified_as_low_trust` | PASS | The candidate identified last_verified_version: unverified, treated the documentation as low trust, and declined to rely on it alone. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=ea5599bb065f4b4aa70ca1faddb2c1b5c19e89f5a3e87e950eb14bee3d2c6837; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly recognized the mapped document and its unverified status, but incorrectly blocked execution and failed to inspect the code fixture or complete the audit.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=261beabbe5bb52c3af575905084b92b5ec870f020091dc1005996d5c08b42eb2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed the audit, compared the documentation with src/config/required.env, identified the contradiction, and noted the limitation that runtime rejection was not independently verified.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane stopped at an unsupported handoff gate and omitted the requested code-versus-documentation audit.
- It failed to verify API_TOKEN against src/config/required.env and did not report the required discrepancy and configuration risk.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
