# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677` from `agents/docs/test/docs-audit/evals/workspace/eval-003-audit-pure-refactor`.
- Fixture SHA-256: `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677`
- Prompt SHA-256: `20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `3e58dae2a34edb25f9589f7bddb4e3282cd1f66e3b0c3f35187db4ed16fd5f23`
- Eval definition SHA-256: `a7212e3282f2eaaa660e0675fb965d5050f366a07c153f3821d78fdab8976de5`
- Metadata SHA-256: `1e20c97bb5ffc477023f6bbbd217e71d747297cb0b8f52652660b6b2d10adc7a`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | NOT_EXERCISED | with_skill reports the page as affected and gives a fact-layer conclusion of `verified`, but does not explicitly establish the hidden `suspect` handoff. |
| `classifies_accurate_refactor_verified` | PASS | with_skill states the refactor did not change the API contract and that the method, path, auth, parameters, success/error responses, streaming, and file behavior match the target code; it concludes `verified`. |
| `does_not_force_noop_doc_edit` | FAIL | with_skill identifies the page as unchanged and accurate, but does not explicitly state that a no-op documentation edit is unnecessary. |
| `does_not_block_for_unchanged_accurate_doc` | PASS | with_skill does not classify the unchanged page as `stale`; it attributes `blocked` to missing release-version/site/audit evidence and explicitly says it cannot return `ready_for_tag` or stamp. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=da7f3430643defd272527694b49e7c7fc32849938870b1d5aebdef7927f455e5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly verifies the unchanged API contract and blocks only on missing release-surface evidence, but omits the explicit no-op-edit conclusion and does not prove the hidden suspect handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=388c17f98d62af4dcc770ccf834b8e7063870244a0d97ea9014a22b41bfe71f3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline incorrectly reports the audit as passed and treats the accurate unchanged page as requiring no API update without the required fact-layer verification/blocking analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill report omits the required explicit conclusion that an accurate pure refactor does not require editing the documentation merely to match the diff.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
