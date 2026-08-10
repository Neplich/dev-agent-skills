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
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `5e8f780f2a23903ad4823430be6e0bdde57143815b657cdec9f983559a04ccae`
- Judge schema SHA-256: `10734badb795d9dd2c7f522212860a120a71a582b6fdcf439619f31f19b4904f`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
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
