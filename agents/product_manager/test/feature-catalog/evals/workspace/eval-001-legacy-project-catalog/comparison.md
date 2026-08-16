# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Identity schema: `2`
- target_skill_sha256: `217c9b057b0819a52534f84f10e4d4a1bc905c2af1e21214f5f09bf51cb17566`
- eval_definition_sha256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- metadata_sha256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- fixture_sha256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6731c51ff9f69981e5ade0a40fa5fb4f93b6c439e428212a1b46155c6fa123f1`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6cef39f1b1cce23592397054fa6d427258c02b6778c43df49e227da056eafd0d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | NOT_EXERCISED | With-skill output correctly pauses for project-scope confirmation; no formal docs were created, but the feature-catalog draft itself was not yet produced. |
| `evidence_and_confidence` | NOT_EXERCISED | No candidate feature entries were produced because the workflow is awaiting scope confirmation. |
| `business_capability_naming` | NOT_EXERCISED | No candidate feature entries were produced because the workflow is awaiting scope confirmation. |
| `open_questions_present` | NOT_EXERCISED | No candidate feature entries or uncertainty questions about feature ownership were produced because the workflow is awaiting scope confirmation. |
| `confirmation_gate` | NOT_EXERCISED | The output asks for project-root scope confirmation, not feature_path confirmation; the later feature-catalog gate cannot yet be exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=647d51139ca6ae9899b1ff534d40b927405ebd97021c4fad794ace329a8c0aaf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Paused at the appropriate project-scope confirmation step with no workspace mutation or formal documentation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=690886cd125c181d68eea06e16a629302e72a52200724c6e5c33c5c9cc727b25; snapshot_sha256=f039b905d82d3e1493f54d0b2a3a09cc76a4ab0e1c32620fd2cba9049224c868
- Behavior: Produced and linked a formal feature catalog and modified README without a confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: After scope confirmation, produce an explicitly pending feature-catalog draft with evidence, confidence, business-capability names, unresolved questions, and a feature_path confirmation gate.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
