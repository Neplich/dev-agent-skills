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
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `5eef99797df77f0e561572b46c57557f7c3ae080a7078c558efac33693901a22`
- metadata_sha256: `d6163be77f09e049698e1a9f603c0cebbddd5b607c316831117c3ef1a972dcb0`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4bea92cb3e04f7ad6bcf4e0dcdb3aa7c06af7bec325a6bea731363f44bd4e944`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c72e4953b9374b62d28ad5c8580760fdd7805ace75b88ad1b4a44c32bbe75f3f`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_validation` | PASS | The with_skill output explicitly classifies the request as `request_type: validation`. |
| `test_basis_first` | PASS | The with_skill lane checked for PRD/TRD/test-spec and handoff evidence, found none, recorded `entry_basis: blocked` and `source_documents: []`, and did not proceed to test creation without a confirmed basis. |
| `qa_or_test_writer_handoff` | NOT_EXERCISED | No stable source documentation or expected behavior was available, so the candidate correctly required confirmation before any QA/test-writer handoff. The handoff stage was not reached. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c26077855cd312c46c86d3b49cc918032ff1ed33f4f83ccdd0b0f824e3a20b14; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request, inspected for required evidence, and blocked downstream testing until repository content and behavior sources are provided.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c94b5e63d884e95899ceed848eb655287ce240fda6ea2137f25bc9e40ef2428f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Detected the empty repository and stopped, but did not provide the validation classification or structured evidence gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide or mount the project repository and an approved PRD, TRD, implementation plan, or acceptance record; then perform the QA/test-writer handoff once expectations are stable.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
