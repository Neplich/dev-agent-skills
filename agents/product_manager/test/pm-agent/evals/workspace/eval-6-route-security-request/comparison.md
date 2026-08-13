# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-006-route-security-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-6-route-security-request`.
- Identity schema: `2`
- target_skill_sha256: `f9ea1bade234ebfd780e1e4773d4808a60f7baa61920e5859daea2b146c1ce93`
- eval_definition_sha256: `33054d35eb6adb9b2259eedec7e911d8545eb305cd711e4206483eea10d13a8f`
- metadata_sha256: `b68604b9408ecd1ae4f680e8b6bea0f1c221e273dc6389c6b8150eff4b36f0d2`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `356a8438fe026d0b1352a3ef7467cbb1d1fa3bb6c089f0c3e64b4d4c5d3741fc`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1`
- Repository HEAD: `2ac10136f4ed18048058361915e66c52b4e038c5`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84ad07662e525000bb3bbf1da6aa3f2d49322c424326b70644431a72cdb52c55`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_security` | PASS | with_skill output explicitly classifies `request_type: security`. |
| `security_scope_first` | PASS | with_skill output records risk_surface, assets, permissions, data_flow, and remediation_expectations in the routing packet before describing the blocked downstream execution. |
| `security_handoff` | NOT_EXERCISED | The candidate correctly identifies `security-agent` as the owner and states execution is blocked because it is unavailable; a completed downstream handoff cannot be exercised without that runtime capability. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=241abc553a2571482b7f7e00f8a6499e24048f6544a8506686a1f067c15be04e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies the request, records the required security scope, and preserves the Security execution boundary while blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6967654719c224e5173481058a7a6a1b87ba55cc03e619dd2e6711b45102ad04; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a useful empty-repository security status and remediation list but does not classify or route the request through the security handoff workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Make security-agent available, then perform the Security handoff with the recorded scope and required output.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
