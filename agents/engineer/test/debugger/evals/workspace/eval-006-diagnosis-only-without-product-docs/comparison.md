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
- target_skill_sha256: `8f85dae9526c56f3d9c6b946dd90d2d85718bee6a272309b91713955601d3385`
- eval_definition_sha256: `758141d0c7bdb4baf9183f3809ac543e55cf003c9bd32dee255fb5647551db21`
- metadata_sha256: `6b3da2f94834b818cd15e9684fbf0d27f2ddba927d4bee151c015473c9bae65d`
- fixture_sha256: `04552831783ca9e7820a306673ad1726c72045bfdd67319f31bdcea978edc2ec`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7bfbf16f369ab03a6fa6352e32724a77040ec0096019024e8c8efaca2c1f4c81`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `454ab746a611a03604fd13b7457fa564744030f0165ded716f10714ca9bf2196`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `3e75308618e40000064b1f17dc0f0b301f828ec4f2f128fc91b1ab1bc2382820`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_diagnosis_only_mode` | PASS | With-skill output explicitly states `mode: diagnosis_only` and `allowed_mutations: none`; locked git evidence shows no changes or untracked outputs. |
| `reports_unaligned_expectation` | PASS | With-skill output explicitly marks `expected_behavior_alignment: unaligned` and does not claim an `implementation_deviation`. |
| `uses_available_evidence` | PASS | The report cites `SessionStoreError: missing session table`, the `sessions` query, and labels the root-cause assessment with confidence while identifying remaining unknowns. |
| `returns_complete_diagnosis_report` | PASS | The report includes observed facts, direct evidence, root-cause conclusion and confidence, impact scope, unknowns, and a minimum next step. |
| `stops_without_repair_plan` | PASS | The output stops after diagnosis, with no repair plan, modification request, commit, push, or PR action. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=454ab746a611a03604fd13b7457fa564744030f0165ded716f10714ca9bf2196; fixture_sha256=04552831783ca9e7820a306673ad1726c72045bfdd67319f31bdcea978edc2ec; output_sha256=82260dc64c4f6abdd2ec653597b90da2636ec0fad4caecea098811f566bc97a1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete read-only diagnosis report with explicit diagnosis-only controls, unaligned expectation status, evidence-backed root cause, scope, unknowns, and a minimal read-only next step.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=454ab746a611a03604fd13b7457fa564744030f0165ded716f10714ca9bf2196; fixture_sha256=04552831783ca9e7820a306673ad1726c72045bfdd67319f31bdcea978edc2ec; output_sha256=2623a32b2260bc1b773957e654c8687c11f18e6ce95afa6eb72f08fa9d5881dc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a concise evidence-based cause but omitted the required diagnosis-only metadata, alignment status, structured complete report, and explicit stop framing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
