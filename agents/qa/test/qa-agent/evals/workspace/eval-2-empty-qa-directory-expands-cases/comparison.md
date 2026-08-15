# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Identity schema: `2`
- target_skill_sha256: `67401f0f5ce98032f224aebfb24715fe0d3d5f8bc92ca57ff320d37e3d49c72a`
- eval_definition_sha256: `191bfa99acdac3657f309157a88a7fec7c17e9d659acf0a1a21ab3c03782508a`
- metadata_sha256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- fixture_sha256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `3ff11c8e572c63705c91226f6db993f90ab7638bbaa39fb6677b573f386556da`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The with_skill output identifies the existing feature path and states the QA directory has no executable cases or scripts; raw trace confirms only TEST_SUITE.md and FLOW_INDEX.md were present. |
| `assertion_2` | PASS | It selects spec-based-tester, passes the target source files, environment instructions, QA memory, credential reference, and execution context, while preserving unresolved specialist gates without returning blocked or re-asking for exploration authorization. |
| `specialist_gate_pointer` | PASS | The output explicitly hands subsequent work to the selected spec-based-tester and keeps the router scoped to routing rather than creating artifacts or executing specialist work. |
| `assertion_6` | PASS | Exactly one narrow route is selected: spec-based-tester. The output defines non-goals excluding broad regression, bug analysis, and implementation fixes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=4c573e2985de79fdb87155b034950d7c85bd62cec9479490ea7b83d9e19ba912; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the authorized profile-settings validation request to one specialist with the required context and gates.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=6994445d0a3d1023efb243e14fdb5ac2a219a0b368097bc7fe49c2341abeb475; snapshot_sha256=33843de20c46d3456575d6cb78e00423b5da43f79b4cdacf4c725531d68cd5c2
- Behavior: Fresh baseline created QA artifacts directly instead of routing through the specialist boundary; browser execution remained unperformed.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
