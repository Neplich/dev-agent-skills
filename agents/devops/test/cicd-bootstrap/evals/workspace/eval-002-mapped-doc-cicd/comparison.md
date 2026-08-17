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
- target_skill_sha256: `b41596991874aec0c37e12acb656078a02504e51d6536f47c1befab8e1f38b4a`
- eval_definition_sha256: `68a87fb5d229c5c451c4b7081adb9e28c9c2e68f2832958c12f8d53464b0ae13`
- metadata_sha256: `7e07a230c7002251551f1819be2a41bc3021e8c2cf111ff3359550f2215bd97f`
- fixture_sha256: `b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `777451b1778a899115de1846bd3248acc1a8fef07fa6857039ca7e40cdac46e8`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace item_7 reads change-map.yaml, then its required build-pipeline.md, before rereading pipeline.rules; no unrelated site-document traversal is shown. |
| `verifies_against_code` | PASS | with_skill locked output and trace identify the document's `test` claim, reread `validation_command = verify`, reject unsupported `test`, and report `verify` as the supported command. |
| `treats_unverified_as_low_trust` | PASS | with_skill locked output identifies `last_verified_version: unverified` as low trust and bases the command on the rules file, while noting no verifiable test/build entry supports `test`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=754da0e306a4129105bc376fc18db857af2a704ffba613ef65cb7a342959d5c5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly follows the mapped evidence chain, treats unverified documentation as low trust, verifies the command against code, and reports `verify`; it appropriately pauses workflow creation pending the required handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=08a3ffdcb2251091cdf30040590082a976faabcf76e7e71f7124b4bb2d5a5ba4; fixture_sha256=b0f5ab103062d754c225176fd1995f4f428e9f29340584ac86077ed978dc1482; output_sha256=11a28bd75b880df0d3269176698dd5fc4826ead3520fc953a53af5d99a3a7b4d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identifies the code/document mismatch and reports `verify`, but does not provide the with_skill lane's explicit handoff-gate and low-trust process context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
