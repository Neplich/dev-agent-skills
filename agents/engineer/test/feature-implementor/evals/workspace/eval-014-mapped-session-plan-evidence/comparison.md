# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Identity schema: `2`
- target_skill_sha256: `7f71c78ab97a67d477751886a8f46d8cfd865bac113be49568de86ccf5343ee9`
- eval_definition_sha256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- metadata_sha256: `8f8181a8b5f8f92c423cfb8a15a35438fa3fefe0e74f7a7daf711ceaa3d79ccb`
- fixture_sha256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6ba93c2da62bbbed9ea41d72d153901f8e8bbbbad20322168e3cf7c265e800fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace reads the change map, then the mapped session API document, while limiting later searches to planning/handoff paths rather than traversing all repository documentation. |
| `verifies_against_code` | PASS | The trace and final checkpoint verify `src/session/config.txt` as 30 minutes, identify the document's 60-minute claim, and include the discrepancy and its impact in the planning gap packet. |
| `treats_unverified_as_low_trust` | PASS | The candidate explicitly treats `last_verified_version: unverified` as low trust and bases the timeout and renewal findings on `src/session/config.txt`, with missing product/technical evidence recorded as blockers. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=9a9874b6aa5ff8654a867bb6ea06184129638eef1b634140048a5492aedfa32c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed the required evidence-first verification, preserved the 30-minute code fact over the unverified 60-minute document claim, and stopped before unauthorized implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=2def109d70256be885ba226cf876f3bc75a35e2fba504c3dd63f0e3b29c13f10; snapshot_sha256=52140ac2506772fb2c7ac52f1967ab1be9b65b8887e800151674a70a8c956e03
- Behavior: Fresh baseline modified configuration and documentation directly after a less disciplined exploration, without the required planning gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
