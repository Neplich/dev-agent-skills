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
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `cc05e28bb9aed099804431e1cee55bda0cec7614cc8c780d6f8ad4d50c137367`
- Eval definition SHA-256: `02c7a6bcc66679fa2f47687ffd7cdba26fff303adab62c4e3435b49f28878db8`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | PASS | With-skill output places “Add OAuth2 login support” under Added. |
| `fix_fixed` | PASS | With-skill output places token-expiry crash resolution under Fixed. |
| `chore_deps` | PASS | With-skill output omits the requests dependency maintenance PR. |
| `build_deps_skipped` | PASS | With-skill output omits the Vite dependency bump. |
| `perf_changed` | PASS | With-skill output places API caching under Changed. |
| `feat_added_breaking` | PASS | With-skill output places the plugin configuration redesign under Changed and marks it BREAKING. |
| `docs_release_workflow_changed` | PASS | With-skill output includes the release publishing workflow and preflight change under Changed. |
| `test_release_acceptance_changed` | PASS | With-skill output includes release acceptance coverage and required evidence under Changed. |
| `ci_release_gate_changed` | PASS | With-skill output includes required repository checks before release under Changed. |
| `docs_typo_skipped` | PASS | With-skill output omits the README typo/copyediting PR. |
| `ci_cache_skipped` | PASS | With-skill output omits the CI cache maintenance PR. |
| `remove_removed` | PASS | With-skill output places Python 3.7 support removal under Removed. |
| `security_security` | PASS | With-skill output places the XSS vulnerability fix under Security. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8d9d87cad7abcb73168e7b8a7cf0eaa982a5e5bbd210ebd142c4deea9ae6eb0a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies all asserted user-visible changes, skips internal maintenance, and marks the breaking redesign.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=171e5ac5da648635f7d76603c860871f91729c1793192007856c0085b22d4167; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also satisfies the assertions, providing comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
