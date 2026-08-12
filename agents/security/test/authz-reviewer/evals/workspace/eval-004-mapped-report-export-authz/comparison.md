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
- target_skill_sha256: `c5c4e1b3eeeb704a06966dee8397bc4f1df239be6ed5f5799f8d4bd382f23626`
- eval_definition_sha256: `8fb5f1e36d08ae5ad3c1dfb46758101e4ce1413f28a63b591aee885fb67bbefb`
- metadata_sha256: `04460ae4a10b7b6f92dfdd6cb899ffd1f5dfbcb4fb34b6242a7bc18e450e6ddd`
- fixture_sha256: `6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the candidate read PM_HANDOFF.md and change-map.yaml, then read the mapped report-export.md and target policy, with no traversal of unrelated formal documents. |
| `verifies_against_code` | PASS | The report and final output identify that the policy allows exact roles admin and analyst, contrast this with the admin-only documentation, and assess the analyst permission as an authorization-boundary mismatch. |
| `treats_unverified_as_low_trust` | PASS | The candidate explicitly labels report-export.md as last_verified_version: unverified and bases the conclusion on code plus runtime checks for admin, analyst, and unknown roles. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The locked Security report records the conclusion, evidence, PM-agent routing, and PM-owned issue filing requirement. The trace shows no subsequent PM-agent confirmation, classification, or issue-creation runtime evidence, so the later interactive step was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=956153b2567d541c97d7a49956fee1365b2dd3779decf5baff92a40059a84ff2; fixture_sha256=6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1; output_sha256=94473d570079b5002c9672e04b382a1cbc25e8f47c5e0407782c1b88c4a125fb; snapshot_sha256=896269540b2c43241ef1893fa425e9253d79a26767cfb02ee0d824932461b176
- Behavior: Correctly performed the authorization review, created the required Security-owned report, and documented PM escalation requirements.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=956153b2567d541c97d7a49956fee1365b2dd3779decf5baff92a40059a84ff2; fixture_sha256=6b2ecd7bb8b1ef79f098d4d11a3ca4f93d8ab0f7969ef301d999bac9f594dbd1; output_sha256=180c17094a0c149f8121adb95748dda49f431faac72978d1beacccea80eeab9a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reached the correct code-versus-document conclusion but did not create the required Security report or demonstrate the escalation workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain PM-agent confirmation and runtime evidence for classification and PM-owned issue creation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
