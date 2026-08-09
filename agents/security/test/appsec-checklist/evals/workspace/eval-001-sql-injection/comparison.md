# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6` from `agents/security/test/appsec-checklist/evals/workspace/eval-001-sql-injection`.
- Fixture SHA-256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `01ca86a4951823e3b6c703072ce5be09764c747ae9938b66975b80e4d41e39dd`
- Eval definition SHA-256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- Metadata SHA-256: `c7304df99ba027e455b94ef86d8c2964c99813b4b7afb5bd532e0bf494b29d15`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | The with_skill report identifies SQL injection via direct interpolation of req.query.name into SQL at src/api/user-search.js:2-4. |
| `evidence_and_impact` | PASS | The report traces the HTTP parameter-to-database path and explains unauthorized directory reads plus conditional data modification, destruction, and availability impact. |
| `severity_rationale` | PASS | It assigns Critical severity and supports it with authenticated reachability, predicate manipulation, PRD violations, affected assets, and conditional driver/database impacts. |
| `remediation` | PASS | It recommends parameterized queries, validation, wildcard handling, least privilege, disabled multi-statements, and concrete regression tests. |
| `writes_protocol_shaped_security_report` | PASS | The locked delivery_snapshot contains docs/security/user-search/appsec-checklist.md with frontmatter including feature, feature_path, version, and date; an Executive Summary with finding count, severity distribution, and posture; and location, risk, remediation, and verification sections. Git evidence shows no other files changed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=40f3a74ff0a24f1c3a1d683915259cd59c8fd2c6ab11f0800fe90dbd13e93135; snapshot_sha256=ad8b8df94941228c8b06201eaff840e6999e9fc43b36e88e87e3af37b903911c
- Behavior: Produced a protocol-shaped security report identifying the SQL injection with code evidence, impact, severity, remediation, and verification steps; no forbidden source or PM document mutations are evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=fb6e859f5c9c3ba44d8dfee7f7d50b9f54c22fab3d07409cfe428ce58154a15b; snapshot_sha256=0e6e4c5a3dbc08dcc9a5b956562aeec158e242d1efb7a297a8fc16c20d0659fa
- Behavior: Identified the main SQL injection and additional wildcard/resource risks and delivered a report, but the locked report lacks the required frontmatter and Executive Summary protocol structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
