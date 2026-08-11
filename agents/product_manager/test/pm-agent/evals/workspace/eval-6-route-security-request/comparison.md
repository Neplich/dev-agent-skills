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
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1`
- Repository HEAD: `e2d0e3e00078c297194828182b4d6445ecbb492d`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c658e8351498435bd5246b692fbf8a3a6d40caa45d6998b37785e6522243068b`
- Skill overlay SHA-256: `6e906e23fd0805526cda111a5e2e74eb02ce2f72534b3e384e90b10a34160090`
- Judge schema SHA-256: `356a8438fe026d0b1352a3ef7467cbb1d1fa3bb6c089f0c3e64b4d4c5d3741fc`
- Eval definition SHA-256: `33054d35eb6adb9b2259eedec7e911d8545eb305cd711e4206483eea10d13a8f`
- Metadata SHA-256: `b68604b9408ecd1ae4f680e8b6bea0f1c221e273dc6389c6b8150eff4b36f0d2`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_security` | PASS | The with_skill delivery explicitly records `request_type: security` for the permissions, dependency, and secrets review request. |
| `security_scope_first` | PASS | The with_skill routing packet explicitly records risk_surface, assets, permissions, data_flow, and remediation_expectations before the review conclusion. |
| `security_handoff` | NOT_EXERCISED | The packet selects `security-agent` and includes scope plus `required_output`, but the locked evidence states that security-agent is unavailable and `downstream_execution: rejected`; an actual downstream handoff is therefore not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b2c80393d4ce259b2b13fa0c26f1c572b5cbfe303fbe94d273abafed4843678b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request, recorded the required security scope, and prepared a Security routing packet; downstream execution was blocked by the unavailable security-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5d23cbe9ae828437cb8bcf75b0eb82b6aada6dc7cbf5bd84f3ecbd4c25d3290c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a sensible read-only repository-empty assessment but did not provide the required security classification, scope packet, or Security handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Make the security-agent stage available and complete the Security handoff using the prepared scope and required output.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
