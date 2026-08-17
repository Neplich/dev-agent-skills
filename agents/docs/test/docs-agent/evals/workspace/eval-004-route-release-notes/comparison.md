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
- target_skill_sha256: `023cc6d8aa109db6ff7dcd662df567ae4f0c79dddb66dfe7bcf6f1eb91d20f39`
- eval_definition_sha256: `38b6af0374fcc8ce56a2a453684404f29e895eaad6d86b973c652b7dd34579f8`
- metadata_sha256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- fixture_sha256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `73f4addc59ec16b0f91c6a70a2a767ce7f6b4ad72612ca19a2131095a0722114`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9d7abf20333b60efc8aeaad2d302ecd422e44bb547e52f5a4d9623347a2b048b`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | PASS | With-skill output identifies the handoff as sufficient and preserves the confirmed version, scope, host repository, evidence sources, and required output. |
| `routes_release_notes_generator` | PASS | With-skill output explicitly routes to `release-notes-gen` and states that it will not route to the other specialists or execute downstream work. |
| `preserves_handoff_context` | PASS | With-skill output retains the version, scope, feature path, host, evidence sources, required artifact, and blockers/risks from the handoff. |
| `references_release_notes_gate_only` | FAIL | With-skill output correctly limits router execution to the specialist gate, but exposes the local `.agents/skills/release-notes-gen/SKILL.md` path, which the assertion forbids. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=0b9f8406fd94a073d0347ee786ee0870e1d4bdcb0ee9b531763dbfbef3cff219; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts and routes the handoff while preserving context, but violates the user-visible boundary by exposing the local specialist skill path.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=7ee32988fb534e6932a531b50a5ef485c5b4af65aa88b947ab383be87d04b200; snapshot_sha256=aa79fcae2a2184b79c8b489ac45fc5674c942c28719483b9ad56f62a7c39c263
- Behavior: Fresh baseline generated the release-notes file directly instead of performing the required router-only handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output exposes a local SKILL.md path to the user.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
