# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `84cb88cc9e25dde2fbf0d2a0fb5349bfe630e32b333634cfdb918d30e60002a8`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | The locked with_skill output reports the repository states but provides no durable-commit confirmation or completed first-bootstrap integrated classification. |
| `asks_first_bootstrap_choice` | FAIL | It identifies billing-api as lacking a documentation site and suggests PM/Docs scope confirmation, but does not explicitly ask the three required choices: include all variants, independent hosting not_applicable, or defer with blocker. |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | No locked evidence shows a repeated bootstrap, re-read configuration, or Internal startup-path drift recheck. |
| `preserves_authorization_boundary` | PASS | The output explicitly states the check was read-only and no files were modified; git evidence also shows no changes, commits, pushes, releases, or deployments. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=fe4360fe69be6281e70aaea42c218c4feb3cedd3e55a9d03ba9a49c07efcb010; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurately performs the requested read-only repository connectivity review and preserves the authorization boundary, but omits the explicit three-way bootstrap choice.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=ebf512367cce7627977b41c253d64e86d1f61149606d857b4b3c54da7d2e487c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a comparable read-only repository review, with similar connectivity findings, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- asks_first_bootstrap_choice was not satisfied: the required three-way user choice was omitted.
- Next: If the bootstrap workflow is continued, explicitly ask the three required hosting/scope choices for the non-integrated documentation host.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
