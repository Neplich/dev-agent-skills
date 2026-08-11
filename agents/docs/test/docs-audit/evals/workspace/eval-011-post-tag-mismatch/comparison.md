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
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
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
| `uses_immutable_pre_tag_authority` | PASS | Trace shows resolution of the pre-tag commit/tree and committed audit/handoff reads; the output distinguishes the modified worktree copy from pre-tag evidence and keeps the result blocked. |
| `validates_current_attempt_history` | PASS | Trace reads the committed attempt-2 audit and handoff, including directly superseded attempt 1; the output identifies the modified worktree audit copy and does not use it to authorize release. |
| `rejects_complete_release_tree_drift` | PASS | Trace resolves and diffs the complete pre-tag and tag trees, including the raw added file; the output reports `A src/catalog/export-v2.py` and concludes `blocked`. |
| `offers_safe_maintainer_recovery` | PASS | The output gives maintainer-owned same-version remediation and new-version release choices, with prerequisites to repair evidence, confirm versioning, clean the worktree, and rerun the audit. |
| `persists_blocked_without_corrupting_authority` | FAIL | The output states that no post-tag blocked record was written and that no tag, branch, or release operation occurred, but it does not state the required recovery condition to restore write capability, persist the blocked record, and verify it by readback. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=28e9e5e9164c542fa9dd460e6edc46566f8ece2efbe666d44957e374df90dee9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performs a read-only post-tag audit, selects and inspects committed evidence, detects authority/tree drift, blocks release, and offers maintainer choices; persistence recovery details are incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=fb74cccd6299d5e3ed3a4345dd3562c367074831e0b8053ca98bad0846238516; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline detects the added release-tree file and recommends blocking, but provides less complete authority, attempt-history, and persistence handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required persistence-failure recovery condition and readback requirement.
- Next: Add explicit recovery instructions: restore write capability, persist the blocked record, verify it by readback, and confirm the prior pre-tag authority remains unchanged.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
