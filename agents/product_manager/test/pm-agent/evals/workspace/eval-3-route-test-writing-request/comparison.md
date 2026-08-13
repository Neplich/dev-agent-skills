# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-003-route-test-writing-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-3-route-test-writing-request`.
- Identity schema: `2`
- target_skill_sha256: `28ec452f7594200030ea15ffdc8d5edc9ae2298318457884574b818964824cf6`
- eval_definition_sha256: `5eef99797df77f0e561572b46c57557f7c3ae080a7078c558efac33693901a22`
- metadata_sha256: `48e1e31078cfd6a23e5c1bdb5481d8f4c6428eb757f9b42750f6377a78297239`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4bea92cb3e04f7ad6bcf4e0dcdb3aa7c06af7bec325a6bea731363f44bd4e944`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8041f8266999d0ba9597ccc13e0354e28fcccb4a3b921ae9b5b9d1e08fe1da7b`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_validation` | PASS | The with_skill output explicitly classifies the request as `request_type: validation`. |
| `test_basis_first` | PASS | The output records `entry_basis: missing`, `source_documents: []`, and explicitly states that PRD/TRD/acceptance evidence is unavailable, so testing is blocked pending that basis. |
| `qa_or_test_writer_handoff` | NOT_EXERCISED | The candidate does not perform a QA/test-writer handoff; it identifies missing documentation and an unavailable qa-agent, deferring re-entry until the prerequisites are supplied. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=065a4e7d6fec70939a480beefc6badfac2a167afa7acc7f170988ab929f7015e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the request as validation, checks for testing basis, reports missing evidence, and stops without mutation or premature handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=41ce2f6c85329ca0458e157f3ea8b483c462eabd617c524a6719a61204f63f66; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline only reports an empty repository and inability to proceed; it does not classify the request or establish a testing-basis gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the refund code, existing tests, and PRD/TRD/IMPLEMENTATION_PLAN or acceptance evidence.
- Next: After expectations are stable and the QA/test-writer runtime is available, perform the handoff and test execution.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
