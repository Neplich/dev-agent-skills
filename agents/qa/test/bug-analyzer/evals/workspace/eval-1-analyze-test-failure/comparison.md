# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca` from `agents/qa/test/bug-analyzer/evals/workspace/eval-1-analyze-test-failure`.
- Identity schema: `2`
- target_skill_sha256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- eval_definition_sha256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- metadata_sha256: `e96ab79b6862e4b82cb2cc5b58266d1ce1ed35caa4271d16c371f2d1b6443e6f`
- fixture_sha256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `84f20ca3637061984a451201365104813c56f53ca0b37a9fb14c70d8de0d29b1`
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
| `assertion_1` | PASS | Locked delivery snapshot’s Evidence table records the scenario, error message, stack trace status, screenshot status, console, limited network evidence, trace status, and environment/build context before classification. |
| `assertion_2` | PASS | The artifact uses the required `suspected / needs more evidence` evidence-status vocabulary and separately records `Confidence: Low`; it does not conflate the axes. |
| `assertion_3` | PASS | The artifact gives High severity with an impact rationale and separately explains Low confidence based on the single observation and missing server-side evidence. |
| `assertion_4` | PASS | The locked delivery snapshot contains a durable Markdown artifact at `docs/qa/login-refresh/bug-login-form-500.md`; no GitHub issue was created. |
| `assertion_5` | NOT_EXERCISED | The artifact explicitly states the log documents only one observation and that stable reproducibility is unconfirmed, so the condition requiring reusable E2E coverage is not exercised. |
| `assertion_6` | PASS | The artifact includes potential user/system impact, implementation/release impact, and evidence references to both fixture files and specific lines. |
| `non_e2e_report_path` | PASS | The delivered path is `docs/qa/login-refresh/bug-login-form-500.md`, has no date in its filename, and is not under `docs/qa-reports/`; the locked workspace has no E2E tree or versioned E2E execution requirement. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=e4796a9e34915ff9c2e18b2f170044d99432cd8a08c810965312b326f0b6ad2d; snapshot_sha256=aa2ade1e6f8bba42cd9ac8988702bae2d2bf00991011ee1fda438fa423c18e09
- Behavior: Created a durable, evidence-grounded Markdown defect report with separated classification, severity, confidence, impact, and references; correctly deferred reusable E2E coverage because reproducibility was unconfirmed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=6d4b70654926dee40f8db29f979d0a31b54615c8f2950e9897a171595c236c5e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a useful prose defect report with severity, reproduction, impact, and evidence limitations, but no durable artifact and no explicit separate evidence-status/confidence fields.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain an additional reproduction and the missing server-side stack trace before exercising the reusable E2E coverage assertion.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
