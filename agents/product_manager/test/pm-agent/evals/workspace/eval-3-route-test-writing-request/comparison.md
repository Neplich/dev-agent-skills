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
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3`
- Repository HEAD: `2197fe25a63cc5e24d3e8041ae0c777df624a155`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3a2a8f0ccc2a03fa28f50320f1effd3135a3ec1cbea6f6e65c09f7a1a3e755f1`
- Skill overlay SHA-256: `bee09702f1ef6acb446d218b58e5df43a1d40019b0d22a709e44c9ddb85f9b39`
- Judge schema SHA-256: `4bea92cb3e04f7ad6bcf4e0dcdb3aa7c06af7bec325a6bea731363f44bd4e944`
- Eval definition SHA-256: `4c0ee7c09752627d6057c1ccc0d45cb292b19c1428b51ca9513725150029cf5a`
- Metadata SHA-256: `48e1e31078cfd6a23e5c1bdb5481d8f4c6428eb757f9b42750f6377a78297239`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_validation` | PASS | With-skill output explicitly classifies the request as `request_type: validation`. |
| `test_basis_first` | PASS | With-skill output records `entry_basis: missing`, names the absent PRD/TRD/acceptance evidence, and blocks test work pending a confirmed source. |
| `qa_or_test_writer_handoff` | NOT_EXERCISED | No handoff occurs because the required source and stable expectations are missing; the output explicitly defers QA/Engineer handoff until the basis is confirmed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=eb625f59ce1ac52f42635fc8ab18e61e6954d8bbf9d7b9f6e6fbc4f9ed97d728; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routed the request as validation, checked for a test basis, and paused safely until source evidence and expectations are available.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3f7994fdecfb94451400a56972388597b7ae51d2d37508524058139c5273a4e3; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=63708b2006d92bbaf13cd36b24989defa1d6c1376b74dc5cd47f7eb4d0c6d129; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline only reported the empty workspace and stopped without validation routing or test-basis handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the refund implementation and PRD/TRD/implementation plan or acceptance record; then stabilize expectations and hand off to QA or a test writer.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
