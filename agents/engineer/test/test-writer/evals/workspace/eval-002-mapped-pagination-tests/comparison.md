# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Identity schema: `2`
- target_skill_sha256: `8676e9bdfb5dcb168ade64b20ca31fd5f471aaa2778319375ec606582ddd34da`
- eval_definition_sha256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- metadata_sha256: `6a60b69beab2bdd4c854670cd54e7749219cde65551c8e29d984d322f4c34c88`
- fixture_sha256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
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
| `reads_mapped_docs_first` | PASS | Trace shows the change-map was read before the mapped pagination API document; the intervening repository scan listed filenames only and did not read unrelated document contents. |
| `verifies_against_code` | PASS | The locked source evidence reports default_page_size: 25 and maximum_page_size: 100, while the candidate explicitly identifies the document's 50-value conflict. The delivered tests assert 25, not 50. |
| `treats_unverified_as_low_trust` | PASS | The candidate explicitly notes last_verified_version: unverified, treats the document as conflicting low-trust evidence, and uses 25 from defaults.txt in the delivered assertion. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=1099252a8829a190f67e7ba3134613d489569193461297b2ba88beaf2f5158b3; snapshot_sha256=9efc0a5159331529a7b73bc24465606999da878b4dfba74142d554d6b2b6a360
- Behavior: Read the mapped documentation, verified the conflicting default against defaults.txt, and delivered four passing unittest boundary tests using the code value 25.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=862d2e2f610adebb22387d4a38e665a1a9fe9109dcdc00975ceedd26fa480abc; snapshot_sha256=8b2a2534aac8e8dd5d4c0f659abcbbc141cc66fcde00d4ff929c9df5b1b73998
- Behavior: Also found the code/document conflict and delivered passing tests, but its trace does not establish the mapped-doc-first workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
