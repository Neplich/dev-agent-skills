# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Identity schema: `2`
- target_skill_sha256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- eval_definition_sha256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- metadata_sha256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- fixture_sha256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `10734badb795d9dd2c7f522212860a120a71a582b6fdcf439619f31f19b4904f`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | with_skill delivery snapshot contains a four-row matrix covering staging/production Public and Internal, including DNS/TLS for Public and authentication/network restriction for Internal. |
| `audits_runtime_environment_differences` | PASS | with_skill delivery snapshot explicitly covers ports, probes/health, Service/Ingress/Gateway, secret/config references, and staging/production differences, marking unavailable items unknown. |
| `does_not_overclaim_missing_evidence` | PASS | with_skill report marks missing runtime and permission evidence unknown, states a documented domain is not DNS reachability evidence, and does not claim readiness or fabricate integration evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=1df04ba83da052bdf4dc3d66afa946c8429dbb69b33d0af2ced977dd354d2a0e; snapshot_sha256=4fa90d405a4ec96d9a95548ab6317a73ddfed5bd061b56d2d9cc6864a599d679
- Behavior: Produced a durable read-only audit covering all requested environments and configuration surfaces, with evidence separated from unknowns.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=da69f9235c716d9a04b876d611c6abcef3c23d23075d2bc80e1f21e705bc3b44; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a careful prose-only baseline audit that identified major evidence gaps but did not deliver a structured audit file.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
