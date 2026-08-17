# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1` from `agents/security/test/authz-reviewer/evals/workspace/eval-004-mapped-report-export-authz`.
- Identity schema: `2`
- target_skill_sha256: `560a4230ae443905926eeddf72dec9114fbb989ca3911007bb3d55a10a342e86`
- eval_definition_sha256: `8fb5f1e36d08ae5ad3c1dfb46758101e4ce1413f28a63b591aee885fb67bbefb`
- metadata_sha256: `ae7084c912c7a22c84bf1353aceb60530fc3393371ee2773e75ed9b9cc1b0840`
- fixture_sha256: `6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `956153b2567d541c97d7a49956fee1365b2dd3779decf5baff92a40059a84ff2`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `382daaa46e228ddafa411ea49b63d6055764b79f7917bec67fcebf40d2845479`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows repository/evidence discovery followed by reading PM_HANDOFF.md, change-map.yaml, and the mapped report-export document before the target policy code was inspected; the delivered report records the mapped document. |
| `verifies_against_code` | PASS | The locked report and final output identify the exact policy, show that strict equality allows admin and analyst, contrast this with the admin-only document, and assess analyst as unexpected access. |
| `treats_unverified_as_low_trust` | PASS | The locked report explicitly identifies last_verified_version: unverified for the change map and formal page, treats the page as low-trust, and uses code as current behavior evidence. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The Security-owned report preserves the discrepancy and directs PM/Security classification and PM/docs routing. Actual PM classification and issue creation are not exercised in the locked evidence, so the later escalation step cannot be judged. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=956153b2567d541c97d7a49956fee1365b2dd3779decf5baff92a40059a84ff2; fixture_sha256=6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1; output_sha256=3a7a66b0c66133691d549a081dc5da5f38f7d7b904530af9e22edd5c7ee33e1e; snapshot_sha256=50768c06c7c5dbe8218fd26b5be11d4c200e53cfff23c7f5eca22d167be13c30
- Behavior: Produced a file-backed authorization review grounded in the mapped document and policy code, correctly identifying admin and analyst as allowed and analyst as conflicting with the recorded admin-only boundary; routed the unresolved classification to PM/Security.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=956153b2567d541c97d7a49956fee1365b2dd3779decf5baff92a40059a84ff2; fixture_sha256=6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1; output_sha256=1321c3c5c66001dd0099409ba66e0f360d4ff673e4cc6471b3ea11818482fd36; snapshot_sha256=ed6bd9aec9754952af6a2be4752e4255385d7be8bc0d7a1384a9f8c284ce08fb
- Behavior: Correctly identified the authorization discrepancy and produced a basic Security report, but provided less explicit low-trust handling and escalation/classification routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain PM/Security classification and, if required, exercise PM-owned issue creation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
