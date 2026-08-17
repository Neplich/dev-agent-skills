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
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- metadata_sha256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- fixture_sha256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `87ef764041bed9ee9555b42ac224112964f5f9e1229cf61ab18c2da424e966e8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | With-skill raw commands resolved the pre-tag commit/tree and used git show for committed audit and handoff; the output isolated the modified worktree copy from that authority. |
| `validates_current_attempt_history` | PASS | The output identified attempt 2, superseded attempt 1, their same v1.2.0 scope, rejected the rewritten worktree copy as authority, and kept the result blocked. |
| `rejects_complete_release_tree_drift` | PASS | Raw Git evidence and the output confirmed the complete tree difference adds src/catalog/export-v2.py, recognized the conflicting patch evidence, and retained blocked status. |
| `offers_safe_maintainer_recovery` | PASS | The output offered actionable same-version remediation and a maintainer-confirmed new-version path, with required evidence repair and full re-audit prerequisites while preserving write boundaries. |
| `persists_blocked_without_corrupting_authority` | PASS | The output recorded blocked_record_persistence as not persisted, required restore-write → persist blocked → readback before rerun, and stated that prior authority and success state remain unchanged. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=fc66c00ccf0409fe98e22a8043ce94624d38474db0b1d7d036fe092c342663d2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly rejected release verification, preserved pre-tag authority, detected tree and evidence drift, and provided safe recovery guidance.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=79a6d21ea88687a56d245ac882962966e7b51bd69f0537f252050eda18ea89a6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline noticed some drift and offered generic follow-up, but did not establish the full authority, attempt-lineage, persistence, and complete-tree safety gates.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
