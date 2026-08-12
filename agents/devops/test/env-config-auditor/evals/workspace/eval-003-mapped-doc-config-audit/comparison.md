# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Identity schema: `2`
- target_skill_sha256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- eval_definition_sha256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- metadata_sha256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- fixture_sha256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
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
| `reads_mapped_docs_first` | PASS | Trace shows the change-map was read, its required_docs resolved to docs/site/api/runtime-config.md, and no unrelated documentation directory was traversed. |
| `verifies_against_code` | PASS | The candidate records the optional documentation claim, the required code rule from src/config/required.env, the conflict, and the bounded risk that runtime startup blocking cannot be established without a loader or test. |
| `treats_unverified_as_low_trust` | PASS | The candidate explicitly identifies last_verified_version: unverified as low-trust navigation and does not rely on the document over the code fact. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=b9a4eed9300c26deaf6dda21f917bcb8a8cb8a81e3c2777e9c71bfc91041dd7b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly audits the mapped document against the configuration definition, preserves the conflict, and treats unverified documentation as low trust; it pauses before producing a broader operational report due to an asserted handoff prerequisite.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=325da3b52b3042d098ca6de898236400ef05dfb53ef5c9522b37b607ace4d7a6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline independently reaches the same configuration conflict and requiredness conclusion, with a fuller prose recommendation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
