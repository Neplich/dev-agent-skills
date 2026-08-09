# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-003-third-party`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-003-third-party`.
- Fixture SHA-256: `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73`
- Prompt SHA-256: `f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `840e4d3e20057f4834a3b010b4142d0e7be2f66540c525231dc34075db0dbbee`
- Judge schema SHA-256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Eval definition SHA-256: `fde37322a972618cf8b85d5463c8e7a856c7547f8c15123669fd15297f556852`
- Metadata SHA-256: `1b358949b025cd13ff498cda0a21978c243d4781824a1ceab1947fe97db21069`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | Locked privacy-map.md directly inventories all three recipients, their fields and data types, collection entry via sendUserEvent, and inferred processing purposes. |
| `sharing_and_retention` | PASS | Locked privacy-map.md identifies sharing to ExampleAnalytics, ExampleAds, and ExamplePay, including configured regions, retention values, undefined advertising retention/region, and deletion-support gaps. |
| `user_rights` | PASS | Locked privacy-map.md explicitly assesses access, deletion, export, rectification, consent, and opt-out propagation, finding no implemented end-to-end support and distinguishing configured payment deletion from verified execution. |
| `compliance_gaps` | PASS | Locked privacy-map.md provides prioritized compliance gaps and actionable recommendations covering consent, rights-request orchestration, regional/DPA evidence, retention, minimization, testing, and privacy-policy updates. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=15551c9adf33298c43b6ce34951715d84a9a50195243f86a0884116558ae9a2e; snapshot_sha256=6153b53f70d0ea8710d500a0085482e9eee5fe50c27a01654fe725ab7c1ed4d4
- Behavior: Delivered a complete, evidence-traceable privacy processing report with inventory, sharing and retention assessment, user-rights status, compliance gaps, and remediation recommendations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=131f694810b7dd7c05f036181c1f3bda54c695635cb16521f94c734badf118fe; snapshot_sha256=4d5cd238240e752560e785caf9de9adf40a576dab3ce06b1000efe42e319cb76
- Behavior: Fresh baseline also delivered a substantially complete report, but with less explicit evidence-freshness qualification and less structured user-rights and compliance analysis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
