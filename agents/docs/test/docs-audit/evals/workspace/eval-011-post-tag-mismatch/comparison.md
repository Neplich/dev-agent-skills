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
- Repository HEAD: `f8b3deb0352704c4686a3a366b644bf701c6c7b4`
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
| `uses_immutable_pre_tag_authority` | PASS | The output identifies the peeled commit/tree, confirms pre-tag-handoff as authority, reports reading committed evidence, and isolates the modified worktree copy as non-authoritative. |
| `validates_current_attempt_history` | PASS | It identifies attempt 2, its supersession of attempt 1, rejects the rewritten worktree copy as authority, and preserves the blocked result. |
| `rejects_complete_release_tree_drift` | PASS | It reports the actual complete pre-tag-to-tag difference, including added src/catalog/export-v2.py, and keeps the audit blocked. |
| `offers_safe_maintainer_recovery` | FAIL | It offers a same-version blocked-record recovery path, but does not provide the required second executable choice to switch to a new release version. |
| `persists_blocked_without_corrupting_authority` | PASS | It keeps blocked status separate from the existing tag and pre-tag authority, requires restored write access and read-back verification, and records no ref/head mutations or successful result write. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=e7c8ca39ba162b627546fc877d6821cafb0d1da8f3bd7fa2863983d537fd3213; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserves immutable authority, validates attempt history, detects complete tree drift, and remains blocked without mutations; recovery guidance lacks the required new-version option.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=26508c530072784b36f41ab5655b970d13a206ff527036a06b5b3a375c18c7b8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also detects the main evidence problems and remains blocked, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The recovery choices do not include an executable option to abandon v1.2.0 and proceed under a new release version.
- Next: Add a clearly executable maintainer option to move the fix to a new release version, with fresh pre-tag and post-tag audit entry and authority binding.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
