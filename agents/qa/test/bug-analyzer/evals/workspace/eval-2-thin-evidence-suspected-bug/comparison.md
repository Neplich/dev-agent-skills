# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Identity schema: `2`
- target_skill_sha256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- eval_definition_sha256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- metadata_sha256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- fixture_sha256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `086365b086fd130d9ef17a34e69f11d6786884f09ea0525a080792033b47d5cb`
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
| `keeps_status_unconfirmed` | PASS | With-skill output explicitly classifies the report as `suspected / needs more evidence` and low confidence; the locked snapshot preserves that status and does not claim confirmation or reproducibility. |
| `separates_impact_from_confidence` | PASS | The locked snapshot separately records evidence status, low confidence, severity rationale, and potential user impact, while noting impact is not proven. |
| `requests_decisive_evidence` | PASS | The locked snapshot requests reproducible steps, expected/actual behavior, environment and version details, plus screenshots/recording, Console, Network, logs, and related traces. |
| `avoids_confirmed_bug_write` | PASS | The only persisted artifact is a clearly labeled unresolved investigation record; no GitHub issue or confirmed bug was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=12c0d6fc648fac8067859050fda4231e41ea76ac402ea2565edb892c1072f5e0; snapshot_sha256=8da5b5359a1814648e06910a279dbb92e29bce1cb58121236d1999f60e214a44
- Behavior: Correctly keeps the report unconfirmed, separates confidence from impact, specifies decisive evidence to collect, and writes only an unresolved investigation record.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=18a11fa98505803d529cc9a481a1ebdfe2446365e1e0f7d80b7e68938834c9ab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also correctly avoids confirming the bug and suggests evidence collection, but provides no persisted investigation artifact.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
