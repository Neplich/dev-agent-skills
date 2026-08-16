# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Identity schema: `2`
- target_skill_sha256: `2ba8dad890b4a470e045fac5a77553d35f40494dd4f5ee0df778eda64ba0f881`
- eval_definition_sha256: `02c7a6bcc66679fa2f47687ffd7cdba26fff303adab62c4e3435b49f28878db8`
- metadata_sha256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cc05e28bb9aed099804431e1cee55bda0cec7614cc8c780d6f8ad4d50c137367`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f75f5f8b8869cc572a0f69646861f4a54c0e1cb5775b8c2dac040f714114c1c9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | PASS | with_skill output places “Add OAuth2 login support” under Added, with an optional auth scope. |
| `fix_fixed` | PASS | with_skill output places token-expiry crash and mobile alignment fixes under Fixed. |
| `chore_deps` | PASS | with_skill explicitly skips dependency-only item #103. |
| `build_deps_skipped` | PASS | with_skill explicitly skips dependency-only item #114. |
| `perf_changed` | PASS | with_skill output places the caching performance improvement under Changed. |
| `feat_added_breaking` | PASS | with_skill places the plugin configuration redesign under Changed and marks it BREAKING. |
| `docs_release_workflow_changed` | PASS | with_skill includes the release publishing workflow update under Changed. |
| `test_release_acceptance_changed` | PASS | with_skill includes tightened release acceptance coverage under Changed. |
| `ci_release_gate_changed` | PASS | with_skill includes required repository checks before release under Changed. |
| `docs_typo_skipped` | PASS | with_skill lists README typo/copyediting item #109 among skipped maintenance items. |
| `ci_cache_skipped` | PASS | with_skill lists internal cache maintenance item #110 among skipped maintenance items. |
| `remove_removed` | PASS | with_skill places Python 3.7 support removal under Removed. |
| `security_security` | PASS | with_skill places the XSS vulnerability patch under Security. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=1c3057ec114e98304d8ed4b305043738bc178ffb4a3c2117907388f79ebbe370; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies all user-visible changes, cleans titles, marks the breaking change, and skips the specified maintenance-only items.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=674d41eb6e91b34d48c83598ca0a639a60170d5f0f6a5a7caa9e65a711da79d7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also produced a substantively correct changelog, with more verbose translations and an explicit empty Deprecated section.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
