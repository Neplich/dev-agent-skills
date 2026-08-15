# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c` from `agents/security/test/appsec-checklist/evals/workspace/eval-004-feature-path-report`.
- Identity schema: `2`
- target_skill_sha256: `9ac7059a9a39550256d4de1ed82086d7f6b3c81bd069d831f0bf87ce02417c58`
- eval_definition_sha256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- metadata_sha256: `e6da11bf7f1086569860f05d808183f3f4b67cd66acd3889483549d3d15b0961`
- fixture_sha256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a8797f637904fc863710b298fe2fad8220a05aa0d79e70ed8997096bddf38e6c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d316d6849a82751d5c66c424af9993a42c304fe892fdb2411469b461bec624ee`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | PASS | Runner trace shows the PRD, TRD, and IMPLEMENTATION_PLAN were read from the required feature paths. |
| `writes_nested_security_report` | PASS | Delivery snapshot contains docs/security/chat-interface/messages/history/search/appsec-checklist.md. |
| `includes_feature_path_frontmatter` | PASS | Report frontmatter contains feature_path, parent_feature, and feature_level: 4 with the required values. |
| `does_not_invent_feature_directory` | PASS | The confirmed feature path and all required documents exist; the report uses the corresponding nested security path and does not invent a top-level synonym. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The report hands the conclusion and evidence back to pm-agent for classification and PM-owned issue filing; actual issue creation is not exercised because no issue-tracker runtime or user confirmation is available. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=e1658253410424c196f35ac03540105fb0235c001ba10973fe67352507278827; snapshot_sha256=629eb3ebc547827fc393750d57ff01b479ff1274c330d277bed2ac64fae2c6c5
- Behavior: Read the required feature documents, identified the security risks, and produced the correctly nested Security report with required frontmatter and PM escalation guidance.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=5d1b6b5e7b059f9e5ac8b6b643f21226b53ee694778f7b584a0ff78f8f674ab2; snapshot_sha256=e7ebc4a086b01d705f11f594b5a79cc6078a485e07fa6f3e07b661784acd5943
- Behavior: Produced a report under the PM documentation tree rather than the required Security path, despite including the feature-path frontmatter.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm PM classification and PM-owned issue creation when an issue-tracker runtime or user confirmation is available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
