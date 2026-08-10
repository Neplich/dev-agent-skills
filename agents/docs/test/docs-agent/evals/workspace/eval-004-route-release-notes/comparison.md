# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e` from `agents/docs/test/docs-agent/evals/workspace/eval-004-route-release-notes`.
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `c7d3b6793c943fb4d4971cf0d6f11988326a2dff978353bf3c4327d4e24c17b7`
- Judge schema SHA-256: `73f4addc59ec16b0f91c6a70a2a767ce7f6b4ad72612ca19a2131095a0722114`
- Eval definition SHA-256: `6d935c2fabb41ac4d322f49d33294bd64934555c17ee2ff70a64426da58d1b41`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | FAIL | With_skill calls the handoff only pending verification and says it has not formed an executable Release Notes entry, contradicting the fixture's explicit target host, confirmed version/scope, evidence sources, and required output. |
| `routes_release_notes_generator` | PASS | The routing decision selects exactly release-notes-gen and sets the execution boundary to routing only, with no reassignment or GitHub Release execution. |
| `preserves_handoff_context` | PASS | The output preserves all required handoff values semantically, including release version and scope within confirmed_scope, plus request_type, change_tier, feature_path, host_repository, source_documents, evidence_sources, required_output, and blockers_risks. |
| `references_release_notes_gate_only` | PASS | It names the release-notes-gen authoritative gate, stops at the router boundary, avoids local skill paths, and does not reproduce detailed downstream protocols. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=8da24e3d37a046bb5c81cf9fb4ff14779d4575540c74ac587f285cdc7ca822ef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes to release-notes-gen and preserves the handoff, but incorrectly treats the complete entry basis as incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=7291f352950f5026d6b26c9ef3b95c3e069fdf22af8cbca4878e05f1791b25c3; snapshot_sha256=2e8880fc34e1f0bafb4a381c6e6e72559e7bb33387615c3fe64c60bbd23403fa
- Behavior: Generates a Release Notes file despite the router-scoped request and does not perform the required routing decision.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane incorrectly rejects the complete specialist entry basis documented in release-handoff.md.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
