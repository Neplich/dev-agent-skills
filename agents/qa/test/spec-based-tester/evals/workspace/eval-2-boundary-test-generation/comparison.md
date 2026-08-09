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
- Fixture SHA-256: `b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1`
- Prompt SHA-256: `fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `fda3e87e887ba889a897540771dbb1fdc6d424a530b084850bba0cba716a1567`
- Judge schema SHA-256: `6d4a307e5ec256ec68d2524f856808da877ec9503f513dcb2032388906c98b67`
- Eval definition SHA-256: `7be9a5847eaa9053c9f4277b2d57d5f5622208652decda6e30f3718fbfec04c5`
- Metadata SHA-256: `9bd3793631be46705766421244d6899c275c646d5598b1a7e8c43c8bec82ad4f`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The report records scope, environment/platform, confirmed assumptions, unknowns, dependency blockers, and browser-URL blockers before execution. |
| `assertion_2` | NOT_EXERCISED | The snapshot records the required QA documents and absent historical results/reports, but locked evidence cannot prove the required read order or user-confirmation gate. |
| `assertion_3` | NOT_EXERCISED | The documented harness was invoked, but missing Vitest prevented boundary execution; the later validation step requires runtime recovery. |
| `assertion_4` | PASS | The delivered report contains a requirement matrix with blocked status and per-check evidence references. |
| `assertion_5` | PASS | The delivered report includes requirement matrix, execution path, evidence references, risk notes, and handoff decision sections. |
| `assertion_6` | PASS | The report records risks and uncovered checks, identifies no confirmed failures, and explicitly says not to hand off to bug-analyzer. |
| `alignment_plan_gate` | PASS | The report confirms PRD, TRD, and IMPLEMENTATION_PLAN.md exist under the same feature path and are Confirmed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51; fixture_sha256=b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1; output_sha256=296393a812bd6a8a4b6f24afc40559ac5f74dc1d06a2853b96880304617346a4; snapshot_sha256=7c1edf993d1f193542a2c9ff219cb33639155d7bd9168c730f716899c0027de3
- Behavior: Performed preflight alignment and QA-memory checks, invoked the preferred harness, recorded the environment block, structured evidence, and avoided unsupported defect escalation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51; fixture_sha256=b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1; output_sha256=2477ad8109d65899ee90721e789c64f621c1e3b0660a029e281587546b5c5c79; snapshot_sha256=896514c0958a563e9b177ced6237f86a9b11aff53053ff6eaf5c9fe8bda99b60
- Behavior: Recorded the harness blocker and unexecuted checks, but lacked the with_skill lane’s documented preflight alignment, structured report, risk notes, and handoff decision.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore test dependencies and rerun TC-001-login-boundaries.
- Next: Provide the configured QA URL and browser access if harness recovery is insufficient.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
