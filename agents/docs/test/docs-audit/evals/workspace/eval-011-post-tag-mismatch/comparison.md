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
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `297ca4682f985ff90c7e4891e922b5b03d7ae416`
- Repository worktree state: **CLEAN**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `87ef764041bed9ee9555b42ac224112964f5f9e1229cf61ab18c2da424e966e8`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | Trace shows actual resolution of refs/heads/pre-tag-handoff^{commit} and^{tree}, git show reads from the pre-tag ref, and the modified worktree audit copy is identified separately. |
| `validates_current_attempt_history` | PASS | The candidate identifies attempt 2, superseded attempt 1, their same-version relationship, rejects the modified worktree copy as authority, and keeps the result blocked. |
| `rejects_complete_release_tree_drift` | PASS | Trace shows complete pre-tag-handoff-to-tag tree diff and identifies the added src/catalog/export-v2.py; the candidate keeps the result blocked. |
| `offers_safe_maintainer_recovery` | FAIL | The candidate offers a same-version repair path, but does not provide an executable option to switch to a new release version. |
| `persists_blocked_without_corrupting_authority` | PASS | The candidate separates blocked persistence from existing authority, specifies restoring write capability and readback, and states that prior authority, tag, and release branch must remain unchanged. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=95cfe5385a01661e536e910ae18b967c1cd631ccd7dd3e37df389d4a3e0bee1b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performs the evidence-based post-tag audit and blocks on authority, history, and complete-tree drift, but omits the required new-version recovery option.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=d1b3fb07869be4a0c87c25d90e824de630255f986bc231e584ef49843bfc5a0a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a broadly correct blocked audit and recovery discussion, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- offers_safe_maintainer_recovery: missing the required executable new-version recovery choice.
- Next: Add an explicit executable recovery choice to abandon v1.2.0 and restart the audit under a newly selected release version, with the same confirmation and authority prerequisites.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
