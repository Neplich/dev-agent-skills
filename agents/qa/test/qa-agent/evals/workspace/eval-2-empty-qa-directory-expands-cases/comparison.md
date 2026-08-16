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
- target_skill_sha256: `944bb130633ab2aa16595ed1d51c447f77cd06660f1aafc548f03bd9b22af162`
- eval_definition_sha256: `191bfa99acdac3657f309157a88a7fec7c17e9d659acf0a1a21ab3c03782508a`
- metadata_sha256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- fixture_sha256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9e5a2664238c6ad34a383d7e96fdb5938260274f9ddd6b1fcc0ee574c941d418`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill explicitly identified the exact feature path as lacking active TC, cases, scripts, and reusable QA assets. |
| `assertion_2` | PASS | with_skill selected spec-based-tester, passed the source files, QA memory, and environment guidance, and applied the specialist execution gates without re-requesting exploration authorization. |
| `specialist_gate_pointer` | PASS | The routing output named spec-based-tester as downstream owner and supplied the target files, environment instructions, and existing E2E memory for specialist handoff. |
| `assertion_6` | PASS | The trace and final routing packet show one narrow route, spec-based-tester, with no parallel QA skill execution or implementation changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=192e6dbdc0fedaa429a93fc8cb013b8ab467518edc9f743a70535149ef5e1328; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routed the authorized validation request to spec-based-tester, recognized the empty QA directory, passed the required context, and stopped at the specialist/runtime gates.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=81a09bc131436f2fc810607084a2a91f556519c9539e99f2c5a0312a621084ce; snapshot_sha256=c534a01edbc59e15c66ea958cb7ae66300467e0b710be272b7f448783963c21a
- Behavior: Fresh baseline independently created QA test assets and described blocked browser execution, rather than demonstrating the specialist-routing behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
