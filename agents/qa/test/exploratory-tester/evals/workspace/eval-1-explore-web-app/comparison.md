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
- target_skill_sha256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- eval_definition_sha256: `32b9d61e575fbee81406ffc68edbaec9418feec621754c8fca12fc2f2edd2c08`
- metadata_sha256: `228751d86855b3dcdb583bdc4a44c4a493c28334ed74368c030ddad805b1f314`
- fixture_sha256: `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3783048bfb479d6e8907a0e84c4199cb646178dd63c9a58d60ddd654db2122dc`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The locked report contains Surface, user-specified 15-minute timebox, heuristics, and escalation signals. |
| `assertion_2` | PASS | Trace shows QA memory files were read first; no new E2E scenarios were created, and FLOW_INDEX was updated incrementally. |
| `assertion_3` | PASS | The report derives the 15-minute timebox from the prompt and prioritizes SearchPanel, FilterPills, ResultsList, focus, and empty-state risks. |
| `assertion_4` | PASS | The report separately includes Observed issues, Suspicious but unconfirmed signals, and Gaps not explored, without labeling unconfirmed risks as defects. |
| `assertion_5` | PASS | The report documents a chartered exploration path and preflight evidence, explicitly records browser execution as blocked, and provides planned boundaries rather than random-click logs. |
| `assertion_6` | PASS | The delivered report contains charter, timebox, exploration path covered, evidence used, and recommended next actions for escalation handoff. |
| `deduplicates_existing_flows` | PASS | The existing TC-001 flow was reused, FLOW_INDEX was updated, and no synonymous TC, case, or script was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=f024748f651be20d49f75a22cc53521892b771dcc09e6b168ca89d7dfd62a9d8; snapshot_sha256=ff450fa4bc0b923accd2978b7f7f7aefb8bf0dc817de5a4977ef577851456d75
- Behavior: Produced a structured blocked exploration handoff and incremental FLOW_INDEX update with required charter, evidence, risk separation, and follow-up details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=dd2695cfbe61f9d1ebeff468bc10485bfd248e344d296abd8da000d5527276b9; snapshot_sha256=81a20894feedebb6a9c9e435a4e4ea517239fde8aa92219e7e5dcf2719da2c0c
- Behavior: Produced a basic blocked handoff with planned coverage and reused TC-001, but without the fuller charter, evidence taxonomy, and FLOW_INDEX handoff detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
