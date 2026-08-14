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
- target_skill_sha256: `87273b18e32710512ee493a3e80a098f8b357ae29e71e4e0a6f3bdb4e8e38c08`
- eval_definition_sha256: `191bfa99acdac3657f309157a88a7fec7c17e9d659acf0a1a21ab3c03782508a`
- metadata_sha256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- fixture_sha256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c61dc207829993f3cf5c3bb3c732dc39c76754cabec6f70bf1bd90a868f073f6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill identifies the target QA memory as having no executable cases/scripts or historical results/reports and retains the correct nested feature path. |
| `assertion_2` | PASS | with_skill carries the target source files, environment instructions, credential reference, feature flag, execution entry, and specialist gate context without re-asking for authorization or returning blocked. |
| `specialist_gate_pointer` | PASS | with_skill explicitly hands follow-up case creation, execution, and evidence archival to spec-based-tester, while preserving QA memory and environment context. |
| `assertion_6` | PASS | with_skill selects only spec-based-tester as the primary route, keeps execution within QA ownership, and makes no implementation changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=e50cb74d44e52847e3922bd8c28ee0aede73d6fbce43fbda3434832d48e718ff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the authorized validation request to spec-based-tester with the required scope, source materials, QA memory condition, environment gate, and ownership boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=86bf6d6d38c1b0b08caad8f2ea729854723de9fcc78e197fee180c1944597b47; snapshot_sha256=7fa49c17cb23077ce09c2431f1edd376f1924b860443c5779001b77070f74199
- Behavior: Created QA artifacts directly and reported browser checks blocked; it did not provide the specialist-routing behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
