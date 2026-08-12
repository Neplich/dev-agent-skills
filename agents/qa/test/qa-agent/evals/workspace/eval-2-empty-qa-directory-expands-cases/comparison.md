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
- target_skill_sha256: `23a4457fc9bf10be6976d98ea55607b47c6c623db1e20d5c73160d9f386c2a36`
- eval_definition_sha256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- metadata_sha256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- fixture_sha256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
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
| `assertion_1` | PASS | With-skill routing identified the existing QA directory as containing no executable cases/scripts/results, and did not fall back to another QA directory. |
| `assertion_2` | PASS | The routing block recorded the confirmed feature update and bounded exploration authority, passed source, QA memory, environment, credential-reference, and execution-entry context to spec-based-tester, and preserved the specialist gate without re-asking. |
| `specialist_gate_pointer` | PASS | The output selected spec-based-tester as the specialist execution owner and preserved its authoritative E2E gates and handoff boundary. |
| `assertion_6` | PASS | Exactly one narrow route, spec-based-tester, was selected; no parallel QA skill execution or implementation repair was performed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=66f7ca854b4ab8f80940e75ff69cb5a6f576f720df18173556a3ef398388add8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routed to spec-based-tester, identified the empty QA baseline, and stopped at documented specialist gates without creating artifacts or claiming execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=ef7cb515ee5428e1fc9ce875bfcb9a69af6c75f50fc5410172f983f8cf74dd4a; snapshot_sha256=c3d8793c9df408a0e72dea96b2099affb95eb1ccff78983f842ae3023e3c81bd
- Behavior: Created QA suite and flow artifacts despite the empty baseline and bypassed the required routing/specialist gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the missing specialist-gate materials before continuing E2E case generation or execution.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
