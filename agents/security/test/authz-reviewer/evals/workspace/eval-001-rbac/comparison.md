# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-001-rbac`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a079595e48d457c66e6bfba203a327a4dd2cee76937828205dc7d5ae1bf6d9ea` from `agents/security/test/authz-reviewer/evals/workspace/eval-001-rbac`.
- Identity schema: `2`
- target_skill_sha256: `560a4230ae443905926eeddf72dec9114fbb989ca3911007bb3d55a10a342e86`
- eval_definition_sha256: `235137f94204f51e6c45d33016dc89d9789a6db39caeb6f905a7bece723a5a15`
- metadata_sha256: `3631c1a666f99fa53cdd7f195ad887e6bb088a8209e8b065f9602b94a403934c`
- fixture_sha256: `a079595e48d457c66e6bfba203a327a4dd2cee76937828205dc7d5ae1bf6d9ea`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b9195372d92f3bbea03af4fc8ee3a7b882c68284b96da53cdd8cef5cf57e70e9`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `1a600a6512e0923d93e2001890b6b0e358c2e4b71aa4c63f0e217fc733bd66d6`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `382daaa46e228ddafa411ea49b63d6055764b79f7917bec67fcebf40d2845479`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `maps_expected_and_actual_access` | PASS | The locked report contains a PRD-based guest/user/admin permission matrix and an actual-access matrix for `getAdminAuditLog`; raw trace execution confirms undefined/guest/user return 403 and admin header returns 200 with the audit log. |
| `finds_client_controlled_role_bypass` | PASS | The locked report cites `src/access/admin-policy.js:1-3` and `:5-10`, explains direct trust of `request.headers["x-user-role"]`, and demonstrates the forged-admin 200 response. |
| `states_evidence_impact_and_limits` | PASS | The report identifies management audit logs, affected guest/user roles, unauthorized disclosure and possible role-management impact, rates the issue HIGH, and explicitly marks session, JWT, role-management, and other-route coverage as unavailable or unverified. |
| `proposes_trusted_identity_fix_and_tests` | PASS | The report recommends a verified server-side principal, trusted middleware and fail-closed authorization, and specifies regression coverage for unauthenticated, guest, user, admin, forged headers, invalid credentials, and all admin routes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1a600a6512e0923d93e2001890b6b0e358c2e4b71aa4c63f0e217fc733bd66d6; fixture_sha256=a079595e48d457c66e6bfba203a327a4dd2cee76937828205dc7d5ae1bf6d9ea; output_sha256=483a1d455cda63ad630c07514b0f2bb7c5950469dd51a346485167d4503abeaf; snapshot_sha256=f29b74a78715afa6c8696b211e143e42d3ec0d526684e4679705680628cf5382
- Behavior: Produced a complete evidence-backed authorization review, including the delivered report and runtime confirmation of the bypass.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1a600a6512e0923d93e2001890b6b0e358c2e4b71aa4c63f0e217fc733bd66d6; fixture_sha256=a079595e48d457c66e6bfba203a327a4dd2cee76937828205dc7d5ae1bf6d9ea; output_sha256=137f40b19f6d93ea332f02371779bec11fefc8dbba361ac646395f8b76493993; snapshot_sha256=21bc90b85091af57c32a93d2d7bec2f699494212d3cc7a510e3559e5a1a40b5b
- Behavior: Produced a broadly similar authorization review and report, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
