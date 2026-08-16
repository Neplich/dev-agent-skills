# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7` from `agents/qa/test/exploratory-tester/evals/workspace/eval-1-explore-web-app`.
- Identity schema: `2`
- target_skill_sha256: `a0ccbf8ef4a1c709d054888b55b087565575c66027bff8bd5b33273b116324d3`
- eval_definition_sha256: `32b9d61e575fbee81406ffc68edbaec9418feec621754c8fca12fc2f2edd2c08`
- metadata_sha256: `228751d86855b3dcdb583bdc4a44c4a493c28334ed74368c030ddad805b1f314`
- fixture_sha256: `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3783048bfb479d6e8907a0e84c4199cb646178dd63c9a58d60ddd654db2122dc`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `649841709df98de32c59aff088c94eff0d9bbe6820d42c21a8e49cd3cf9838cb`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The locked report defines the changed SearchPanel, FilterPills, and ResultsList surface; uses the requested 15-minute timebox; states heuristics for filtering, empty states, and keyboard focus; and defines escalation for reproducible behavior with evidence. |
| `assertion_2` | PASS | The captured trace shows the existing TEST_SUITE.md, FLOW_INDEX.md, and TC-001 case were read before delivery. The report records that no scripts existed, reuses TC-001, and the locked FLOW_INDEX snapshot documents the source files and coverage implication. |
| `assertion_3` | PASS | The report uses the context-provided 15-minute duration, explicitly records that the timebox did not start because preflight was blocked, and prioritizes the changed surfaces plus nearby result-navigation risk. |
| `assertion_4` | PASS | The locked report has separate Observed issues, Suspicious but unconfirmed signals, and Gaps not explored sections, and explicitly avoids treating the documented focus risk as a defect. |
| `assertion_5` | NOT_EXERCISED | The chartered execution path and planned probes are documented, but no browser session or application interaction occurred because QA_BASE_URL and a runnable entry point were unavailable; actual exploratory paths therefore cannot be verified. |
| `assertion_6` | PASS | The locked delivery includes a charter, timebox, feature scope, evidence/preflight basis, exploration path, explicit gaps, blocked status, and recommended next actions for rerun and escalation. |
| `deduplicates_existing_flows` | PASS | The report reuses TC-001, states that no new case or matching script was needed, updates FLOW_INDEX.md incrementally, and keeps unexecuted observations in the exploration report. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=aa29333eb088c8c5caec220ab9b43510a94e8634bc77339e513377621211d2c6; snapshot_sha256=4a947b77555cd3521253e136ef467e57770db42148b754cfcc2d0b668a5da3ab
- Behavior: Produced an accurate blocked exploratory handoff, updated FLOW_INDEX.md, separated confirmed and unconfirmed evidence, and avoided claiming browser execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=8f7f9b5ff498c775434071b7048572159e0401175a0bdb3a1eb7099f7001e684; snapshot_sha256=eb68c1af299a46a17381a7c03e43238893222a89448b6e2fb18777ee3536b2df
- Behavior: Produced a blocked handoff with a useful exploratory matrix and evidence plan, but did not provide the with_skill lane's structured report and FLOW_INDEX update.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Set QA_BASE_URL and provide a runnable application or test entry point.
- Next: Rerun TC-001 using the recorded charter and capture filtering, empty-state, and keyboard-focus evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
