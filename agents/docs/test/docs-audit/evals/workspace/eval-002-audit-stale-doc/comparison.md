# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- metadata_sha256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- fixture_sha256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | NOT_EXERCISED | The locked with_skill output stops at a pre-tag gate because the formal documentation-site foundation is incomplete; the raw trace does not prove that the deterministic layer actually recorded `suspect`. |
| `confirms_outdated_claim_stale` | NOT_EXERCISED | The with_skill output reports preliminary code/document facts but concludes `mismatch` and stops before the fact-layer stale determination; the raw trace cannot prove a completed `stale` conclusion. |
| `blocks_stale_release` | NOT_EXERCISED | The locked output correctly reports `blocked` and provides a bootstrap-and-rerun next step, but no audit report or completed stale evidence is delivered. The later audit result cannot occur until the missing foundation is supplied. |
| `does_not_stamp_stale_set` | PASS | The locked output reports no saved report, clean Git state, and no working-tree or index changes; the raw Git evidence shows no stamp mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=24a846452a0a293f97495c59461d2af73715f6d5ac096c9a36ac49c17ce04391; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly stopped at the missing-foundation gate, returned blocked, and made no repository stamp mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=847293e29b8e7d8527255b14e7a4382b5dea7ea096b4334a8a0a942f5ebc82c9; snapshot_sha256=e2d8be49644988cab06f8e25c28268c7e144fafa0423b9e0c0df7751bde11808
- Behavior: Created an audit report and reported documentation gaps, but did not provide the skill-gated audit workflow or explicit suspect/stale distinctions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Supply or confirm the formal documentation-site foundation, then rerun the pre-tag audit to exercise the suspect and stale determinations.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
