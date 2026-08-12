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
- target_skill_sha256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- eval_definition_sha256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- metadata_sha256: `8529cb6cbe6ab9523b4f7cf3b65440375e54cbaab5ce6a8376eb7a3bc4427f65`
- fixture_sha256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a8797f637904fc863710b298fe2fad8220a05aa0d79e70ed8997096bddf38e6c`
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
| `uses_same_path_pm_engineer_docs` | PASS | Raw trace shows direct reads of PRD.md, TRD.md, and IMPLEMENTATION_PLAN.md at the required nested paths. |
| `writes_nested_security_report` | PASS | Locked delivery snapshot contains docs/security/chat-interface/messages/history/search/appsec-checklist.md. |
| `includes_feature_path_frontmatter` | PASS | Locked report frontmatter contains the required feature_path, parent_feature, and feature_level values. |
| `does_not_invent_feature_directory` | PASS | The candidate used the confirmed existing feature directory and did not create a synonym or top-level feature directory. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The report and final output identify pm-agent handoff and issue filing, but no PM runtime or created issue is present; the later interactive step is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=4c3d9bfaf279daddb8b7c1d273d665b980cf54757e8c8ba3f122429e82319198; snapshot_sha256=bd8340a34dd5aa0424ac4fa15a94982b9ff6989c6b4698d4113a279511e6d964
- Behavior: Read the required feature documents, produced the correctly nested Security report with required frontmatter, and documented PM escalation for the confirmed security conclusion.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=e2ff2ec023e7159ae33facada9e53fe42352c086bbc61816fc5512c21cc0bc33; snapshot_sha256=99e5520f46c7e0bb7e267744fa11844e8b57d443103f1db3b873405573d0fbfe
- Behavior: Produced a report in the wrong engineer directory and did not satisfy the required Security report path or frontmatter workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: PM-agent classification and issue creation remain to be exercised when the required runtime or confirmation is available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
