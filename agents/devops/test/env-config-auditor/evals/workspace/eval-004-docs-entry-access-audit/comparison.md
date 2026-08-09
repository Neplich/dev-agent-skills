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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `10734badb795d9dd2c7f522212860a120a71a582b6fdcf439619f31f19b4904f`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | With_skill explicitly covers staging and production for Public DNS/TLS and Internal authentication/network controls, marking unavailable evidence as unknown where appropriate. |
| `audits_runtime_environment_differences` | PASS | With_skill covers ports, probes, Service/Ingress/Gateway evidence, secret/config references, and staging-versus-production differences, distinguishing known facts from unknown values. |
| `does_not_overclaim_missing_evidence` | PASS | With_skill records missing permissions/runtime/config evidence as unknown, avoids treating documented domains as verified integration, and limits formal-docs-sync to later landed and verified facts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=1843cfa8447fd8425aa65acb4388c3c8642ac6112ab376f88c02091030bce7a2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a complete read-only audit covering all requested access and runtime dimensions, with explicit unknowns and verification boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=30167cace5de71fff3476d876e54408bfadd21624c37ff7322c26228d2beb628; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a useful baseline audit with partial coverage, but less explicit runtime and evidence-boundary detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
