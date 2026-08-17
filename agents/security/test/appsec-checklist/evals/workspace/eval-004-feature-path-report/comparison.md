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
- target_skill_sha256: `412a68c0dfdb2d720e3447fdc4faf74b408d3de29706093a3a69fb0ca69d983c`
- eval_definition_sha256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- metadata_sha256: `e6da11bf7f1086569860f05d808183f3f4b67cd66acd3889483549d3d15b0961`
- fixture_sha256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a8797f637904fc863710b298fe2fad8220a05aa0d79e70ed8997096bddf38e6c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `035cdf3596c1888564523ed3d4e73116a3d2b231b30d91c462fb62cf6da52e05`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | PASS | With-skill trace shows the PRD, TRD, IMPLEMENTATION_PLAN, and src/search.ts were read from the canonical feature path. |
| `writes_nested_security_report` | PASS | Locked delivery snapshot contains docs/security/chat-interface/messages/history/search/appsec-checklist.md. |
| `includes_feature_path_frontmatter` | PASS | The locked report frontmatter contains feature_path, parent_feature, and feature_level with the required values. |
| `does_not_invent_feature_directory` | PASS | The candidate used the confirmed nested feature path and did not create a synonym or top-level feature directory. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The report and final message return the release-readiness conclusion and evidence to pm-agent for classification and PM-owned issue filing; actual downstream issue creation is not exercised because it requires the PM workflow/user confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=dabceb9af941a20b7d01ee1de44c249deb5aada821e412c74c37b480c8f8a939; snapshot_sha256=fcadc4bf7dff81b72e2b08d86d675be012c3663288e0cabcc1016e0f4f176ca9
- Behavior: Read the canonical PM/Engineer documents and source, wrote the correctly nested Security-owned report with required frontmatter, and escalated the release-readiness conclusion to pm-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=7872e35225db0ec0ca0d86c1e9be01151ceb36c24c0f3ae53c33262b2c49a0c3; snapshot_sha256=3aa38d69b1dc3a9d940f6282efe7b2ce87f430b52be3a2e38623ec1e6368fdf7
- Behavior: Produced a security review with relevant findings but wrote it under the Engineer feature directory instead of the required nested Security report path and did not provide the required PM escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: pm-agent must classify the escalation and, after required confirmation, create the tracking issue.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
