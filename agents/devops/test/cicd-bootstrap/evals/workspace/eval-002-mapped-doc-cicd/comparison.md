# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-002-mapped-doc-cicd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-002-mapped-doc-cicd`.
- Identity schema: `2`
- target_skill_sha256: `aed48fddfc5ff065b4c42b3cee1081c6e2b92b1fe8557c1413f01e05c0f91ef0`
- eval_definition_sha256: `68a87fb5d229c5c451c4b7081adb9e28c9c2e68f2832958c12f8d53464b0ae13`
- metadata_sha256: `7e07a230c7002251551f1819be2a41bc3021e8c2cf111ff3359550f2215bd97f`
- fixture_sha256: `b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f170ac0192e8f110fe74b7c61766437cb8268e62c38697fb51b94a3db4467e5f`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | The with_skill trace reads build-pipeline.md in item_7 before reading change-map.yaml content in item_8, so it did not first hit the map and then read the mapped document. |
| `verifies_against_code` | PASS | The locked fixture has validation_command = verify in pipeline.rules and test in the documentation; with_skill identifies the conflict, selects verify, and explains that test must not be used. |
| `treats_unverified_as_low_trust` | PASS | with_skill explicitly identifies last_verified_version: unverified, treats the document as low-trust navigation, and bases the command on pipeline.rules; it also reports the missing verify runtime evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=7b1a8a0b1efb0246e73eb68bdb9b3f3828dec4f3c08d9eef48a1f0d15a4851cc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the unverified documentation conflict, verifies the command against code, and proposes verify, but reads the mapped build document before reading the change-map content.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=2c5673eca6469314ac5c3f888f54ae29725bdaebcab5e9cec6e7e25a8b1c1ede; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly selects verify and identifies the documentation conflict, but does not provide evidence of the unverified-document trust treatment or mapped-document-first process.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill execution order violates the mapped-document-first assertion.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
