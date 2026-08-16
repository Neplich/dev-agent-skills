# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- metadata_sha256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- fixture_sha256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `87ef764041bed9ee9555b42ac224112964f5f9e1229cf61ab18c2da424e966e8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | With_skill directly resolved the pre-tag and tag refs, read committed audit/handoff content from pre-tag authority, and treated the modified worktree audit copy as diagnostic rather than authoritative. |
| `validates_current_attempt_history` | PASS | With_skill identified committed attempt 2 and its directly superseded same-version attempt 1, rejected the rewritten current worktree copy as authority, and retained blocked status. |
| `rejects_complete_release_tree_drift` | PASS | With_skill verified the complete pre-tag-to-tag drift and identified the added src/catalog/export-v2.py from the raw tree evidence, while keeping the result blocked. |
| `offers_safe_maintainer_recovery` | PASS | With_skill offered executable same-version repair and new-version alternatives, with authority reconstruction, maintainer confirmation, and audit rerun prerequisites plus the docs-site-bootstrap responsibility boundary. |
| `persists_blocked_without_corrupting_authority` | PASS | With_skill reported blocked_record_persistence as not_persisted, specified restore-write, persist, readback, and rerun recovery order, and stated that prior authority and release refs remain unchanged with no success state. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=b7e28169387f9caf67d85b16fa14da563adf43471923b111733204556a0547b7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly produced a blocked post-tag audit grounded in immutable authority, complete tree drift, attempt history, safe recovery choices, and non-corrupting persistence handling.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=ce5feab00bd36a2e5e531f0ce1996384c4cd7429be5ca1e484112d1351377234; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Detected some release drift and evidence gaps, but did not establish the full protocol-level authority, attempt-history, recovery, and persistence-boundary result.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
