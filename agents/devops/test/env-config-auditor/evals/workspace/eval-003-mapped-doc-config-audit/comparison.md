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
- target_skill_sha256: `bd10ad28cda2e258647de2487fc41636124b4b1a48dc9f75b2dda06e6bfc2473`
- eval_definition_sha256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- metadata_sha256: `a409117cbc37644389cd1b3fee7ddaa2ea9110d0eb3d552191443a51d68ee791`
- fixture_sha256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `204b02cf02ba29acba94a8f2b9d77989cc545ccad0b3e283133a98976ab6ca74`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | With-skill trace correctly applied the PM/DevOps handoff gate and stopped before configuration audit; mapped-document reading was therefore not exercised. |
| `verifies_against_code` | NOT_EXERCISED | With-skill trace stopped at the required handoff gate before comparing runtime-config.md with required.env; code verification was not exercised. |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | With-skill trace stopped before the audit and did not inspect the target documents' verification metadata; low-trust handling was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=b105f5c2d4d69ce4b8d4e5f7379ce33d8214a0426143b7c4d1606c6aec2bff51; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly enforced the mandatory handoff gate and made no repository mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=a2c61760875e33966d47a759e4462ea9602b18468787e6afb75bbebc8dae1ae3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed the requested audit and identified the documentation-versus-code conflict.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the required PM/DevOps handoff packet, then perform the mapped-document and code verification audit.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
