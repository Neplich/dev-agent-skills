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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `5eef99797df77f0e561572b46c57557f7c3ae080a7078c558efac33693901a22`
- metadata_sha256: `d6163be77f09e049698e1a9f603c0cebbddd5b607c316831117c3ef1a972dcb0`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4bea92cb3e04f7ad6bcf4e0dcdb3aa7c06af7bec325a6bea731363f44bd4e944`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `18890b0f7019a064bb6b93c6d2a7d316b9f13976166a66df2dd5dd2de14400f0`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_validation` | PASS | With-skill output explicitly sets `request_type: validation`. |
| `test_basis_first` | PASS | The candidate inspected the workspace and documented that PRD/TRD and related approved test-basis documents were absent, leaving `source_documents: []` and blocking test implementation before any handoff. |
| `qa_or_test_writer_handoff` | NOT_EXERCISED | The candidate conditionally identifies Engineer/test-writer as the next owner only after product/technical expectations are confirmed; the required source documents and runtime evidence are missing, so the actual handoff was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9b84a91a533954b22d2a169546f637f61d66441e65498a2d4f8ac235ec816b3a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request as validation, checked for an approved testing basis, and blocked implementation/handoff until expectations and source documents are available.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=53b07b9bd52ff76711ffe4f8d05823ea36763c8650ead7105fc367354a97069f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported the empty repository but did not classify the request, establish the testing-basis gate, or provide a conditional downstream handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the refund-flow implementation/tests and an approved PRD, TRD, implementation plan, or acceptance record; then confirm the stabilized expectations before handing off to Engineer/test-writer.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
