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
- Repository HEAD: `33a503192c752d6227de1bc0d8d8a2e78e31cdf5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b87fb93cdb85ecb0436a61b1aedfcf9c8b41c4cd8f9eff41c412a3196c1d245`
- Skill overlay SHA-256: `56390e18f057b654978938889dac7daf0263eaaf39d741419b573d12bff2c198`
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
| `request_type_security` | PASS | With-skill output explicitly classifies the request as `request_type: security`. |
| `security_scope_first` | PASS | The initial routing block records `risk_surface`, `assets`, `permissions`, `data_flow`, and `remediation_expectations` before the recorded inspection steps. |
| `security_handoff` | NOT_EXERCISED | The candidate identifies `selected_owner: security-agent` and supplies scope plus `required_output`, but states the actual Security handoff is blocked because `security-agent` is unavailable. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=bbfd35cfac94950680718164abf278d36eb84e48715a2c77ecdb4bbd0f046a49; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Classifies the request as security and records the required scope fields first; downstream handoff is explicitly blocked pending security-agent availability.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4c9c8412e3b3bcd669399692ce9d4a56a3ffd26c4b8a9161e4d2c0f096c1eaa0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a substantive audit-style response about the empty repository but does not classify, scope, or hand off the request through the required security workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Install or make `security-agent` available, then perform the Security handoff with the recorded scope and required output.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
