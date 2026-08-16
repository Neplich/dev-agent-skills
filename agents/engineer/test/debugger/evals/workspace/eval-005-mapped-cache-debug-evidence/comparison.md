# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-005-mapped-cache-debug-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d` from `agents/engineer/test/debugger/evals/workspace/eval-005-mapped-cache-debug-evidence`.
- Identity schema: `2`
- target_skill_sha256: `8f85dae9526c56f3d9c6b946dd90d2d85718bee6a272309b91713955601d3385`
- eval_definition_sha256: `793c3f5cce4575964aaa387ece63f94a0f71e528641010e1ee2d932bd04007a8`
- metadata_sha256: `9f6661ea39a62ed90ab2d91bca6b54621f4ad68a03180feca81017ec357ed9b2`
- fixture_sha256: `5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `3e75308618e40000064b1f17dc0f0b301f828ec4f2f128fc91b1ab1bc2382820`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill trace reads `docs/site/api/cache.md` before `docs/site/standards/change-map.yaml` and also scans unrelated files before resolving the map. |
| `verifies_against_code` | PASS | The with_skill report cites `src/cache/ttl.txt` as `ttl_seconds: 60`, contrasts it with the documented 300 seconds, qualifies runtime uncertainty, and structures the discrepancy and root-cause assessment. |
| `treats_unverified_as_low_trust` | PASS | The report explicitly records `last_verified_version: unverified`, marks expected behavior unaligned, limits confidence, and states that runtime adoption remains unconfirmed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=8064b9550322a5dc7c2343049faddb2db1d5b1a740cf510e01c8392e12f6beda; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified and cautiously reported the 60-second versus 300-second discrepancy, but violated the required mapped-document read order.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=d7fa0813f72ccb119ff1dc5f2d49cea119ee8819b40084d49754b38ee0ab70e4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported the same static discrepancy with less explicit uncertainty and no demonstrated mapped-document-first workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane did not read the change-map before the mapped API document and performed broader repository scans first.
- Next: Resolve `src/cache/` through the change-map first, then read only the mapped `docs/site/api/cache.md` before code verification.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
