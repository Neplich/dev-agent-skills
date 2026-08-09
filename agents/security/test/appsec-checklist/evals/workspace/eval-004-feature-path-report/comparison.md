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
- Fixture SHA-256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `a8797f637904fc863710b298fe2fad8220a05aa0d79e70ed8997096bddf38e6c`
- Eval definition SHA-256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- Metadata SHA-256: `8529cb6cbe6ab9523b4f7cf3b65440375e54cbaab5ce6a8376eb7a3bc4427f65`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | PASS | Locked report lists the PRD, TRD, and IMPLEMENTATION_PLAN under the required feature path. |
| `writes_nested_security_report` | PASS | Delivery snapshot contains docs/security/chat-interface/messages/history/search/appsec-checklist.md. |
| `includes_feature_path_frontmatter` | PASS | Report frontmatter contains the required feature_path, parent_feature, and feature_level values. |
| `does_not_invent_feature_directory` | PASS | The report uses the existing nested feature directory and does not invent a top-level synonym. |
| `escalates_fact_changing_conclusion_to_pm` | PASS | Report includes a PM escalation payload, assigns classification and issue filing to pm-agent, and excludes direct Security issue filing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=6b7262db05e1cca1463380d76b3675fa6a2d9fcfca23607a98b5f346fe1c6ae1; snapshot_sha256=89badf4bee0864d9005220165ddc48bbdbb8f3aa39ed1e4b484e9bd2be1df3dc
- Behavior: Created the correctly nested Security report with required frontmatter, documented the security findings, and included PM escalation evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=d3ccb6fc325c212284af035ff05da713930c3aecc54fb8cf6bce0a1f695706ad; snapshot_sha256=7078a4a1bc6e57b28363079a63cc42fc5f9b39910d51e8c20da66bf8f9f161d8
- Behavior: Created an engineer-path SECURITY_REVIEW.md instead of the required nested Security report and did not provide the required PM escalation handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
