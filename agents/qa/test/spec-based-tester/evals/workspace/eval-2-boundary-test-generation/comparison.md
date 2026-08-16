# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-002-boundary-test-generation`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1` from `agents/qa/test/spec-based-tester/evals/workspace/eval-2-boundary-test-generation`.
- Identity schema: `2`
- target_skill_sha256: `a902e30cb15a83b00f6e242ec0746a619c9c75741852be4c26efbe1dc710f3e3`
- eval_definition_sha256: `7be9a5847eaa9053c9f4277b2d57d5f5622208652decda6e30f3718fbfec04c5`
- metadata_sha256: `9bd3793631be46705766421244d6899c275c646d5598b1a7e8c43c8bec82ad4f`
- fixture_sha256: `b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6d4a307e5ec256ec68d2524f856808da877ec9503f513dcb2032388906c98b67`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2ae6df1e5892f15e69faa5eb27f67247be532cf172f30b6323b139a66d25acc0`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The locked result report records scope, confirmed assumptions, unknowns/blockers, and the same-path PRD/TRD/implementation-plan gate before the execution path. |
| `assertion_2` | PASS | The locked report states TEST_SUITE.md, FLOW_INDEX.md, the reusable case, script, prior results, and prior reports were read or recorded absent before execution. |
| `assertion_3` | NOT_EXERCISED | The prescribed harness was attempted, but vitest was unavailable before test collection; no boundary behavior was exercised, so this assertion is not exercised rather than failed. |
| `assertion_4` | PASS | The locked result contains a per-check status table with blocked statuses and traceable evidence links/references. |
| `assertion_5` | PASS | The locked report contains requirement matrix, execution path, evidence references, risk discussion, and handoff decision sections. |
| `assertion_6` | PASS | The locked report records uncovered checks and risks, and explicitly declines bug-analyzer handoff because no reproducible product failure was observed. |
| `alignment_plan_gate` | PASS | The locked report confirms same-path PRD, TRD, and IMPLEMENTATION_PLAN.md documents, all marked Confirmed, before scoped verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51; fixture_sha256=b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1; output_sha256=49277b4c591e9d3ea737312642d6f0973fc3ac55a1a85841896f9c36c8152335; snapshot_sha256=64598178ffec03b4b9f11063ecb0fdf0f961a471d62070194d71c4db5bf50f3f
- Behavior: The candidate followed the documented QA workflow, preserved structured evidence, accurately reported all five boundary checks as blocked, and avoided an unsupported bug handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51; fixture_sha256=b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1; output_sha256=3fbb849694c429be6068c5454e87c0f6d782383cd6f6708628c27eb4d935233a; snapshot_sha256=340fa04bde5dc760886f8ad0212f9a503aa0e1d6dd35d4f3bb1a24bebf964dd0
- Behavior: The fresh baseline also attempted the harness and recorded blocked results, but produced a thinner report without the full preflight, validation frame, structured matrix, and handoff documentation present in the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore test dependencies and rerun npm test -- login-boundaries.
- Next: If needed, provide the configured QA application URL and approved QA account reference for the documented browser fallback.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
