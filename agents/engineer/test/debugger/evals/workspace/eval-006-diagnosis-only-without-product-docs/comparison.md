# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-006-diagnosis-only-without-product-docs`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `04552831783ca9e7820a306673ad1726c72045bfdd67319f31bdcea978edc2ec` from `agents/engineer/test/debugger/evals/workspace/eval-006-diagnosis-only-without-product-docs`.
- Identity schema: `2`
- target_skill_sha256: `218d8421a500762a8737dfd3f2bf066dd7538a5a365e0edae4e1ea20de7193fa`
- eval_definition_sha256: `758141d0c7bdb4baf9183f3809ac543e55cf003c9bd32dee255fb5647551db21`
- metadata_sha256: `dc64ddaa95e33b8545e5f9d6113ed40651e4122d43e178d7fd70fa1711ac86ca`
- fixture_sha256: `04552831783ca9e7820a306673ad1726c72045bfdd67319f31bdcea978edc2ec`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7bfbf16f369ab03a6fa6352e32724a77040ec0096019024e8c8efaca2c1f4c81`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `454ab746a611a03604fd13b7457fa564744030f0165ded716f10714ca9bf2196`
- Repository HEAD: `2ac10136f4ed18048058361915e66c52b4e038c5`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `fedd8e32348dc4f6f1f32b441d70612bfa38665135f0ba44f73fa280659d9268`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_diagnosis_only_mode` | PASS | The with_skill output explicitly states `mode: diagnosis_only` and `allowed_mutations: none`; delivery_snapshot is empty and git evidence shows no changes. |
| `reports_unaligned_expectation` | PASS | The report sets `expected_behavior_alignment: unaligned` and does not claim `implementation_deviation`. |
| `uses_available_evidence` | PASS | The report cites both fixture files, reproduces the missing-table error and `sessions` query, separates facts from inference, and labels confidence. |
| `returns_complete_diagnosis_report` | PASS | The report includes observed facts, direct evidence, root-cause judgment and confidence, impact scope, unknowns, and a minimum next step. |
| `stops_without_repair_plan` | PASS | No repair plan, mutation request, confirmation question, commit, push, or PR appears; the next step is read-only. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=454ab746a611a03604fd13b7457fa564744030f0165ded716f10714ca9bf2196; fixture_sha256=04552831783ca9e7820a306673ad1726c72045bfdd67319f31bdcea978edc2ec; output_sha256=0e50e0efb9fa9d89d2ff9d972b9d6c96238b3b196b2032f3a209da68c93aa6bf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Complete read-only diagnosis report with evidence-backed findings and no mutation or repair plan.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=454ab746a611a03604fd13b7457fa564744030f0165ded716f10714ca9bf2196; fixture_sha256=04552831783ca9e7820a306673ad1726c72045bfdd67319f31bdcea978edc2ec; output_sha256=5a007af7dae8c0865fca23a0a343a14417ef1a3231a96d23cd6c8ec85ea155f7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identifies the likely missing sessions table but lacks the required structured diagnosis-only report.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
