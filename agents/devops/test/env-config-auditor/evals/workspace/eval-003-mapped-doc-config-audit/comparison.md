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
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `204b02cf02ba29acba94a8f2b9d77989cc545ccad0b3e283133a98976ab6ca74`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | With-skill trace reads skill and handoff-contract files first, then stops; it never reads the mapped runtime-config document. |
| `verifies_against_code` | FAIL | With-skill output does not read or report src/config/required.env, the documented optional declaration, or the required-vs-optional conflict; it incorrectly blocks on an unsupported handoff prerequisite. |
| `treats_unverified_as_low_trust` | FAIL | With-skill output does not identify last_verified_version: unverified or apply the required low-trust treatment. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=36d0362f593f1e83f8a9ab573f8efb84550ac3e0f7a11cb52a50e9111404ba23; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Incorrectly returned to PM without auditing the supplied configuration evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=e3a5498b2e77d9a772e3172ae1b5b18fbebfd5f5bdc4844dbfd1af172e281287; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline correctly mapped the documentation, verified the required declaration, and treated unverified documents as conflicting low-trust evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- All three with_skill assertions fail: the candidate did not perform the requested fixture audit or provide its required conclusions.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
