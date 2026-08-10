# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Fixture SHA-256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `6313e0e9db35ff19a83ce603b2d6fd37c38949f33c4534ab8f41ff96a5baa978`
- Judge schema SHA-256: `dfbcad96e39d7a0ba2503c7d345d86b54a6c9e1188ff1c09f99476b24380e820`
- Eval definition SHA-256: `11398fbb2de74bd454f6e9c88338b5fcf6dffb0fd21436f1f6c99eaff5b1117d`
- Metadata SHA-256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | PASS | with_skill explicitly identifies manual-handoff.md and carries host repository, bounded scope, running-interface evidence, and required output into the routing decision. |
| `routes_manual_gen` | PASS | with_skill selects manual-gen and does not select any competing documentation specialist. |
| `preserves_manual_handoff_context` | PASS | with_skill preserves the handoff context, including request_type, change_tier, feature_path, host_repository, scope, evidence_sources, required_output, and blockers_risks. |
| `references_manual_gate_only` | PASS | with_skill names the manual-gen authoritative boundary and explicitly states that the router does not generate the manual or collect screenshots. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=6b9774387b72a24e7675e9facc5cc8574f0d6a15c65234d6780d91932c82d6e9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the handoff to manual-gen, preserves its context, records missing prerequisites, and stops at the router boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=2edc2ce94fefbe52e37fa690a15702383b918e0553f90ca742f8a909a74c08ec; snapshot_sha256=d51d19926c7ac16cfb8c3f40ec2a77d453a2de7330807b26ec117b50d5be3a2d
- Behavior: Generates and writes a manual with illustrative SVG assets instead of performing the required routing behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
