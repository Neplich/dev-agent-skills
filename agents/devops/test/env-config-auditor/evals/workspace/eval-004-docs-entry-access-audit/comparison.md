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
- target_skill_sha256: `bd10ad28cda2e258647de2487fc41636124b4b1a48dc9f75b2dda06e6bfc2473`
- eval_definition_sha256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- metadata_sha256: `677e94c942760005f41ea164933b85cc762b6c8428640c65d6becfb051027269`
- fixture_sha256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `10734badb795d9dd2c7f522212860a120a71a582b6fdcf439619f31f19b4904f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `204b02cf02ba29acba94a8f2b9d77989cc545ccad0b3e283133a98976ab6ca74`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | The locked deploy/ENV_AUDIT.md contains a four-row matrix covering Staging/Production × Public/Internal, with Public DNS/TLS and Internal authentication/network restriction evidence fields. |
| `audits_runtime_environment_differences` | PASS | The locked report explicitly covers ports, probes/health, Service/Ingress/Gateway, secret/config references, environment differences, and local/Docker/Helm/CI/CD coverage, marking unavailable items unknown. |
| `does_not_overclaim_missing_evidence` | PASS | The report defines unknown as unavailable evidence, states that documented configuration or domains do not prove reachability, certificate validity, probe success, or effective access control, and limits formal-document follow-up to verified facts and unresolved owners. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=24cb5152a97c7479788d21dbd472ab7a872110dcafd27eda584bcbf56b8d7193; snapshot_sha256=e677227717a706565a0f101330445a150a40f02bd093ba1384e5a7a1bc6eceed
- Behavior: Produced a durable, read-only environment audit covering all four runtime variants and clearly separating confirmed evidence from unknowns.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=3a2bf611be8cddd12c225553e947b922d94a0b4571e31b116e06156d89bdd449; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a correct comparison audit in final prose but did not produce a durable audit file.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
