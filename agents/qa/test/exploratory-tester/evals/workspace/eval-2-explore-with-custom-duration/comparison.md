# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3` from `agents/qa/test/exploratory-tester/evals/workspace/eval-2-explore-with-custom-duration`.
- Identity schema: `2`
- target_skill_sha256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- eval_definition_sha256: `234873760fb9d0649d16f54118fbf0383fa2955b9451730f9429892d78a6d7e0`
- metadata_sha256: `4befffc2e8037477b9995f3ded3869d8476cd9a66637621d7f8e8d3fc8c6fed3`
- fixture_sha256: `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `795b13efa8aba1d005ca8e2bf3be74790d6a011a9b79e7e9c3ef0bb4863b7e5d`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | Blocked report records the target surface, 5-minute timebox, environment URL, heuristics, escalation signals, and runtime-unverified risks. |
| `assertion_2` | PASS | Blocked report records the TEST_SUITE/FLOW_INDEX read set, absent cases/scripts/history, confirms feature-update, and states no expansion occurred, so no index/TC/script update was needed. |
| `version_entry_and_subagent` | PASS | Report explicitly blocks on missing platform version, documents repo harness → Chrome/browser connector → Playwright fallback order, and states TC execution is delegated to a subagent when TC exists. |
| `assertion_3` | NOT_EXERCISED | No runtime errors were exercised because execution was blocked; therefore console/network/crash classification was not exercised. |
| `assertion_4` | PASS | The delivered report includes the planned execution-entry path, test scope, and references to the report, TEST_SUITE.md, and qa-env.md. |
| `assertion_5` | PASS | The delivered report distinguishes the unconfirmed toast risk and gives concrete follow-up requirements for platform/browser version and executable environment entry. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=ca9abf4a1e7898299f7776b44d1e5624d8385a6a506bd03dd7fc62b3f58e2bec; snapshot_sha256=0f9713f0ac22a865c4d54e4fd2b24903656d4ede18453dc01bd7a3dcbbb9faa9
- Behavior: Correctly gated the exploratory run as blocked, produced a structured evidence-backed report, and preserved the required QA routing and handoff information.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=769d356712f491b5e177225e96791f9a7f938d74cf27de93788a745c479776b0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Attempted a network reachability check, reported DNS failure, and provided only a prose summary without the structured blocked report or process evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the platform/browser version and an accessible executable QA entry point, then rerun the chartered exploration.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
