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
- Identity schema: `2`
- target_skill_sha256: `cf826e2e86ef193d8a7294a87c743dead6af892aefcc220dd56ae949fa5c3b40`
- eval_definition_sha256: `38b6af0374fcc8ce56a2a453684404f29e895eaad6d86b973c652b7dd34579f8`
- metadata_sha256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- fixture_sha256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `73f4addc59ec16b0f91c6a70a2a767ce7f6b4ad72612ca19a2131095a0722114`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b639e5a542e8c14d9db634c15148cb2563d801ada17ecc608983807552b63d49`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | PASS | with_skill explicitly accepts the confirmed host, version, scope, evidence sources, and required Release Notes output. |
| `routes_release_notes_generator` | PASS | with_skill routes the request to `release-notes-gen` and preserves the stated authorization boundary. |
| `preserves_handoff_context` | PASS | The handoff retains the fixture's confirmed version, scope, host, evidence sources, and output path without changing those facts. |
| `references_release_notes_gate_only` | PASS | with_skill identifies `release-notes-gen` as the downstream specialist, does not perform generation, and exposes no local SKILL.md path. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=1737354e8ca770d11dd7288b29fd3457010bf509d7f5e0feb5c3863cf7d8a6da; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepted the entry basis and routed a bounded handoff to release-notes-gen without performing downstream generation or forbidden release actions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=0309d43900450c250b27042c42505f42678de54a212f339e9fec3e7601514d05; snapshot_sha256=4e8d2492d29adabe9bab5964c83c70b89152147a4f7d4d72e1c3fad998baee5b
- Behavior: Fresh baseline generated a Release Notes file directly instead of demonstrating the required specialist routing boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
