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
- target_skill_sha256: `ad5f15f98798fd005013d9360ccfb1f546134b65d875e1399c704387da8bd759`
- eval_definition_sha256: `32b9d61e575fbee81406ffc68edbaec9418feec621754c8fca12fc2f2edd2c08`
- metadata_sha256: `228751d86855b3dcdb583bdc4a44c4a493c28334ed74368c030ddad805b1f314`
- fixture_sha256: `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3783048bfb479d6e8907a0e84c4199cb646178dd63c9a58d60ddd654db2122dc`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1f8ea470403a23486f27834f156d91882ffb60f2aff635a7aa34b64347c884e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The delivered report defines the surface as SearchPanel, FilterPills, and ResultsList; gives a 15-minute timebox; lists change-specific heuristics; and names escalation signals. |
| `assertion_2` | PASS | The report records the QA memory read set, including TEST_SUITE.md, FLOW_INDEX.md, cases/TC-001-filter-results.md, and the absence of scripts/results/_reports. The locked FLOW_INDEX update documents the files read and coverage implications; no new E2E case or duplicate script was created. |
| `assertion_3` | PASS | The report explicitly derives the 15-minute timebox from the user request, states that it did not start because QA_BASE_URL was unavailable, and prioritizes the changed surfaces plus the known keyboard-focus risk. |
| `assertion_4` | PASS | The report has separate Observed issues, Suspicious but unconfirmed signals, and Gaps not explored sections, and labels the environment and focus items as unconfirmed rather than product defects. |
| `assertion_5` | PASS | The report describes a chartered preflight path, the reused TC-001 smoke entry, the three intended probes, and explicit unexecuted UI boundaries; it contains no random-click log. Browser exploration was blocked before runtime execution. |
| `assertion_6` | PASS | The delivered exploratory-report.md contains charter, timebox, exploration path covered, evidence/preflight details, and recommended next actions, with reproducibility and escalation guidance. |
| `deduplicates_existing_flows` | PASS | The locked FLOW_INDEX update says to reuse TC-001, explicitly records that no duplicate TC was created, and the report states that no reusable case or matching script changes were needed; one-time observations remain in the report. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=df54569b3806b86d99b4dcc363e7837ca1475f2b6cf1c25c33833b895186e11a; snapshot_sha256=9655f39321c21bdd7c35a58721570dfa5cb832e9541e1d312e94b499f8d09904
- Behavior: Produced a structured, evidence-backed exploratory handoff; updated FLOW_INDEX without duplicating existing flows; correctly reported the runtime blocker and unexecuted UI areas.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=cdd8e0b54b1d080f029252a942d333eaccb8b17122f5788ff39c5f557a42648d; snapshot_sha256=296a5bfa420dbe55c7dec4357469a0939aaf1d862e7ce66e70067b0b4701af4d
- Behavior: Produced a basic blocked handoff with charter and checks, but did not update the existing FLOW_INDEX or provide the same structured separation of evidence and coverage gaps.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide QA_BASE_URL and a browser-capable execution entry, then rerun TC-001 followed by empty-state and keyboard-navigation exploration within the 15-minute charter.
- Next: Capture per-TC runtime evidence and update the relevant report; escalate only reproducible product failures with exact steps and console/network evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
