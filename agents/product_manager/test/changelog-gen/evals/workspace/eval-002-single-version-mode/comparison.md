# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Identity schema: `2`
- target_skill_sha256: `2ba8dad890b4a470e045fac5a77553d35f40494dd4f5ee0df778eda64ba0f881`
- eval_definition_sha256: `8e1f2a2b7cff1dcc676c7dcd6956883a0a24ee6d97754afcf56bc59fdaf06a61`
- metadata_sha256: `814184c8bd7a959b3f0695c85bef4dd34c73bd316a08d00ccc354207f37fabc9`
- fixture_sha256: `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `609660421781976ec561327c947a31da6f7d421bc63e99d2f3f00692dcdf763a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f75f5f8b8869cc572a0f69646861f4a54c0e1cb5775b8c2dac040f714114c1c9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | Locked with_skill file contains `## [v0.120.2] - 2026-08-05`. |
| `release_tag` | PASS | Locked release evidence specifies tag `v0.120.2`, matching the delivered heading and filename. |
| `pr_conventional_commit` | PASS | PR titles are cleaned of conventional prefixes; the retained `client` scope is explicitly permitted. |
| `breaking_change_breaking` | PASS | PR #302 is labeled `⚠️ **BREAKING**` in the delivered file. |
| `section` | PASS | Added, Changed, and Fixed sections each contain a PR entry; no empty section is present. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=30bf5157dd8ff3d27ac44caa3f8e7b19c1055205dfa2c20c7e13f4f8e773abc2; snapshot_sha256=76a876a0b38992a3479bcdd867af175829a42a29c810a13c6b90ad7d72560810
- Behavior: Generated the requested changelog file with the correct version/date, all three PR references, cleaned titles, and breaking-change marking.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=044d7d8a77ada4e4296d53576ae7f5a32edeeb57217e066fdb6676bba355edce; snapshot_sha256=1e6cf03524b4358f6211bca0df4515f33a57066e4a6bed368ddcd734e15d5438
- Behavior: Generated a changelog with all three PR references and cleaned titles, but omitted the required v prefix and breaking marker format.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
