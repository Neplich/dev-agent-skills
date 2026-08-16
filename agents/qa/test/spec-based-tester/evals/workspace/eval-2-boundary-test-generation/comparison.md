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
- target_skill_sha256: `14753ae64e96384b284b9c0b0f3a08e0639fc554929720623cd02fae3a9c29a0`
- eval_definition_sha256: `7be9a5847eaa9053c9f4277b2d57d5f5622208652decda6e30f3718fbfec04c5`
- metadata_sha256: `9bd3793631be46705766421244d6899c275c646d5598b1a7e8c43c8bec82ad4f`
- fixture_sha256: `b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6d4a307e5ec256ec68d2524f856808da877ec9503f513dcb2032388906c98b67`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6cb100241ab8151af36dbd15ed1bd54941ad005e84cbff29ba2242c5550d11ef`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The locked result records scope, feature path, environment assumptions, missing URL/source dependencies, and blocked conditions before the execution path. |
| `assertion_2` | PASS | Runner trace shows QA memory and required QA documents were read before project-file exploration; the delivery report records prior results and reports as absent before the run. |
| `assertion_3` | NOT_EXERCISED | The documented targeted harness was selected and attempted, but it stopped before test discovery because vitest was unavailable; no boundary case reached runtime execution. |
| `assertion_4` | PASS | The locked result and summary report mark all five checks blocked and provide execution-log, result, snapshot, and report references. |
| `assertion_5` | PASS | The locked result contains requirement matrix, execution path, evidence references, risks, and handoff decision sections. |
| `assertion_6` | PASS | The report identifies uncovered runtime validation, records risks and recovery steps, and explicitly withholds bug-analyzer handoff absent a reproducible product failure. |
| `alignment_plan_gate` | PASS | The locked preflight and result confirm same-path Confirmed PRD, TRD, and IMPLEMENTATION_PLAN.md alignment before execution. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51; fixture_sha256=b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1; output_sha256=bf815816179325c6ef689bcc693717ce2f81bfc570fd8f548ce54b09380a0f2b; snapshot_sha256=5949f169e36a828541649fe6cbeac0785856b8b7aa0bc037f53855b38eed1be1
- Behavior: Performed the documented QA preflight and evidence-first workflow, attempted the prescribed harness, correctly recorded all five boundary checks as blocked, and created durable result, snapshot, execution-log, and summary-report evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fca68fb7467bf000e3c38b2b867a8aeab7cf98cabe927e8e96f334144b3ecb51; fixture_sha256=b4127bff8b3b1c32e35f1a58623703ca5f4eb13030dd5763812f9d858500fda1; output_sha256=9455159127708c82b5d7924c3314240f4b989b467e12d13e18ae402217ea65c3; snapshot_sha256=d308b9e4288d1e69c07c1d55ce045673ed3147a6f405baf32b56d99d313165f4
- Behavior: Fresh baseline attempted the harness and recorded a basic blocked result, but omitted the structured preflight, requirement matrix, execution path, risk, and handoff reporting present in the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore/install repository test dependencies and rerun npm test -- login-boundaries.
- Next: If visible requirements remain uncovered, provide a configured QA application URL and browser access for fallback checks.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
