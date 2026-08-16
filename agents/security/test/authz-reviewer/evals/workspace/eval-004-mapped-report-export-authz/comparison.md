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
- target_skill_sha256: `28d6bd56202068b6de6f4e41d3bc74df73f15108b0013486fcd02eaa93f991d8`
- eval_definition_sha256: `8fb5f1e36d08ae5ad3c1dfb46758101e4ce1413f28a63b591aee885fb67bbefb`
- metadata_sha256: `ae7084c912c7a22c84bf1353aceb60530fc3393371ee2773e75ed9b9cc1b0840`
- fixture_sha256: `6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `956153b2567d541c97d7a49956fee1365b2dd3779decf5baff92a40059a84ff2`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `217840028dda2eba806419edc71588064b0361d1a26fbfdbb7a47693678ccfa6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace reads PM handoff, then change-map and its mapped required document, before reading the policy code; the delivered report records the mapped evidence and no unrelated formal-document contents. |
| `verifies_against_code` | PASS | The locked report and trace identify `src/access/report-export-policy.js` as the decisive evidence, correctly state that exact `admin` and `analyst` values are allowed, and identify the admin-only documentation mismatch and resulting risk. |
| `treats_unverified_as_low_trust` | PASS | The locked report explicitly identifies both the change-map and API page as `last_verified_version: unverified`, treats them as low-trust, and bases the authorization result on the implementation code. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The locked report and final output return the conclusion and evidence to `pm-agent` for classification and issue filing, while preserving the Security-owned report and avoiding direct Docs handoff or Security issue creation. Actual issue creation is not exercised because no user confirmation is present. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=956153b2567d541c97d7a49956fee1365b2dd3779decf5baff92a40059a84ff2; fixture_sha256=6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1; output_sha256=a59a02e75ef8c45df6225ab239887c42948d73e075f91e89ab2c33732c81b4cd; snapshot_sha256=e90a8627801b062e638c5477a491233080d3d2dcd76e6c1e7a5088af5bc5905d
- Behavior: Correctly follows mapped-document and low-trust verification requirements, grounds the finding in code, produces the required Security report, and hands the conclusion to PM.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=956153b2567d541c97d7a49956fee1365b2dd3779decf5baff92a40059a84ff2; fixture_sha256=6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1; output_sha256=3b726c9ca507bb91fb94d6f059d467538f128dba62e25a55783823278a9706dd; snapshot_sha256=7634e3ac80fe477997ae2a5114d5982394e38d941eec39f7d9a93aea61b70b90
- Behavior: Fresh baseline reaches the core authorization finding and produces a report, but does not demonstrate the mapped-document trust handling or PM escalation process.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: After PM classification is confirmed, PM should create the tracking issue and continue the prescribed handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
