# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Identity schema: `2`
- target_skill_sha256: `14753ae64e96384b284b9c0b0f3a08e0639fc554929720623cd02fae3a9c29a0`
- eval_definition_sha256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- metadata_sha256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- fixture_sha256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6cb100241ab8151af36dbd15ed1bd54941ad005e84cbff29ba2242c5550d11ef`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace item_5 reads change-map.yaml, then its mapped profile-validation.md, then validation.rules; no unrelated document contents were traversed. |
| `verifies_against_code` | PASS | The output identifies the code limit as 64, the formal document's 80-character claim, both paths, the 16-character discrepancy, and its impact. |
| `treats_unverified_as_low_trust` | PASS | The output and trace explicitly identify last_verified_version: unverified and treat the documentation as blocked/low-trust while grounding the observed limit in code. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=e4551fe568927c40525f54b92b5500b0f10fa70ebdc4d58ec56cb9b8580ddc19; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly follows the mapped-document-to-code evidence path, identifies 64 versus 80, and treats unverified documentation as low trust.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=ba3e58216a49185ee78e7d242ff7b4441d518f42340a6db6e0a1f7796d2625e3; snapshot_sha256=5355930be7ce26894a4b39c5dee7d926e46b1264c9ad005d8928dfba71818f45
- Behavior: Fresh baseline modified formal documentation and change-map metadata, created a requirements matrix, and claimed completion.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm the product standard and provide the required PM/QA acceptance basis before formal pass/fail testing.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
