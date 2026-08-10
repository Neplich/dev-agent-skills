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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `5754523ab6dc67a27703c13629b577962774677f13b55627e2b1a056ffc0bc71`
- Judge schema SHA-256: `6d4a307e5ec256ec68d2524f856808da877ec9503f513dcb2032388906c98b67`
- Eval definition SHA-256: `7be9a5847eaa9053c9f4277b2d57d5f5622208652decda6e30f3718fbfec04c5`
- Metadata SHA-256: `9bd3793631be46705766421244d6899c275c646d5598b1a7e8c43c8bec82ad4f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill delivery report records scope, feature path, platform version, unknowns, dependency blocker, and QA URL blocker in Preflight baseline before the blocked execution path. |
| `assertion_2` | PASS | Locked with_skill trace shows QA suite, flow index, case, and script reads before project exploration; the report records prior results/_reports as absent and reuses TC-001. |
| `assertion_3` | NOT_EXERCISED | The prescribed harness was invoked, but Vitest was unavailable before test discovery; no boundary input execution occurred. |
| `assertion_4` | PASS | The locked result and summary report provide a requirement matrix marking all five checks blocked with command and file evidence references. |
| `assertion_5` | PASS | The delivered report contains requirement matrix, execution path, evidence references, risk notes, and handoff decision sections. |
| `assertion_6` | PASS | Risk notes identify zero runtime coverage and uncovered items; handoff is blocked to Engineer/CI or QA environment owner with no bug-analyzer handoff. |
| `alignment_plan_gate` | PASS | The report confirms same-path PRD, TRD, and Confirmed IMPLEMENTATION_PLAN.md alignment for feature_path auth/login/login-form, with platform version v1.2.0-rc.1 confirmed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51; fixture_sha256=b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1; output_sha256=806581df988593a9e3210227ef70c8a6d446e6c8f4ecdeacce064f23d4983041; snapshot_sha256=cb2504462df934fec1b42c26073cb2a85365c8788e45a054d1929a7ea2f89424
- Behavior: Read and aligned the required documentation, reused TC-001, recorded structured evidence, and correctly reported a blocked run without filing a defect.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51; fixture_sha256=b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1; output_sha256=2d20b5666cb3445dbaa5363f581f8b87e5e18b925b0d44b2d98ffccd78a80d8a; snapshot_sha256=3dcd68c6a97112204b2cc9724bc3321d6a945ab51289f00dbfc4ff5da0d960e2
- Behavior: Attempted the harness and reported the dependency blocker, but delivered only minimal result artifacts without the structured preflight, matrix, risk, and handoff report.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore dependencies and rerun npm test -- login-boundaries.
- Next: If needed after harness restoration, provide the QA URL and perform browser fallback checks.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
