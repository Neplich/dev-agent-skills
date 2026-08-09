# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-002-session`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a` from `agents/security/test/authz-reviewer/evals/workspace/eval-002-session`.
- Fixture SHA-256: `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a`
- Prompt SHA-256: `2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5d96dce7dbfccf9a7b2e510ce571be9b1aa80472fabf9a5779117cb4e21d3b09`
- Skill overlay SHA-256: `89401c75c36dd79dd8bf55d1b0c23cbd794402b7f29f62d05ae9f27f5e25c3f9`
- Judge schema SHA-256: `a3c690bb602cdac9c05191ab0581fc35b8fd034dd27825093b3b51de5926404b`
- Eval definition SHA-256: `86d9727a0807549b3bf3936da079aa7238a2b14b16eed4306c9bda4eb6d7be43`
- Metadata SHA-256: `f26166d912f73c7f118a1561bee3e62973123b274975fb4a17a869fba31f82a0`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `authorization_model` | FAIL | with_skill refused to review despite PM_HANDOFF.md defining the security scope, roles, permissions, assets, source documents, and authorization boundaries. |
| `access_control_findings` | FAIL | with_skill produced no analysis of session creation, expiration, rotation, logout invalidation, JWT, or permission-check defects. |
| `evidence_and_impact` | FAIL | with_skill produced no evidence, impact, or severity analysis; it incorrectly claimed the handoff was not provided. |
| `remediation` | FAIL | with_skill produced no authz-review.md delivery, remediation guidance, or regression verification recommendations. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=598cc5786d898bd74f6ca5f5e361b4836c3ab6bd9243570f49ff67bd4173bedf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Refused to begin the review, incorrectly stating that the required PM/Security handoff was missing; no delivery snapshot was produced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=5e338871219674398feb11d401f71161bf2dc2b7c6aa3f074355a5a036811a2c; snapshot_sha256=f91a2d1976a5fee972949551f4ec2b59199c74e74bde217df057ef04dfb3172f
- Behavior: Completed the review, delivered authz-review.md, identified three high-severity session defects, documented unavailable evidence, and provided remediation and regression guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane declined the requested review and delivered no report or security findings.
- Its stated prerequisite was contradicted by the read-only fixture, which includes PM_HANDOFF.md and the referenced PRD and implementation.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
